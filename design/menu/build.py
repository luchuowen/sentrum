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
# A — columns
A = '<div class="mm mA"><div class="wrap"><div class="cols">' + ''.join(f'<div class="col" style="--i:{i}"><a class="ch" href="#">{gl(a["slug"])}<span class="n">0{i+1}</span><b>{amp(a["name"])}</b></a><ul>' + ''.join(f'<li><a href="#">{n}</a></li>' for s, n, p in a['svcs']) + '</ul></div>' for i, a in enumerate(areas)) + '</div>' + foot + '</div></div>'
# B — split preview with photo
B = '<div class="mm mB"><div class="wrap"><div class="sp"><ul class="sp-l">' + ''.join(f'<li><button type="button" data-i="{i}" class="{"on" if i == 0 else ""}"><span class="n">0{i+1}</span>{amp(a["name"])}<i>→</i></button></li>' for i, a in enumerate(areas)) + '</ul><div class="sp-r">' + ''.join(f'<div class="pane{" on" if i == 0 else ""}" data-i="{i}"><figure><img src="{imgs[a["slug"]]}" alt=""></figure><div class="pt"><p class="k">{amp(a["name"])}</p><h3>{a["head"]}</h3><ul>' + ''.join(f'<li><a href="#"><b>{n}</b><span>{p}</span></a></li>' for s, n, p in a['svcs']) + f'</ul><a class="more" href="#">Explore {amp(a["name"]).lower()} →</a></div></div>' for i, a in enumerate(areas)) + '</div></div>' + foot + '</div></div>'
# C — blueprint: building lights the hovered system
step = {'networks': 'backbone', 'security': 'security', 'communications-av': 'rooms', 'power-data-centre': 'core', 'supply-fabrication-support': 'steel'}
bld = pathlib.Path('src/components/SceneBuilding.astro').read_text()
parts = re.search(r'(<g class="ctx">.*?)\{noteSets', bld, re.S).group(1)
parts = re.sub(r'class=\{`sig\$\{on\(\'(\w+)\'\)\}`\}', r'class="sig"', parts)
parts = re.sub(r'class=\{`part\$\{on\(\'(\w+)\'\)\}`\}', r'class="part"', parts)
C = '<div class="mm mC"><div class="wrap"><div class="bp"><div class="bp-l">' + ''.join(f'<a href="#" class="row{" on" if i == 0 else ""}" data-s="{step[a["slug"]]}">{gl(a["slug"])}<span><b>{amp(a["name"])}</b><em>{" · ".join(n for s, n, p in a["svcs"])}</em></span><i>→</i></a>' for i, a in enumerate(areas)) + f'</div><div class="bp-r"><svg class="lb" viewBox="0 40 900 560" data-hl="backbone">{parts}</svg><p class="ro"><span class="ro-s">01 · NETWORKS</span><span>Hover a system</span></p></div></div>' + foot + '</div></div>'
names = [a['name'] for a in areas]
t = pathlib.Path('design/menu/menu.tpl.html').read_text()
for k, v in {'A': hdr('A') + A, 'B': hdr('B') + B, 'C': hdr('C') + C, 'NAMES': json.dumps(names)}.items(): t = t.replace('{{' + k + '}}', v)
for k, v in F.items(): t = t.replace('{{F' + k + '}}', v)
pathlib.Path(sys.argv[1]).write_text(t); print(len(t) // 1024, 'KB')
