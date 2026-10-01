# Three clean directions for the home "What we deliver" section -> one self-contained artifact fragment.
import base64, pathlib, sys
b = lambda p, m: f'data:{m};base64,' + base64.b64encode(pathlib.Path(p).read_bytes()).decode()
S = [('Networks','Cabling, WiFi and satellite','cap-networks'),('Security','Access control, intrusion and cyber','cap-security'),
     ('Comms & AV','Calls, meetings and displays','cap-av'),('Power & DC','Servers and backup power','cap-power'),('Fabrication','Steel, supply and support','cap-fabrication')]
imgcss = '\n'.join(f'.im-{s[2]}{{background-image:url({b("public/img/"+s[2]+".jpg","image/jpeg")})}}' for s in S)
head = '<header class="hd"><div><p class="k">What we deliver</p><h2>Five systems, and one team accountable for all of them.</h2></div><a class="more" href="#">All 14 services <span aria-hidden="true">→</span></a></header>'
A = '<ul class="tl">' + ''.join(f'<li><a href="#" class="tl-c"><span class="tl-i im-{s[2]}"></span><span class="tl-t"><b>{s[0]}</b><i aria-hidden="true">→</i></span></a></li>' for s in S) + '</ul>'
B = '<div class="hl"><ul>' + ''.join(f'<li><a href="#" data-im="im-{s[2]}"><span class="n">0{i+1}</span><b>{s[0]}</b><em>{s[1]}</em><i aria-hidden="true">→</i></a></li>' for i, s in enumerate(S)) + '</ul><div class="hl-p" aria-hidden="true"></div></div>'
C = '<ul class="bd">' + ''.join(f'<li><a href="#" class="bd-r im-{s[2]}"><span class="n">0{i+1}</span><b>{s[0]}</b><em>{s[1]}</em><i aria-hidden="true">→</i></a></li>' for i, s in enumerate(S)) + '</ul>'
t = pathlib.Path('design/sections/sections.tpl.html').read_text()
t = t.replace('{{IMGCSS}}', imgcss).replace('{{HEAD}}', head).replace('{{A}}', A).replace('{{B}}', B).replace('{{C}}', C)
for k, p in {'F4':'instrument-sans-latin-400-normal','F5':'instrument-sans-latin-500-normal','F6':'instrument-sans-latin-600-normal','FM':'jetbrains-mono-latin-500-normal'}.items():
    t = t.replace('{{'+k+'}}', b(f'public/fonts/{p}.woff2','font/woff2'))
pathlib.Path(sys.argv[1]).write_text(t); print(len(t)//1024,'KB')
