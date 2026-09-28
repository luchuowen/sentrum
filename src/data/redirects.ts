// Legacy sentrumcoms.net URL → new path. Mirrored in firebase.json "redirects" (301).
export const redirects: Record<string, string> = {
  '/index.html': '/',
  // about/contact legacy paths unverified — confirm before cutover
  '/about.html': '/company/',
  '/contact.html': '/contact/',
  '/network-infrastructure.html': '/solutions/networks/structured-cabling/',
  '/wifi-installation.html': '/solutions/networks/wifi/',
  '/vsat-installation.html': '/solutions/networks/vsat/',
  '/access-control.html': '/solutions/security/access-control/',
  '/intrusion-detection.html': '/solutions/security/intrusion-detection/',
  '/cyber-security.html': '/solutions/security/cyber-security/',
  '/unified-communications.html': '/solutions/communications-av/unified-communications/',
  '/video-wall-installation.html': '/solutions/communications-av/video-walls/',
  '/audio-visual-system.html': '/solutions/communications-av/audio-visual/',
  '/server-installation.html': '/solutions/power-data-centre/servers/',
  '/power-installation.html': '/solutions/power-data-centre/power-ups/',
  '/fabrication.html': '/solutions/supply-fabrication-support/fabrication/',
  '/it-equipment.html': '/solutions/supply-fabrication-support/it-equipment/',
  '/technical-support.html': '/solutions/supply-fabrication-support/technical-support/',
};
