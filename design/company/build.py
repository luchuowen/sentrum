# Three directions for the home "The company / Technologies we work with" section.
import base64, pathlib, sys
b = lambda p, m: f'data:{m};base64,' + base64.b64encode(pathlib.Path(p).read_bytes()).decode()
BR = ['Cisco','HPE','Dell','Check Point','Ubiquiti','D-Link','Siemon','Black Box','iDirect','Yeastar','Yealink','Planar','Samsung','Epson','Bose','Yamaha','Behringer','ZKTeco','Optex','Hikvision','Dahua','Delta','Tripp Lite','Havells','Crabtree','Giganet']
G = [('Networks',['Cisco','HPE','Ubiquiti','D-Link','Siemon','Black Box','Giganet']),('Satellite',['iDirect']),('Security',['Check Point','Hikvision','Dahua','ZKTeco','Optex']),
     ('Comms & AV',['Yeastar','Yealink','Planar','Samsung','Epson','Bose','Yamaha','Behringer']),('Power & data centre',['Dell','Delta','Tripp Lite','Havells','Crabtree'])]
assert sorted(sum((g[1] for g in G),[])) == sorted(BR)
amp = lambda s: s.replace('&','&amp;')
name = '<h2>Sentrum Communication &amp; Technologies Ltd</h2>'
line = '<p class="lede">A Nairobi-based systems integrator, working across Kenya and Africa.</p>'
more = '<a class="more" href="#">About the company <span aria-hidden="true">→</span></a>'
tender = '<div class="tender"><p><b>Preparing a tender?</b> Ask for our company profile and registration documents.</p><a class="cta" href="#">Request company profile <span aria-hidden="true">→</span></a></div>'
note = '<p class="note">Brand names are trademarks of their owners.</p>'
# A — Coordinates
row = lambda items: ''.join(f'<span>{amp(x)}</span><i aria-hidden="true">/</i>' for x in items)
half = len(BR)//2
A = (f'<div class="ca"><div class="ca-l"><p class="k">The company</p>{name}{line}<dl class="facts"><div><dt>Head office</dt><dd>Wilson Airport, Block 34</dd></div><div><dt>Services</dt><dd>14, one contract</dd></div><div><dt>Team experience</dt><dd>15+ years</dd></div></dl>{more}</div>'
     '<figure class="radar" aria-label="Head office position: 1.3204° S, 36.8127° E, Wilson Airport, Nairobi"><div class="scope"><span class="sweep"></span><span class="ring r1"></span><span class="ring r2"></span><span class="ring r3"></span><span class="cross"></span><span class="blip"></span></div>'
     '<figcaption><span class="mono">1.3204° S · 36.8127° E</span><span>Wilson Airport, Nairobi</span></figcaption></figure></div>'
     '<div class="mq-h"><p class="k">Technologies we work with</p>' + note + '</div>'
     f'<div class="mq" aria-label="Technologies we work with: {", ".join(BR)}"><div class="mq-r"><div class="mq-t">{row(BR[:half])*2}</div></div><div class="mq-r rev"><div class="mq-t">{row(BR[half:])*2}</div></div></div>{tender}')
# B — Datasheet
B = (f'<div class="cb"><div class="cb-top"><div><p class="k">The company</p>{name}{line}</div>{more}</div>'
     '<dl class="spec"><div><dt>Head office</dt><dd>Wilson Airport, Block 34, Nairobi</dd></div><div><dt>Services</dt><dd>14, under one contract</dd></div><div><dt>Team experience</dt><dd>Over 15 years</dd></div><div><dt>Position</dt><dd class="mono">1.3204° S · 36.8127° E</dd></div></dl>'
     '<div class="tbl"><div class="tbl-h"><span>Technologies we work with</span><span>By system</span></div>'
     + ''.join(f'<div class="tr" style="--d:{i*.12:.2f}s"><span class="sys"><span class="n">0{i+1}</span>{amp(g)}</span><span class="brs">' + ''.join(f'<span style="--j:{j}">{amp(x)}</span>' for j,x in enumerate(br)) + f'</span><span class="ct">{len(br):02d}</span></div>' for i,(g,br) in enumerate(G))
     + f'</div><div class="cb-foot">{note}{tender}</div></div>')
# C — Patch panel
C = (f'<div class="cc"><div class="cc-l"><p class="k">The company</p>{name}{line}<dl class="mini"><div><dt>Head office</dt><dd>Wilson Airport, Block 34, Nairobi</dd></div><div><dt>Services</dt><dd>14, under one contract</dd></div><div><dt>Team experience</dt><dd>Over 15 years</dd></div><div><dt>Position</dt><dd class="mono">1.3204° S · 36.8127° E</dd></div></dl>{more}</div>'
     '<div class="panel"><div class="pn-h"><span>Technologies we work with</span><span>26 ports</span></div><ul class="ports">'
     + ''.join(f'<li><span class="jack" aria-hidden="true"><i></i></span><span class="pn">{amp(x)}</span><span class="pnum" aria-hidden="true">{i+1:02d}</span></li>' for i,x in enumerate(BR))
     + f'</ul><span class="screw s1"></span><span class="screw s2"></span><span class="screw s3"></span><span class="screw s4"></span></div></div><div class="cc-foot">{note}{tender}</div>')
t = pathlib.Path('design/company/company.tpl.html').read_text().replace('{{A}}',A).replace('{{B}}',B).replace('{{C}}',C)
for k, p in {'F4':'instrument-sans-latin-400-normal','F5':'instrument-sans-latin-500-normal','F6':'instrument-sans-latin-600-normal','FM':'jetbrains-mono-latin-500-normal'}.items():
    t = t.replace('{{'+k+'}}', b(f'public/fonts/{p}.woff2','font/woff2'))
pathlib.Path(sys.argv[1]).write_text(t); print(len(t)//1024,'KB')
