# Multi-page preview of the built site for the Artifact tool: every page as a flat .html file, assets copied, internal links rewritten.
import pathlib, re, shutil, sys
d = pathlib.Path('dist'); out = pathlib.Path(sys.argv[1]); shutil.rmtree(out, ignore_errors=True); out.mkdir(parents=True)
pages = sorted(p for p in d.rglob('index.html')) + [d / '404.html']
def flat(path):  # '/solutions/networks/' -> 'solutions-networks.html', '/' -> 'home.html'
    path = path.split('#')[0].strip('/'); return (path.replace('/', '-') or 'home') + '.html'
names = {}
for p in pages:
    rel = '/' + str(p.parent.relative_to(d)).replace('.', '') + '/' if p.name == 'index.html' else '/404/'
    rel = re.sub(r'/+', '/', rel); names[rel] = flat(rel)
def fix(h):
    h = re.sub(r'(src|href|content)="/((?:img|fonts|brand|brands)/[^"]+)"', r'\1="\2"', h)
    h = re.sub(r'url\(/((?:img|fonts|brand|brands)/[^)]+)\)', r'url(\1)', h)
    def link(m):
        u = m.group(1); hash_ = '#' + u.split('#')[1] if '#' in u else ''
        base = u.split('#')[0].split('?')[0]
        return f'href="{names[base]}{hash_}"' if base in names else m.group(0)
    h = re.sub(r'href="(/[^"]*)"', link, h)
    return h
for p, (rel, n) in zip(pages, names.items()):
    (out / n).write_text(fix(p.read_text()))
for sub in ['img', 'fonts', 'brand', 'brands']:
    if (d / sub).exists(): shutil.copytree(d / sub, out / sub)
nice = {'home.html': 'Home (unchanged)', 'solutions.html': 'Solutions', 'how-we-work.html': 'How we work', 'remote-and-satellite.html': 'Remote & satellite', 'company.html': 'Company', 'support.html': 'Support', 'contact.html': 'Contact', 'privacy.html': 'Privacy', '404.html': '404'}
rows = ''.join(f'<li><a href="{n}">{nice.get(n, n[:-5].replace("solutions-", "").replace("-", " ").title())}</a><span>{n}</span></li>' for n in sorted(names.values(), key=lambda x: (x not in nice, list(nice).index(x) if x in nice else 0, x)))
(out / 'index.html').write_text(f'''<title>Sentrum Site Preview</title>
<style>:root{{--bg:#0B1620;--fg:#fff;--mu:#8FA6B6;--ln:#22394B;--ac:#29A9E1;color-scheme:dark}}body{{background:var(--bg);color:var(--fg);font:16px/1.5 system-ui,sans-serif;margin:0}}
main{{max-width:760px;margin:0 auto;padding:40px 16px}}h1{{font-size:32px;letter-spacing:-.02em;margin:0}}p{{color:var(--mu)}}ul{{list-style:none;padding:0;border-top:1px solid var(--ln)}}
li{{display:flex;justify-content:space-between;gap:12px;border-bottom:1px solid var(--ln)}}a{{color:#fff;text-decoration:none;padding:12px 0;flex:1}}a:hover{{color:var(--ac)}}span{{color:var(--mu);font:12px ui-monospace,monospace;padding-top:16px}}</style>
<main><h1>Sentrum — site preview</h1><p>Every page of the redesigned site. Links inside the pages work too.</p><ul>{rows}</ul></main>''')
print(len(names), 'pages')
