# Three directions for the home "How we work" section -> one self-contained artifact fragment.
import base64, math, pathlib, sys
b = lambda p, m: f'data:{m};base64,' + base64.b64encode(pathlib.Path(p).read_bytes()).decode()
S = [('Survey','We visit the site and see what is there.'),('Design','We plan the layout and cost every item.'),
     ('Supply','We source equipment from established makers.'),('Install','Our engineers install and label everything.'),
     ('Commission','We test it, set it up and train your team.'),('Support','We stay on to support what we install.')]
n = lambda i: f'0{i+1}'
head = '<header class="hd"><div><p class="k">How we work</p><h2>The same team, from first survey to support.</h2></div><a class="more" href="#">The full process <span aria-hidden="true">→</span></a></header>'
# A — Stage
A = ('<div class="sa"><div class="sa-main"><div class="sa-num" aria-hidden="true"><span class="sa-z">0</span><span class="sa-roll"><span class="sa-strip">'
     + ''.join(f'<span>{i+1}</span>' for i in range(6)) + '</span></span></div><div class="sa-txt" aria-live="polite">'
     + ''.join(f'<div class="sa-s{" on" if i==0 else ""}"><h3>{s[0]}</h3><p>{s[1]}</p></div>' for i,s in enumerate(S)) + '</div></div><ol class="sa-seg">'
     + ''.join(f'<li><button type="button" data-i="{i}"{" class=on" if i==0 else ""}><i></i><span class="n">{n(i)}</span><span class="sa-l">{s[0]}</span></button></li>' for i,s in enumerate(S)) + '</ol></div>')
# B — Loop
R, C = 230, 300
nodes, labels = '', ''
for i, s in enumerate(S):
    a = math.radians(-90 + i*60); x, y = C + R*math.cos(a), C + R*math.sin(a)
    lx, ly = C + (R+44)*math.cos(a), C + (R+44)*math.sin(a)
    anc = 'middle' if abs(math.cos(a)) < .2 else ('start' if math.cos(a) > 0 else 'end')
    nodes += f'<circle class="lp-n" data-i="{i}" cx="{x:.1f}" cy="{y:.1f}" r="7"/>'
    labels += f'<text class="lp-t" data-i="{i}" x="{lx:.1f}" y="{ly+5:.1f}" text-anchor="{anc}">{s[0]}</text>'
B = (f'<div class="lp"><div class="lp-ring"><svg viewBox="0 0 600 600" aria-hidden="true"><circle class="lp-base" cx="{C}" cy="{C}" r="{R}"/>'
     f'<circle class="lp-arc" cx="{C}" cy="{C}" r="{R}" transform="rotate(-90 {C} {C})"/>{nodes}<circle class="lp-dot" r="5"/><circle class="lp-halo" r="16"/>{labels}</svg>'
     '<div class="lp-c" aria-live="polite">' + ''.join(f'<div class="lp-s{" on" if i==0 else ""}"><span class="n">{n(i)} / 06</span><h3>{s[0]}</h3><p>{s[1]}</p></div>' for i,s in enumerate(S)) + '</div></div></div>')
# C — Sweep
C_ = ('<div class="sw"><p class="sw-w">' + ''.join(f'<span class="wg"><button type="button" class="w" data-i="{i}">{s[0]}</button><span class="sep">{"," if i<5 else "."}</span></span> ' for i,s in enumerate(S))
      + '</p><div class="sw-cap" aria-live="polite">' + ''.join(f'<p class="sw-s{" on" if i==0 else ""}"><span class="n">{n(i)} / 06</span>{s[1]}</p>' for i,s in enumerate(S)) + '</div></div>')
t = pathlib.Path('design/process/process.tpl.html').read_text()
t = t.replace('{{HEAD}}', head).replace('{{A}}', A).replace('{{B}}', B).replace('{{C}}', C_)
for k, p in {'F4':'instrument-sans-latin-400-normal','F5':'instrument-sans-latin-500-normal','F6':'instrument-sans-latin-600-normal','FM':'jetbrains-mono-latin-500-normal'}.items():
    t = t.replace('{{'+k+'}}', b(f'public/fonts/{p}.woff2','font/woff2'))
pathlib.Path(sys.argv[1]).write_text(t); print(len(t)//1024,'KB')
