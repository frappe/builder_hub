"""Fast delivery of template previews and assets to builder sites.

Page previews are 2560x1440 screenshots, but the template picker shows them
~220px wide. So the catalog also points at small thumbnails, and /builder_assets/
media goes out cacheable instead of with Frappe's default no-store.
"""

import hashlib
import re
from pathlib import Path

import frappe
from PIL import Image

ASSETS_PREFIX = "/builder_assets/"
THUMBNAIL_WIDTH = 640
# <preview stem>-thumb-<first 8 hex of the preview's md5>.webp
THUMBNAIL_NAME = re.compile(r"-thumb-[0-9a-f]{8}\.webp$")
MEDIA_TYPES = ("image/", "font/", "video/")


def get_thumbnail_url(preview_url: str | None) -> str | None:
	"""Site-relative thumbnail URL for a /builder_assets/ preview. None when there is
	no preview file or the thumbnail can't be written; the picker then uses the preview."""
	preview_path = resolve_asset_path(preview_url)
	if not preview_url or not preview_path:
		return None
	try:
		thumbnail_path = PreviewThumbnail(preview_path).ensure()
	except Exception:
		frappe.log_error(f"Failed to create template thumbnail for {preview_url}")
		return None
	folder_url = preview_url.split("?", 1)[0].rsplit("/", 1)[0]
	return f"{folder_url}/{thumbnail_path.name}"


def set_asset_cache_headers(response=None, request=None):
	"""Let browsers cache /builder_assets/ media. Frappe defaults every response to
	no-store, so previews and hot-linked template images were refetched on every view."""
	if request is None or response is None or response.status_code != 200:
		return
	if not request.path.startswith(ASSETS_PREFIX):
		return
	# dynamic routes share the prefix (tokens.css) and must stay fresh
	if not (response.mimetype or "").startswith(MEDIA_TYPES):
		return
	if THUMBNAIL_NAME.search(request.path):
		# the name carries the content hash, so a cached copy can never go stale
		response.headers["Cache-Control"] = "public, max-age=31536000, immutable"
	else:
		response.headers["Cache-Control"] = "public, max-age=86400, stale-while-revalidate=604800"


class PreviewThumbnail:
	"""Downscaled copy of a preview, stored beside it. Named after the preview's content
	hash, so a regenerated preview gets a new thumbnail URL and old copies are dropped."""

	def __init__(self, preview_path: Path):
		self.preview_path = preview_path
		digest = hashlib.md5(preview_path.read_bytes()).hexdigest()[:8]
		self.path = preview_path.with_name(f"{preview_path.stem}-thumb-{digest}.webp")

	def ensure(self) -> Path:
		if not self.path.exists():
			self.generate()
			self.remove_outdated()
		return self.path

	def generate(self):
		with Image.open(self.preview_path) as image:
			image = image.convert("RGB")
			# bound by width only, so tall previews stay sharp under object-cover
			image.thumbnail((THUMBNAIL_WIDTH, image.height), Image.Resampling.LANCZOS)
			# write aside and rename, so concurrent requests never serve a partial file
			partial_path = self.path.with_name(f".{self.path.name}.{frappe.generate_hash(length=6)}")
			image.save(partial_path, "WEBP", quality=80, method=6)
			partial_path.replace(self.path)

	def remove_outdated(self):
		for path in self.preview_path.parent.glob(f"{self.preview_path.stem}-thumb-*.webp"):
			if path != self.path:
				path.unlink(missing_ok=True)


def resolve_asset_path(url: str | None) -> Path | None:
	"""File behind a /builder_assets/ URL, looked up the way Frappe's StaticPage
	serves it: the first installed app whose www folder has it."""
	if not isinstance(url, str) or not url.startswith(ASSETS_PREFIX):
		return None
	relative_path = url.split("?", 1)[0].lstrip("/")
	for app in frappe.get_installed_apps():
		www_path = Path(frappe.get_app_path(app, "www")).resolve()
		path = (www_path / relative_path).resolve()
		if path.is_relative_to(www_path) and path.is_file():
			return path
	return None
