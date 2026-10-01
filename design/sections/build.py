# Three premium directions for the home "What we deliver" section -> one self-contained artifact fragment.
import base64, pathlib, sys
b = lambda p, m: f'data:{m};base64,' + base64.b64encode(pathlib.Path(p).read_bytes()).decode()
G = {  # 48x48 line glyphs, stroke = currentColor
 'net': '<path d="M8 20a22 22 0 0 1 32 0M14 26a13.5 13.5 0 0 1 20 0M20 32a5.5 5.5 0 0 1 8 0"/><circle cx="24" cy="38" r="1.6" fill="currentColor" stroke="none"/>',
 'sec': '<path d="M24 6l14 5v11c0 9-6 16-14 20-8-4-14-11-14-20V11z"/><circle cx="24" cy="21" r="3.2"/><path d="M24 24.2V30"/>',
 'av':  '<rect x="6" y="9" width="36" height="23" rx="2"/><path d="M24 32v7M16 39h16M13 21h5l3-5 4 10 3-5h7"/>',
 'pwr': '<rect x="12" y="6" width="24" height="36" rx="2"/><path d="M12 18h24M12 30h24"/><circle cx="17.5" cy="12" r="1.2" fill="currentColor" stroke="none"/><circle cx="17.5" cy="24" r="1.2" fill="currentColor" stroke="none"/><circle cx="17.5" cy="36" r="1.2" fill="currentColor" stroke="none"/><path d="M24 12h7M24 24h7M24 36h7"/>',
 'sup': '<path d="M24 14v28M16 42l8-28 8 28M18.5 33h11M20.6 25h6.8"/><path d="M18 9a8.5 8.5 0 0 1 12 0M14.5 5.5a13.5 13.5 0 0 1 19 0"/>',
}
S = [('Networks &amp; Connectivity','Cabling, fibre, WiFi and VSAT.','cap-networks','net','Structured cabling · WiFi · VSAT'),
     ('Security Systems','Access control, intrusion and cyber.','cap-security','sec','Access control · Intrusion · Cyber'),
     ('Communications &amp; AV','Unified comms, video walls and AV.','cap-av','av','Unified comms · Video walls · AV'),
     ('Power &amp; Data Centre','Servers, UPS and electrical.','cap-power','pwr','Servers · UPS · Electrical'),
     ('Supply, Fabrication &amp; Support','Equipment, masts and aftercare.','cap-fabrication','sup','IT supply · Fabrication · Support')]
svg = lambda k: f'<svg viewBox="0 0 48 48" aria-hidden="true">{G[k]}</svg>'
imgcss = '\n'.join(f'.im-{s[2]}{{background-image:url({b("public/img/"+s[2]+".jpg","image/jpeg")})}}' for s in S)
n = lambda i: f'0{i+1}'
head = '<header class="hd"><div><p class="k">What we deliver</p><h2>Five systems. <span>One accountable team.</span></h2></div><a class="more" href="#">All 14 services <span aria-hidden="true">→</span></a></header>'
A = ('<div class="co"><div class="co-bg" aria-hidden="true">' + ''.join(f'<span class="im-{s[2]}{" on" if i==0 else ""}"></span>' for i,s in enumerate(S)) + '</div>'
     + ''.join(f'<a href="#" class="co-c{" on" if i==0 else ""}" data-i="{i}"><span class="co-m im-{s[2]}" aria-hidden="true"></span><span class="n">{n(i)}</span><span class="co-b"><b>{s[0]}</b><em>{s[1]}</em></span><i aria-hidden="true">→</i></a>' for i,s in enumerate(S)) + '</div>')
B = ('<div class="st"><div class="st-media" aria-hidden="true">' + ''.join(f'<span class="st-l im-{s[2]}{" on" if i==0 else ""}" style="z-index:{1 if i==0 else 0}"></span>' for i,s in enumerate(S))
     + '<div class="st-cap"><span class="st-ct"><b>01</b> / 05</span><span class="st-sv">' + S[0][4] + '</span></div></div><ol class="st-list">'
     + ''.join(f'<li data-i="{i}" data-sv="{s[4]}"{" class=on" if i==0 else ""}><span class="st-mi im-{s[2]}" aria-hidden="true"></span><span class="n">{n(i)}</span><h3><a href="#">{s[0]}</a></h3><p>{s[1]}</p></li>' for i,s in enumerate(S)) + '</ol></div>')
C = '<ul class="gl">' + ''.join(f'<li><a href="#"><span class="gl-ph im-{s[2]}" aria-hidden="true"></span><span class="gl-top"><span class="n">{n(i)}</span><i aria-hidden="true">→</i></span>{svg(s[3])}<span class="gl-b"><b>{s[0]}</b><em>{s[1]}</em></span></a></li>' for i,s in enumerate(S)) + '</ul>'
t = pathlib.Path('design/sections/sections.tpl.html').read_text()
t = t.replace('{{IMGCSS}}', imgcss).replace('{{HEAD}}', head).replace('{{A}}', A).replace('{{B}}', B).replace('{{C}}', C)
for k, p in {'F4':'instrument-sans-latin-400-normal','F5':'instrument-sans-latin-500-normal','F6':'instrument-sans-latin-600-normal','FM':'jetbrains-mono-latin-500-normal'}.items():
    t = t.replace('{{'+k+'}}', b(f'public/fonts/{p}.woff2','font/woff2'))
pathlib.Path(sys.argv[1]).write_text(t); print(len(t)//1024,'KB')
