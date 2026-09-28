---
name: factory
description: Factory status or migration — prints version, caps and gate results; applies playbook migrations.
disable-model-invocation: true
---
`status`: print `.factory/manifest.json` version, run `bash scripts/factory-check.sh gates`, report CLAUDE.md/DECISIONS.md line counts.
`migrate`: read `docs/Software_Factory_Playbook.md` §9 entries after `playbook_version`, apply in order, record in `applied_migrations`.
