import { defineConfig } from 'astro/config';
import { fileURLToPath } from 'url';
import svelte from '@astrojs/svelte';
import tailwind from '@astrojs/tailwind';
import sitemap from '@astrojs/sitemap';

export default defineConfig({
  site: 'https://multiserviciospj.com',
  base: '/',
  integrations: [
    svelte(),
    tailwind({
      configFile: fileURLToPath(new URL('./tailwind.config.mjs', import.meta.url)),
    }),
    sitemap(),
  ],
  build: {
    assets: 'assets',
  },
  vite: {
    build: {
      cssMinify: true,
    },
  },
});
