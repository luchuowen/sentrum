// Capture a pinned/scroll-driven section at several progress points. Usage: node scripts/shoot-pin.mjs design/design-5.html '#stage' [fractions]
import { chromium } from 'playwright';
import path from 'node:path'; import http from 'node:http'; import fs from 'node:fs';
const [file, sel, fr = '0.02,0.3,0.6,0.95'] = process.argv.slice(2);
const dir = path.dirname(path.resolve(file)); const name = path.basename(file, '.html');
const types = { '.html': 'text/html', '.svg': 'image/svg+xml', '.woff2': 'font/woff2', '.jpg': 'image/jpeg', '.png': 'image/png' };
const srv = http.createServer((q, r) => { const f = path.join(dir, decodeURIComponent(q.url.split('?')[0])); fs.readFile(f, (e, d) => { if (e) { r.writeHead(404); r.end(); return; } r.writeHead(200, { 'content-type': types[path.extname(f)] || 'application/octet-stream' }); r.end(d); }); }).listen(0);
const b = await chromium.launch();
for (const [tag, w, h] of [['desktop', 1440, 900], ['mobile', 390, 844]]) {
  const p = await b.newPage({ viewport: { width: w, height: h }, isMobile: tag === 'mobile' });
  await p.goto(`http://127.0.0.1:${srv.address().port}/${path.basename(file)}`, { waitUntil: 'networkidle' });
  for (const f of fr.split(',').map(Number)) {
    await p.evaluate(([s, f]) => { const el = document.querySelector(s); const span = el.offsetHeight - innerHeight; scrollTo(0, el.offsetTop + span * f); }, [sel, f]);
    await p.waitForTimeout(700);
    await p.screenshot({ path: `design/screenshots/${name}-${tag}-pin${Math.round(f * 100)}.jpg`, quality: 80 });
  }
  await p.close();
}
await b.close(); srv.close(); console.log('pin shots ok');
