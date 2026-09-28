# SPEC — Sentrum Communication & Technologies website

Status: approved for design exploration · 2026-09-28 · Evidence: `docs/reference/legacy-site.md`, `docs/reference/*.docx`, live site review, market + design research (summarised in §12).

## 1. Positioning
**Sentrum designs, installs and supports the communications, security and power infrastructure organisations run on — one engineering team from site survey to long-term support, with its own fabrication shop.**

What must be understood in 5 seconds: *what* (network, satellite, security, AV and power infrastructure) · *how* (one accountable team: survey → design → supply → install → commission → support) · *where* (Nairobi HQ, projects across Kenya and Africa) · *next step* (request a site survey / talk to an engineer).

Differentiators we can evidence today:
1. **Breadth under one contract** — 14 disciplines normally split across several contractors.
2. **Satellite and remote-site capability** — iDirect, SkyEdge and Comtech platforms; SCPC and broadcast backhaul; Ku-band terminals to teleport antennas and RFTs; multi-site, multi-country rollouts.
3. **In-house fabrication** — masts, VSAT and video-wall mounts, UPS racks, aviation-light brackets, CCTV mounts, gates, TV carts. Fewer subcontractors, faster installs.
4. **Technical team with 15+ years in the field.**
5. **Broad technology base** — the 26 brands on the legacy site (status unconfirmed → "technologies we work with").

## 2. Audiences
| Audience | Arrives needing | Must leave knowing / doing |
|---|---|---|
| Corporate IT & facilities managers | a network refresh, office fit-out, meeting-room AV, access control, UPS | Sentrum covers the whole scope; how a job runs; → request survey/quote |
| Procurement & tender teams (government, parastatals, counties, NGOs/UN) | shortlisting for an RFQ/tender | registration, compliance documents, scope categories, contacts → download/request company profile |
| Operators of remote sites (NGOs, UN agencies, energy, mining, broadcast, service providers) | connectivity + power where terrestrial networks don't reach | VSAT platform depth, fabrication, field delivery → talk to an engineer |
| Existing clients | a fault or support request | how to reach support fast → call/WhatsApp/support form |

Main contractors/consultants (sub-contracting ICT/ELV packages) are a plausible fourth audience — **owner to confirm**.

## 3. Visitor jobs-to-be-done
1. "Can this company handle my whole scope?" → capability map on home + solution pages.
2. "Have they done work like mine?" → project proof (content-conditional) + specific technical detail per service.
3. "Are they a safe choice to procure?" → Company & credentials page, company profile download, physical address, direct lines.
4. "What happens if I engage them?" → delivery model + what the buyer receives.
5. "How do I start, now?" → one clear enquiry path on every page; phone/WhatsApp on mobile.
6. "Something is broken." → Support route visible in header/footer.

## 4. Information architecture
Primary nav: **Solutions · Remote & Satellite · How we work · Company · Contact** + persistent CTA **Request a site survey**. Utility: phone, WhatsApp, Support.

```
/                                   Home
/solutions/                         Capability map (5 areas, 14 services)
  /solutions/networks/              Networks & Connectivity
     /structured-cabling/  /wifi/  /vsat/
  /solutions/security/              Security Systems
     /access-control/  /intrusion-detection/  /cyber-security/  (+ /cctv/ if confirmed)
  /solutions/communications-av/     Communications & AV
     /unified-communications/  /video-walls/  /audio-visual/
  /solutions/power-data-centre/     Power & Data Centre
     /servers/  /power-ups/
  /solutions/supply-fabrication-support/
     /it-equipment/  /fabrication/  /technical-support/
/remote-and-satellite/              Signature page: VSAT + power + fabrication for hard-to-reach sites
/how-we-work/                       Delivery model, what clients receive, support
/projects/                          CONDITIONAL — ships only with ≥3 owner-supplied projects
/company/                           About, mission, values, team, HQ, credentials & procurement pack
/contact/                           Enquiry form, direct lines, WhatsApp, map, directions
/support/                           Fault/support route (content-conditional detail)
/privacy/  /404
```
Legacy URL map (`/vsat-installation.html` → `/solutions/networks/vsat/`, etc.) is kept in `src/data/redirects.ts` for when sentrumcoms.net is pointed at the new build.

## 5. Service architecture (page template)
Each service page: plain-language outcome → **scope we deliver** (list from legacy evidence) → environments it's used in → how the job runs → technologies we work with (brand names only) → related services → enquiry block pre-filled with the service. Each capability-area page: the problem → services → delivery → related remote/satellite angle where true → CTA.

## 6. Content strategy
- Rewrite everything; legacy copy is evidence, not copy. Specific nouns over adjectives. Short statements, useful detail.
- Banned phrases (gated): cutting-edge, seamless integration, transform your business, world-class, innovative solutions. Also avoid "pioneers", "top notch", "decades".
- Never invented: clients, projects, partner tiers, certifications, licences, awards, statistics, testimonials, SLAs, response times.
- Content-conditional modules (hidden until supplied): Projects, Sectors, credentials list, support SLA, partner status labels, team.
- Owner content request list: see blueprint §G. Brand line "It's not about the technology. It's about what you do with it." may be retained (owner choice).

## 7. Visual & interaction principles
- One strong idea per page; composition from a visible grid; hierarchy of display / reading / metadata layers.
- Colour from the logo: Sentrum blue `#29A9E1` and wordmark grey `#5A5B5D`, plus neutrals. Colour has a job (signal, state, link) — no gradients, glows, glass.
- Imagery: real Sentrum site photography when supplied; until then original generated imagery (Nano Banana Pro) that depicts representative equipment and environments — never captioned as a specific Sentrum project.
- Motion explains a mechanism or state (signal path, layer reveal, power switchover); one signature interaction per page; `prefers-reduced-motion` honoured; content never hidden behind animation.
- Mobile first: proposition + CTA in first viewport; sticky Call · WhatsApp · Survey bar.
- Avoid: purple/blue SaaS gradients, generic dark templates, glassmorphism, bento grids, centred hero + two pills, arbitrary 01/02/03 labels, decorative mono, orbs, stock tech photos, icon-grid repetition, fake metrics, decorative WebGL.

## 8. Technology
- **Astro (static output)**, TypeScript, vanilla CSS with design tokens; no UI framework; islands only where interaction needs JS. Self-hosted WOFF2 via @fontsource. `astro:assets` for AVIF/WebP responsive images.
- **Firebase**: project `sentrum` (display name "Sentrum"); Hosting (static); Firestore in **europe-west4** for enquiries; one 2nd-gen Cloud Function (europe-west4) `submitEnquiry` validating, rate-limiting (honeypot + time-trap + per-IP), writing to Firestore and notifying by email (Trigger Email extension; SMTP credentials from owner — dependency). Security rules deny all client reads/writes.
- Analytics: privacy-light (GA4 with consent or cookieless) — owner decision at build; events: survey submit, tel, WhatsApp, profile download.

## 9. Performance (budgets, mobile, lab)
Lighthouse mobile ≥ 95 performance / 100 accessibility / 100 best-practices / 100 SEO · LCP ≤ 2.0 s · CLS ≤ 0.05 · INP ≤ 200 ms · JS ≤ 30 KB gz per page · CSS ≤ 40 KB gz · home total transfer ≤ 800 KB · hero image ≤ 160 KB AVIF · fonts ≤ 2 families, ≤ 4 files preloaded ≤ 1 · hashed assets cached 1 year.

## 10. Accessibility — WCAG 2.2 AA
Semantic landmarks; one H1; ordered headings; skip link; keyboard-operable menu (Esc closes, focus trapped in mobile menu); visible 2 px focus; 24×24 min targets (44 on mobile CTAs); contrast AA (text ≥ 4.5:1); labelled form fields, inline errors with `aria-describedby`; meaningful alt / empty alt for decorative; reduced motion; no content in images of text.

## 11. SEO
Unique titles (≤ 60) and descriptions (≤ 155); canonical (single `SITE_URL` constant, default `https://sentrum.navac.co.ke`); OG/Twitter cards with designed OG image; `sitemap.xml`, `robots.txt`; JSON-LD Organization/LocalBusiness (name, logo, address, phone), BreadcrumbList, Service on service pages; clean URLs; internal links service ↔ area ↔ contact; no FAQ schema, no keyword stuffing.

## 12. Research summary (inputs, not deliverables)
- Kenyan peers (Teledata, Talinda, HSC, Informed, Symphony, Copy Cat, Liquid…): group into 4–7 solution areas; OEM logo walls universal; licences rarely shown (only Teledata); project proof scarce; sector pages rare; hygiene poor. Opportunity: evidence, clarity, procurement readiness, speed.
- Award-level references (Awwwards SOTD 2024–26: Terminal Industries, Seasats, ON.energy, NEVERHACK, United Carriers, USAvionix, Q-Industrial; Oxide, Astranis, K2): one idea per page; claims only this company could make; 1–2 colour systems with defined roles; spec-sheet/mono metadata layer as real information; motion that shows a mechanism; IA that follows how buyers buy.

## 13. Asset workflow
1. Prompt written per asset in `assets/prompts/<page>-<slot>.md` (subject, composition, lens, light, environment, materials, palette, aspect, crop notes, relation to layout).
2. Generate in Nano Banana Pro (owner logs in), inspect, regenerate as needed.
3. Save master to `assets/masters/`; derive via `astro:assets` (AVIF/WebP, widths 480–2400); verify in page at desktop + mobile crops.
4. No stock imagery. No image implies a named client/project. Replace with real photography when supplied.

## 14. Hosting & deployment
Firebase Hosting preview channels for review; production deploy and DNS change only after owner approval. Custom domain `sentrum.navac.co.ke`: add only the records Firebase issues for that host (TXT verification + A/CNAME) — never apex, MX, SPF, DKIM, DMARC, NS or other subdomains. `firebase.json`: clean URLs, trailing-slash policy, security headers (HSTS, CSP, X-Content-Type-Options, Referrer-Policy, Permissions-Policy, frame-ancestors 'none'), long cache for hashed assets, custom 404.

## 15. Scope boundaries
In: pages in §4, enquiry flow, SEO/a11y/perf foundations, asset generation, deployment. Out: CMS, blog/insights, e-commerce, client portal, multilingual, company-profile PDF design, on-site photography, paid media. Conditional: Projects, Sectors, credentials detail, support SLA.

## 16. Launch verification criteria
All pages built and screenshot-reviewed at 1440/1024/768/390; `factory-check full` green; zero console errors; all links resolve; form end-to-end (valid, invalid, spam, rate-limit) with Firestore write + email; Lighthouse budgets met on home + one service page; axe clean; metadata/OG/JSON-LD validated; sitemap/robots live; security headers present; SSL valid on sentrum.navac.co.ke; DNS diff limited to the subdomain; fresh-context reviewer pass against SPEC + PLAN with genuine findings fixed; no placeholder text or imagery anywhere.
