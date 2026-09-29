import base64, pathlib, sys
root = pathlib.Path('.'); t = pathlib.Path('design/heroes/heroes.tpl.html').read_text()
b = lambda p, m: f'data:{m};base64,' + base64.b64encode(pathlib.Path(p).read_bytes()).decode()
rep = {'F_IS400': b('public/fonts/instrument-sans-latin-400-normal.woff2', 'font/woff2'), 'F_IS500': b('public/fonts/instrument-sans-latin-500-normal.woff2', 'font/woff2'),
 'F_IS600': b('public/fonts/instrument-sans-latin-600-normal.woff2', 'font/woff2'), 'F_JB': b('public/fonts/jetbrains-mono-latin-500-normal.woff2', 'font/woff2'),
 'F_BR': b('/tmp/claude-0/node_modules/@fontsource-variable/bricolage-grotesque/files/bricolage-grotesque-latin-wght-normal.woff2', 'font/woff2'),
 'LOGO_W': b('brand/sentrum-logo-white.svg', 'image/svg+xml'), 'LOGO': b('brand/sentrum-logo.svg', 'image/svg+xml')}
for k, v in rep.items(): t = t.replace('{{' + k + '}}', v)
t = t.replace('const NOTES=', 'const NOTES=').replace('NOTES[id]', 'NOTES[id]')
pathlib.Path(sys.argv[1]).write_text(t); print(len(t)//1024, 'KB')
