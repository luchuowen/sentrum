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
