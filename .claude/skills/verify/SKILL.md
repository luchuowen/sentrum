---
name: verify
description: Run full verification and record evidence in the open change artifact.
disable-model-invocation: true
---
1. `bash scripts/factory-check.sh full`.
2. Screenshots at 1440×900 and 390×844 for every touched page (`node scripts/shoot.mjs <file>`); inspect them.
3. Console errors, links, forms, alt text, headings, contrast, reduced motion.
4. Run the `reviewer` agent; fix genuine findings; paste commands + results into `## Verification`.
