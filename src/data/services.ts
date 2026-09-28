// All service content. Source: docs/reference/legacy-site.md. Plain-language lines are for non-technical buyers.
// Never add claims (clients, certifications, SLAs, numbers) that are not in the legacy evidence.

export type Service = {
  slug: string; name: string; plain: string; summary: string;
  deliver: string[]; usedIn: string[]; tech?: string[];
};
export type Area = {
  slug: string; name: string; short: string; step: string; img: string;
  headline: string; plain: string; services: Service[];
};

export const areas: Area[] = [
  {
    slug: 'networks', name: 'Networks & Connectivity', short: 'Networks', step: 'backbone', img: '/img/cap-networks.jpg',
    headline: 'The cables, WiFi and links everything else runs on.',
    plain: 'Every phone, laptop, camera and screen in a building needs a reliable connection. We install that connection — cables through the walls, WiFi in the ceilings, and a satellite link where there is no fibre.',
    services: [
      {
        slug: 'structured-cabling', name: 'Structured cabling & fibre',
        plain: 'The organised network of cables inside your walls and ceilings that connects every desk, device and floor.',
        summary: 'Copper and fibre cabling designed, installed and configured as one tidy, dependable network.',
        deliver: ['Structured copper cabling and optical fibre', 'Router and switch configuration', 'VPN and network management systems', 'Physical or virtual network design', 'Installation, integration, training and support'],
        usedIn: ['Offices and headquarters', 'Campuses', 'Warehouses and branch offices'],
        tech: ['Cisco', 'HPE', 'Siemon', 'Black Box', 'D-Link', 'Giganet'],
      },
      {
        slug: 'wifi', name: 'WiFi',
        plain: 'Wireless internet that reaches every meeting room, office and waiting area — without dead spots.',
        summary: 'Access points placed, powered and configured so people can move around the building without losing connection.',
        deliver: ['Access points and antennas', 'Power over Ethernet — no extra sockets needed', 'Coverage for offices, meeting rooms and visitor areas', 'Layouts that can change without re-cabling'],
        usedIn: ['Offices', 'Hospitality and waiting areas', 'Temporary and flexible workspaces'],
        tech: ['Ubiquiti', 'Cisco', 'D-Link'],
      },
      {
        slug: 'vsat', name: 'VSAT & satellite',
        plain: 'Internet and data links by satellite, for sites that cable and mobile networks don’t reach.',
        summary: 'Terminals installed and commissioned on shared-hub and dedicated networks — for one site or rollouts across several countries.',
        deliver: ['Shared-hub networks on iDirect, SkyEdge and Comtech', 'SCPC and TV broadcast backhaul', 'Small Ku-band terminals to large teleport antennas and RFTs', 'Rapid deployment and commissioning of multiple sites', 'Masts and mounts from our own fabrication floor'],
        usedIn: ['Remote and field sites', 'Operations across several countries', 'Broadcasters and service providers'],
        tech: ['iDirect'],
      },
    ],
  },
  {
    slug: 'security', name: 'Security Systems', short: 'Security', step: 'security', img: '/img/cap-security.jpg',
    headline: 'Control who gets in — to the building and to the network.',
    plain: 'Security has two sides: the doors and perimeter people can walk through, and the network that hackers try to get into. We protect both.',
    services: [
      {
        slug: 'access-control', name: 'Access control',
        plain: 'Card or code readers that decide who can open which door, and when.',
        summary: 'IP-based door access that can be managed door by door or as a group — and linked to your fire alarm.',
        deliver: ['Door readers, magnetic locks, door closers and switches', 'Power supplies and wiring', 'IP-based controllers, managed individually or as a group', 'Integration with fire alarm systems', 'Installation and testing'],
        usedIn: ['Offices and restricted areas', 'Server and comms rooms', 'Staff and visitor entrances'],
        tech: ['ZKTeco'],
      },
      {
        slug: 'intrusion-detection', name: 'Intrusion detection',
        plain: 'Sensors that notice when someone enters an area they shouldn’t — and raise the alarm.',
        summary: 'Motion and perimeter sensors chosen for each space, with alerts you can manage from a phone.',
        deliver: ['Passive infrared (PIR) and microwave sensors', 'Dual-technology and area-reflective sensors', 'Ultrasonic and vibration sensors', 'RFID', 'Smartphone app activation'],
        usedIn: ['Perimeters and fences', 'Stores and warehouses', 'Remote and unmanned sites'],
        tech: ['Optex'],
      },
      {
        slug: 'cyber-security', name: 'Cyber security',
        plain: 'Protection for your network, computers and phones against hackers and malware.',
        summary: 'Firewalls, endpoint and mobile protection working as one security architecture.',
        deliver: ['Network firewalls', 'Endpoint protection for computers', 'Mobile-device threat protection', 'Threat intelligence to spot risks early'],
        usedIn: ['Businesses', 'Service providers', 'Government agencies'],
        tech: ['Check Point'],
      },
    ],
  },
  {
    slug: 'communications-av', name: 'Communications & AV', short: 'Comms & AV', step: 'rooms', img: '/img/cap-av.jpg',
    headline: 'Rooms where people can call, meet, present and decide.',
    plain: 'From desk phones to video calls to a wall of screens in an operations room — we choose, install and set up the equipment so it simply works.',
    services: [
      {
        slug: 'unified-communications', name: 'Unified communications',
        plain: 'Phone calls, video meetings and messaging on one system, over your network.',
        summary: 'IP telephony and conferencing that let people work together across the office or across countries.',
        deliver: ['IP telephony for voice calls', 'Web and video conferencing', 'Audio messaging', 'Moving existing phone systems onto IP'],
        usedIn: ['Offices and branch networks', 'Teams working from several sites'],
        tech: ['Yeastar', 'Yealink'],
      },
      {
        slug: 'video-walls', name: 'Video walls',
        plain: 'Several screens joined into one large display, showing many sources at once.',
        summary: 'Brand advice, design and installation of multi-screen displays that operators can rearrange as needed.',
        deliver: ['Advice on video wall brands and sizes', 'Design for the room and viewing distance', 'Multiple inputs shown and resized live', 'Mount brackets from our own fabrication floor', 'Installation and support'],
        usedIn: ['Operations and monitoring centres', 'Situation rooms and newsrooms', 'Conference and lecture rooms'],
        tech: ['Planar', 'Samsung'],
      },
      {
        slug: 'audio-visual', name: 'Audio-visual systems',
        plain: 'The screens, projectors, microphones and speakers that make meetings and events work.',
        summary: 'We assess the room and the audience first, then recommend and install the right system.',
        deliver: ['Consultation and room assessment', 'Video collaboration and projection systems', 'Interactive whiteboards', 'Recording equipment', 'PA and sound systems'],
        usedIn: ['Boardrooms', 'Lecture halls and training rooms', 'Events'],
        tech: ['Epson', 'Bose', 'Yamaha', 'Behringer'],
      },
    ],
  },
  {
    slug: 'power-data-centre', name: 'Power & Data Centre', short: 'Power & DC', step: 'core', img: '/img/cap-power.jpg',
    headline: 'Keep the servers, and everything that depends on them, running.',
    plain: 'Servers hold your business data and applications. They need the right hardware, a safe room and power that never drops. We handle all three.',
    services: [
      {
        slug: 'servers', name: 'Servers',
        plain: 'The central computers that store your files and run your business systems.',
        summary: 'Consultancy, supply, installation, configuration and support — sized to what your business actually needs.',
        deliver: ['Consultancy on the right server for the workload', 'Supply and installation', 'Configuration', 'Maintenance and support'],
        usedIn: ['Comms rooms', 'Small data centres', 'Offices outgrowing shared computers'],
        tech: ['HPE', 'Dell'],
      },
      {
        slug: 'power-ups', name: 'Power, UPS & electrical',
        plain: 'Backup power that keeps equipment running during outages, plus the electrical work behind it.',
        summary: 'UPS-backed clean power, electrical fit-outs, lighting and solar.',
        deliver: ['UPS “clean power” that bridges outages and protects equipment', 'Web-based UPS monitoring', 'Electrical fit-outs: breakers, switches, distribution boards, sockets', 'Solar power installations', 'Lighting: recessed, security, motion-sensor and photocell', 'Emergency repairs'],
        usedIn: ['Comms rooms', 'Offices', 'Off-grid and remote sites'],
        tech: ['Delta', 'Tripp Lite', 'Havells', 'Crabtree'],
      },
    ],
  },
  {
    slug: 'supply-fabrication-support', name: 'Supply, Fabrication & Support', short: 'Fabrication', step: 'steel', img: '/img/cap-fabrication.jpg',
    headline: 'Our own steel, the right equipment, and support after go-live.',
    plain: 'Many installs need a mast, a bracket or a rack made to measure. We make them ourselves, supply the equipment, and stay on to support what we install.',
    services: [
      {
        slug: 'fabrication', name: 'Metal fabrication',
        plain: 'Custom steel parts — masts, mounts and racks — made to fit your site.',
        summary: 'Made on our own floor to your specification, so installs don’t wait on another contractor.',
        deliver: ['Masts', 'VSAT and video-wall mount brackets', 'UPS racks', 'Aviation-light brackets', 'CCTV bracket mounts', 'Automated gates and TV carts'],
        usedIn: ['Rooftops and remote sites', 'Control rooms', 'Comms rooms'],
      },
      {
        slug: 'it-equipment', name: 'IT equipment supply',
        plain: 'The right computers, network and office technology, sourced and installed for you.',
        summary: 'From advice to delivery, installation and after-sales service, through major distributors.',
        deliver: ['Consultancy on the right equipment', 'Delivery and installation', 'After-sales service', 'Sourcing through major distributors'],
        usedIn: ['New offices and expansions', 'Equipment refreshes'],
        tech: ['Dell', 'HPE', 'Samsung', 'Epson'],
      },
      {
        slug: 'technical-support', name: 'Technical support',
        plain: 'Help with the systems we installed for you, after they go live.',
        summary: 'We implement and support the systems we install.',
        deliver: ['Support for the systems we implement', 'Advice on the right technology for your needs and budget'],
        usedIn: ['Every system we deliver'],
      },
    ],
  },
];

export const allServices = areas.flatMap((a) => a.services.map((s) => ({ ...s, area: a })));
export const serviceUrl = (a: Area, s: Service) => `/solutions/${a.slug}/${s.slug}/`;
export const areaUrl = (a: Area) => `/solutions/${a.slug}/`;
