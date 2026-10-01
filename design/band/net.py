import base64, pathlib, sys, re, json
b = lambda p, m: f'data:{m};base64,' + base64.b64encode(pathlib.Path(p).read_bytes()).decode()
F = {k: b(f'public/fonts/{v}.woff2', 'font/woff2') for k, v in {'4': 'instrument-sans-latin-400-normal', '5': 'instrument-sans-latin-500-normal', '6': 'instrument-sans-latin-600-normal', 'm': 'jetbrains-mono-latin-500-normal'}.items()}
site = pathlib.Path('src/data/site.ts').read_text()
proc = [(a, c.replace("\\'", "’")) for a, c in re.findall(r"\['(\w+)', '((?:[^'\\]|\\.)*)'\]", site[site.index('export const process'):site.index('];', site.index('export const process'))])]
rail = '<ol class="rail">' + ''.join(f'<li style="--i:{i}"><b>0{i+1}</b><strong>{t}</strong><span>{d}</span></li>' for i, (t, d) in enumerate(proc)) + '<li class="go"><a href="#">How we work <i>→</i></a></li></ol>'
t = pathlib.Path('design/band/net.tpl.html').read_text()
for k, v in F.items(): t = t.replace('{{F' + k + '}}', v)
t = t.replace('{{TEL}}', b('public/img/env-teleport.jpg', 'image/jpeg')).replace('{{NET}}', b('public/img/cap-networks.jpg', 'image/jpeg')).replace('{{RAIL}}', rail)
t = t.replace('{{VLIST}}', ''.join(f'<li><b>0{i+1}</b><span><strong>{a}</strong>{d}</span></li>' for i, (a, d) in enumerate(proc)))
t = t.replace('{{NODES}}', ''.join(f'<li style="--i:{i}"><i></i><b>0{i+1}</b><strong>{a}</strong><span>{d}</span></li>' for i, (a, d) in enumerate(proc)))
pathlib.Path(sys.argv[1]).write_text(t); print(len(t)//1024, 'KB')
