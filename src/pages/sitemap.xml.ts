import { areas, areaUrl, serviceUrl } from '../data/services';
import { SITE_URL } from '../data/site';
export function GET() {
  const paths = ['/', '/solutions/', ...areas.map(areaUrl), ...areas.flatMap((a) => a.services.map((s) => serviceUrl(a, s))),
    '/remote-and-satellite/', '/how-we-work/', '/company/', '/contact/', '/support/', '/privacy/'];
  const body = `<?xml version="1.0" encoding="UTF-8"?>\n<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">\n${paths.map((p) => `  <url><loc>${SITE_URL}${p}</loc></url>`).join('\n')}\n</urlset>\n`;
  return new Response(body, { headers: { 'Content-Type': 'application/xml' } });
}
