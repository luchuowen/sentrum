# Three directions for the Solutions dropdown -> one self-contained artifact fragment.
import base64, pathlib, re, sys, json
b = lambda p, m: f'data:{m};base64,' + base64.b64encode(pathlib.Path(p).read_bytes()).decode()
src = pathlib.Path('src/data/services.ts').read_text()
areas = []
for blk in re.split(r"\n  \{\n    slug: ", src)[1:]:
    slug = blk.split("'")[1]; name = re.search(r"name: '([^']+)'", blk).group(1)
    head = re.search(r"headline: '([^']+)'", blk).group(1).replace("\\'", "’"); img = re.search(r"img: '([^']+)'", blk).group(1)
    svcs = re.findall(r"slug: '([\w-]+)', name: '([^']+)',\n\s+plain: '((?:[^'\\]|\\.)*)'", blk)
    areas.append(dict(slug=slug, name=name, head=head, img=img, svcs=[(s, n.replace('&', '&amp;'), p.replace("\\'", "’")) for s, n, p in svcs]))
g = dict(re.findall(r"'([\w-]+)': '(.*?)',\n", pathlib.Path('src/data/glyphs.ts').read_text()))
F = {k: b(f'public/fonts/{v}.woff2', 'font/woff2') for k, v in {'4': 'instrument-sans-latin-400-normal', '5': 'instrument-sans-latin-500-normal', '6': 'instrument-sans-latin-600-normal', 'm': 'jetbrains-mono-latin-500-normal'}.items()}
logo = b('brand/sentrum-logo-white.svg', 'image/svg+xml')
imgs = {a['slug']: b('public' + a['img'], 'image/jpeg') for a in areas}
gl = lambda s: f'<svg class="gl" viewBox="0 0 48 48" aria-hidden="true">{g[s]}</svg>'
amp = lambda s: s.replace('&', '&amp;')
def hdr(v): return f'''<header class="hdr"><div class="wrap"><img src="{logo}" alt="Sentrum Communications" width="148" height="40">
<nav class="nav"><button class="dd on" type="button" aria-expanded="true">Solutions <i aria-hidden="true"></i></button><a href="#">Remote &amp; Satellite</a><a href="#">How we work</a><a href="#">Company</a><a href="#">Contact</a></nav><a class="cta" href="#">Request a site survey →</a></div></header>'''
foot = '<div class="mm-foot"><span>Not sure what you need? <a href="#">Start from your problem →</a></span><a class="all" href="#">All solutions <i>→</i></a></div>'
short = {'networks': 'Cabling, WiFi and VSAT', 'security': 'Access, intrusion and cyber', 'communications-av': 'Phones, video walls and AV', 'power-data-centre': 'Servers and backup power', 'supply-fabrication-support': 'Equipment, masts and support'}
# A — quiet list
A = '<div class="dd-w"><div class="wrap rel"><div class="pop pA">' + ''.join(f'<a href="#">{amp(a["name"])}<i>→</i></a>' for a in areas) + '<a class="all" href="#">All solutions</a></div></div></div>'
# B — two-step flyout
B = '<div class="dd-w"><div class="wrap rel"><div class="pop pB"><div class="l">' + ''.join(f'<button type="button" data-i="{i}" class="{"on" if i == 0 else ""}">{amp(a["name"])}<i>›</i></button>' for i, a in enumerate(areas)) + '<a class="all" href="#">All solutions</a></div><div class="r">' + ''.join(f'<ul data-i="{i}" class="{"on" if i == 0 else ""}">' + ''.join(f'<li><a href="#">{n}</a></li>' for s_, n, p_ in a['svcs']) + '</ul>' for i, a in enumerate(areas)) + '</div></div></div></div>'
# C — light card
C = '<div class="dd-w"><div class="wrap rel"><div class="pop pC">' + ''.join(f'<a href="#">{gl(a["slug"])}<span><b>{amp(a["name"])}</b><em>{short[a["slug"]]}</em></span></a>' for a in areas) + '<a class="all" href="#">See all solutions <i>→</i></a></div></div></div>'
names = [a['name'] for a in areas]
t = pathlib.Path('design/menu/menu.tpl.html').read_text()
for k, v in {'A': hdr('A') + A, 'B': hdr('B') + B, 'C': hdr('C') + C}.items(): t = t.replace('{{' + k + '}}', v)
for k, v in F.items(): t = t.replace('{{F' + k + '}}', v)
pathlib.Path(sys.argv[1]).write_text(t); print(len(t) // 1024, 'KB')
