# Builder Hub

A centralized hub of [Frappe Builder](https://github.com/frappe/builder) page templates
(and, in future, plugins and components). Builder sites fetch the catalog and per-page
bundles from a Builder Hub site over HTTP, so templates get their own release cycle -
users always get the latest without upgrading the builder app.

Each template is a real Builder Page (`is_template = 1`) grouped under a `template_group`,
sharing a set of Builder Components and Variables. Groups are bundled as fixtures under
`builder_hub/builder_templates/<group>/` and synced into the hub site on install/migrate.

## Templates

Eight multi-page template groups. Each has a shared navbar/footer + theme
across its pages, with a built-in light/dark toggle.

### Fronds

An earthy multi-page starter for boutique brands.

![Fronds - Landing](builder_hub/www/builder_assets/fronds/fronds_landing/preview.webp)

**Pages:** Landing · About · Contact

---

### Atelier

A bold studio site for agencies and freelancers: oversized type, a geometric inline-SVG
hero, a services index, a selected-work grid, and a built-in contact form.

![Atelier - Home](builder_hub/www/builder_assets/atelier/atelier_home/preview.webp)

**Pages:** Home · Work · Contact

---

### Mono

A dark, bold-type portfolio for studios and freelancers.

![Mono - Home](builder_hub/www/builder_assets/mono/mono_home/preview.webp)

**Pages:** Home · Project (case study) · About · Contact

---

### Verso

An ultra-minimal personal site: a fixed left sidebar, typographic lists instead of cards,
and a near-monochrome palette.

![Verso - Home](builder_hub/www/builder_assets/verso/verso_home/preview.webp)

**Pages:** Home · Work · Writing · About

---

### Husk

An ultra-minimal, warm-toned personal site with a centered single column and a slim nav.

![Husk - Home](builder_hub/www/builder_assets/husk/husk_home/preview.webp)

**Pages:** Home · Work · About

---

### Quill

A clean editorial template for blogs and publications: a featured story, a typographic
article index, and a full reading layout with pull-quotes and an author note.

![Quill - Home](builder_hub/www/builder_assets/quill/quill_home/preview.webp)

**Pages:** Home · Article · About

---

### Commit

A vivid conference starter with an animated hero and live countdown, a speaker grid, a
two-day schedule, and ticket tiers. Ships with scroll-reveal and marquee client scripts.

![Commit - Home](builder_hub/www/builder_assets/commit/commit_home/preview.webp)

**Pages:** Home · Speakers · Schedule · Tickets

---

### Forge

An icon-rich SaaS / devtools starter with a teal palette and Space Grotesk type: a stat
strip, a nine-feature grid, a sixteen-integration wall, spotlights, an eighteen-item
capability checklist, plans, and FAQ cards.

![Forge - Home](builder_hub/www/builder_assets/forge/forge_home/preview.webp)

**Pages:** Home · Features · Pricing

## How it works

- **`builder_hub.api.get_catalog()`** (guest) - returns the template groups + their pages
  with absolute preview and `live_url`s, for any builder site's template picker.
- **`builder_hub.api.get_template_bundle(page)`** (guest) - returns one template page plus
  its shared components, variables, client scripts and fonts as import-ready dicts.
- A builder site points at the hub via `template_hub_url` in its site config (or
  `common_site_config.json` bench-wide), fetches the catalog, and materializes a page from
  the bundle on demand. The "Preview" action opens the hub's published page in a new tab.

Template content lives in this app; the import/export machinery lives in `builder`
(`builder.template_sync`), which this app reuses - `builder_hub` depends on `builder`.

## Installation

You can install this app using the [bench](https://github.com/frappe/bench) CLI:

```bash
cd $PATH_TO_YOUR_BENCH
bench get-app $URL_OF_THIS_REPO --branch develop
bench install-app builder_hub
```

`builder_hub` requires the `builder` app (installed automatically as a dependency).

## Contributing

This app uses `pre-commit` for code formatting and linting. Please [install pre-commit](https://pre-commit.com/#installation) and enable it for this repository:

```bash
cd apps/builder_hub
pre-commit install
```

Pre-commit is configured to use the following tools for checking and formatting your code:

- ruff
- eslint
- prettier
- pyupgrade

## License

mit
