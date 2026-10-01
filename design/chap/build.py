import base64, pathlib, re, sys, html as H
b = lambda p, m: f'data:{m};base64,' + base64.b64encode(pathlib.Path(p).read_bytes()).decode()
d = pathlib.Path('dist/solutions/index.html').read_text()
arts = re.findall(r'<article class="chap.*?</article>', d, re.S)[:2]
A = []
for a in arts:
    A.append(dict(img=b('public' + re.search(r'<img src="([^"]+)"', a).group(1), 'image/jpeg'),
      short=H.unescape(re.search(r'</span>([^<]+)</figcaption>', a).group(1)), svg=re.search(r'(<svg class="chap-g".*?</svg>)', a, re.S).group(1),
      name=re.search(r'<h2[^>]*><a[^>]*>(.*?)</a>', a).group(1), hl=re.search(r'class="chap-hl">(.*?)</p>', a).group(1),
      svcs=re.findall(r'<li><a[^>]*><b>(.*?)</b><span>(.*?)</span>', a)))
F = {k: b(f'public/fonts/{v}.woff2', 'font/woff2') for k, v in {'4': 'instrument-sans-latin-400-normal', '5': 'instrument-sans-latin-500-normal', '6': 'instrument-sans-latin-600-normal', 'm': 'jetbrains-mono-latin-500-normal'}.items()}
def txt(a, i, num=False):
    return (f'<div class="t">' + (f'<span class="big" aria-hidden="true">0{i+1}</span>' if num else '') + f'{a["svg"]}<h2>{a["name"]}</h2><p class="hl">{a["hl"]}</p><ul>' +
      ''.join(f'<li><a href="#"><em>0{j+1}</em><b>{n}</b><span>{p}</span><i>→</i></a></li>' for j, (n, p) in enumerate(a['svcs'])) +
      f'</ul><a class="more" href="#">Explore {a["name"].lower()} <i>→</i></a></div>')
def dirA(a, i):  # technical plate
    return f'''<article class="ch{' flip' if i else ''}"><div class="in"><figure class="ph"><span class="cm tl"></span><span class="cm tr"></span><span class="cm bl"></span><span class="cm br"></span><div class="imw"><div class="im" style="background-image:url({a['img']})"></div></div><figcaption><span>FIG. 0{i+1}</span><span>{a['short'].upper()}</span><span>{len(a['svcs'])} SERVICES</span></figcaption></figure>{txt(a, i)}</div></article>'''
def dirB(a, i):  # detail inset
    return f'''<article class="ch{' flip' if i else ''}"><div class="in"><figure class="ph"><div class="im" style="background-image:url({a['img']})"></div><div class="zoom" style="background-image:url({a['img']})"><span>DETAIL ×3</span></div><span class="lbl"><b>0{i+1}</b>{a['short']}</span></figure>{txt(a, i)}</div></article>'''
def dirC(a, i):  # edge bleed
    return f'''<article class="ch{' flip' if i else ''}"><figure class="ph"><div class="im" style="background-image:url({a['img']})"></div><span class="vt">0{i+1} / 05 — {a['short'].upper()}</span></figure><div class="tw">{txt(a, i, True)}</div></article>'''
t = pathlib.Path('design/chap/chap.tpl.html').read_text()
for k, v in F.items(): t = t.replace('{{F' + k + '}}', v)
for k, f in {'A': dirA, 'B': dirB, 'C': dirC}.items(): t = t.replace('{{' + k + '}}', ''.join(f(a, i) for i, a in enumerate(A)))
pathlib.Path(sys.argv[1]).write_text(t); print(len(t)//1024, 'KB', [a['name'] for a in A])
