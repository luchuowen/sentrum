# Build a self-contained fragment of the built home page for the Artifact tool (fonts/images inlined as data URIs, internal links inert).
import re, base64, sys, pathlib
d = pathlib.Path('dist'); h = (d / 'index.html').read_text()
css = '\n'.join(re.findall(r'<style[^>]*>(.*?)</style>', h, re.S))
body = re.search(r'<body[^>]*>(.*)</body>', h, re.S).group(1)
body = re.sub(r'<script type="application/ld\+json">.*?</script>', '', body, flags=re.S)
mime = {'.jpg': 'image/jpeg', '.svg': 'image/svg+xml', '.woff2': 'font/woff2'}
cache = {}
def data(m):
    p = m.group(0)
    if p not in cache:
        f = d / p.lstrip('/'); cache[p] = f'data:{mime[f.suffix]};base64,' + base64.b64encode(f.read_bytes()).decode()
    return cache[p]
rx = r'/(?:fonts|img|brand)/[\w.-]+\.(?:woff2|jpg|svg)'
css = re.sub(rx, data, css); body = re.sub(rx, data, body)
body = re.sub(r'href="/[^"]*"', 'href="#"', body)   # inner pages are not part of this preview
guard = '<script>document.addEventListener("click",e=>{const a=e.target.closest&&e.target.closest("a");if(a&&/^[\\/#]/.test(a.getAttribute("href")||""))e.preventDefault()},true)</script>'
out = f'<title>Sentrum Communications</title>\n<script>document.documentElement.classList.add("js")</script>\n<style>{css}</style>\n{body}\n{guard}\n'
pathlib.Path(sys.argv[1]).write_text(out); print(len(out) // 1024, 'KB')
