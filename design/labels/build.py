# Three label treatments for the line-art scenes -> one artifact fragment.
import re, pathlib, base64, sys
html = pathlib.Path('dist/solutions/networks/index.html').read_text()
css = '\n'.join(re.findall(r'<style[^>]*>(.*?)</style>', html, re.S))
for f in re.findall(r'url\((/fonts/[^)]+)\)', css):
    css = css.replace(f'url({f})', 'url(data:font/woff2;base64,' + base64.b64encode(pathlib.Path('public' + f).read_bytes()).decode() + ')')
svg = re.search(r'<svg class="lb".*?</svg>', html, re.S).group(0)
svg = re.sub(r'<g class="notes".*?</g>\s*</g>\s*(?=</svg>)', '', svg, flags=re.S)  # drop baked notes
svg = re.sub(r'<g class="notes".*</svg>', '</svg>', svg, flags=re.S)
crop = [float(v) for v in re.search(r'viewBox="([^"]+)"', svg).group(1).split()]
cx, cy, cw, ch = crop; k = cw / 480
notes = [(333,300,40,-64,'Riser','Backbone between floors'),(500,318,120,40,'WiFi','Access points in the ceiling'),(120,566,30,-60,'Fibre entry','Where the provider comes in'),(600,152,-140,-50,'VSAT','Satellite where fibre ends')]
P = lambda x, y: (f'{(x-cx)/cw*100:.2f}%', f'{(y-cy)/ch*100:.2f}%')
def dots(num=False):
    o = ''
    for i, (x, y, *_r) in enumerate(notes):
        l, t = P(x, y); o += f'<span class="lx-pt" style="left:{l};top:{t};--i:{i}">' + (f'<b>{i+1:02d}</b>' if num else '') + '</span>'
    return o
def leaders():
    o = f'<svg class="lx-ld" viewBox="{cx} {cy} {cw} {ch}" preserveAspectRatio="xMidYMid meet" aria-hidden="true">'
    for i, (x, y, dx, dy, *_r) in enumerate(notes):
        ex, ey = x + dx*k, y + dy*k; tk = 18*k*(1 if dx > 0 else -1)
        o += f'<path style="--i:{i}" d="M{x} {y}L{ex} {ey}" pathLength="1"/>'
    return o + '</svg>'
def chips():
    o = ''
    for i, (x, y, dx, dy, t, d) in enumerate(notes):
        ex, ey = x + dx*k, y + dy*k; l, tp = P(ex, ey)
        o += f'<div class="lx-chip {"r" if dx > 0 else "lft"}" style="left:{l};top:{tp};--i:{i}"><b>{t}</b><span>{d}</span></div>'
    return o
A = f'<div class="lx-fig fA">{svg}{leaders()}{dots()}{chips()}</div>'
B = f'<div class="lx-fig fB">{svg}{dots(True)}</div><ol class="lx-legend">' + ''.join(f'<li><b>{i+1:02d}</b><span><strong>{t}</strong>{d}</span></li>' for i, (*_x, t, d) in enumerate(notes)) + '</ol>'
C = f'<div class="lx-fig fC">{svg}{dots()}<div class="lx-cap" aria-live="polite"><b></b><span></span><i></i></div></div>'
import json
t = pathlib.Path('design/labels/labels.tpl.html').read_text()
t = t.replace('{{CSS}}', css).replace('{{A}}', A).replace('{{B}}', B).replace('{{C}}', C).replace('{{NOTES}}', json.dumps([[P(x,y), tt, d] for x, y, dx, dy, tt, d in notes]))
pathlib.Path(sys.argv[1]).write_text(t); print(len(t)//1024, 'KB')
