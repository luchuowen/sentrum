"""Assemble design/src/*.html → design/*.html.
Includes: <!--NAME_SVG--> → design/assets/<name>.svg.html ; <!--INC:path--> → design/<path>."""
import re, pathlib
root = pathlib.Path(__file__).resolve().parent.parent / "design"
for src in sorted((root / "src").glob("design-*.html")):
    html = src.read_text()
    for name in set(re.findall(r"<!--([A-Z0-9]+)_SVG-->", html)):
        html = html.replace(f"<!--{name}_SVG-->", (root / "assets" / f"{name.lower()}.svg.html").read_text())
    for inc in set(re.findall(r"<!--INC:([\w./-]+)-->", html)):
        html = html.replace(f"<!--INC:{inc}-->", (root / inc).read_text())
    (root / src.name).write_text(html)
    print("built", src.name, len(html))
