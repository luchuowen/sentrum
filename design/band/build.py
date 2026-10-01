import base64, pathlib, sys, re, json
b = lambda p, m: f'data:{m};base64,' + base64.b64encode(pathlib.Path(p).read_bytes()).decode()
F = {k: b(f'public/fonts/{v}.woff2', 'font/woff2') for k, v in {'4': 'instrument-sans-latin-400-normal', '5': 'instrument-sans-latin-500-normal', '6': 'instrument-sans-latin-600-normal', 'm': 'jetbrains-mono-latin-500-normal'}.items()}
site = pathlib.Path('src/data/site.ts').read_text()
proc = re.findall(r"\['(\w+)', '((?:[^'\\]|\\.)*)'\]", site[site.index('export const process'):site.index('];', site.index('export const process'))])
proc = [(a, c.replace("\\'", "’")) for a, c in proc]
t = pathlib.Path('design/band/band.tpl.html').read_text()
for k, v in F.items(): t = t.replace('{{F' + k + '}}', v)
t = t.replace('{{IMG}}', b('public/img/cap-security.jpg', 'image/jpeg')).replace('{{P}}', json.dumps(proc))
pathlib.Path(sys.argv[1]).write_text(t); print(proc, len(t)//1024, 'KB')
