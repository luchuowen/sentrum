# Decisions (current truth; ≤ 250 lines)

## Project
- 2026-09-28 Repo `luchuowen/sentrum` was empty; bootstrapped by this session. Cloud session cannot push (proxy not authorised for the repo); owner pushes from the Mac clone at ~/Desktop/PROJECTS/Mine/Claude/sentrum.
- 2026-09-28 Original logo recovered byte-for-byte (path data hash-verified) from https://sentrumcoms.net/assets/images/logo.svg and logo-white.svg → `brand/`. Colours: wordmark #5a5b5d, globe #29a9e1. Only two approved treatments: colour and all-white.
- 2026-09-28 Fonts are self-hosted from @fontsource (npm). Google Fonts CDN is unreachable from build sandboxes and is a third-party request anyway.
- 2026-09-28 Proposal (KES 150,000, 7-day plan) and internal blueprint live in `docs/reference/`.

## Content
- Legacy claims usable verbatim: HQ Wilson Airport Block 34 3rd Office; +254 720 288 713; info@sentrumcoms.net; technical team 15+ years; "across Africa"; VSAT platforms iDirect/SkyEdge/Comtech, SCPC, Ku-band → teleport antennas/RFTs, multi-country rollouts; fabrication item list.
- Unknown until owner supplies: licences/accreditations, partner tiers, projects/clients, sectors, founding year, support SLA, WhatsApp number, CCTV as a service.

## Lessons
- 2026-09-28 Never combine `.wrap` with a `padding: X 0` shorthand on the same element — use `padding-block`.
- 2026-09-28 No `backdrop-filter` on headers that contain fixed-position mobile menus.
- 2026-09-29 Final direction = 5 Live Section on night-navy (#0B1620) hero, white Remote & satellite; auto carousel (7 s) + desktop scroll-pin sync. Source: design/src/design-final.html.
- 2026-09-29 Never use `overflow:hidden` on an ancestor of a sticky element (breaks pinning); use `overflow:clip`.
- 2026-09-29 Auto-advancing heroes must not pause on hover of the whole hero (a desktop pointer is always over it) — pause on the carousel controls/caption only.
- 2026-09-29 Home body below hero: expanding capability panels (swipe rail on mobile), image-led Remote & satellite, "Where we work" image cards, process, company + technologies, tender card, close. Images in design/assets/img are DRAFTS (Canva-generated, upscaled previews) — replace with full-res generations before build.
- 2026-09-29 Production build = Astro 7 static, 28 pages from src/data (services.ts, site.ts). Inner pages: navy PageHero with the building drawing lit on that page's system (data-hl), then "In plain terms". Kickers sans; mono only for data.
- 2026-09-29 Support/technical-support copy limited to "we implement and support what we install" — legacy has no support detail. Don't add SLAs, hours or scope until the owner supplies them.
- 2026-09-29 Enquiry function: honeypot + 3 s time-trap + 5/hour per hashed IP (ratelimits, needs Firestore TTL on expireAt). CSP allows 'unsafe-inline' (inline islands, JSON-LD) — tighten with hashes later.
- 2026-09-29 Verify: `bash scripts/factory-check.sh full`, `node scripts/shoot-site.mjs`, `AXE=<axe.min.js> node scripts/axe.mjs` (needs playwright linked into node_modules).

## Home hero: three scenes on one timeline (inc11)
- Scene 1 building (6 beats × `--dur` 5s), scene 2 Horizon (canvas, 11s), scene 3 Strata (svg, 6 × 3.8s). One 13-beat timeline; loop ≈ 64s.
- Scenes stacked in a grid, crossfaded; inactive scenes `inert` + `aria-hidden`. Tabs (The building / Remote sites / Six layers) + Pause/Play (WCAG 2.2.2).
- Pin runway 12×26svh, only when ≥961w and ≥740h; smaller screens follow the active scene's height (JS `fit()`).
- Strata layer names are real links to area pages. SVG classes renamed (`tp`, `gl`, `ld`, `flow3`) to avoid `.top`/`flow` collisions; no `role="img"` on SVGs containing links.
- Grid-square backgrounds removed (`.top`, `.ph`, `.proc`). `.cta` is now a pill.
- Copy uses only verified content (VSAT, masts, UPS/solar). Horizon lede: "Farms, mines, camps and border sites" is illustrative wording, confirm with owner.

## Home hero v2: X-ray (replaces the three-scene carousel)
- Owner rejected the 3-scene carousel. One idea instead: "The other half of your building." A lens over a plain elevation reveals the systems inside (link, rooms, backbone, core, perimeter, steel).
- Lens tours the six systems (5.5 s each), follows the pointer, drag on touch; index buttons jump; Pause/Play for WCAG 2.2.2. Reduced motion: no auto tour.
- No pin/scroll-hijack. Horizon and Strata scenes dropped (still in design/heroes). Old carousel/pin CSS removed.
- Lit layer = second SVG masked by a radial-gradient circle; both share `<use href="#xr-shell">`. Mapping uses VB (desktop/mobile crops).

## Hero v2.1: compact (inc13)
- Removed repeats: kicker/coords (location is in the strip), caption title (index shows the name), lede list of systems, strip "Own fabrication" (= Steel). Strip now 3 items.
- Desktop hero ~640px at 1440×900 (was ~880); drawing capped at 470px; mobile hides the ghost CTA (sticky Call bar covers it).

## Hero v3 — Rooftop, 3-slide carousel
- Owner picked "A · Rooftop". Slides: Satellite (rooftop photo, signal arcs), Security (access reader, scan + verify), Supply & fabrication (weld sparks).
- Each slide: own photo shape (arc / arch / arc), own canvas animation, shared callout system. 7s autoplay, tabs, pause button, swipe, reduced-motion static.
- Strip cut to 3 items (dropped repeat). Images are drafts; full-res needed from owner.
- v3.1: owner removed tab/pause bar (autoplay stays, pauses on hover/focus/swipe); photo restored to large (540px wide, 644:800); slide 2 shape = chamfered corner; slide 3 = Networks & cabling (patch panel, data-packet animation) replacing fabrication (add-on, not core).
- What we deliver: owner picked C · Glyphs (centred); replaced expanding panels. Line glyphs per system, photo wipes up on hover, list layout on mobile.
- How we work: owner picked Stage · Side (odometer counter beside heading), replaced the circle timeline.
- Company: owner picked A · Coordinates; technologies as an orbit around the head-office radar. Marks from Simple Icons (CC0) for 8 brands in public/brands/; the other 18 show names until official logo files are supplied. Footer: '© year Sentrum Communication' + 'Designed by NAVAC GLOBAL'. Home closing CTA band removed.
