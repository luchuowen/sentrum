#!/usr/bin/env bash
# SessionStart(compact|resume): re-inject the open change artifact and governing rules.
root=$(git rev-parse --show-toplevel 2>/dev/null) || exit 0
cd "$root"
latest=$(ls -t .factory/changes/*.md 2>/dev/null | grep -v TEMPLATE | head -1)
[ -n "$latest" ] && { echo "Open change artifact: $latest ($(wc -l < "$latest") lines) — re-read before continuing."; }
echo "Files changed on branch:"; git status --short | head -30
for r in .claude/rules/*.md; do [ -f "$r" ] && echo "Rule file available: $r"; done
echo "Reminder: never invent company claims; only original logo files in brand/; DNS scoped to sentrum.navac.co.ke only."
