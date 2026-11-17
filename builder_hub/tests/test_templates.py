from __future__ import annotations

import json

import frappe
from frappe.tests import IntegrationTestCase

from builder_hub import api
from builder_hub.patches import remove_low_use_templates


def make_template_page(group: str, blocks: list) -> str:
	"""A template page of `group`. Created as a plain page and flagged afterwards, so
	developer mode doesn't export a fixture group into the app while the test runs."""
	page = frappe.get_doc(
		{
			"doctype": "Builder Page",
			"page_title": f"{group} test page",
			"route": f"templates/{group}/{frappe.generate_hash(length=6)}",
			"draft_blocks": json.dumps(blocks),
		}
	).insert(ignore_permissions=True)
	frappe.db.set_value("Builder Page", page.name, {"is_template": 1, "template_group": group})
	return page.name


def make_component(component_id: str, data_script: str = "") -> str:
	frappe.get_doc(
		{
			"doctype": "Builder Component",
			"component_id": component_id,
			"component_name": component_id,
			"block": json.dumps({"blockId": "root", "element": "div", "children": []}),
			"component_data_script": data_script,
		}
	).insert(ignore_permissions=True)
	return component_id


def instance_of(component_id: str) -> dict:
	return {
		"blockId": frappe.generate_hash(length=8),
		"element": "div",
		"extendedFromComponent": component_id,
		"children": [],
	}


class TemplateBundleTests(IntegrationTestCase):
	def setUp(self):
		frappe.set_user("Administrator")
		self.group = f"zztest{frappe.generate_hash(length=6).lower()}"

	def test_bundle_carries_component_data_script(self):
		script = "component.rows = [{'label': row} for row in (props.get('entries') or [])]"
		component = make_component(f"{self.group}_list", script)
		page = make_template_page(
			self.group, [{"blockId": "root", "element": "div", "children": [instance_of(component)]}]
		)

		bundle = api._get_template_bundle(page, "test")

		shipped = {c["component_id"]: c for c in bundle["components"]}
		self.assertEqual(shipped[component]["component_data_script"], script)


class RemoveLowUseTemplatesTests(IntegrationTestCase):
	def setUp(self):
		frappe.set_user("Administrator")

	def test_removes_retired_groups_and_keeps_everything_else(self):
		component = make_component("scrap_zztest_nav")
		retired_page = make_template_page("scrap", [{"blockId": "root", "element": "div", "children": []}])
		token = frappe.get_doc(
			{
				"doctype": "Builder Token",
				"token_name": "zztest ink",
				"type": "Color",
				"value": "#111111",
				"group": "scrap",
			}
		).insert(ignore_permissions=True)
		kept_page = make_template_page("zzkept", [{"blockId": "root", "element": "div", "children": []}])
		# the patch commits after each delete, so the kept page outlives the test's rollback
		self.addCleanup(frappe.db.commit)
		self.addCleanup(frappe.delete_doc, "Builder Page", kept_page, force=True, ignore_permissions=True)

		remove_low_use_templates.execute()

		self.assertFalse(frappe.db.exists("Builder Page", retired_page))
		self.assertFalse(frappe.db.exists("Builder Component", component))
		self.assertFalse(frappe.db.exists("Builder Token", token.name))
		self.assertTrue(frappe.db.exists("Builder Page", kept_page))
