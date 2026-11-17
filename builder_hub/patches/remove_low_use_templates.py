"""Remove the retired `scrap`, `recipe`, `canvas`, `affiche`, `reel` and `fetch`
template groups from a site.

These were the least used groups: each was built around one niche concept that
real businesses could not adapt. Same rationale as remove_ember_relay_templates:
`reconcile_deleted_templates` only prunes pages within still-shipped groups, so
a wholly-removed group must be deleted explicitly on install/migrate.
"""

from builder_hub.patches.remove_ember_relay_templates import _delete_group

RETIRED_GROUPS = ("scrap", "recipe", "canvas", "affiche", "reel", "fetch")


def execute():
	for group in RETIRED_GROUPS:
		_delete_group(group)
