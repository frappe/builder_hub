# Template Generation Prompts

Reusable prompts for generating Builder Hub template groups at the house quality bar.
Paste one into a session (or Builder AI) and fill the brackets. They encode the rules from
PLAN.md so the output lands in the pipeline instead of needing a rewrite.

## Master prompt

```
Create a new template group for builder_hub.

Business: [fictional business or product, one sentence. Give it a name and a voice.]
Category: [industry category from PLAN.md's matrix]
Aesthetic direction: [2-4 sentences. Name the genre and the mood, cite reference sites
  for GENRE ONLY, and say explicitly: do not copy their layout, copy, or trade dress.]

House rules (non-negotiable):
- Read builder_templates/PLAN.md first. Claim a structural archetype that is NOT in the
  registry table; add your row and a full YAML brief before building.
- 3-4 pages (home + 2-3 that fit the business). Unique single-word codename, next order
  number, correct categories.
- 5-7 Builder Variable color tokens with light AND dark values; every color in blocks and
  client-script CSS goes through var(--token, fallback). No raw hex anywhere else,
  including inline styles inside innerHTML.
- Google Fonts only, a deliberate pairing (display / body / mono). Real italics come from
  the ital-axis loader; use them if the design wants a voice.
- Imagery: [none, built from blocks | Pexels via pexels_api_key in common_site_config |
  Unsplash hotlinks]. If photographic: curate by contact sheet to ONE color register,
  never take the first search result.
- Motion: default to stillness. Subtle hover and focus transitions only; no entrance
  animations, kinetic type or counters unless this brief explicitly asks. Anything that
  does move ships as a CSS+JS pair armed only under a prefers-reduced-motion check, with
  the page complete without JS. Root block needs originalElement: "body". Custom data
  attributes, never data-track.
- Copy is witty, honest, specific. Real prices, real hours, deadpan asides. No em dashes.
- Verify live on builder-hub.localhost: sync, screenshot desktop + mobile + dark, click
  every interactive piece, fix, re-shoot. Generate 2560x1440 preview webps and confirm
  the catalog and bundle APIs serve the group.
```

## Genre prompts (fill the business, keep the direction)

Quiet editorial / component-gallery family (the plot genre):

```
A [dev tool / design tool / API product] site in the quiet editorial genre: bookish serif
display over a clean grotesk, vast whitespace, a narrow centered measure, one electric
accent used only for links and data. The product demos are LIVE, built from blocks and
CSS in borderless warm-grey cards, never screenshots. Include
a short signed letter from the maker and a masonry wall of one-line quotes set in serif
italic. Everything holds still; the typography carries the energy. The site should feel
like a well-set book that happens to ship software.
```

Minimal wireframe (the tide genre):

```
A [photo-led local business] site drawn as "the wireframe that shipped": every module a
sharp 1px outlined box, zero border radius, zero shadows. Photos live in fig-numbered
frames with mono caption tabs; facts live in hairline meta cells; one deliberate
placeholder joke stays unreplaced. Serif does the talking, mono does the labeling.
High-quality photography in one muted register carries all the warmth.
```

Classic kit modernized (the primer genre):

```
A neutral, broadly reusable [SaaS / business] starter where every section is the modern
rendition of a classic site-builder section: split hero with a block-built product mock,
logo marquee, icon feature grid, alternating splits, testimonials, accordion FAQ, CTA
band, multi-column footer. Soft inset panels, one brand accent, full dark mode. The most
re-purposable group in the catalog, not the loudest.
```

Glow SaaS (aurora's family, needs a new angle):

```
A dark product landing with restrained glow: gradient text used once, glass surfaces
used twice, and a bento grid where every tile does something (a working toggle, a
sparkline, a mono code snippet). Claim a structural twist aurora doesn't own.
```

Artifact conceit (the recipe/groove/chit family):

```
Pick an everyday printed or physical artifact [receipt, boarding pass, field guide,
prescription pad, seed packet, transit map] and build the ENTIRE site as that artifact,
with dense faithful furniture and deadpan copy. The artifact must be an object with
parts you can set type in, not a mood. Wit lands in the details (the fine print, the
stamps, the torn edges), and the business information stays genuinely usable.
```

Service vertical (the rivet..align batch):

```
A [trade / clinic / studio / firm] site that a real business could use tomorrow: strong
modern design system, honest voice ("the price is the price"), published prices, a real
schedule or process, and one signature structural idea no shipped group owns. Modern and
aesthetic beats clever; wit stays in the copy.
```

## Notes

- One template per prompt. Ask for options first ("pitch 3 archetypes, I'll pick") when
  the direction is open.
- "Like [site] but don't copy" means: identify the genre conventions (type scale, spacing
  temperature, furniture kinds), then invent different furniture, fonts, accent, copy and
  a different fictional business inside those conventions.
- The generator-script workflow lives in past session scratchpads (primer_gen.py,
  tide_gen.py, plot_gen.py pattern): block factory + component-instance mirroring +
  token var() references + client-script CSS/JS pair, emitted as fixtures.
