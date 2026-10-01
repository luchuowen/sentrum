import base64, pathlib, sys
b = lambda p, m: f'data:{m};base64,' + base64.b64encode(pathlib.Path(p).read_bytes()).decode()
F = {k: b(f'public/fonts/{v}.woff2', 'font/woff2') for k, v in {'4': 'instrument-sans-latin-400-normal', '5': 'instrument-sans-latin-500-normal', '6': 'instrument-sans-latin-600-normal', 'm': 'jetbrains-mono-latin-500-normal'}.items()}
img = b('public/img/rooftop-vsat.jpg', 'image/jpeg'); logo = b('brand/sentrum-logo-white.svg', 'image/svg+xml')
t = pathlib.Path('design/close/close.tpl.html').read_text()
for k, v in F.items(): t = t.replace('{{F' + k + '}}', v)
t = t.replace('{{IMG}}', img).replace('{{LOGO}}', logo)
pathlib.Path(sys.argv[1]).write_text(t); print(len(t)//1024, 'KB')
