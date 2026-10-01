# Three directions for the home "What we deliver" section -> one self-contained artifact fragment.
import base64, pathlib, sys
b = lambda p, m: f'data:{m};base64,' + base64.b64encode(pathlib.Path(p).read_bytes()).decode()
S = [
 ('networks','Networks & Connectivity','Networks','Cabling, WiFi and satellite links','The connections every phone, laptop and camera depends on — and a satellite link where fibre stops.',['Structured cabling & fibre','WiFi','VSAT & satellite'],'cap-networks'),
 ('security','Security Systems','Security','Doors, perimeters and the network edge','Who can open which door, sensors that notice intruders, and firewalls that keep hackers out.',['Access control','Intrusion detection','Cyber security'],'cap-security'),
 ('communications-av','Communications & AV','Comms & AV','Rooms where people meet and decide','Phones, video calls, video walls and sound — chosen for each room and set up to simply work.',['Unified communications','Video walls','Audio-visual systems'],'cap-av'),
 ('power-data-centre','Power & Data Centre','Power & DC','Servers, kept running','The computers that hold your data, and backup power that keeps them on through outages.',['Servers','Power, UPS & electrical'],'cap-power'),
 ('supply-fabrication-support','Supply, Fabrication & Support','Fabrication','Our own steel, and support after go-live','Masts, mounts and racks made on our floor. Equipment supplied. Support after go-live.',['Metal fabrication','IT equipment supply','Technical support'],'cap-fabrication'),
]
img = {s[6]: b(f'public/img/{s[6]}.jpg','image/jpeg') for s in S}
imgcss = '\n'.join(f'.im-{k}{{background-image:url({v})}}' for k, v in img.items())
chips = lambda s: ''.join(f'<li>{x}</li>' for x in s[5])
head = lambda: '<header class="hd"><div><p class="k">What we deliver</p><h2>Five systems, and one team accountable for all of them.</h2></div><a class="more" href="#">All 14 services <span aria-hidden="true">→</span></a></header>'
# A: index rows
A = '<ol class="ix">' + ''.join(f'<li><a href="#" class="ix-r"><span class="n">0{i+1}</span><span class="ix-t"><b>{s[1]}</b><em>{s[3]}</em></span><span class="ix-d">{s[4]}</span><ul class="ch">{chips(s)}</ul><span class="ix-p im-{s[6]}" role="img" aria-label=""></span><span class="ar" aria-hidden="true">→</span></a></li>' for i, s in enumerate(S)) + '</ol>'
# B: split tabs
tabs = ''.join(f'<button role="tab" id="bt{i}" aria-controls="bp{i}" aria-selected="{"true" if i==0 else "false"}" tabindex="{0 if i==0 else -1}"><span class="n">0{i+1}</span>{s[1]}</button>' for i, s in enumerate(S))
panes = ''.join(f'<div role="tabpanel" id="bp{i}" aria-labelledby="bt{i}" class="sp{" on" if i==0 else ""}"><div class="sp-i im-{s[6]}" role="img" aria-label="{s[1]}"></div><div class="sp-c"><p class="tg">{s[1]}</p><h3>{s[3]}</h3><p>{s[4]}</p><ul class="ch">{chips(s)}</ul><a class="cta" href="#">Explore {s[2].lower() if s[2]!="Comms & AV" else "communications & AV"} →</a></div></div>' for i, s in enumerate(S))
B = f'<div class="sp-w"><div class="sp-l" role="tablist" aria-label="Five systems">{tabs}</div><div class="sp-r">{panes}</div></div>'
# C: arch columns
C = '<ul class="ac">' + ''.join(f'<li><a href="#" class="ac-c"><span class="ac-i im-{s[6]}" role="img" aria-label=""><i>0{i+1}</i></span><b>{s[1]}</b><span>{s[4]}</span><span class="ac-m">{" · ".join(s[5])}</span></a></li>' for i, s in enumerate(S)) + '</ul>'
t = pathlib.Path('design/sections/sections.tpl.html').read_text()
t = t.replace('{{IMGCSS}}', imgcss).replace('{{HEAD}}', head()).replace('{{A}}', A).replace('{{B}}', B).replace('{{C}}', C)
for k, p in {'F4':'instrument-sans-latin-400-normal','F5':'instrument-sans-latin-500-normal','F6':'instrument-sans-latin-600-normal','FM':'jetbrains-mono-latin-500-normal'}.items():
    t = t.replace('{{'+k+'}}', b(f'public/fonts/{p}.woff2','font/woff2'))
pathlib.Path(sys.argv[1]).write_text(t); print(len(t)//1024,'KB')
