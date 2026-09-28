# 2026-09-28 phase1-discovery-design  ·  size: standard

## Intent
Initialise the factory, complete discovery, write SPEC.md, produce four divergent static homepage directions for owner selection.
Out of scope: production build, Nano Banana assets, Firebase, DNS. Constraints: real logo only; no invented claims; no generic SaaS tropes.

## Spec
Factory files per playbook §2 (CLAUDE.md, manifest, DECISIONS, hooks, agents, skills, factory-check). SPEC.md per brief.
`design/design-{1..4}.html` built from `design/src/` by `scripts/build-designs.py`; self-hosted fonts; desktop + mobile screenshots.

## Plan
1. Recover original logo (hash-verified) → brand/. 2. Legacy evidence doc. 3. Research (Kenyan peers — see blueprint; award-level references). 4. SPEC.md. 5. Four directions, render, fix, re-render. 6. DESIGN-DIRECTIONS.md.

## Verification
- `bash scripts/factory-check.sh full` → green (gates, caps, logo reference, local links).
- `node scripts/shoot.mjs design/design-N.html` ×4 → no console errors, no horizontal overflow at 1440 and 390; screenshots in design/screenshots/.
- Mobile menu opened and screenshotted for all four; fixed backdrop-filter containing-block bug (D1) and grid stretch (D2).
- Guard hook proven: Write to brand/sentrum-logo.svg → exit 2.
- Fixed: `.wrap` horizontal padding overridden by section `padding` shorthands (all four) → padding-block.

## Learned
- Section classes combined with `.wrap` must use `padding-block`, never `padding: X 0` (it silently kills gutters).
- A `backdrop-filter` header becomes the containing block for `position:fixed` children — mobile menus inside it collapse.
