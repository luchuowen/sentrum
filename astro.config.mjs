import { defineConfig } from 'astro/config';
export default defineConfig({
  site: 'https://sentrum.navac.co.ke',
  trailingSlash: 'always',
  build: { format: 'directory', inlineStylesheets: 'always' },
  compressHTML: true,
});
