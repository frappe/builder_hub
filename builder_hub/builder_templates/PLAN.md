# Template Library Plan

Design briefs for the industry-organized template library. This doc is the source of truth for
what gets built; it is not consumed by code. Each brief below is authored first, then turned into
a real fixture group in this directory (same pipeline as `lull`, `keys`, `verge`).

Rules that apply to every template:

- Each template is a `template_group` of 3-4 pages: home, products/services, about, contact
  (page names adapt to the business, e.g. "menu" is the products page of a restaurant).
- Each template must own a distinct **structural archetype**: nav shape, hero shape, section
  shapes and footer must differ from every other shipped group. Distinct fonts and palettes are
  not enough. See the archetype registry below.
- Palette is 5-7 named `Builder Variable` colors with light + dark hex values. Dark-first
  templates set `dark_value: None` and `color-scheme: dark` in group CSS (the `verge` pattern).
- Fonts come from Google Fonts. Italics need a CSS `@import ...:ital@0;1` client script,
  the built-in font loader only carries `wght`.
- Imagery hotlinks `images.unsplash.com` (established pattern across groups).
- Codenames are unique single words. Taken: field, fronds, husk, keys, lull, mono, nook,
  quill, verge, verso, plus every built group below (through tally and intake).
  Retired, do not reuse: forge, grain, copper, ware, beacon, signal, quip, hex, prism,
  tally, intake, prospect (the Jul 2026 SaaS/app-UI batch and its prospectus follow-up were
  all retired; the user's direction is Framer-grade polish or a conceit that lands),
  commit (original conference starter, retired Jul 17 2026), arcade (CRT cabinet, strong
  execution but retired on user preference), cobalt and hustle
  (Jul 2026 marketing batch, retired same week: competent genre executions without a strong
  conceit; the bar is what a top design agency would ship), fathom (scroll-dive freediving
  school, retired Jul 19 2026: technically slick scrollytelling but atmospheric rather than
  artifact-like; the lesson is that conceits must be objects with furniture, not moods).
- Templates need not be themed (light/dark toggle optional): app-UI and product templates may
  ship a single neutral look, but every color still goes through Builder Variables so the whole
  template rethemes by editing the palette.
- Motion is welcome but must degrade: ember set the pattern with a CSS + JavaScript client
  script pair (IntersectionObserver reveal-on-scroll with stagger classes, marquee, Ken Burns,
  view-timeline parallax as progressive enhancement). The JS arms hidden states only when
  `prefers-reduced-motion` allows, so no-JS and reduced-motion users see a complete static page.
  Pipeline gotcha: a page's root block must carry `"originalElement": "body"` (Builder's canvas
  convention) or JavaScript client scripts are never rendered into the published page. Second
  gotcha: Builder stamps `data-track` on rendered blocks for click analytics, so custom
  waypoint attributes must use another name (groove uses `data-tune`).

## Archetype registry (shipped groups)

| Group  | Archetype |
|--------|-----------|
| fronds | earthy starter, standard hero + sections |
| mono   | dark oversized-type portfolio |
| verso  | ultra minimal fixed sidebar |
| husk   | warm centered single column |
| quill  | clean editorial blog, article layouts |
| lull   | arch photo hero + circle rows, weekly schedule |
| nook   | full-viewport overlay chapters |
| keys   | fixed-sidebar app shell, listings as rows |
| field  | newspaper three-column front page, drop caps |
| verge  | dark type-over-photo, rotated posters, tour list |
| hem    | hairline viewport frame, corner nav, numbered ledger rows |
| silk   | dark mirrored 50/50 splits, stacked monogram nav, numeral collection |
| tulle  | layered offset tissue panels, script overlays, pill nav, RSVP card footer |
| denim  | bordered cells, marquee tickers, rotated stickers, checkerboard grid |
| pleat  | magazine spreads with folio bars, paired portrait+detail images, colophon |
| ridge  | gapless photo mosaic wall, hover captions, overlay nav |
| canvas | site as a live design file: dotted canvas, selection boxes, cursors, comments |
| vitae  | document: paper sheet on a desk, letterhead, date-left CV entries |
| reel   | screening room: letterboxed 21:9 stills, timecodes, slate cards, credits crawl |
| margin | book page: reading column + numbered margin notes, dotted-leader TOC |
| plinth | drawing set: type-only index with hover thumbnails, sheet furniture, titleblock |
| encore | keynote: spotlight hero, act rules, footlit demo frame, stage notes, applause, one more thing |
| aurora | glow SaaS landing: gradient hero + text, glass bento grid, glowing product frame, quote wall |
| bureau | agency mega-type: acid highlight marks, typographic case covers, numbered service mega-list |
| scrap  | zine paste-up: torn rotated panels, masking tape, xerox photos, ransom headlines, staples |
| affiche | poster wall: full-viewport swiss posters, diagonal bands, vertical rails, catalog table |
| annum  | year timeline: split ledger hero, spine timeline with year dots and big photos, ledger |
| recipe | recipe cards: ruled index cards with red margin rules, dog-ears, chef's margin notes, stamps, tear-off coupon |
| candor | statement screens: full-viewport one-color statement hero, cropped mega wordmark, serif fee table, no photos |
| fetch  | product bento: super-rounded pastel tiles, blob photo frames, star reviews, size table, guarantee card |
| ember  | hearth menu-card: split wordmark/photo hero, hours marquee rule, roman-numeral snap strip, double-hairline menu frames, reserve-banner footer, scroll-reveal motion |
| groove | the record: scroll-spun CSS vinyl hero with tonearm-as-progress, NOW PLAYING pill retuning per section, back-of-sleeve tracklist panels, 45-single stat discs, vinyl video bands, sleeves that eject their disc on hover, crate-flip roster, hype stickers, runout-groove marquee footer with CSS barcode |
| gambit | the annotated game: score-sheet move rows with notation and italic commentary, CSS chessboard diagrams with unicode pieces, ECO-coded service openings, engine-eval results, time-control pricing, monochrome warm greys |
| chit   | the till receipt: every page a thermal receipt (zigzag torn edges, dashed rules, dotted price leaders), print-feed hero from a printer slot, punch-card loyalty, 86'd strikethrough items, barcode stubs, Courier Prime only |
| optic  | the eye chart: shrinking Snellen hero rows with 20/x acuity margins and a lean-in joke line, blur-to-focus reveals, pure-CSS line-drawn frames, prescription-pad Rx grid, black on white |
| rivet  | industrial trades: concrete paper + safety orange, Archivo caps, grayscale duotone job photos, numbered service cards, honest fixed-price rows, dark pricing manifesto, fixed 24/7 emergency strip, ticker, count-up stats |
| enamel | soft clinical: warm cream + one clinical blue, Plus Jakarta Sans, pill buttons, morphing-blob hero portrait with bobbing chips, rounded fee tables, minute-by-minute first-visit timeline, blue CTA card |
| counsel| quiet ivory law: Source Serif 4 + Inter small caps, hairline rules, numbered practice-index rows with hover indent, dark outcomes band with serif numerals, grayscale-to-color portraits, italic "in practice" asides |
| uptime | status page as brand: deep slate + status green, Space Grotesk, pulsing operational pill, staggered uptime tick bar, counting SLA stats, glass sticky nav, partner wall panels, case-study stat grids, per-seat tiers |
| tempo  | gym poster: near-black + volt, Anton caps, duotone photos, volt ticker, real weekly class grid (h-scroll on mobile), hard-shadow button hovers, volt quote panel, house-rules ledger |
| spruce | the checklist: airy white + leaf green, Figtree, literal checkbox rows with staggered tick-in, floating today-card over hero photo, public rates table, written scopes, 53-point-clean card |
| align  | warm clinic: bone + clay, Fraunces over Karla, condition-first card nav ("where does it catch?"), four-stage recovery arc with dot rail, initial-avatar clinician cards, minute-by-minute assessment card |

New briefs must claim an archetype not on this list, and the list grows as templates ship.

## Category matrix

Industry categories replace the current gallery taxonomy (Marketing / Editorial / Portfolio /
Local business). Existing groups get re-tagged into these when the first new template ships.
Five template slots per category, each with a different theme.

Templates can carry MULTIPLE picker categories (Jul 17 2026): the gallery lists a group under
every category in its manifest. Current multi-category groups: fronds, verge, bureau (Marketing
crossovers), hem, tulle, denim, pleat (Fashion crossovers), margin, affiche (Portfolio
crossovers), encore, aurora (Technology + Marketing).

### Education (trustworthy blues and greens, friendly)
| Codename | Theme | Concept |
|----------|-------|---------|
| slate    | light | K-12 school, calm blue, term dates and admissions |
| quad     | bright | university department, bold collegiate color blocking |
| crayon   | pastel | preschool / daycare, soft primaries, rounded shapes |
| atlas    | editorial | online academy, course catalog as a syllabus |
| chalk    | dark | exam-prep / coaching institute, chalkboard green-black |

### Agency & Studio (bold type, one loud accent), bureau BUILT Jul 2026
| Codename | Theme | Concept |
|----------|-------|---------|
| bureau   | bright | Framer-grade agency: mega type, acid marks, typographic case covers (built: 3 pages, order 26, category Marketing) |

### Fashion (high contrast, editorial, photo-led), BUILT Jul 2026, orders 13-17
| Codename | Theme | Concept |
|----------|-------|---------|
| hem      | minimal | atelier / tailor, white space, hairline type (built: 3 pages) |
| silk     | dark | evening-wear label, black with champagne accents (built: 4 pages) |
| tulle    | pastel | bridal boutique, blush and ivory (built: 3 pages) |
| denim    | bright | streetwear drop site, saturated color, big product tiles (built: 4 pages) |
| pleat    | editorial | seasonal lookbook, magazine spreads (built: 3 pages) |

### Food & Beverage (warm ambers, creams, deep reds)
| Codename | Theme | Concept |
|----------|-------|---------|
| ember    | dark | wood-fire fine dining, charcoal and ember orange (built: 4 pages, order 34, brief below) |
| crumb    | light minimal | artisan bakery, flour white, one warm accent |
| scoop    | bright pastel | gelato café, candy colors, playful shapes |
| graze    | editorial | farm-to-table restaurant, producer stories |
| zest     | sunshine | street-food brand, citrus yellow, bold stickers |

### Portfolio & Personal (one person, one voice; joins husk/mono/verso), BUILT Jul 2026, orders 18-22
| Codename | Theme | Concept |
|----------|-------|---------|
| ridge    | dark | photographer, gapless photo mosaic wall, index overlay (built: 3 pages) |
| canvas   | bright | designer, site as a live design file with comments left in (built: 3 pages) |
| vitae    | minimal | consultant CV as a paper sheet on a desk, letterhead and entries (built: 3 pages) |
| reel     | dark | filmmaker, letterboxed 21:9 stills with timecode captions (built: 3 pages) |
| margin   | warm light | writer/academic, body column with numbered margin notes (built: 3 pages) |
| plinth   | minimal | architects, type-only project index with drawing-sheet furniture (built: 3 pages) |
| scrap    | paper | graphic designer, cut-and-paste zine: torn panels, tape, xerox, ransom type (built: 3 pages, order 27) |
| affiche  | bright | design studio, site as a series of swiss posters, type only (built: 3 pages, order 28) |
| annum    | moss light + dark | maker's one-project-a-year photo timeline, user-spec (built: 3 pages, order 29) |

### Manufacturing & Industrial (steel blue, gray, safety-orange accents)
| Codename | Theme | Concept |
|----------|-------|---------|
| girder   | light | steel fabricator, blueprint blues, spec tables |
| lathe    | dark | precision CNC shop, machined gray, tolerance callouts |
| crate    | bright | packaging / logistics, kraft brown and safety orange |
| weld     | bold | metalworks, industrial black-yellow hazard accents |
| gauge    | minimal | engineering consultancy, gray scale, one blue accent |

### Professional Services (navy, slate, restrained accents)
| Codename | Theme | Concept |
|----------|-------|---------|
| ledger   | light | accounting firm, crisp white, forest green accent |
| counsel  | dark | law firm, deep navy, serif authority |
| compass  | bright | management consulting, confident color, case results |
| docket   | editorial | boutique legal practice, document-like layouts |
| mint     | pastel | payroll / HR services, mint and cream, friendly |

### Health & Wellness (sage, soft neutrals, calm)
| Codename | Theme | Concept |
|----------|-------|---------|
| sage     | pastel | day spa, sage green, soft arcs |
| pulse    | bright | fitness studio, energetic red-coral, class grid |
| haven    | light | therapy practice, warm neutrals, gentle type |
| align    | minimal | physiotherapy / chiropractic, clinical white, teal |
| tonic    | dark | strength gym, near-black, electric lime |

### Travel & Hospitality (sky, sand, saturated and photo-forward)
| Codename | Theme | Concept |
|----------|-------|---------|
| drift    | light | travel agency, sky blue, itinerary cards |
| dune     | pastel | desert resort, sand and terracotta |
| fjord    | dark | adventure tour operator, deep teal, expedition log |
| plaza    | bright | city hotel, jewel tones, amenity grid |
| tide     | minimal | coastal B&B, sea glass, quiet type |

### Technology / SaaS (electric accents on dark or clean white), encore + aurora BUILT Jul 2026
| Codename | Theme | Concept |
|----------|-------|---------|
| encore   | dark | SaaS site staged as a product keynote, user-picked conceit (built: 3 pages, order 24) |
| aurora   | dark | Framer-grade glow landing: glass bento, gradient text (built: 3 pages, order 25) |
| orbit    | bright | product landing, gradient accents, feature orbits |
| stack    | minimal | B2B platform, gray scale, integration logos |
| neon     | bold | startup launch, electric violet on off-black |
| (dev tool slot) | dark | developer-tool marketing; first build (hex) retired Jul 2026, rebuild wants a conceit |

### Apps & Dashboards (persona-survey driven: web_app_ui 63 + dashboard 17 + internal_tool 18 of 217 signups; theme-less, variable-driven, no photos)
First builds (tally: dashboard shell, intake: internal tool) retired Jul 2026: technically
clean but generic mockups, no conceit. The demand is real; rebuilds must find the wit first.
| Codename | Theme | Concept |
|----------|-------|---------|
| (dashboard slot) | neutral | analytics dashboard shell; first build (tally) retired |
| (internal tool slot) | neutral | request queue / approvals; first build (intake) retired |
| roster   | neutral | team directory / lightweight CRM: people cards, profile page |
| console  | neutral | admin console: settings-heavy, permissions matrix, API keys |
| beam     | neutral | status page: uptime bars, incident history, subscribe |

## Brief schema

Every template gets one YAML brief in this doc before it is built. The fields map 1:1 onto the
fixture pipeline artifacts:

```yaml
codename:      # unique single word, becomes template_group and page-name prefix
category:      # industry category above, goes into template.json categories
title:         # display title, goes into template.json
description:   # one line for template.json
theme:         # light | dark | bright | pastel | minimal | editorial | sunshine | bold
concept: >     # short pitch of the fictional business the template portrays
palette:       # maps to Builder Variable rows (name, value, dark_value)
  - {name: paper, value: "#FFFFFF", dark_value: "#111111"}   # dark-first: dark_value: null
fonts:
  display:     # Google Font for headlines
  body:        # Google Font for copy
archetype: >   # the unique structural skeleton: nav, hero, section shapes, footer
imagery: >     # Unsplash art direction and example search terms
pages:         # 3-4 pages; route "/" is the home page
  - name:      # <codename>_<page>
    route:
    title:
    sections:  # ordered section-by-section outline
```

## Brief: ember (Food & Beverage, dark), BUILT Jul 2026

Built Jul 19 2026 to the brief below, with these deviations: 4 pages (home / menu / about /
contact), order 34; the chef is Elias Voss (male, to match the available dark-kitchen
photography); the tasting runs seven courses, not six, so the hero reads "One fire, seven
courses, no shortcuts." First group to ship the motion system: `ember_motion` (JS) arms
`em-rise` reveal-on-scroll with stagger delays via IntersectionObserver, `ember_styles` (CSS)
carries a Ken Burns hero, the hours marquee under the hero, hover zoom/lift/underline
micro-interactions, a scroll-snap course strip with `scroll-padding`, and a `view()`-timeline
parallax on the sparks band gated behind `@supports`. Everything is inert under
`prefers-reduced-motion` and without JavaScript.

```yaml
codename: ember
category: Food & Beverage
title: Ember
description: A dark wood-fire restaurant with a framed menu card and course strip.
theme: dark
concept: >
  Ember is a 24-seat wood-fired tasting room. Everything is cooked over a single open hearth.
  The site should feel like the room: dim, warm, unhurried. Candlelit photography, generous
  spacing, a single flame-orange accent used sparingly. The primary conversion is a table
  reservation, so hours and the reserve action stay visible on every page.
palette:            # dark-first, dark_value: null on all rows, color-scheme: dark in group CSS
  - {name: char,  value: "#141110", dark_value: null}   # page background, warm charcoal
  - {name: smoke, value: "#201B18", dark_value: null}   # raised surfaces, cards
  - {name: bone,  value: "#EDE4D6", dark_value: null}   # primary text, warm cream
  - {name: ash,   value: "#9E9486", dark_value: null}   # muted text, captions
  - {name: seam,  value: "#382F29", dark_value: null}   # hairlines, borders, menu frame
  - {name: flame, value: "#E2571B", dark_value: null}   # accent: links, reserve CTA, numerals
fonts:
  display: Fraunces        # high-contrast warm serif; italic needs the ital @import script
  body: Figtree
archetype: >
  Printed-menu-card structure. Nav is a hairline top bar with links split left and right of a
  centered wordmark, reserve button far right. Home hero is full viewport, split 60/40: left is
  the stacked oversized serif wordmark over a one-line promise, right is a full-bleed hearth
  photo; a thin rule under the hero carries hours and address as a single running line. Courses
  appear as a horizontal scroll-snap strip with large roman numerals (I, II, III). The menu page
  is a centered menu-card column inside a double hairline frame (seam color), dish left, price
  right. Footer is a full-width reservation banner with an oversized serif line, then a
  three-column info row. No other group uses framed-card sections or a numbered snap strip.
imagery: >
  Moody, low-key, warm-toned Unsplash photography. Open-fire kitchens, plated dishes on dark
  ceramics, candlelit tables, chef hands at the pass. Searches: "wood fired cooking", "fine
  dining dark", "plated dish dark background", "restaurant candlelight interior". Avoid bright
  daylight shots; every image should sit comfortably on the char background.
pages:
  - name: ember_home
    route: /
    title: Ember, wood-fired tasting room
    sections:
      - Hero: split wordmark + hearth photo, reserve button, hours/address rule underneath
      - Tonight at the hearth: three signature dishes as photo cards on smoke surfaces
      - The courses: horizontal snap strip, roman numerals, one line per course
      - Ambiance band: full-width interior photo with a short pull quote in Fraunces italic
      - Reserve banner footer: oversized "Reserve a table", phone, address, hours columns
  - name: ember_menu
    route: /menu
    title: Menu
    sections:
      - Page header: small-caps "Menu", date line, one-line note on sourcing
      - Tasting menu: double hairline framed card, seven numbered courses, price for the set
      - A la carte: two framed columns (hearth / garden), dish name left, price right
      - Wine note: short paragraph on the list, ash-colored, with a flame link to enquire
      - Reserve banner footer (shared component)
  - name: ember_about
    route: /about
    title: About
    sections:
      - Opening statement: full-width serif paragraph on cooking with fire
      - Chef story: portrait photo beside two columns of copy
      - Philosophy row: three short principles (fire, seasons, patience) with roman numerals
      - Team strip: small portraits with name and role captions
      - Reserve banner footer (shared component)
  - name: ember_contact
    route: /contact
    title: Contact
    sections:
      - Reservation block: hours table on smoke surface, phone and email as flame links
      - Find us: address, directions note, landmark photo (no embedded map)
      - Private dining: short paragraph and enquiry mailto CTA
      - Reserve banner footer (shared component)
components: [ember_nav, ember_reserve_footer]
```

## Brief: hem (Fashion, minimal)

```yaml
codename: hem
category: Fashion
title: Hem
description: A minimal atelier site framed by a hairline border, with numbered services.
theme: minimal
concept: >
  Hem is a made-to-measure atelier. Quiet luxury: warm off-whites, one clay accent, huge
  whitespace. The site sits inside a fixed hairline frame, like a garment seam around the
  viewport. Conversion is a fitting appointment.
palette:
  - {name: paper, value: "#FAF9F7", dark_value: "#171512"}
  - {name: ink,   value: "#1C1A17", dark_value: "#EDEAE4"}
  - {name: muted, value: "#8B857C", dark_value: "#948E84"}
  - {name: line,  value: "#E7E3DC", dark_value: "#2B2823"}
  - {name: clay,  value: "#A56B46", dark_value: "#C08D63"}
  - {name: wash,  value: "#F1EEE9", dark_value: "#201D19"}
fonts: {display: Cormorant Garamond, body: Karla}   # italic via @import script
archetype: >
  Hairline viewport frame (fixed inset border on every page). Nav lives inside the frame
  corners: brand top-left, links top-right, no bar. Hero is mostly whitespace: giant lowercase
  serif wordmark anchored bottom-left, one small offset portrait top-right. Sections are
  numbered ledger rows (No. 01 / 02 / 03) with hairline top rules and off-center two-column
  bodies. Footer is a single centered line inside the frame. No other group frames the viewport
  or numbers its sections.
imagery: >
  Tailoring close-ups, fabric bolts, pinned muslin, quiet studio corners. Warm light, muted
  tones. Searches: "tailor atelier", "fabric texture", "sewing studio", "minimal clothing rail".
pages:
  - {name: hem_home, route: /, sections: [corner nav + framed whitespace hero, numbered craft rows (cut, cloth, finish), single large studio image band, appointment line footer]}
  - {name: hem_services, route: /services, sections: [page header with No. index, made-to-measure / alterations / wardrobe edit as ledger rows with prices, process timeline as numbered hairline list, appointment line footer]}
  - {name: hem_studio, route: /studio, sections: [about the cutter (portrait + two-column story), studio images pair, visit block (hours, address, fitting appointment mailto), footer]}
components: [hem_frame_nav, hem_footer_line]
```

## Brief: silk (Fashion, dark)

```yaml
codename: silk
category: Fashion
title: Silk
description: A dark evening-wear house with mirrored splits and a champagne hairline.
theme: dark
concept: >
  Silk is an evening-wear label: bias-cut gowns, black-tie tailoring. Near-black pages, ivory
  type, one champagne accent. Composed, symmetrical, slow. Conversion is a private appointment.
palette:            # dark-first, dark_value: null, color-scheme: dark
  - {name: noir,      value: "#0D0B09", dark_value: null}
  - {name: onyx,      value: "#171310", dark_value: null}
  - {name: ivory,     value: "#F2EBDD", dark_value: null}
  - {name: fog,       value: "#A2937D", dark_value: null}
  - {name: seam,      value: "#2E2820", dark_value: null}
  - {name: champagne, value: "#C9A15E", dark_value: null}
fonts: {display: Italiana, body: Jost}
archetype: >
  Mirrored 50/50 splits. Nav is centered and stacked: monogram above a letterspaced links row,
  hairline below. Every section is a half/half split that alternates image side, divided by a
  champagne hairline down the center. Collection pieces are tall runway-crop images with roman
  numeral captions. Footer is a centered monogram over a small-caps address line. No other
  group is built from alternating center-ruled splits.
imagery: >
  Evening gowns, black tailoring, low-key editorial portraits. Deep shadows, warm highlights.
  Searches: "evening gown dark", "black dress editorial", "suit low key portrait".
pages:
  - {name: silk_home, route: /, sections: [stacked monogram nav, split hero (gown photo / house statement), three mirrored feature splits (gowns, tailoring, appointments), champagne pull-quote, monogram footer]}
  - {name: silk_collection, route: /collection, sections: [collection header with season line, runway-crop pieces as alternating splits with numerals and fabric notes, price-on-request note, monogram footer]}
  - {name: silk_house, route: /house, sections: [house story split (portrait / two columns), craft principles as numeral rows, atelier image split, monogram footer]}
  - {name: silk_appointments, route: /appointments, sections: [appointment statement, private fitting details split (hours+address / what to expect), enquiry mailto CTA, monogram footer]}
components: [silk_nav, silk_footer]
```

## Brief: tulle (Fashion, pastel)

```yaml
codename: tulle
category: Fashion
title: Tulle
description: A blush bridal boutique with layered tissue panels and script accents.
theme: pastel
concept: >
  Tulle is a bridal boutique. Blush, ivory, rosewood. Soft and layered, like tissue paper in a
  dress box; script italic accents like a handwritten invitation. Conversion is booking a
  try-on appointment.
palette:
  - {name: pearl,    value: "#FCF9F7", dark_value: "#1E1917"}
  - {name: cocoa,    value: "#453A36", dark_value: "#EFE6E1"}
  - {name: blush,    value: "#F6E4DF", dark_value: "#2A211F"}
  - {name: rosewood, value: "#B76E79", dark_value: "#D4939D"}
  - {name: fawn,     value: "#A6968F", dark_value: "#9C8D86"}
  - {name: veil,     value: "#F0E1DB", dark_value: "#322724"}
fonts: {display: Playfair Display, script: Parisienne, body: Mulish}
archetype: >
  Layered tissue panels: sections are overlapping offset rounded panels (blush on pearl,
  shifted up into the previous section) with script words floating over corners. Nav is a soft
  pill centered near the top. Hero is a centered invitation: script line, serif headline,
  small-caps date-style subline, one arched-corner photo behind offset panels. Dresses are
  offset alternating cards, each a panel with a script number. Footer is an RSVP card: bordered
  invitation block with centered type. Lull owns arches and circles; tulle owns offset
  overlapping panels and script overlays.
imagery: >
  Wedding dresses, veils, bouquets, soft-focus bridal portraits. Airy, bright, blush-toned.
  Searches: "wedding dress boutique", "bridal veil", "bouquet pastel", "bride soft light".
pages:
  - {name: tulle_home, route: /, sections: [pill nav, invitation hero with layered panels, three signature dress cards (script numbers), kind-words quote panel, RSVP footer card]}
  - {name: tulle_dresses, route: /dresses, sections: [collection header with script accent, offset alternating dress panels (silhouette, fabric, price band), fittings note panel, RSVP footer card]}
  - {name: tulle_visit, route: /visit, sections: [boutique story panel pair (photo + copy), what-to-expect list as soft rows, visit card (hours, address, appointment mailto), RSVP footer card]}
components: [tulle_nav, tulle_rsvp_footer]
```

## Brief: denim (Fashion, bright)

```yaml
codename: denim
category: Fashion
title: Denim
description: A loud streetwear drop site with thick borders, tickers and price stickers.
theme: bright
concept: >
  Denim is a streetwear label that sells in drops. Chalk background, indigo ink, denim blues,
  stitch-orange accents. Everything boxed in thick 2px borders, marquee tickers, rotated price
  stickers. Loud but organized. Conversion is shop-the-drop.
palette:
  - {name: chalk,  value: "#F5F4EF", dark_value: "#12141D"}
  - {name: indigo, value: "#1B2A6B", dark_value: "#E8EBF7"}
  - {name: sky,    value: "#DCE4F7", dark_value: "#1D2440"}
  - {name: cobalt, value: "#3552C8", dark_value: "#7A93E8"}
  - {name: stitch, value: "#FF6A2B", dark_value: "#FF8B55"}
  - {name: slate,  value: "#6B7398", dark_value: "#8A91B0"}
fonts: {display: Archivo Black, body: Space Grotesk}
archetype: >
  Boxed-cell chaos. Nav is a row of bordered cells (each link its own box, cart cell filled
  stitch-orange). A marquee ticker strip runs under the nav and again mid-page. Hero is a giant
  boxed wordmark with a rotated NEW DROP sticker overlapping the corner. Products are a
  checkerboard grid of bordered tiles, alternating photo tiles and sky-filled text tiles, each
  photo tile carrying a rotated price sticker. Footer is stacked oversized outlined link rows.
  No other group uses bordered cells, tickers or sticker rotation.
imagery: >
  Denim stacks, sneakers, tees on racks, streetwear looks. Punchy daylight. Searches: "denim
  jeans stack", "sneakers product", "streetwear look", "clothing rack shop".
pages:
  - {name: denim_home, route: /, sections: [cell nav + ticker, boxed wordmark hero with sticker, drop 04 checkerboard (6 tiles), fit guide split boxes, mailing-list bar, stacked-links footer]}
  - {name: denim_drops, route: /drops, sections: [drops header cells (04 live / 03 archive), full product checkerboard with price stickers, sizing table box, stacked-links footer]}
  - {name: denim_story, route: /story, sections: [boxed manifesto in oversized caps, factory photo strip with captions cells, timeline as ticker rows, stacked-links footer]}
  - {name: denim_stockists, route: /stockists, sections: [stockists header, city list as bordered ledger rows, wholesale enquiry box with mailto, stacked-links footer]}
components: [denim_nav, denim_footer]
```

## Brief: pleat (Fashion, editorial)

```yaml
codename: pleat
category: Fashion
title: Pleat
description: An editorial lookbook shot as magazine spreads with folio bars.
theme: editorial
concept: >
  Pleat is a seasonal lookbook, presented like a fashion magazine issue: folio bar with issue
  and date, numbered looks as full spreads, oversized Bodoni italics, one crimson accent.
  Made for labels that shoot seasonal campaigns. Conversion is a stockist/press enquiry.
palette:
  - {name: page,    value: "#FFFFFF", dark_value: "#131313"}
  - {name: ink,     value: "#101010", dark_value: "#F2F2F2"}
  - {name: stone,   value: "#757068", dark_value: "#A09A92"}
  - {name: rule,    value: "#E2E0DC", dark_value: "#2E2C29"}
  - {name: crimson, value: "#B3202C", dark_value: "#E04654"}
  - {name: cream,   value: "#F5F3EF", dark_value: "#1C1B19"}
fonts: {display: Bodoni Moda, body: Work Sans}   # italic via @import script
archetype: >
  Magazine spreads. Nav is a folio bar: issue number left, brand centered in Bodoni, date
  right, double rule beneath. Home opens as a cover: oversized italic masthead over a cover
  photo with crimson cover lines. Each look is a spread section: folio line (LOOK 01 / 12), a
  portrait image paired with a detail crop, and an oversized italic caption; spreads separated
  by double rules with page numbers. Footer is a colophon block: masthead, credits columns,
  crimson enquiry line. Field owns newspaper columns and quill owns blog lists; pleat owns
  paired-image spreads with folio furniture.
imagery: >
  Editorial fashion portraits with matching detail crops. Studio and street, strong styling.
  Searches: "fashion editorial portrait", "model street style", "fashion detail fabric".
pages:
  - {name: pleat_home, route: /, sections: [folio nav, cover with masthead + cover lines, contents line, looks 01-03 as spreads, crimson subscribe/enquiry band, colophon footer]}
  - {name: pleat_looks, route: /looks, sections: [issue contents header, looks 01-06 as full spreads with credits, stockist note, colophon footer]}
  - {name: pleat_studio, route: /studio, sections: [about the studio spread (portrait + manifesto), services in folio rows (campaign, lookbook, casting), press + contact block with mailto, colophon footer]}
components: [pleat_folio_nav, pleat_colophon]
```

## Brief: ridge (Portfolio, dark)

```yaml
codename: ridge
category: Portfolio
title: Ridge
description: A dark photography portfolio built as a gapless photo mosaic wall.
theme: dark
concept: >
  Ridge is a landscape and documentary photographer. The site is the work: a gapless mosaic
  of photographs edge to edge, near-black chrome, one signal-orange accent. Captions appear
  on hover; everything else stays out of the way. Conversion is a print or commission enquiry.
palette:            # dark-first, dark_value: null, color-scheme: dark
  - {name: coal,   value: "#101012", dark_value: null}
  - {name: slateb, value: "#1A1A1E", dark_value: null}
  - {name: bone,   value: "#EDEBE6", dark_value: null}
  - {name: gray,   value: "#8E8C88", dark_value: null}
  - {name: linec,  value: "#2A2A2F", dark_value: null}
  - {name: signal, value: "#FF4D00", dark_value: null}
fonts: {display: Syne, body: Inter}
archetype: >
  Gapless mosaic wall. Nav is a thin overlay bar: name left, series links + enquire right.
  Home opens with a short statement row then goes straight into a flex mosaic: rows of photos
  with mixed widths (40/60, 33/33/33, 55/45), zero gaps, hover captions sliding up. A series
  page repeats the mosaic filtered to one series with an index header (No., place, year).
  Info page is a small portrait + statement + press list. No other group is a gapless mosaic.
imagery: >
  Landscape, road, water, people at distance. Moody, high contrast. The mosaic mixes
  orientations; pick images that survive hard crops.
pages:
  - {name: ridge_home, route: /, sections: [overlay nav, one-line statement, mosaic wall (8-10 photos, hover captions), enquire strip footer]}
  - {name: ridge_series, route: /series, sections: [series index header (No./place/year rows), mosaic filtered to the series with caption bars, edition note, enquire strip]}
  - {name: ridge_info, route: /info, sections: [portrait + statement, selected press ledger, prints and commissions block with mailto, enquire strip]}
components: [ridge_nav, ridge_enquire]
```

## Brief: canvas (Portfolio, bright), replaced quip (retired: bento boards read generic)

```yaml
codename: canvas
category: Portfolio
title: Canvas
description: A designer portfolio presented as a live design file, comments left in.
theme: bright
concept: >
  Nadia is a product designer. Her site IS a design file: dotted canvas background,
  sections inside blue selection boxes with corner handles and layer-name tabs
  (hero / v3, final FINAL), collaborator cursors drifting over the page, pink comment
  pins with real comment cards, sticky notes in a handwriting font. Toolbar nav with a
  Share button; status-bar footer (autosaved just now · 100%). Conversion: "invite me
  to your file" email.
palette:
  - {name: paperc, value: "#FCFCFB", dark_value: "#15171C"}
  - {name: inkc,   value: "#1B1F27", dark_value: "#EDEFF4"}
  - {name: blue,   value: "#2F7BFF", dark_value: "#6FA5FF"}   # selection chrome
  - {name: pink,   value: "#FF4F9A", dark_value: "#FF7DB4"}   # comment pins
  - {name: lemon,  value: "#FFD84D", dark_value: "#D9B33A"}   # sticky notes
  - {name: mutedc, value: "#8A93A6", dark_value: "#8A93A6"}
fonts: {display: Sora, body: Inter, hand: Caveat}
archetype: >
  Design-file chrome as page furniture: dotted grid canvas, selection boxes with
  handles + label tabs, cursor pills, comment pins and cards, stickies, toolbar and
  status bar. No other group imitates software chrome.
pages:
  - {name: canvas_home, route: /, sections: [toolbar, hero selection box with cursors + pin + sticky, recruiter comment card, three project frames (staggered), status bar]}
  - {name: canvas_work, route: /work, sections: [header, three case frames each with cover + facts + client comment card + pin, status bar]}
  - {name: canvas_about, route: /about, sections: [photo instance frame + bio frame + tools sticky, version-history changelog frame (v1 agency / v2 bank / v3 independent), CTA frame with cursor, status bar]}
components: [canvas_nav, canvas_footer]
```

## Brief: vitae (Portfolio, minimal)

```yaml
codename: vitae
category: Portfolio
title: Vitae
description: A consultant's CV presented as a crisp paper sheet on a desk.
theme: minimal
concept: >
  Vitae is a fractional CFO / consultant one-pager. The site looks like a beautifully set
  A4 resume lying on a warm gray desk: letterhead, hairline-ruled entries, dates in the left
  column, a navy accent. Print-ready feeling, zero decoration. Conversion is a intro call.
palette:
  - {name: desk,   value: "#E9E7E2", dark_value: "#141414"}
  - {name: paperv, value: "#FFFFFF", dark_value: "#1E1E1E"}
  - {name: inkv,   value: "#232323", dark_value: "#ECEAE6"}
  - {name: mutedv, value: "#8A8781", dark_value: "#96938D"}
  - {name: linev,  value: "#E4E2DD", dark_value: "#2E2E2E"}
  - {name: navy,   value: "#1F3A64", dark_value: "#7C9CD0"}
fonts: {display: EB Garamond, body: IBM Plex Sans}
archetype: >
  Paper sheet on a desk. Everything lives on a centered white sheet (max 840px) with a soft
  shadow over a desk-gray page background. Letterhead top: name in Garamond, contact line,
  navy rule. Sections are CV entries: date span left column, role + bullets right. Skills as
  hairline chips. Footer is the signature block. Other pages are additional sheets: an
  engagements sheet, a references/contact sheet. No other group frames content as a document.
imagery: >
  Almost none: one small formal portrait on the contact sheet. The document IS the design.
pages:
  - {name: vitae_home, route: /, sections: [desk bg + sheet, letterhead, summary paragraph, experience entries (date left / role right), education + skills chips, signature footer]}
  - {name: vitae_engagements, route: /engagements, sections: [sheet header, case entries with outcome numbers (dates left), approach list, signature footer]}
  - {name: vitae_contact, route: /contact, sections: [sheet with portrait + availability line, engagement terms rows, intro-call mailto block, signature footer]}
components: [vitae_letterhead, vitae_signature]
```

## Brief: reel (Portfolio, dark)

```yaml
codename: reel
category: Portfolio
title: Reel
description: A filmmaker portfolio of letterboxed stills with timecode captions.
theme: dark
concept: >
  Reel is a director / DP. The site is a screening room: near-black, every still presented
  letterboxed at 21:9 with a mono timecode caption (00:04:12), titles in condensed caps like
  film slates. One amber accent like a tungsten lamp. Conversion is a rep/production enquiry.
palette:            # dark-first, dark_value: null, color-scheme: dark
  - {name: screen, value: "#0A0A0C", dark_value: null}
  - {name: slate2, value: "#141418", dark_value: null}
  - {name: ivory2, value: "#F4F2EC", dark_value: null}
  - {name: dim,    value: "#8F8D86", dark_value: null}
  - {name: liner,  value: "#26262B", dark_value: null}
  - {name: amber,  value: "#E8B14E", dark_value: null}
fonts: {display: Oswald, body: Archivo, mono: IBM Plex Mono}
archetype: >
  Screening room. Nav is a slate bar: name, roles, enquire, all condensed caps. Films are
  stacked letterboxed frames: full-width 21:9 stills with black bars implied by the page,
  each with a mono timecode + title + client row beneath, separated by generous black.
  A film page shows the frame, then a slate card (director / client / runtime rows in mono)
  and paired production stills. About page is a credits crawl: centered rows like end
  credits. No other group letterboxes imagery or uses timecodes/credit-crawl furniture.
imagery: >
  Cinematic frames: stage light, streets at night, sets, silhouettes. Everything crops to
  21:9 without losing the subject.
pages:
  - {name: reel_films, route: /, sections: [slate nav, name + roles opener, four letterboxed stills with timecode/title/client rows, enquire slate footer]}
  - {name: reel_film, route: /film, sections: [hero letterbox frame, slate card (mono production rows), two production stills pair, next-film link row, enquire slate]}
  - {name: reel_about, route: /about, sections: [portrait letterboxed, credits crawl (role rows centered), awards mono list, enquire slate]}
components: [reel_nav, reel_enquire]
```

## Brief: margin (Portfolio, warm light)

```yaml
codename: margin
category: Portfolio
title: Margin
description: A writer's site with a reading column and numbered margin notes.
theme: warm light
concept: >
  Margin is an essayist / researcher. The layout is a book page: a measured reading column
  with true margin notes: small numbered asides sitting in the wide right margin, a library-green
  accent for note numbers and links. Quiet, bookish, deeply readable. Conversion is a
  newsletter/contact email.
palette:
  - {name: paperm, value: "#FBF8F2", dark_value: "#1B1915"}
  - {name: inkm,   value: "#2B2620", dark_value: "#EDE8DF"}
  - {name: mutedm, value: "#97897A", dark_value: "#9C9184"}
  - {name: rulem,  value: "#EAE3D6", dark_value: "#2F2B24"}
  - {name: laurel, value: "#3F6B4F", dark_value: "#8FBC9B"}
  - {name: washm,  value: "#F3EEE3", dark_value: "#242019"}
fonts: {display: Newsreader, body: Newsreader, caps: Inter}
archetype: >
  Book page with margin notes. Nav is a running head: title left, page-style links right,
  thin rule. Content is a two-column book grid: reading column (65ch) left, wide margin
  right holding numbered notes (superscript green numerals in the text, matching notes in
  the margin, top-aligned to their paragraph). Essays list as a table of contents with
  chapter numerals and dotted leaders. Footer is a colophon line. On mobile the notes tuck
  inline as tinted asides. No other group has true margin-note anatomy.
imagery: >
  Sparse: a desk photo or a book still on the about page. Type carries the site.
pages:
  - {name: margin_home, route: /, sections: [running-head nav, opening essay excerpt with 3 margin notes, table of contents with dotted leaders, newsletter line, colophon]}
  - {name: margin_essays, route: /essays, sections: [contents header, full TOC by year with numerals and leaders, selected quote with margin note, colophon]}
  - {name: margin_about, route: /about, sections: [bio column with margin notes (portrait as a margin figure), now list, contact + newsletter block, colophon]}
components: [margin_head, margin_colophon]
```

## Brief: plinth (Portfolio, minimal)

```yaml
codename: plinth
category: Portfolio
title: Plinth
description: A minimal architect portfolio: a type-only index with hover thumbnails.
theme: minimal
concept: >
  Plinth is a two-person architecture practice. The site borrows the language of a
  drawing set: sheet numbers (SHT A-01), scale and revision notes in Space Mono, a
  titleblock footer, and a project index that is pure typography: five giant rows,
  hover to see the building. One drafting-blue accent. Conversion: a studio visit email.
palette:
  - {name: sheetp,   value: "#FFFFFF", dark_value: "#161617"}
  - {name: graphite, value: "#17181A", dark_value: "#EDEDEB"}
  - {name: fogp,     value: "#9A9DA3", dark_value: "#8F9296"}
  - {name: hairp,    value: "#ECECEA", dark_value: "#2A2A2C"}
  - {name: draft,    value: "#2B5BD7", dark_value: "#7D9BF0"}
  - {name: panelp,   value: "#F6F6F4", dark_value: "#1D1D1F"}
fonts: {display: Instrument Sans, mono: Space Mono}
archetype: >
  Drawing set. Head bar with sheet coordinates; index rows of 56px project names with
  mono PRJ numbers and meta, hairline rules, hover thumbnail floating in from the right;
  project page as a numbered sheet (hero, SPECIFICATION table, captioned pair, NEXT row);
  titleblock footer (firm / drawn / scale / rev). No other group is a type-only index or
  uses drawing-sheet furniture.
pages:
  - {name: plinth_home, route: /, sections: [sheet bar + statement, five index rows with hover thumbnails, capabilities row, titleblock]}
  - {name: plinth_project, route: /project, sections: [sheet header, elevation hero with caption, specification table + narrative, captioned image pair, next-project row, titleblock]}
  - {name: plinth_profile, route: /profile, sections: [profile statement + portrait with caption, numbered principles, studio visit block with mailto, titleblock]}
components: [plinth_head, plinth_titleblock]
```

## Brief: hex (Technology, dark), RETIRED Jul 2026 (generic, no conceit)

Dev-tool marketing. Terminal windows with traffic-light dots, mono install command, man-page
flag cards (--incremental, --why), hyperfine benchmark terminal, tier cards, release-notes
changelog with FEATURE/FIX/BREAKING tags, status-dot footer. Space Grotesk + JetBrains Mono.
Palette void/panelx/textx/dimx/linex/mintx/violx, dark-only. Pages: home, pricing, changelog.
No photos anywhere.

## Brief: prism (Technology, neutral), RETIRED Jul 2026 (generic by design, which was the mistake)

The theme-less SaaS site: white, Inter, ONE brand variable (indigo) so the whole site rethemes
by editing a single color. Product screenshots are mock UI built from blocks (browser frame,
stat cards, bar chart, table rows), so no images to replace. Metrics band, alternating feature
rows, testimonial cards, a real comparison pricing TABLE with tick rows, honest FAQ, CTA band
footer. Pages: home, pricing, contact.

## Brief: tally (App UI, neutral), RETIRED Jul 2026 (a mockup, not a template with a soul)

A dashboard app-shell starter, not a website: fixed sidebar (logo, icon nav, usage meter),
topbar (search pill, bell, avatar), KPI cards with delta colors, a CSS bar chart, progress
rows, activity feed, data tables with status pills in overflow-x scrollers, settings page with
field rows, toggle switches, team list and a danger zone. Inter, 7 variables, no theme toggle.
Pages: overview (home), customers, settings. Distinct from keys (property listings shell):
tally owns analytics furniture.

## Brief: intake (App UI, neutral), RETIRED Jul 2026 (same batch, same lesson)

An internal-tool starter: topbar-only chrome with an INTERNAL env badge, request queue rows
(id, title, priority/SLA/status chips), request detail with meta grid, approval action bar and
a dotted audit timeline, and a new-request form using real input/textarea elements plus a
dashed drop zone. Public Sans, teal accent, amber warnings. Pages: queue (home), request, new.

## Brief: prospect (Technology, paper), RETIRED Jul 2026 (conceit didn't land with the user)

The flagship SaaS-marketing conceit: the site IS a printed investment prospectus. Cover with
prospectus number, red double-border seal badges (rotated), table of contents, numbered Items
with folio rules, the product shown as captioned Exhibits (Fig. 1 plates built from blocks: a
mock ledger), pricing as a double-ruled rate card with footnotes, a Risk Factors section that
answers objections deadpan, and a signature page with dotted lines where the CTA is
"Countersign". Source Serif 4 + IBM Plex Mono, paper/ink/seal palette, light-only, no photos.
Pages: home (the document), rates (schedule + readable fine print + month-end guarantee),
appendix (A: firm, B: anticipated questions, C: correspondence). Distinct from vitae (a CV
sheet on a desk) and margin (book page): prospect owns securities-filing furniture.

## Brief: encore (Technology, dark), BUILT

The keynote conceit, picked by the user from an options round: the site is a product launch
keynote. Radial spotlight hero (ACT I), demo in a stage frame with gold footlights (ACT II),
three reveal cards with ( applause ) captions (ACT III), "And it's available today." (ACT IV),
a One More Thing encore section, gold stage-note asides in mono, and a house-lights-up footer.
Pricing page is "the pricing slide, uncut" plus questions from the audience; about page is
Backstage with a setlist changelog and cast credits. Gabarito + Inter + IBM Plex Mono,
house/stage/lumen/gold palette, dark-only, no photos.

## Brief: aurora (Technology, dark), BUILT

The Framer-grade one: violet radial glow hero, gradient-clipped headline text, glass cards
(blur + 4% white), a glowing mock product frame built from blocks, text logo row, bento grid
(sparkline card, working toggle rows, avatar stack, mono API snippet, security card), gradient
stat trio, offset testimonial wall, glow CTA band. Inter everywhere, tight tracking. Pricing
with a featured glowing tier; contact with real inputs. Dark-only, no photos.

## Brief: bureau (Marketing / Agency, bright), BUILT

The Framer-grade agency site: Hanken Grotesk mega type with acid marker highlights, case
studies as typographic covers (each client a colored poster tile with its own wordmark
styling, no photos), numbered services mega-list with acid hover, black manifesto band ("Nice
brands finish last."), client name wall, and a full-acid footer with a giant "Let's talk".
Work page adds client-reported result chips; contact page has budget chips and a
what-happens-next row. Light, no toggle.

## Brief: scrap (Portfolio, paper), BUILT

The cut-and-paste zine: a graphic designer's portfolio assembled like a photocopied fanzine.
Torn-edge photo panels (clip-path polygons) at slight rotations that straighten on hover,
masking-tape strips, xerox photo treatment (grayscale + contrast), ransom-note headlines
mixing Anton, Courier Prime and Permanent Marker, marker scribbles for asides and client
quotes, staple-run dividers, a black house-rules band, and a colophon page that lists the
paper stock. Aged-paper single theme, red and highlighter-yellow accents. 3 pages
(home / werk / colophon), order 27.

## Brief: affiche (Portfolio, bright), BUILT

The Swiss poster wall: Studio Oksen's site as a stack of full-viewport International-Style
posters. Inter Tight 900 mega type ("Grafik ist Arbeit."), red/black/white only, rotated
vertical type rails on the poster edges, diagonal red bands, a red-circle manifesto poster
("Form folgt Haltung."), block-built mini poster reproductions on the work page, and a dense
Werkverzeichnis catalog table with red numbers (deliberately smaller and denser than plinth's
giant index rows). German-flavored copy. Light, no toggle, no photos. 3 pages
(home / arbeit / kontakt), order 28.

## Brief: annum (Portfolio, warm light + dark), BUILT

The one-thing-a-year maker portfolio, built to the user's spec: image-heavy hero + personal
projects timeline. Split ledger hero (user-picked over the first full-bleed-overlay version):
text on solid bone at left with a huge stacked Bricolage Grotesque headline and a clickable
year ledger (2026 to 2021, anchor links into the timeline with hover arrows), full-height
workshop tool-wall photo column at right with a fig caption chip. Ledger-style nav: brand lockup
with sub-line, numbered links (01/02/03), a pulsing "now making: salve" status chip, and a
2px year-progress rule under the bar. Then a spine timeline with amber year dots, big rounded
photos, status and material chips per project (balm, allotment, cabin, bike frame, stools,
ceramics), a stats band (6 years / 6 things / 0 abandoned), an amber "2027 is unclaimed" CTA
card, a year-by-year ledger page with a type-only "prehistory" section, and an about page
with portrait and numbered house rules. Bricolage Grotesque + Inter, cool paper palette with
moss green accent (user-picked over amber, indigo, oxblood, brass), light/dark toggle. 3 pages (home / ledger / about), order 29.

## Brief: fetch (Marketing, playful), BUILT

The single-product DTC site (Squarespace Wesley Pets inspired): one dog collar for one
audience. Cream ground, Baloo 2 rounded display type, super-rounded (24 to 32px) pastel color
tiles in butter/sky/tangerine, a beagle hero in a butter frame with a deadpan caption, a
full-width lake field-test photo band with a claim chip, star-rating review cards from
verified goodest dogs, a size table with honest fit notes, material spec tiles, and a
break-it-we-replace-it-forever guarantee card. Single bright theme. 3 pages
(home / collar / help), order 33.

## Brief: recipe (Marketing, warm craft), BUILT

The agency-as-recipe-cards site, same agency-grade bar: ruled index cards (multi-layer CSS
background: blue rules + double red margin line) with all content set right of the margin,
dog-ear corner folds (CSS border triangles with a drop shadow), a rotated TESTED TWICE rubber
stamp with a mask-image fade, a subtle grease-stain radial blob, Kalam handwritten chef's
notes in a method margin column, timing chips (prep 2 weeks / cook 90 days / difficulty:
honest), checkbox ingredient lists (you bring / we bring), star-rated "clean plates"
testimonial cards, a tasting menu of services as priced recipe cards (soufflé / flash-fried /
slow simmer), a brigade page, house rules taped above the stove, a scissors tear-off coupon
CTA and a gingham footer band. Young Serif + Albert Sans + Kalam on linen. Single warm theme.
3 pages (home / menu / kitchen), order 32.

## Brief: candor (Marketing, statement), BUILT

The statement brand, Squarespace Cedar Group inspired: a deep pine full-viewport hero holding
one giant Source Serif statement with a mega wordmark cropped off the bottom edge, cream
sections with numbered serif service rows, a house-position pine band ("We will tell you if we
are the wrong hire"), a fee table with a thick top rule and fixed prices, roman-numeral working
principles, and a start page that sets expectations for the first call. Serif everywhere,
no photos, single theme. 3 pages (home / work / start), order 31.

## Brief: fathom (Travel & Hospitality, depth gradient), RETIRED Jul 19 2026

The scroll-dive freediving school: a 560vh runner pinning a 100vh stage, a rAF-driven `--p`
variable crossfading water gradients over an underwater video layer, waypoint cards at
−4/−10/−16/−26/−42 m, a live depth-gauge HUD, a dive-line course ledger, and a bright
surface footer after dark pages. Retired same day it shipped, on user feedback ("boring"):
the mechanics were sound but the experience was an atmosphere, not an artifact. Reusable
learnings kept in the rules above (JS client scripts need `originalElement: body`;
`backdrop-filter` ancestors trap `position: fixed`; per-page component-instance style
overrides work by patching the mirrored node's baseStyles). Its committed video assets were
removed with it.

## Brief: groove (Marketing, warm hi-fi), BUILT Jul 2026

The record label, replacing fathom after the user asked to "read the pattern": the shipped
catalog keeps artifact conceits with dense furniture (recipe cards, the design file, the
keynote, the zine), so groove makes the site a record. Night Shift Records, an independent
vinyl label, 70s hi-fi palette (cream / ink / burnt orange / mustard), Unbounded (display,
swapped from Abril Fatface in the Jul 20 revision round) + DM Sans + DM Mono. The hero is a
pure-CSS vinyl record (repeating-radial grooves, conic sheen, orange centre label with the
type set AROUND the spindle hole, brand above, pressing details below) that spins with
scroll via a `--spin` variable, under a tonearm whose angle is whole-page progress
(`--armp`) with the stylus resting on the grooves: the page IS Side A. A fixed NOW PLAYING
pill (ink, pulsing orange dot) retunes per section from `data-tune` attributes (NOT
`data-track`, which Builder stamps on blocks for click analytics). The label's services are
the BACK OF THE SLEEVE: an ink panel with a mustard offset shadow, SIDE A header between
hairlines, dotted-leader track lines with runtimes and mono credit lines, an uppercase
credits paragraph and a © ℗ row with a small barcode (the B-side page repeats the panel as
SIDE B with an orange shadow and prices as runtimes). Stats are three 45-singles: CSS discs
with coloured centre labels holding the numbers, hover-rotate. Two committed video bands
(Pexels 19281032, a red-label record spinning in the dark, on home; Pexels 5118420, a hand
cueing the needle, as the B-side Thursday ritual; ~330-460 KB each, muted/looped with a JS
play() safeguard). Releases are square sleeves whose vinyl ejects sideways on hover
(`.gr-sleeve:hover z-index` lift, cream rim for dark covers), the roster is a crate flipped
sideways (perspective rotateY snap strip), hype stickers with offset shadows sit on the
record wrap, the demo-drop card is the conversion, and the footer is the runout groove: a
marquee of etched matrix text plus a CSS barcode. Chunky 2px-ink-border buttons with offset
shadows that press down on hover. No JS / reduced motion: record and arm sit static, pill
hidden, everything readable. 3 pages (home / roster / bside), order 35.

## Brief: gambit (Marketing, monochrome), BUILT Jul 2026

First of the minimalist-monochrome trio (user ask: "minimalist, subtle and monochrome").
Gambit &amp; Partners, a two-partner strategy advisory written as an annotated chess game.
Warm-grey monochrome (paper/ink/muted/line/sq/panel), Crimson Pro + IBM Plex Mono, with REAL
italics for the annotation commentary via the new ital-axis font loader (no @import script
needed anymore). Furniture: a CSS chessboard diagram in the hero holding an accurate
Queen's Indian position ("After 4...Bb7. Comfortable for everyone, which never lasts"),
process as score-sheet move rows (1. Nf3!? Listen · 5. h3!? Give yourself luft), results as
engine evaluations (−1.4 → +2.3, "engine-checked by reality"), services as ECO-coded
openings (C50 Italian / B20 Sicilian / A10 English) with character tags, pricing as time
controls (Classical / Rapid / Blitz), partner cards with peak ratings, and a footer that
scores the page 1–0 ("Resignation is also a move"). Subtle motion only: soft rises, row
nudges, offset-shadow card hovers. 3 pages (home / openings / club), order 36.

## Brief: chit (Food & Beverage, monochrome), BUILT Jul 2026

Second of the monochrome trio. Small Change, a nine-seat espresso bar whose every page is a
thermal till receipt on a counter-grey ground: zigzag torn bottom edges (clip-path), dashed
rules, dotted price leaders, star headers, ORDER #047 lines and barcode stubs, all in Courier
Prime and thermal grey-blacks (counter/paper/ink/faded/line). The hero receipt physically
feeds out of a printer-slot bar on load (masked translateY, 2.1s ease-out). The whole pitch
is ON the receipt ("A NINE-SEAT ESPRESSO BAR THAT TAKES COFFEE SERIOUSLY AND ITSELF NOT AT
ALL"), items carry deadpan notes (tap water 0.00, "always. asking is allowed"), the menu is
one long register roll with an 86'd cold brew struck through ("IT KNOWS WHAT IT DID"),
loyalty is a punched card (six of ten filled, record holder Margit, 214 cards), the visit
page is the STORE COPY with a customer-signature line, and the footer is the customer-copy
stub with hours as price rows and "NO REFUNDS ON SUNSHINE" legal. 3 pages
(home / menu / visit), order 37.

## Brief: optic (Local business, monochrome), BUILT Jul 2026

Third of the monochrome trio. Lindqvist Optik, a one-room opticians in Malmö whose home page
IS an eye chart: nine Snellen rows shrinking from a 170px "L" to a 7.5px row 9, spelling the
pitch cumulatively ("L / OO / K CLO / SELY NOW / WE MAKE GLASSES / FOR PEOPLE WHO LOOK
CLOSELY..."), with row numbers left and 20/200→20/10 acuity fractions right; the last row
rewards leaning in ("YOU ARE LEANING IN. THAT IS EXACTLY THE KIND OF PERSON WE MAKE GLASSES
FOR."). Pure black on white with two greys, Schibsted Grotesk + IBM Plex Mono. Reveals
sharpen from blur(9px) into focus, the one motion idea and it IS the conceit. The three
frames are drawn entirely in CSS (round Arvid, rectangular Berit, browline Cleo: two lens
shapes, a bridge and temples from borders), the exam page carries a prescription-pad Rx grid
(SPH/CYL/AXIS with deadpan notes: "squints at menus") in a sheet with an offset shadow, and
the footer's smallest type is an 8.5px joke ("If you can read this, thank your optician").
The forever-adjustment promise is the whole marketing strategy, stated as such. 3 pages
(home / exam / visit), order 38.

## Brief: rivet (Local business / trades, industrial), BUILT Jul 21 2026

First of the service-industry batch (user pivot: "we are generating very niche templates
which can be less useful... create templates for the service industry, modern and
aesthetic"). The bar shifts from artifact conceits to broadly-usable verticals carried by a
strong modern design system; wit stays. Rivet is a plumbing/electrical/heating contractor:
concrete-paper ground, charcoal ink, safety orange, Archivo 800 caps. Blunt honest voice
("FIXED. PROPERLY.", "We turn up. We fix it. We sweep up."), grayscale job photography,
numbered service cards, fixed prices published in ledger rows, a dark "the price is the
price" manifesto, live-ish availability board, service-area chips, and a fixed bottom 24/7
emergency strip with a pulsing dot ("Burst pipe? No power?"). Count-up stats, dark ink
ticker. 3 pages (home / services / book), order 39, categories Local business + Marketing.

## Brief: enamel (Local business / dental, soft clinical), BUILT Jul 21 2026

A calm dental practice: warm cream, one clinical blue, Plus Jakarta Sans, pill buttons,
24px radii. Voice is kind and honest ("Dentistry for people who'd rather be anywhere
else"). Morphing-blob hero portrait with two bobbing floating chips, a four-step
nothing-happens-without-a-conversation strip, emoji-icon treatment cards, fees published in
rounded tables ("Fees, published like normal shops do"), a nervous-patients section with
hand-signal promises, an $18/mo membership without dark patterns, and a minute-by-minute
first-visit timeline. 3 pages (home / treatments / visit), order 40, Local business.

## Brief: counsel (Marketing / law, quiet ivory), BUILT Jul 21 2026

Harrow & Vale, a quiet law firm: ivory ground, Source Serif 4 display, Inter small caps,
oxblood accent used sparingly. Confidence through restraint: no gavels, no columns
clip-art. Numbered practice-index rows that indent on hover, a dark outcomes band ("$1.4B
closed the boring way", "0 press releases about clients, ever"), an italic pull quote (via
the @import ital fallback), grayscale partner portraits that colorize on hover, house rules
as roman-numeral panels, fees "discussed like adults" with a free first hour. 3 pages
(home / practice / enquire), order 41, Marketing + Local business.

## Brief: uptime (Technology / IT services, status green), BUILT Jul 21 2026

The user-requested "IT services / partners / digital presence" concept. A managed-services
firm whose brand is a status page: deep slate, status green, Space Grotesk + Inter,
blinking-cursor wordmark ("uptime_"). Pulsing "All client systems operational" pill, a
60-day uptime tick bar that staggers in (two amber wobbles for honesty), counting SLA
stats (99.98% / 11 min median), four service panels, per-seat pricing tiers with the exit
plan in the contract, a fictional partner wall, and three case studies with real numbers
("40→5 min lost per person weekly", "1 hero, still employed, sleeping"). 3 pages
(home / services / partners), order 42, Technology + Marketing.

## Brief: tempo (Local business / fitness, volt poster), BUILT Jul 21 2026

A strength & conditioning studio: near-black, off-white, volt #D8FF3D, Anton caps over
Inter. Anti-globo-gym positioning ("SHOW UP. THAT'S THE PROGRAM.", "zero mirror culture",
"0 treadmills. sorry. not sorry"). Duotone photography, a volt ticker, four class-format
cards, a REAL weekly schedule grid (flex table, h-scrolls on mobile), house rules
enforceable by frowning (PR bell rung exactly once per PR), hard-shadow button hovers,
memberships where the cancel button "is not hidden in a hedge maze". 3 pages
(home / schedule / join), order 43, Local business.

## Brief: spruce (Local business / cleaning, checklist), BUILT Jul 21 2026

A home cleaning service whose design motif is the literal checklist: airy white, leaf
green, Figtree, checkbox rows everywhere whose ticks scale-in staggered on scroll.
Floating "Today · Flat 4B" checklist card bobbing over the hero photo, a public
bedrooms+bathrooms rates table ("Find your home. That's your price."), written scopes per
clean, the 53-point clean sample card ("That one sticky drawer handle. Fixed."), flat-price
add-ons (fridge archaeology $35, post-party rescue with glitter surcharge), a 48-hour
re-clean guarantee, and a quote flow that is just three things in an email. 3 pages
(home / services / quote), order 44, Local business.

## Brief: align (Local business / physio, warm clinic), BUILT Jul 21 2026

A physiotherapy & movement clinic: bone neutrals, clay accent, Fraunces display over Karla.
Condition-first navigation ("Where does it catch?" cards: backs, knees, shoulders, sports,
post-op, "Not sure? Fine."), a four-stage recovery arc (Understand / Calm it down /
Rebuild / Return & stay) on a dot rail, anti-churn positioning ("Fewer visits, on
purpose", "0 mystery ultrasounds sold", "discharge is the goal"), initial-avatar clinician
cards, published session fees, a minute-by-minute first hour ("bring shorts, leave with a
plan") and house beliefs said out loud ("we treat you, not your MRI"). 3 pages
(home / care / visit), order 45, Local business.

## Follow-ups

- ember shipped Jul 19 2026 (order 34), opening the Food & Beverage category. Next briefs in
  that column: crumb, scoop, graze, zest.
- groove shipped Jul 19 2026 (order 35), replacing the retired fathom. The taste rule that is
  now three-for-three: build artifacts with furniture and wit, never atmospheres.
- Jul 21 2026 direction update: the user flagged the artifact conceits as "very niche...
  less useful" and asked for service-industry templates, modern and aesthetic. The
  seven-template service batch (rivet, enamel, counsel, uptime, tempo, spruce, align,
  orders 39-45) is the new model: broadly-usable verticals carried by a strong, distinct
  modern design system and witty honest copy; a skeuomorphic conceit is optional, the
  quality bar is unchanged. Remaining obvious verticals if the batch lands: fade
  (barber/salon, proposed and skipped this round), accounting, vet clinic, landscaping,
  auto shop, moving company.
- Re-tag the original shipped groups' `template.json` categories into the industry taxonomy when
  the first new template ships (fronds/verge -> closest vertical or General, mono/husk/verso
  -> Portfolio stays? decide then). commit was retired Jul 17 2026 instead of re-tagging.
- Expand briefs category by category after ember validates the schema, one fully detailed brief
  per template before building it.
