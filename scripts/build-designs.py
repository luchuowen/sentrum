"""Assemble design/src/*.html → design/*.html, inlining <!--NAME_SVG--> from design/assets/<name>.svg.html."""
import re, pathlib
root = pathlib.Path(__file__).resolve().parent.parent / "design"
for src in sorted((root / "src").glob("design-*.html")):
    html = src.read_text()
    for name in set(re.findall(r"<!--([A-Z0-9]+)_SVG-->", html)):
        html = html.replace(f"<!--{name}_SVG-->", (root / "assets" / f"{name.lower()}.svg.html").read_text())
    (root / src.name).write_text(html)
    print("built", src.name, len(html))
