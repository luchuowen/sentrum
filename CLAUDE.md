# Sentrum website — agent rules (factory v2.1)

Redesign of sentrumcoms.net for Sentrum Communication & Technologies Ltd (Nairobi systems integrator).
Target: https://sentrum.navac.co.ke · Firebase project `sentrum` · Firestore region europe-west4.

## Commands
- verify quick: `bash scripts/factory-check.sh quick` · full: `bash scripts/factory-check.sh full`
- screenshots (design phase): `node scripts/shoot.mjs design/design-N.html` → `design/screenshots/`

## Source of truth
- `SPEC.md` product spec · `PLAN.md` build plan (after direction chosen) · `DESIGN-DIRECTIONS.md`
- `docs/reference/legacy-site.md` = what Sentrum verifiably offers today. Anything not there is a content requirement.

## Loop
1. `/change <slug>` sizes the work and opens `.factory/changes/…` (trivial = no artifact).
2. Critical paths (`.factory/manifest.json`: Firebase config, functions, rules, deploy) → plan mode, `/effort high`, reviewer.
3. Build one page at a time; desktop + mobile screenshots before moving on. The Stop hook runs the quick gate.
4. `/verify` before claiming done; `/ship` to learn, commit, push. Agents never merge or deploy to production.

## Working style
- Scope = the ask: pre-existing issues go in the summary as follow-ups, not the diff.
- Batch independent reads/searches/commands into one response.
- Own the mission: the owner is usually not watching; stop only for credentials, irreversible production actions, or true blockers.

## Invariants without a mechanical check
- Never invent clients, projects, partner tiers, certifications, licences, awards, statistics or testimonials.
- Brand names from the legacy logo wall are "technologies we work with" — never "partner/certified" until confirmed.
- Only the original logo files in `brand/` — never recreated, recoloured or approximated.
- DNS: only records for `sentrum.navac.co.ke`. Never touch navac.co.ke apex, MX/SPF/DKIM/DMARC, NS or other subdomains.
- No production deploy or DNS cutover without the owner's explicit approval in chat.
- No generic SaaS tropes (purple gradients, glass cards, bento grids, orbs, pill-everything, fake metrics).

## Memory
- `.factory/DECISIONS.md` is current truth; read it before assuming something is unbuilt.
- `/ship` appends what was learned; `factory-check` fails when it exceeds its cap → compact into `.factory/history/`.
