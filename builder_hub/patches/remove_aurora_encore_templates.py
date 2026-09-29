"""Remove the retired `aurora` and `encore` template groups from a site.

Same rationale as remove_ember_relay_templates: `reconcile_deleted_templates`
only prunes pages within still-shipped groups, so a wholly-removed group must
be deleted explicitly on install/migrate.
"""

from builder_hub.patches.remove_ember_relay_templates import _delete_group

RETIRED_GROUPS = ("aurora", "encore")


def execute():
	for group in RETIRED_GROUPS:
		_delete_group(group)
