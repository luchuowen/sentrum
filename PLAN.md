# PLAN — Sentrum production build

Source of truth for how the site is built. Design: `design/design-final.html` (hero) + `DESIGN-DIRECTIONS.md`. Scope: `SPEC.md`.

## 1. Architecture
- **Astro 7, static output**, `trailingSlash: 'always'`, `build.format: 'directory'`. No UI framework; vanilla TS islands inlined per component.
- **Data-driven pages**: `src/data/site.ts` (company facts, nav, contact) and `src/data/services.ts` (5 areas × 14 services, plain-language copy). Area and service pages are generated from it with `getStaticPaths`.
- **Firebase**: Hosting serves `dist/`; `/api/enquiry` rewrites to Cloud Function `submitEnquiry` (2nd gen, europe-west4) → Firestore `enquiries` (europe-west4) + `mail` doc for the Trigger Email extension. Rules deny all client access. Not deployed until the owner approves.

## 2. Files
```
src/layouts/Base.astro        head/SEO/JSON-LD, header, footer, mobile bar, menu
src/components/Hero.astro     home hero: live section + stretch-dot carousel (from design-final)
src/components/Building.astro section drawing; `highlight` prop lights one system (inner-page heroes)
src/components/PageHero.astro navy inner-page hero: breadcrumb, title, plain-language lede, drawing
src/components/CtaBand.astro  closing survey band
src/pages/…                   index, solutions/, solutions/[area]/, solutions/[area]/[service]/,
                              remote-and-satellite/, how-we-work/, company/, contact/, support/, privacy/, 404
src/pages/sitemap.xml.ts      generated sitemap
src/styles/global.css         tokens + components (one file, ~20 KB)
public/                       fonts, brand, img, robots.txt, favicon, og.png
functions/                    submitEnquiry (TypeScript)
firebase.json, .firebaserc, firestore.rules, firestore.indexes.json
```

## 3. Page sequence (each: build → desktop + mobile screenshots → fix → next)
1. Layout + home (hero + body)   2. Solutions hub   3. Five area pages   4. Fourteen service pages
5. Remote & satellite   6. How we work   7. Company   8. Contact (form)   9. Support   10. Privacy, 404

## 4. Design review decisions (award bar)
Kept: live section hero, stretch-dot carousel, expanding capability panels, image-led remote section, environment cards.
Changed after self-review:
- Mono uppercase kickers everywhere → sans kickers; mono reserved for real data (specs, coordinates).
- "In-house" as a big stat → removed (not a number). Facts: 14 · 15+ · Nairobi HQ.
- Brand tag cloud → quiet typographic list in columns.
- Inner pages open on a navy hero with the same building drawing, lit on that page's system — one visual language site-wide, no stock hero photos.
- Every service page leads with **"In plain terms"** for non-technical visitors, then scope, where it's used, how a job runs, related services.

## 5. Content model (per service)
`slug, name, plain (one sentence, no jargon), summary, deliver[] (scope bullets from legacy evidence), usedIn[], tech[] (brands, only where the legacy site lists them), faq? (none — no invented answers)`.

## 6. Performance · a11y · SEO
- Fonts: 3 Instrument Sans weights + 1 JetBrains Mono, WOFF2, preload 600. Images: `loading=lazy`, explicit sizes. JS per page < 8 KB.
- WCAG 2.2 AA: skip link, landmarks, one H1, focus rings, reduced motion, form labels + inline errors, 44 px mobile targets.
- Unique title/description, canonical, OG/Twitter, JSON-LD (Organization/LocalBusiness on all pages, Service + BreadcrumbList on service pages), sitemap.xml, robots.txt, custom 404.

## 7. Verification
`npm run build` · `bash scripts/factory-check.sh full` (gates, local links in dist, logo reference) · Playwright screenshots of every page at 1440 and 390 with console-error and overflow checks · axe-core scan · fresh-context reviewer agent against SPEC + PLAN.

## 8. Known content gaps (owner)
Licences/accreditations, projects, WhatsApp number, CCTV confirmation, support hours/SLA, full-resolution imagery (current `public/img` are draft previews), SMTP credentials for enquiry email.
