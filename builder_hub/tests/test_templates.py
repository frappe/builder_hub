from __future__ import annotations

import json

import frappe
from frappe.tests import IntegrationTestCase

from builder_hub import api


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

