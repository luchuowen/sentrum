// axe-core WCAG 2.2 AA scan of every built page. Usage: AXE=/path/axe.min.js node scripts/axe.mjs
import { chromium } from 'playwright'; import http from 'node:http'; import fs from 'node:fs'; import path from 'node:path';
const axe = fs.readFileSync(process.env.AXE, 'utf8');
const srv = http.createServer((q, r) => { let f = path.join('dist', q.url.split('?')[0]); if (f.endsWith('/')) f += 'index.html'; fs.readFile(f, (e, d) => { if (e) { r.writeHead(404); return r.end(); } r.writeHead(200, { 'content-type': { '.svg': 'image/svg+xml', '.woff2': 'font/woff2', '.html': 'text/html', '.jpg': 'image/jpeg' }[path.extname(f)] || '' }); r.end(d); }); }).listen(0);
const pages = [...fs.readFileSync('dist/sitemap.xml', 'utf8').matchAll(/<loc>https:\/\/[^/]+([^<]*)<\/loc>/g)].map((m) => m[1]).concat('/404.html');
const b = await chromium.launch(); const out = {};
for (const w of [1440, 390]) { const pg = await b.newPage({ viewport: { width: w, height: 900 }, reducedMotion: 'reduce' });
  for (const p of pages) { await pg.goto(`http://127.0.0.1:${srv.address().port}${p}`, { waitUntil: 'networkidle' }); await pg.addScriptTag({ content: axe });
    const r = await pg.evaluate(async () => (await axe.run(document, { runOnly: ['wcag2a', 'wcag2aa', 'wcag21aa', 'wcag22aa', 'best-practice'] })).violations.map((v) => `${v.id} (${v.impact}) ×${v.nodes.length}: ${v.nodes.slice(0, 2).map((n) => n.target.join(' ')).join(' | ')}`));
    r.forEach((x) => { (out[x.split(' ')[0]] ||= new Set()).add(`${w} ${p}: ${x}`); }); }
  await pg.close(); }
await b.close(); srv.close();
const keys = Object.keys(out); console.log(keys.length ? keys.map((k) => [...out[k]].slice(0, 4).join('\n')).join('\n') : 'axe: 0 violations');
