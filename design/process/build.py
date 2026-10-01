# Three compact variations of the "Stage" counter for the home "How we work" section.
import base64, pathlib, sys
b = lambda p, m: f'data:{m};base64,' + base64.b64encode(pathlib.Path(p).read_bytes()).decode()
S = [('Survey','We visit the site and see what is there.'),('Design','We plan the layout and cost every item.'),
     ('Supply','We source equipment from established makers.'),('Install','Our engineers install and label everything.'),
     ('Commission','We test it, set it up and train your team.'),('Support','We stay on to support what we install.')]
n = lambda i: f'0{i+1}'
more = '<a class="more" href="#">The full process <span aria-hidden="true">→</span></a>'
h2 = '<h2>The same team, from first survey to support.</h2>'
odo = lambda: '<div class="odo" aria-hidden="true"><span class="z">0</span><span class="roll"><span class="strip">' + ''.join(f'<span>{i+1}</span>' for i in range(6)) + '</span></span></div>'
txt = lambda: '<div class="tx" aria-live="polite">' + ''.join(f'<div class="ts{" on" if i==0 else ""}"><h3>{s[0]}</h3><p>{s[1]}</p></div>' for i,s in enumerate(S)) + '</div>'
seg = lambda lbl=True: '<ol class="seg">' + ''.join(f'<li><button type="button" data-i="{i}"><i></i><span class="n">{n(i)}</span>{"<span class=sl>"+s[0]+"</span>" if lbl else ""}</button></li>' for i,s in enumerate(S)) + '</ol>'
# A — Side: heading left, counter right
A = f'<div class="st sa"><div class="hd">{"<p class=k>How we work</p>"}{h2}{more}</div><div class="stage"><div class="row">{odo()}{txt()}</div>{seg(False)}</div></div>'
# B — Band: counter, step text and a live index in one row
idx = '<ol class="ix">' + ''.join(f'<li><button type="button" data-i="{i}"><span class="n">{n(i)}</span>{s[0]}</button></li>' for i,s in enumerate(S)) + '</ol>'
B = f'<div class="st sb"><div class="top"><div><p class="k">How we work</p>{h2}</div>{more}</div><div class="band">{odo()}{txt()}{idx}</div></div>'
# C — Ticker: outline number fills, name rolls, one continuous notched bar
roll = '<div class="nm" aria-hidden="true"><span class="nstrip">' + ''.join(f'<span>{s[0]}</span>' for s in S) + '</span></div>'
desc = '<div class="tx" aria-live="polite">' + ''.join(f'<div class="ts{" on" if i==0 else ""}"><p><span class="visually-hidden">{s[0]}: </span>{s[1]}</p></div>' for i,s in enumerate(S)) + '</div>'
bar = '<div class="bar" aria-hidden="true"><i class="bar-f"></i>' + ''.join(f'<span style="left:{i*100/6:.4f}%"></span>' for i in range(1,6)) + '</div>'
C = f'<div class="st sc"><div class="top"><div><p class="k">How we work</p>{h2}</div>{more}</div><div class="tk">{odo()}{roll}{desc}</div>{bar}</div>'
t = pathlib.Path('design/process/process.tpl.html').read_text()
t = t.replace('{{A}}', A).replace('{{B}}', B).replace('{{C}}', C)
for k, p in {'F4':'instrument-sans-latin-400-normal','F5':'instrument-sans-latin-500-normal','F6':'instrument-sans-latin-600-normal','FM':'jetbrains-mono-latin-500-normal'}.items():
    t = t.replace('{{'+k+'}}', b(f'public/fonts/{p}.woff2','font/woff2'))
pathlib.Path(sys.argv[1]).write_text(t); print(len(t)//1024,'KB')
