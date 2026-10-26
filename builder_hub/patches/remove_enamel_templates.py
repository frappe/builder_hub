"""Remove the retired `enamel` template group from a site.

Deleting a group's fixtures from the app does NOT remove it downstream:
`reconcile_deleted_templates` only prunes pages *within* a still-shipped group,
so a wholly-removed group lingers in every site's DB until explicitly deleted.
This patch does that deletion, idempotently, on install/migrate.

Only the shipped template artifacts are removed: template pages, the group's
private components (`enamel_*`) and its grouped design tokens. User pages
created from the template (no `template_group`) are left untouched.
"""

import frappe

GROUP = "enamel"


def execute():
	for page in frappe.get_all(
		"Builder Page",
		filters={"is_template": 1, "template_group": GROUP},
		pluck="name",
	):
		safe_delete("Builder Page", page)

	for component in frappe.get_all(
		"Builder Component",
		filters={"component_id": ("like", f"{GROUP}\\_%")},
		pluck="name",
	):
		safe_delete("Builder Component", component)

	doctype = token_doctype()
	if frappe.get_meta(doctype).has_field("group"):
		for token in frappe.get_all(doctype, filters={"group": GROUP}, pluck="name"):
			safe_delete(doctype, token)


def token_doctype():
	"""Builder Variable was renamed to Builder Token; sites may carry either."""
	return "Builder Token" if frappe.db.exists("DocType", "Builder Token") else "Builder Variable"


def safe_delete(doctype, name):
	"""Best-effort delete that can never abort the migrate it runs in.

	A user page still referencing a removed component would raise
	LinkExistsError and `force` does not bypass every guard across versions,
	so swallow and log rather than halt `bench migrate`. Commit on success so
	a later failure's rollback can't undo earlier deletes.
	"""
	try:
		frappe.delete_doc(doctype, name, force=True, ignore_permissions=True)
		frappe.db.commit()
	except Exception:
		frappe.db.rollback()
		frappe.log_error(title=f"remove_enamel_templates: kept {doctype} {name}")
