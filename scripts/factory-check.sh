#!/usr/bin/env bash
# factory-check: gates | quick | full   (CI runs the same)
set -uo pipefail
mode=${1:-quick}
root=$(git rev-parse --show-toplevel 2>/dev/null || pwd); cd "$root"
fail=0
gates() {
python3 - <<'PY' || fail=1
import json, re, os, sys, glob
m = json.load(open(".factory/manifest.json")); bad = 0
for g in m["gates"]:
    flags = re.I if g["pattern"].startswith("(?i)") else 0
    rx = re.compile(g["pattern"].replace("(?i)", ""), flags)
    for base in g["paths"]:
        files = [base] if os.path.isfile(base) else [f for f in glob.glob(base + "/**/*", recursive=True) if os.path.isfile(f)]
        for f in files:
            if any(f.startswith(e) for e in g.get("exclude", [])) or f.endswith((".png",".jpg",".webp",".avif",".woff2",".woff")): continue
            for i, line in enumerate(open(f, encoding="utf-8", errors="ignore"), 1):
                if rx.search(line): print(f"GATE {g['name']}: {f}:{i}: {line.strip()[:100]}"); bad = 1
for f, cap in m["caps"].items():
    n = sum(1 for _ in open(f)) if os.path.exists(f) else 0
    if n > cap: print(f"CAP {f}: {n} lines > {cap}"); bad = 1
# every design/page HTML must use an original logo file from brand/ or its copy
for f in glob.glob("design/design-*.html") + glob.glob("dist/**/*.html", recursive=True):
    t = open(f, encoding="utf-8").read()
    if "sentrum-logo" not in t: print(f"LOGO: {f} does not reference the original logo asset"); bad = 1
sys.exit(bad)
PY
}
quick() {
  gates
  if [ -f package.json ] && grep -q '"check"' package.json; then npm run -s check || fail=1; fi
}
full() {
  quick
  if [ -f package.json ] && grep -q '"build"' package.json; then npm run -s build || fail=1; fi
  if [ -f package.json ] && grep -q '"test"' package.json; then npm test -s || fail=1; fi
  # local link integrity for static HTML
  python3 - <<'PY' || fail=1
import re, os, glob, sys
bad = 0
for f in glob.glob("design/*.html") + glob.glob("dist/**/*.html", recursive=True):
    d = os.path.dirname(f); t = open(f, encoding="utf-8").read()
    for ref in re.findall(r'(?:src|href)="([^"#?]+)"', t):
        if ref.startswith(("http", "mailto:", "tel:", "data:", "/")) or ref == "": continue
        if not os.path.exists(os.path.join(d, ref)): print(f"LINK {f}: missing {ref}"); bad = 1
sys.exit(bad)
PY
}
case "$mode" in gates) gates;; quick) quick;; full) full;; *) echo "usage: gates|quick|full"; exit 64;; esac
[ $fail -eq 0 ] && echo "factory-check $mode: green" || { echo "factory-check $mode: RED"; exit 1; }
