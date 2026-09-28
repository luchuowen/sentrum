export const SITE_URL = 'https://sentrum.navac.co.ke';
export const company = {
  name: 'Sentrum Communication & Technologies Ltd',
  short: 'Sentrum Communications',
  phone: '+254 720 288 713', tel: '+254720288713',
  email: 'info@sentrumcoms.net',
  address: 'Wilson Airport, Block 34, 3rd Office', city: 'Nairobi', country: 'Kenya',
  geo: { lat: -1.3204, lng: 36.8127 },
  // WhatsApp number not yet confirmed by owner — links go to /contact/ until it is.
  whatsapp: null as string | null,
};
export const nav = [
  { href: '/solutions/', label: 'Solutions' },
  { href: '/remote-and-satellite/', label: 'Remote & Satellite' },
  { href: '/how-we-work/', label: 'How we work' },
  { href: '/company/', label: 'Company' },
  { href: '/contact/', label: 'Contact' },
];
export const brands = ['Cisco','HPE','Dell','Check Point','Ubiquiti','D-Link','Siemon','Black Box','iDirect','Yeastar','Yealink','Planar','Samsung','Epson','Bose','Yamaha','Behringer','ZKTeco','Optex','Hikvision','Dahua','Delta','Tripp Lite','Havells','Crabtree','Giganet'];
export const process = [
  ['Survey', 'We visit the site and see what’s there.'],
  ['Design', 'We plan the layout and list every item and cost.'],
  ['Supply', 'We source the equipment from established makers.'],
  ['Install', 'Our engineers install it, on our own steel.'],
  ['Commission', 'We test it, set it up and train your team.'],
  ['Support', 'We stay on to support what we install.'],
];
