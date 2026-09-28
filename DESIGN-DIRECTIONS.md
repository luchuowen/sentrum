# Design directions — choose one

Four homepage directions, each a complete design language (nav → hero → solutions → proof → CTA → footer, desktop + mobile).
Files: `design/design-1.html` … `design-4.html` (sources in `design/src/`). Screenshots: `design/screenshots/`.
All use the original logo from `brand/` and only content evidenced in `docs/reference/legacy-site.md`.

| | 1 · Cross-Section | 2 · Register | 3 · Footprint | 4 · Broadsheet |
|---|---|---|---|---|
| **Big idea** | The whole offer drawn as one building: scroll through it and each system lights up in place | The company as a precise technical document: a filterable register of every discipline | Inside the building *and* beyond the fibre — geography and signal path as the story | An editorial argument: one claim per chapter, proof in the margin |
| **Answers first** | "What do you actually do in my building?" | "Can you cover my exact scope?" | "Can you reach my remote site?" | "Why does this matter, and why you?" |
| **Signature interaction** | Sticky architectural cross-section; layers highlight as you read (chips on mobile) | "I'm planning…" filter highlights the disciplines that apply | Animated signal path satellite → dish → mast → UPS → rack → WiFi → room | None needed — typography carries it; hover-only details |
| **Palette** | Drafting paper, ink navy, logo blue as the active layer | White, black, logo blue as the only colour, visible 12-col grid | Night navy + chart paper, logo blue for Kenya/signal | Pure white, black, blue-ink italics |
| **Type** | Instrument Sans + JetBrains Mono (drawing labels only) | Schibsted Grotesk + IBM Plex Mono (table metadata) | Archivo (expanded caps) + JetBrains Mono (coordinates) | Newsreader (display serif) + Hanken Grotesk |
| **Imagery direction** | Line drawings as the hero; photography supports service pages | Technical line drawings of fabricated items; datasheet photos | Dot-matrix map (real geography, HQ pin only); night photography of sites | Large editorial photography plates (Nano Banana Pro, then real project photos) |
| **Tone** | Calm, architectural, explanatory | Exact, procurement-grade, no-nonsense | Ambitious, field-going, distinctive | Confident, considered, corporate-senior |
| **Best for** | Facilities/IT buyers who think in rooms and floors | Procurement and technical evaluators | Owners who want the remote/VSAT edge to lead | Leadership audiences; strongest brand statement |
| **Risk** | Drawing must stay accurate and legible as scope grows | Can feel austere to non-technical visitors | Dark hero must not drift toward generic "dark tech" | Relies most on excellent photography |

## Shared across all four
- Positioning: one engineering team for network, satellite, security, AV and power infrastructure, from site survey to support; own fabrication.
- IA from `SPEC.md` §4 (Solutions · Remote & Satellite · How we work · Company · Contact) with "Request a site survey" as the primary CTA and a sticky Call / WhatsApp / Survey bar on mobile.
- Procurement hook ("Preparing a tender or vendor file? Request our company profile").
- Verified facts only: 14 disciplines, 15+ years team experience, Wilson Airport HQ, VSAT platforms, fabrication items, 26 technology brands (as "technologies we work with").

## Open content points (do not block the choice)
- WhatsApp number (the bar links to contact for now), licences/accreditations, projects, partner status, CCTV as a service.
- Direction 2 maps brands to disciplines (e.g. Optex → intrusion detection) by product category; owner to confirm.
- Direction 4's photography plate is an art-direction brief, produced with Nano Banana Pro only after selection.

## Recommendation
**Direction 1 (Cross-Section)**, carrying Direction 2's register as the Solutions index page. It explains 14 disciplines in one picture, makes "one team" visible rather than claimed, works without project photography (which Sentrum has not supplied yet), and has no close equivalent among Kenyan peers. Direction 3 is the stronger choice if the owner wants remote/VSAT work to lead the brand.

---

# Round 2 — hybrids of 1 · Cross-Section and 3 · Footprint (signal path)

Owner feedback: keep Cross-Section's "text changes on the structure", lose the half-page text scrolling beside a sticky drawing; keep Footprint's signal path.
All three share one drawing (`design/assets/bld.svg.html`), one set of step copy (`design/partials/steps.html`) and one controller (`design/partials/stepper.js`). The signal now **travels through the building**: satellite → dish → riser → floors → comms room → entrances → rooms, and segments stay lit once the signal has "arrived".

| | 5 · Live Section | 6 · Night Section | 7 · Signal Line |
|---|---|---|---|
| **Mechanism** | Whole stage pins; scroll swaps the text **in place** and advances the signal (no partial scrolling) | No scroll-jacking: system index beside the drawing, auto-advances every 6 s, stops on first interaction | Pinned panorama: camera pans remote site → satellite → head office as you scroll; text swaps in a band below |
| **First frame** | Headline + full building with the whole signal flowing | Wide-caps headline, night drawing, "The link" selected | Headline + dashed route from remote mast to head office |
| **Navigation** | 6-part progress stepper (click to jump) | Tabs (keyboard arrows) | Route rail with stops (click to jump) |
| **Look** | Drafting paper, Instrument Sans (from 1) | Night + chart paper, Archivo wide (from 3) + East Africa map section | Chart paper, Hanken Grotesk; the remote site gets equal billing |
| **Mobile** | Drawing on top, text below, both pinned | Drawing, swipeable tabs, caption | Panorama top 38%, text + rail below |
| **Best when** | The building story should lead | Owner prefers conventional scrolling | Remote/VSAT work should lead |

Recommendation: **5**, with 6's no-scroll behaviour as the fallback on reduced motion. Evidence: `design/screenshots/design-{5,6,7}-*` including `-pin*` frames captured at several scroll positions.

---

# Decision — final direction (`design/design-final.html`)

Owner chose **5 · Live Section** with changes:
- Top section (header + hero) on night navy `#0B1620` (owner-specified, from direction 3); white logo; Sentrum blue `#29A9E1` for accents and CTAs. Remote & satellite section is white; process on paper; company white; closing band blue; footer ink.
- Systems carousel **advances by itself** (7 s per system). The active system's signal is drawn in sync with its timer bar.
- On desktop the hero is also pinned for a short span, so **scrolling still steps through the systems**; auto-advance keeps the scroll position in sync so the next scroll continues from the visible slide. After the last system, scrolling continues into the page.
- Controls: progress bars (click/arrow keys), prev / pause / next, swipe on touch. Pauses on hover/focus of the carousel, hidden tab, or when the hero leaves the screen. Reduced motion: starts paused, no animation.
- Mobile: no pinning; auto-advance + swipe + controls; slide area sized to the tallest slide.
- Carousel controls: **B · Stretch dots** (owner choice) — six dots, the active one stretches into a filling bar; tap a dot to jump, tap the active bar to pause/play ("Paused" label appears). Arrows, counter and pause button removed.
