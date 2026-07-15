"""Public (guest) API of the Builder Hub.

A builder site fetches the template catalog + per-page bundles from here over
HTTP (server-side, so no CORS needed). All template machinery lives in the
builder app; this module only reuses it to serve content — builder never
imports builder_hub (which would be circular, since builder_hub depends on
builder).
"""

import frappe
from frappe.utils import get_url
from frappe.utils.caching import redis_cache


@frappe.whitelist(allow_guest=True)
def get_catalog() -> list[dict]:
	"""Template groups with their pages, for any builder site's picker. Built from
	this hub's published template pages + on-disk group manifests. Preview +
	per-page live_url are absolute so a remote consumer can load them."""
	return _get_catalog(get_url())


@redis_cache(ttl=3600)
def _get_catalog(base_url: str) -> list[dict]:
	from builder.template_sync import get_all_group_manifests

	pages = frappe.get_all(
		"Builder Page",
		filters={"is_template": 1, "template_group": ("is", "set")},
		fields=["name", "page_title", "preview", "route", "template_group"],
		order_by="creation asc",
		ignore_permissions=True,
	)
	for p in pages:
		p.preview = abs_url(p.preview)
		# absolute URL of the published page on this hub (opened in a new tab as
		# the template preview). abs_url only handles asset paths, so build it here.
		p.live_url = f"{get_url()}/{p.route}" if p.route else None

	by_group: dict[str, list] = {}
	for p in pages:
		by_group.setdefault(p.template_group, []).append(p)

	groups = []
	for group, manifest in get_all_group_manifests("builder_hub").items():
		group_pages = by_group.pop(group, [])
		if not group_pages:
			continue
		order = {
			pg.get("name"): i for i, pg in enumerate(manifest.get("pages") or []) if isinstance(pg, dict)
		}
		group_pages.sort(key=lambda p: (order.get(p.name, len(order)), p.page_title or ""))
		groups.append(
			{
				"name": group,
				"title": manifest.get("title") or group.replace("_", " ").title(),
				"description": manifest.get("description") or "",
				"categories": manifest.get("categories") or [],
				"preview": abs_url(manifest.get("preview")) or group_pages[0].preview,
				"order": manifest.get("order"),
				"pages": group_pages,
			}
		)
	groups.sort(key=lambda g: (g.get("order") is None, g.get("order") or 0, g["title"]))
	return groups


@frappe.whitelist(allow_guest=True)
def get_template_bundle(page: str) -> dict:
	"""Everything a consumer needs to materialize one template page locally:
	the page (blocks, scripts, data script), plus its shared components,
	variables, client scripts and fonts as import-ready dicts. Asset URLs are
	absoluteized to this hub."""
	return _get_template_bundle(page, get_url())


@redis_cache(ttl=3600)
def _get_template_bundle(page: str, base_url: str) -> dict:
	from builder.export_import_standard_page import extract_fonts_from_blocks
	from builder.utils import extract_components_from_blocks

	if not frappe.db.get_value("Builder Page", page, "is_template"):
		# never expose arbitrary (or private) hub pages through this open endpoint
		frappe.throw(frappe._("{0} is not a template page").format(page), frappe.PermissionError)

	page_doc = frappe.get_doc("Builder Page", page)
	blocks = frappe.parse_json(page_doc.draft_blocks or page_doc.blocks or "[]")
	blocks = _absolutize(blocks)

	component_ids = extract_components_from_blocks(blocks)
	components = []
	for cid in component_ids:
		comp = frappe.get_doc("Builder Component", cid)
		comp_block = _absolutize(frappe.parse_json(comp.block or "{}"))
		components.append(
			{
				"doctype": "Builder Component",
				"name": comp.name,
				"component_id": comp.component_id,
				"component_name": comp.component_name,
				"block": frappe.as_json(comp_block, indent=0),
			}
		)

	variables = [
		{
			"doctype": "Builder Variable",
			"name": v.name,
			"variable_name": v.variable_name,
			"type": v.type,
			"value": v.value,
			"dark_value": v.dark_value,
			"group": v.group,
		}
		for v in frappe.get_all(
			"Builder Variable",
			filters={"group": page_doc.template_group},
			fields=["name", "variable_name", "type", "value", "dark_value", "group"],
		)
	]

	client_scripts = [
		{
			"doctype": "Builder Client Script",
			"name": cs.builder_script,
			"script_type": frappe.db.get_value("Builder Client Script", cs.builder_script, "script_type"),
			"script": frappe.db.get_value("Builder Client Script", cs.builder_script, "script"),
		}
		for cs in page_doc.client_scripts
	]

	fonts = set(extract_fonts_from_blocks(blocks))
	for comp in components:
		fonts.update(extract_fonts_from_blocks(frappe.parse_json(comp["block"])))
	font_docs = []
	for font_name in fonts:
		font = frappe.db.get_value(
			"User Font", {"font_name": font_name}, ["name", "font_name", "font_file"], as_dict=True
		)
		if font:
			font_docs.append(
				{
					"doctype": "User Font",
					"name": font.name,
					"font_name": font.font_name,
					"font_file": abs_url(font.font_file),
				}
			)

	return {
		"page": {
			"page_title": page_doc.page_title,
			"route": page_doc.route,
			"preview": abs_url(page_doc.preview),
			"blocks": blocks,
			"page_data_script": page_doc.page_data_script,
			"head_html": page_doc.head_html,
			"body_html": page_doc.body_html,
			"meta_description": page_doc.meta_description,
		},
		"components": components,
		"variables": variables,
		"client_scripts": client_scripts,
		"fonts": font_docs,
	}


def abs_url(path: str | None) -> str | None:
	if isinstance(path, str) and (path.startswith("/builder_assets/") or path.startswith("/files/")):
		return get_url() + path
	return path


def _absolutize(obj):
	"""Rewrite site-relative /builder_assets/ and /files/ asset URLs (quoted JSON
	string values — img/video src, preview, etc.) to absolute hub URLs."""
	base = get_url()
	s = frappe.as_json(obj, indent=0)
	s = s.replace('"/builder_assets/', f'"{base}/builder_assets/')
	s = s.replace('"/files/', f'"{base}/files/')
	return frappe.parse_json(s)


def allow_template_embedding(response=None, request=None):
	"""Serve template pages with a frame-ancestors CSP so any builder site can
	embed them in the picker's inline preview. Browsers ignore X-Frame-Options
	(added by the Frappe Cloud proxy as sameorigin) when frame-ancestors is set.
	"""
	if request is None or response is None:
		return
	if request.path.startswith("/templates/"):
		response.headers["Content-Security-Policy"] = "frame-ancestors *"
		response.headers.pop("X-Frame-Options", None)
