/**
 * ══════════════════════════════════════════════════════════════════
 * YaDev Design System — Astro Config Template
 * ══════════════════════════════════════════════════════════════════
 *
 * SETUP:
 *   1. Copy to: astro.config.mjs (project root)
 *   2. Replace PLACEHOLDER_SITE_URL with the client domain.
 *   3. Remove base: '/' if deploying to root (most projects).
 *
 * IMPORTANT NOTES:
 *
 *   fileURLToPath configFile fix:
 *     The tailwind configFile must be an absolute path resolved
 *     via fileURLToPath(). Without this, Vite fails to locate
 *     tailwind.config.mjs when the project folder contains special
 *     characters (e.g., spaces, &, accents in the path).
 *     This applies on both Windows and Linux. Always use this pattern.
 *
 *   build.assets = 'assets':
 *     Astro's default output folder for hashed assets is '_astro/'.
 *     Hostinger's Apache config blocks folders starting with an
 *     underscore by default. Using 'assets' avoids 404 errors on
 *     CSS, JS, and font files after deployment.
 *     NEVER use the default '_astro' folder for Hostinger deploys.
 *
 * ══════════════════════════════════════════════════════════════════
 */

import { defineConfig } from 'astro/config';
import { fileURLToPath }  from 'url';
import svelte             from '@astrojs/svelte';
import tailwind           from '@astrojs/tailwind';
import sitemap            from '@astrojs/sitemap';

export default defineConfig({
  /**
   * [PLACEHOLDER] Replace with client's production domain.
   * Used for sitemap generation and canonical URL resolution.
   * Must include protocol, no trailing slash.
   */
  site: 'https://PLACEHOLDER_SITE_URL',

  /**
   * base: '/'
   * Only needed when deploying to a sub-path (e.g., /ecomag/).
   * For root domain deployments, remove this line entirely.
   */
  // base: '/',

  integrations: [
    svelte(),

    tailwind({
      /**
       * configFile — absolute path fix for special characters in path.
       * fileURLToPath(new URL('./tailwind.config.mjs', import.meta.url))
       * resolves to an absolute path that Vite can handle reliably
       * regardless of OS or folder name encoding.
       *
       * DO NOT simplify this to just `configFile: './tailwind.config.mjs'`
       * — it breaks on Windows when the path contains '&', spaces, or
       * accented characters.
       */
      configFile: fileURLToPath(new URL('./tailwind.config.mjs', import.meta.url)),
    }),

    sitemap(),
  ],

  build: {
    /**
     * assets: 'assets' — CRITICAL for Hostinger deployment.
     *
     * Hostinger shared hosting (Apache) may return 403 Forbidden
     * for folders starting with underscore (_astro/) due to
     * .htaccess AllowOverride and directory restrictions.
     *
     * By setting this to 'assets', all compiled CSS/JS/fonts go
     * into /assets/ which is always accessible.
     *
     * If you change this, ALL .htaccess cache rules for 'assets/**'
     * must be updated to match the new folder name.
     */
    assets: 'assets',
  },

  vite: {
    build: {
      /**
       * cssMinify: true — minifies CSS output.
       * Reduces file size without any functional change.
       * Keep enabled for all production builds.
       */
      cssMinify: true,
    },
    /**
     * Optional: path aliases for cleaner imports.
     * Uncomment and add entries as needed.
     *
     * Usage in components:
     *   import Layout from '@layouts/Layout.astro'
     *   import { colors } from '@ds/tokens'
     */
    // resolve: {
    //   alias: {
    //     '@components': fileURLToPath(new URL('./src/components', import.meta.url)),
    //     '@layouts':    fileURLToPath(new URL('./src/layouts',    import.meta.url)),
    //     '@styles':     fileURLToPath(new URL('./src/styles',     import.meta.url)),
    //     '@ds':         fileURLToPath(new URL('./src/design-system', import.meta.url)),
    //     '@assets':     fileURLToPath(new URL('./src/assets',     import.meta.url)),
    //   },
    // },
  },
});
