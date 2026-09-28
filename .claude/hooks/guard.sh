#!/usr/bin/env bash
# PreToolUse(Edit|Write): protected paths, append-only dirs, wasteful whole-file rewrites.
set -euo pipefail
input=$(cat)
root=$(git rev-parse --show-toplevel 2>/dev/null || pwd)
tool=$(printf '%s' "$input" | python3 -c 'import sys,json;print(json.load(sys.stdin).get("tool_name",""))')
file=$(printf '%s' "$input" | python3 -c 'import sys,json;print(json.load(sys.stdin).get("tool_input",{}).get("file_path",""))')
[ -z "$file" ] && exit 0
rel=${file#"$root"/}
python3 - "$root" "$rel" "$tool" <<'PY' "$input"
import sys, json, subprocess, os
root, rel, tool = sys.argv[1:4]
payload = json.loads(sys.argv[4])
m = json.load(open(os.path.join(root, ".factory/manifest.json")))
def fail(msg): print(msg, file=sys.stderr); sys.exit(2)
for p in m.get("protected", []):
    if rel == p or rel.startswith(p.rstrip("/") + "/"):
        fail(f"guard: {rel} is protected (manifest.protected). Owner must name this exact file to allow an edit.")
for d in m.get("append_only_dirs", []):
    if rel.startswith(d.rstrip("/") + "/"):
        r = subprocess.run(["git", "-C", root, "cat-file", "-e", f"HEAD:{rel}"], capture_output=True)
        if r.returncode == 0: fail(f"guard: {rel} is in append-only dir {d} and already committed; add a new file instead.")
if tool == "Write":
    path = os.path.join(root, rel)
    new = payload.get("tool_input", {}).get("content", "")
    if os.path.exists(path):
        old = open(path, encoding="utf-8", errors="ignore").read().splitlines()
        if len(old) >= 150:
            newl = new.splitlines(); oldset = set(old)
            changed = sum(1 for l in newl if l not in oldset)
            if changed < 0.25 * len(old):
                fail(f"guard: Write re-emits {len(old)}-line {rel} to change ~{changed} lines; use Edit.")
PY
