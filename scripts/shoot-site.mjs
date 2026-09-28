// Screenshot built pages (dist/) at 1440 + 390. Usage: node scripts/shoot-site.mjs [path ...]  (default: all)
import { chromium } from 'playwright';
import http from 'node:http'; import fs from 'node:fs'; import path from 'node:path';
const root = path.resolve('dist'); const out = 'screenshots'; fs.mkdirSync(out, { recursive: true });
const types = { '.html': 'text/html', '.css': 'text/css', '.js': 'text/javascript', '.svg': 'image/svg+xml', '.woff2': 'font/woff2', '.png': 'image/png', '.jpg': 'image/jpeg', '.xml': 'application/xml', '.txt': 'text/plain' };
const srv = http.createServer((q, r) => { let f = path.join(root, decodeURIComponent(q.url.split('?')[0].split('#')[0])); if (f.endsWith('/')) f += 'index.html';
  fs.readFile(f, (e, d) => { if (e) { r.writeHead(404, { 'content-type': 'text/html' }); r.end(fs.readFileSync(path.join(root, '404.html'))); return; } r.writeHead(200, { 'content-type': types[path.extname(f)] || 'application/octet-stream' }); r.end(d); }); }).listen(0);
const base = `http://127.0.0.1:${srv.address().port}`;
let pages = process.argv.slice(2);
if (!pages.length) pages = [...fs.readFileSync('dist/sitemap.xml', 'utf8').matchAll(/<loc>https:\/\/[^/]+([^<]*)<\/loc>/g)].map((m) => m[1]).concat('/404.html');
const b = await chromium.launch(); const issues = [];
for (const p of pages) {
  const name = p === '/' ? 'home' : p.replace(/^\/|\/$/g, '').replace(/\//g, '_').replace('.html', '');
  for (const [tag, vp] of [['d', { width: 1440, height: 900 }], ['m', { width: 390, height: 844, isMobile: true, deviceScaleFactor: 2 }]]) {
    const ctx = await b.newContext({ viewport: { width: vp.width, height: vp.height }, deviceScaleFactor: vp.deviceScaleFactor || 1, isMobile: !!vp.isMobile, reducedMotion: 'reduce' });
    const pg = await ctx.newPage();
    pg.on('console', (m) => m.type() === 'error' && issues.push(`${name} ${tag}: ${m.text()}`));
    pg.on('pageerror', (e) => issues.push(`${name} ${tag}: ${e.message}`));
    pg.on('response', (r) => r.status() >= 400 && !r.url().endsWith('404.html') && p !== '/404.html' && issues.push(`${name} ${tag}: ${r.status()} ${r.url()}`));
    await pg.goto(base + p, { waitUntil: 'networkidle' }); await pg.evaluate(() => document.fonts.ready);
    await pg.evaluate(async () => { for (let y = 0; y < document.body.scrollHeight; y += 700) { scrollTo(0, y); await new Promise((r) => setTimeout(r, 30)); } scrollTo(0, 0); });
    await pg.waitForTimeout(150);
    await pg.screenshot({ path: `${out}/${name}-${tag}.jpg`, quality: 70, fullPage: true });
    const ov = await pg.evaluate(() => document.documentElement.scrollWidth - innerWidth); if (ov > 0) issues.push(`${name} ${tag}: overflow ${ov}px`);
    await ctx.close();
  }
}
await b.close(); srv.close();
console.log(issues.length ? 'ISSUES:\n' + [...new Set(issues)].join('\n') : `${pages.length} pages ok`);
