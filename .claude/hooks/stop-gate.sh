#!/usr/bin/env bash
# Stop: run the quick gate when tracked sources changed since the last green run.
input=$(cat)
if printf '%s' "$input" | grep -q '"stop_hook_active": *true'; then exit 0; fi
root=$(git rev-parse --show-toplevel 2>/dev/null) || exit 0
cd "$root"
stamp=.factory/.last-green
sig=$( (git diff HEAD --stat; git ls-files -o --exclude-standard) 2>/dev/null | sha1sum | cut -d' ' -f1)
[ -f "$stamp" ] && [ "$(cat "$stamp")" = "$sig" ] && exit 0
if out=$(bash scripts/factory-check.sh quick 2>&1); then echo "$sig" > "$stamp"; exit 0; fi
echo "$out" | tail -40 >&2
exit 2
