import base64, pathlib, re, sys, json, html as H
b = lambda p, m: f'data:{m};base64,' + base64.b64encode(pathlib.Path(p).read_bytes()).decode()
d = pathlib.Path('dist/solutions/index.html').read_text()
qs = [H.unescape(q) for q in re.findall(r'<button role="tab"[^>]*>“(.*?)”</button>', d)]
ps = re.findall(r'<div role="tabpanel".*?</div>', d, re.S)
items = []
for q, p in zip(qs, ps):
    svg = re.search(r'(<svg.*?</svg>)', p, re.S).group(1)
    sysn = H.unescape(re.search(r'</svg>(.*?)</p>', p, re.S).group(1))
    items.append(dict(q=q, svg=svg, sys=sysn, name=H.unescape(re.search(r'<h3>(.*?)</h3>', p).group(1)), plain=H.unescape(re.search(r'</h3>\s*<p>(.*?)</p>', p, re.S).group(1)), li=[H.unescape(x) for x in re.findall(r'<li>(.*?)</li>', p)]))
F = {k: b(f'public/fonts/{v}.woff2', 'font/woff2') for k, v in {'4': 'instrument-sans-latin-400-normal', '5': 'instrument-sans-latin-500-normal', '6': 'instrument-sans-latin-600-normal', 'm': 'jetbrains-mono-latin-500-normal'}.items()}
t = pathlib.Path('design/finder/finder.tpl.html').read_text()
for k, v in F.items(): t = t.replace('{{F' + k + '}}', v)
t = t.replace('{{DATA}}', json.dumps(items))
pathlib.Path(sys.argv[1]).write_text(t); print(len(items), 'items', len(t)//1024, 'KB'); print(items[0])
