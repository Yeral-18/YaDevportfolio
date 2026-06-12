import { defineConfig } from 'astro/config';
import { fileURLToPath } from 'url';
import svelte from '@astrojs/svelte';
import tailwind from '@astrojs/tailwind';
import sitemap from '@astrojs/sitemap';
import { assertProductionReady } from './src/lib/site-config';

// Gate de producción: bloquea el build si quedan placeholders (contacto, telemetría,
// NIT, proyectos, logo vectorial). Staging builda libre; solo producción valida.
if (process.env.DEPLOY_TARGET === 'production') assertProductionReady();

export default defineConfig({
  site: 'https://coicem.com',
  base: '/',
  integrations: [
    svelte(),
    tailwind({
      // fileURLToPath: la ruta del monorepo tiene espacios/&; necesario para el glob.
      configFile: fileURLToPath(new URL('./tailwind.config.mjs', import.meta.url)),
    }),
    sitemap(),
  ],
  build: {
    assets: 'assets',   // CRÍTICO: Hostinger bloquea la carpeta _astro/
  },
  vite: {
    build: { cssMinify: true },
  },
});
