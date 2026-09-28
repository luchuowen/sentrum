// Screenshot a local HTML file at desktop + mobile. Usage: node scripts/shoot.mjs design/design-1.html [outdir]
import { chromium } from 'playwright';
import path from 'node:path';
import http from 'node:http';
import fs from 'node:fs';
const file = process.argv[2]; const out = process.argv[3] || 'design/screenshots';
const name = path.basename(file, '.html');
const dir = path.dirname(path.resolve(file));
const types = { '.html': 'text/html', '.css': 'text/css', '.js': 'text/javascript', '.svg': 'image/svg+xml', '.woff2': 'font/woff2', '.png': 'image/png', '.jpg': 'image/jpeg', '.webp': 'image/webp', '.avif': 'image/avif' };
const srv = http.createServer((q, r) => { const f = path.join(dir, decodeURIComponent(q.url.split('?')[0])); fs.readFile(f, (e, d) => { if (e) { r.writeHead(404); r.end(); return; } r.writeHead(200, { 'content-type': types[path.extname(f)] || 'application/octet-stream' }); r.end(d); }); }).listen(0);
const url = `http://127.0.0.1:${srv.address().port}/${path.basename(file)}`;
const b = await chromium.launch();
const errors = [];
for (const [tag, vp] of [['desktop', { width: 1440, height: 900 }], ['mobile', { width: 390, height: 844, isMobile: true, deviceScaleFactor: 2 }]]) {
  const ctx = await b.newContext({ viewport: { width: vp.width, height: vp.height }, deviceScaleFactor: vp.deviceScaleFactor || 1, isMobile: !!vp.isMobile });
  const p = await ctx.newPage();
  p.on('console', m => m.type() === 'error' && errors.push(`${tag}: ${m.text()}`));
  p.on('pageerror', e => errors.push(`${tag}: ${e.message}`));
  await p.goto(url, { waitUntil: 'networkidle' });
  await p.evaluate(() => document.fonts.ready);
  await p.screenshot({ path: `${out}/${name}-${tag}-fold.jpg`, quality: 82 });
  await p.screenshot({ path: `${out}/${name}-${tag}-full.jpg`, quality: 78, fullPage: true });
  const ov = await p.evaluate(() => document.documentElement.scrollWidth - window.innerWidth);
  if (ov > 0) errors.push(`${tag}: horizontal overflow ${ov}px`);
  await ctx.close();
}
await b.close(); srv.close();
console.log(errors.length ? 'ISSUES:\n' + errors.join('\n') : `${name}: ok`);
