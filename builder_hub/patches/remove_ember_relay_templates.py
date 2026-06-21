"""Remove the retired `ember` and `relay` template groups from a site.

Deleting a group's fixtures from the app does NOT remove it downstream:
`reconcile_deleted_templates` only prunes pages *within* a still-shipped group,
so a wholly-removed group lingers in every site's DB until explicitly deleted.
This patch does that deletion, idempotently, on install/migrate.

Only the shipped template artifacts are removed — template pages
(`is_template=1` + `template_group`), the group's private components
(`<group>_*`) and its grouped variables. User pages created from these
templates (no `template_group`) are left untouched; the shared
`builder_theme_toggle*` client scripts (used by other groups) are not deleted.
"""

import frappe

RETIRED_GROUPS = ("ember", "relay")


def execute():
	for group in RETIRED_GROUPS:
		_delete_group(group)


def _safe_delete(doctype, name):
	"""Best-effort delete that can never abort the migrate it runs in.

	A user page still referencing one of these (now-removed) template
	components would raise LinkExistsError, and `force` does not bypass every
	guard across versions — so swallow and log rather than halt `bench migrate`.
	Commit on success so a later failure's rollback can't undo earlier deletes.
	"""
	try:
		frappe.delete_doc(doctype, name, force=True, ignore_permissions=True)
		frappe.db.commit()
	except Exception:
		frappe.db.rollback()
		frappe.log_error(title=f"remove_ember_relay_templates: kept {doctype} {name}")


def _delete_group(group):
	# 1. template pages of this group
	for page in frappe.get_all(
		"Builder Page",
		filters={"is_template": 1, "template_group": group},
		pluck="name",
	):
		_safe_delete("Builder Page", page)

	# 2. the group's private components (id convention: "<group>_<name>")
	for component in frappe.get_all(
		"Builder Component",
		filters={"component_id": ("like", f"{group}\\_%")},
		pluck="name",
	):
		_safe_delete("Builder Component", component)

	# 3. the group's variables (make_variable stored group=<group>)
	if frappe.get_meta("Builder Variable").has_field("group"):
		for variable in frappe.get_all(
			"Builder Variable", filters={"group": group}, pluck="name"
		):
			_safe_delete("Builder Variable", variable)
