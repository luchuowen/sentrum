// Line-art scene settings for inner pages. Coordinates are in the Building drawing's 900×620 space.
// Each note: anchor (x,y), label direction (dx,dy in screen px), title and one short line.
export type Note = { x: number; y: number; dx: number; dy: number; t: string; d: string };
export type Focus = { steps: string[]; crop: string; notes: Note[] };

const N = (x: number, y: number, dx: number, dy: number, t: string, d: string): Note => ({ x, y, dx, dy, t, d });

export const areaScene: Record<string, Focus> = {
  networks: { steps: ['backbone', 'uplink'], crop: '0 40 900 560', notes: [
    N(333, 300, 40, -64, 'RISER', 'Backbone between floors'),
    N(500, 318, 120, 40, 'WIFI', 'Access points in the ceiling'),
    N(120, 566, 30, -60, 'FIBRE ENTRY', 'Where the provider comes in'),
    N(600, 152, -140, -50, 'VSAT', 'Satellite where fibre ends'),
  ] },
  security: { steps: ['security'], crop: '0 380 900 220', notes: [
    N(429, 480, 70, -50, 'READER', 'Decides who opens the door'),
    N(75, 470, 10, -70, 'PERIMETER', 'Sensors along the fence'),
    N(230, 500, -20, 70, 'FIREWALL', 'Guards the network edge'),
    N(815, 470, -60, -70, 'GATE', 'Alarm on entry'),
  ] },
  'communications-av': { steps: ['rooms'], crop: '120 180 560 260', notes: [
    N(240, 256, 30, -80, 'VIDEO WALL', 'Screens acting as one display'),
    N(530, 396, 40, -70, 'IP PHONES', 'Calls over the data network'),
    N(163, 234, -10, 80, 'PROJECTOR', 'Presentations in any room'),
  ] },
  'power-data-centre': { steps: ['core'], crop: '120 140 420 420', notes: [
    N(209, 490, 150, -60, 'RACKS', 'Servers kept in order'),
    N(273, 516, 120, 30, 'UPS', 'Power through outages'),
    N(250, 180, 120, -20, 'SOLAR', 'Where mains is unreliable'),
  ] },
  'supply-fabrication-support': { steps: ['steel'], crop: '120 40 760 520', notes: [
    N(716, 300, 70, -40, 'MAST', 'Fabricated on our own floor'),
    N(590, 186, -150, -60, 'MOUNT', 'Dish and equipment brackets'),
    N(209, 440, -40, -80, 'RACK FRAME', 'Built to fit the room'),
  ] },
};

export const serviceScene: Record<string, Focus> = {
  'structured-cabling': { steps: ['backbone'], crop: '140 180 520 380', notes: [
    N(333, 420, -110, 30, 'RISER', 'Copper and fibre, floor to floor'), N(470, 370, 60, -50, 'FLOOR RUN', 'Every desk on the same network') ] },
  wifi: { steps: ['backbone'], crop: '400 160 280 220', notes: [
    N(500, 318, -90, 40, 'ACCESS POINT', 'Powered over the data cable'), N(560, 205, 40, -40, 'COVERAGE', 'No dead spots between rooms') ] },
  vsat: { steps: ['uplink'], crop: '520 20 380 210', notes: [
    N(594, 158, -60, 40, 'DISH', 'Aligned and commissioned'), N(832, 64, -40, 60, 'SATELLITE', 'Shared hub or dedicated SCPC') ] },
  'access-control': { steps: ['security'], crop: '340 420 160 140', notes: [
    N(429, 480, 30, -40, 'READER', 'Card or code at the door'), N(400, 510, 30, 36, 'LOCK', 'Magnetic lock and closer') ] },
  'intrusion-detection': { steps: ['security'], crop: '0 410 380 170', notes: [
    N(75, 470, 60, -50, 'SENSORS', 'Notice movement on the fence'), N(220, 552, 40, -50, 'ALARM PATH', 'Wired back to the panel') ] },
  'cyber-security': { steps: ['security', 'core'], crop: '150 420 180 140', notes: [
    N(230, 500, 40, -50, 'FIREWALL', 'Filters traffic at the edge'), N(190, 470, -40, -40, 'NETWORK', 'Protected behind it') ] },
  'unified-communications': { steps: ['rooms'], crop: '440 350 200 110', notes: [
    N(485, 396, -30, -40, 'DESK PHONE', 'Calls on the data network'), N(575, 396, 30, -40, 'EXTENSION', 'Every desk reachable') ] },
  'video-walls': { steps: ['rooms'], crop: '150 200 180 110', notes: [
    N(240, 256, 40, -40, 'VIDEO WALL', 'One image across many screens') ] },
  'audio-visual': { steps: ['rooms'], crop: '130 200 230 120', notes: [
    N(163, 234, -20, 50, 'PROJECTOR', 'Bright, sharp presentations'), N(260, 270, 40, 30, 'DISPLAY', 'Sound and picture set up to work') ] },
  servers: { steps: ['core'], crop: '150 410 170 150', notes: [
    N(190, 470, -30, -40, 'SERVERS', 'Installed and configured'), N(230, 500, 40, -30, 'STORAGE', 'Your data, kept safe') ] },
  'power-ups': { steps: ['core'], crop: '150 150 220 410', notes: [
    N(273, 516, 50, -20, 'UPS', 'Battery backup on every outage'), N(250, 180, 50, 30, 'SOLAR', 'Clean power on the roof') ] },
  fabrication: { steps: ['steel'], crop: '540 60 240 490', notes: [
    N(716, 300, 40, -40, 'MAST', 'Lattice steel, made in-house'), N(590, 186, -60, 40, 'MOUNT', 'Dish bracket to fit the roof') ] },
  'it-equipment': { steps: ['core', 'rooms', 'backbone'], crop: '140 180 520 380', notes: [
    N(209, 490, -60, -40, 'RACKS', 'Servers and switches'), N(500, 318, 50, -40, 'WIFI', 'Access points'), N(530, 396, 50, 30, 'PHONES', 'Desk handsets') ] },
  'technical-support': { steps: ['backbone', 'core', 'security', 'rooms', 'uplink'], crop: '0 40 900 560', notes: [
    N(500, 318, 100, -40, 'SUPPORT', 'We know what we installed'), N(209, 490, -100, -60, 'CHANGES', 'Upgrades as you grow') ] },
};

export const hubNotes: Record<string, Note[]> = {
  backbone: areaScene.networks.notes,
  security: areaScene.security.notes,
  rooms: areaScene['communications-av'].notes,
  core: areaScene['power-data-centre'].notes,
  steel: areaScene['supply-fabrication-support'].notes,
};
