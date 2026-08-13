app_name = "builder_hub"
app_title = "Builder Hub"
app_publisher = "Frappe Technologies Pvt Ltd"
app_description = "Centralized hub of Frappe Builder page templates, plugins and components"
app_email = "suraj@frappe.io"
app_license = "mit"

# Apps
# ------------------

required_apps = ["builder"]

# Sync the hub's template fixtures into this site's DB (published, so their
# routes resolve for public Preview). Reuses builder's importer pointed at this
# app — builder imports nothing from builder_hub (avoids a circular dependency).
after_install = "builder_hub.install.after_install"
after_migrate = "builder_hub.install.after_migrate"

# Each item in the list will be shown as an app in the apps page
# add_to_apps_screen = [
# 	{
# 		"name": "builder_hub",
# 		"logo": "/assets/builder_hub/logo.png",
# 		"title": "Builder Hub",
# 		"route": "/builder_hub",
# 		"has_permission": "builder_hub.api.permission.has_app_permission"
# 	}
# ]

# Includes in <head>
# ------------------

# include js, css files in header of desk.html
# app_include_css = "/assets/builder_hub/css/builder_hub.css"
# app_include_js = "/assets/builder_hub/js/builder_hub.js"

# include js, css files in header of web template
# web_include_css = "/assets/builder_hub/css/builder_hub.css"
# web_include_js = "/assets/builder_hub/js/builder_hub.js"

# include custom scss in every website theme (without file extension ".scss")
# website_theme_scss = "builder_hub/public/scss/website"

# include js, css files in header of web form
# webform_include_js = {"doctype": "public/js/doctype.js"}
# webform_include_css = {"doctype": "public/css/doctype.css"}

# include js in page
# page_js = {"page" : "public/js/file.js"}

# include js in doctype views
# doctype_js = {"doctype" : "public/js/doctype.js"}
# doctype_list_js = {"doctype" : "public/js/doctype_list.js"}
# doctype_tree_js = {"doctype" : "public/js/doctype_tree.js"}
# doctype_calendar_js = {"doctype" : "public/js/doctype_calendar.js"}

# Svg Icons
# ------------------
# include app icons in desk
# app_include_icons = "builder_hub/public/icons.svg"

# Home Pages
# ----------

# application home page (will override Website Settings)
# home_page = "login"

# website user home page (by Role)
# role_home_page = {
# 	"Role": "home_page"
# }

# Generators
# ----------

# automatically create page for each record of this doctype
# website_generators = ["Web Page"]

# automatically load and sync documents of this doctype from downstream apps
# importable_doctypes = [doctype_1]

# Jinja
# ----------

# add methods and filters to jinja environment
# jinja = {
# 	"methods": "builder_hub.utils.jinja_methods",
# 	"filters": "builder_hub.utils.jinja_filters"
# }

# Installation
# ------------

# before_install = "builder_hub.install.before_install"
# after_install = "builder_hub.install.after_install"

# Uninstallation
# ------------

# before_uninstall = "builder_hub.uninstall.before_uninstall"
# after_uninstall = "builder_hub.uninstall.after_uninstall"

# Integration Setup
# ------------------
# To set up dependencies/integrations with other apps
# Name of the app being installed is passed as an argument

# before_app_install = "builder_hub.utils.before_app_install"
# after_app_install = "builder_hub.utils.after_app_install"

# Integration Cleanup
# -------------------
# To clean up dependencies/integrations with other apps
# Name of the app being uninstalled is passed as an argument

# before_app_uninstall = "builder_hub.utils.before_app_uninstall"
# after_app_uninstall = "builder_hub.utils.after_app_uninstall"

# Desk Notifications
# ------------------
# See frappe.core.notifications.get_notification_config

# notification_config = "builder_hub.notifications.get_notification_config"

# Permissions
# -----------
# Permissions evaluated in scripted ways

# permission_query_conditions = {
# 	"Event": "frappe.desk.doctype.event.event.get_permission_query_conditions",
# }
#
# has_permission = {
# 	"Event": "frappe.desk.doctype.event.event.has_permission",
# }

# Document Events
# ---------------
# Hook on document methods and events

# doc_events = {
# 	"*": {
# 		"on_update": "method",
# 		"on_cancel": "method",
# 		"on_trash": "method"
# 	}
# }

# Scheduled Tasks
# ---------------

# scheduler_events = {
# 	"all": [
# 		"builder_hub.tasks.all"
# 	],
# 	"daily": [
# 		"builder_hub.tasks.daily"
# 	],
# 	"hourly": [
# 		"builder_hub.tasks.hourly"
# 	],
# 	"weekly": [
# 		"builder_hub.tasks.weekly"
# 	],
# 	"monthly": [
# 		"builder_hub.tasks.monthly"
# 	],
# }

# Testing
# -------

# before_tests = "builder_hub.install.before_tests"

# Extend DocType Class
# ------------------------------
#
# Specify custom mixins to extend the standard doctype controller.
# extend_doctype_class = {
# 	"Task": "builder_hub.custom.task.CustomTaskMixin"
# }

# Overriding Methods
# ------------------------------
#
# override_whitelisted_methods = {
# 	"frappe.desk.doctype.event.event.get_events": "builder_hub.event.get_events"
# }
#
# each overriding function accepts a `data` argument;
# generated from the base implementation of the doctype dashboard,
# along with any modifications made in other Frappe apps
# override_doctype_dashboards = {
# 	"Task": "builder_hub.task.get_dashboard_data"
# }

# exempt linked doctypes from being automatically cancelled
#
# auto_cancel_exempted_doctypes = ["Auto Repeat"]

# Ignore links to specified DocTypes when deleting documents
# -----------------------------------------------------------

# ignore_links_on_delete = ["Communication", "ToDo"]

# Request Events
# ----------------
# before_request = ["builder_hub.utils.before_request"]
# after_request = ["builder_hub.utils.after_request"]
after_request = ["builder_hub.api.allow_template_embedding"]

# Job Events
# ----------
# before_job = ["builder_hub.utils.before_job"]
# after_job = ["builder_hub.utils.after_job"]

# User Data Protection
# --------------------

# user_data_fields = [
# 	{
# 		"doctype": "{doctype_1}",
# 		"filter_by": "{filter_by}",
# 		"redact_fields": ["{field_1}", "{field_2}"],
# 		"partial": 1,
# 	},
# 	{
# 		"doctype": "{doctype_2}",
# 		"filter_by": "{filter_by}",
# 		"partial": 1,
# 	},
# 	{
# 		"doctype": "{doctype_3}",
# 		"strict": False,
# 	},
# 	{
# 		"doctype": "{doctype_4}"
# 	}
# ]

# Authentication and authorization
# --------------------------------

# auth_hooks = [
# 	"builder_hub.auth.validate"
# ]

# Automatically update python controller files with type annotations for this app.
export_python_type_annotations = True

# Require all whitelisted methods to have type annotations
require_type_annotated_api_methods = True

# default_log_clearing_doctypes = {
# 	"Logging DocType Name": 30  # days to retain logs
# }

# Translation
# ------------
# List of apps whose translatable strings should be excluded from this app's translations.
# ignore_translatable_strings_from = []

