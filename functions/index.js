// POST /api/enquiry → Firestore `enquiries` + `mail` (Trigger Email extension). Region europe-west4 (never europe-west2).
import { onRequest } from 'firebase-functions/v2/https';
import { createHash } from 'node:crypto';
import { initializeApp } from 'firebase-admin/app';
import { getFirestore, FieldValue } from 'firebase-admin/firestore';

initializeApp();
const db = getFirestore();
const TO = process.env.ENQUIRY_TO || 'info@sentrumcoms.net';
const LIMITS = { name: 120, organisation: 160, email: 160, phone: 40, location: 160, topic: 60, message: 4000 };
const MULTI = new Set(['message']);
const clean = (v, n, multi = false) => String(v ?? '').replace(multi ? /[\u0000-\u0008\u000B\u000C\u000E-\u001F]/g : /[\u0000-\u001F\u007F]+/g, multi ? '' : ' ').trim().slice(0, n);
const TOPICS = new Set(['not-sure', 'profile', 'support', 'structured-cabling', 'wifi', 'vsat', 'access-control', 'intrusion-detection', 'cyber-security',
  'unified-communications', 'video-walls', 'audio-visual', 'servers', 'power-ups', 'fabrication', 'it-equipment', 'technical-support']);
const MIN_FILL_MS = 3000, WINDOW_MS = 60 * 60 * 1000, MAX_PER_WINDOW = 5;
// Per-IP limit: at most MAX_PER_WINDOW enquiries per hour. The IP is stored only as a salted hash.
async function allowed(ip) {
  const id = createHash('sha256').update(`sentrum:${ip}`).digest('hex').slice(0, 32);
  const ref = db.collection('ratelimits').doc(id);
  return db.runTransaction(async (tx) => {
    const now = Date.now(); const doc = await tx.get(ref); const d = doc.exists ? doc.data() : null;
    const fresh = !d || now - d.start > WINDOW_MS;
    const count = fresh ? 1 : d.count + 1;
    if (count > MAX_PER_WINDOW) return false;
    tx.set(ref, { start: fresh ? now : d.start, count, expireAt: new Date(now + WINDOW_MS) });
    return true;
  });
}
const esc = (s) => s.replace(/[&<>"']/g, (c) => ({ '&': '&amp;', '<': '&lt;', '>': '&gt;', '"': '&quot;', "'": '&#39;' })[c]);

export const submitEnquiry = onRequest({ region: 'europe-west4', maxInstances: 5, memory: '256MiB', timeoutSeconds: 20 }, async (req, res) => {
  const isForm = (req.get('content-type') || '').includes('application/x-www-form-urlencoded');
  const reply = (code, body) => (isForm ? res.redirect(303, code < 300 ? '/contact/?sent=1' : '/contact/?error=1') : res.status(code).json(body));
  if (req.method !== 'POST') return res.status(405).set('Allow', 'POST').end();
  const b = req.body || {};
  if (b.website) return reply(200, { ok: true }); // honeypot: pretend success
  const t = Number(b.t);
  if (t && Date.now() - t < MIN_FILL_MS) return reply(200, { ok: true }); // time-trap: too fast for a person
  const d = Object.fromEntries(Object.entries(LIMITS).map(([k, n]) => [k, clean(b[k], n, MULTI.has(k))]));
  if (!TOPICS.has(d.topic)) d.topic = 'not-sure';
  const errors = [];
  if (d.name.length < 2) errors.push('name');
  if (!/^[^\s@]+@[^\s@]+\.[^\s@]{2,}$/.test(d.email)) errors.push('email');
  if (d.phone.replace(/\D/g, '').length < 7) errors.push('phone');
  if (d.message.length < 10) errors.push('message');
  if (errors.length) return reply(400, { ok: false, errors });
  try {
    if (!(await allowed(req.ip || 'unknown'))) return reply(429, { ok: false, error: 'rate' });
    const ref = await db.collection('enquiries').add({ ...d, createdAt: FieldValue.serverTimestamp(), ua: clean(req.get('user-agent'), 300) });
    const rows = Object.entries(d).filter(([, v]) => v).map(([k, v]) => `<tr><th align="left" valign="top">${k}</th><td>${esc(v).replace(/\n/g, '<br>')}</td></tr>`).join('');
    await db.collection('mail').add({
      to: TO, replyTo: d.email,
      message: { subject: `Website enquiry — ${d.name}${d.organisation ? ` (${d.organisation})` : ''}`, text: Object.entries(d).map(([k, v]) => `${k}: ${v}`).join('\n'), html: `<table cellpadding="6">${rows}</table><p>Ref ${ref.id}</p>` },
    });
    return reply(200, { ok: true });
  } catch (e) {
    console.error('enquiry failed', e);
    return reply(500, { ok: false });
  }
});
