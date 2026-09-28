---
name: change
description: Open a change artifact for a non-trivial change and size it (trivial/standard/critical).
disable-model-invocation: true
---
1. Copy `.factory/changes/TEMPLATE.md` to `.factory/changes/<YYYY-MM-DD>-<slug>.md`.
2. Fill Intent with every known constraint. Size from paths: any `manifest.critical_paths` → critical (plan mode, `/effort high`).
3. Fill Spec and Plan before building.
