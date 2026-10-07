import { defineConfig } from 'astro/config';
import tailwindcss from '@tailwindcss/vite';

// https://astro.build/config
export default defineConfig({
  outDir: './site',
  build: {
    format: 'directory',
  },
  redirects: {
    '/mallorca/rutes': '/rutes',
    '/mallorca/acampada_i_refugis': '/acampada',
    '/mallorca/transport': '/transport',
    '/mallorca/agrupaments': '/agrupaments',
    '/mallorca/admin_comentaris': '/admin',
  },
  vite: {
    plugins: [tailwindcss()],
  },
});
