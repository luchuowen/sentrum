import base64, pathlib, re, sys
b = lambda p, m: f'data:{m};base64,' + base64.b64encode(pathlib.Path(p).read_bytes()).decode()
src = pathlib.Path('src/data/services.ts').read_text()
areas = [(blk.split("'")[1], re.search(r"name: '([^']+)'", blk).group(1)) for blk in re.split(r"\n  \{\n    slug: ", src)[1:]]
g = dict(re.findall(r"'([\w-]+)': '(.*?)',\n", pathlib.Path('src/data/glyphs.ts').read_text()))
short = {'networks': 'Cabling, WiFi and VSAT', 'security': 'Access, intrusion and cyber', 'communications-av': 'Phones, video walls and AV', 'power-data-centre': 'Servers and backup power', 'supply-fabrication-support': 'Equipment, masts and support'}
amp = lambda s: s.replace('&', '&amp;')
gl = lambda s: f'<svg class="gl" viewBox="0 0 48 48" aria-hidden="true">{g[s]}</svg>'
F = {k: b(f'public/fonts/{v}.woff2', 'font/woff2') for k, v in {'4': 'instrument-sans-latin-400-normal', '5': 'instrument-sans-latin-500-normal', '6': 'instrument-sans-latin-600-normal', 'm': 'jetbrains-mono-latin-500-normal'}.items()}
logo = b('brand/sentrum-logo-white.svg', 'image/svg+xml'); logod = b('brand/sentrum-logo.svg', 'image/svg+xml')
th = {k: b(f'public/img/{v}.jpg', 'image/jpeg') for k, v in {'r': 'remote-site', 'h': 'cap-fabrication', 'c': 'env-office', 'k': 'env-campus'}.items()}
links = [('Remote &amp; Satellite', 'r'), ('How we work', 'h'), ('Company', 'c'), ('Contact', 'k')]
def bar(dark=True): return f'<div class="bar"><img src="{logo if dark else logod}" alt="Sentrum"><button class="tg" type="button" aria-label="Close menu"><i></i><i></i></button></div>'
# A — indexed
A = f'<div class="ph pA">{bar()}<nav><div class="it sol"><button type="button" class="row"><em>01</em><b>Solutions</b><s></s></button><div class="sub"><div class="tiles">' + ''.join(f'<a href="#">{gl(s)}<span>{amp(n)}</span></a>' for s, n in areas) + '<a class="all" href="#">All solutions →</a></div></div></div>' + ''.join(f'<a class="row it" href="#" style="--d:{i+1}"><em>0{i+2}</em><b>{t}</b><i>→</i></a>' for i, (t, _) in enumerate(links)) + '</nav><div class="ft"><p class="k">Talk to us</p><a href="#">+254 720 288 713</a><a href="#">info@sentrumcoms.net</a><a class="cta" href="#">Request a site survey →</a><p class="co">1.3204° S · 36.8127° E · Wilson Airport</p></div></div>'
# B — light sheet
B = f'<div class="ph pB">{bar()}<div class="sheet"><p class="k">Solutions</p><div class="sys">' + ''.join(f'<a href="#">{gl(s)}<span><b>{amp(n)}</b><em>{short[s]}</em></span><i>›</i></a>' for s, n in areas) + '</div><div class="grid">' + ''.join(f'<a href="#">{t}<i>↗</i></a>' for t, _ in links) + '</div><a class="cta" href="#">Request a site survey <i>→</i></a><div class="ct"><a href="#">Call</a><a href="#">Email</a></div></div></div>'
# C — photo index
C = f'<div class="ph pC">{bar()}<nav><div class="it sol"><button type="button" class="row"><b>Solutions</b><span class="cnt">5 systems</span><s></s></button><div class="sub"><ul>' + ''.join(f'<li><a href="#">{gl(s)}{amp(n)}</a></li>' for s, n in areas) + '</ul></div></div>' + ''.join(f'<a class="row it" href="#" style="--d:{i+1}"><b>{t}</b><span class="tb" style="background-image:url({th[k]})"></span></a>' for i, (t, k) in enumerate(links)) + '</nav><div class="ft"><a class="cta" href="#">Request a site survey →</a><div class="ct"><a href="#">+254 720 288 713</a><span>·</span><a href="#">Email us</a></div></div></div>'
t = pathlib.Path('design/mnav/mnav.tpl.html').read_text()
for k, v in F.items(): t = t.replace('{{F' + k + '}}', v)
t = t.replace('{{A}}', A).replace('{{B}}', B).replace('{{C}}', C)
pathlib.Path(sys.argv[1]).write_text(t); print(len(t)//1024, 'KB')
