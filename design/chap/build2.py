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
def txt(a, i):
    return (f'<div class="t"><p class="ix"><b>0{i+1}</b><span></span>05</p><h2>{a["name"]}</h2><p class="hl">{a["hl"]}</p><ul>' +
      ''.join(f'<li data-j="{j}"><a href="#"><b>{n}</b><span>{p}</span><i>→</i></a></li>' for j, (n, p) in enumerate(a['svcs'])) +
      f'</ul><a class="more" href="#">Explore {a["name"].lower()} <i>→</i></a></div>')
def art(a, i, fig):
    return f'<article class="ch{" flip" if i else ""}" style="--img:url({a["img"]})"><div class="in">{fig(a, i)}{txt(a, i)}</div></article>'
N = 5
def fA(a, i):
    return '<figure class="ph slats">' + ''.join(f'<span class="sl" style="--k:{k}"><span></span></span>' for k in range(N)) + f'<figcaption><span class="g">{a["svg"]}</span>{a["short"]}</figcaption></figure>'
def fB(a, i):
    return f'<figure class="ph cham"><span class="ol"></span><span class="im"></span><span class="tag">0{i+1} / {a["short"].upper()}</span><span class="rul"></span></figure>'
def fC(a, i):
    return f'<figure class="ph duo"><span class="im"></span><span class="tint"></span><span class="num">0{i+1}</span><span class="foc">{a["svcs"][0][0]}</span></figure>'
t = pathlib.Path('design/chap/chap2.tpl.html').read_text()
for k, v in F.items(): t = t.replace('{{F' + k + '}}', v)
for k, f in {'A': fA, 'B': fB, 'C': fC}.items(): t = t.replace('{{' + k + '}}', ''.join(art(a, i, f) for i, a in enumerate(A)))
pathlib.Path(sys.argv[1]).write_text(t); print(len(t)//1024, 'KB')
