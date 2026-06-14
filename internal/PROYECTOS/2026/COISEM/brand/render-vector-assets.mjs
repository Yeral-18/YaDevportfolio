/**
 * render-vector-assets.mjs — Rasteriza el logo VECTORIZADO (fiel al original) a los
 * assets que usa el sitio. Reemplaza el redibujo a mano por el logo profesional real.
 */
import { Resvg } from '../coicem-web/node_modules/@resvg/resvg-js/index.js';
import { readFile, writeFile } from 'node:fs/promises';

async function raster(svgName, w, outUrl, bg) {
  let svg = await readFile(new URL(`./${svgName}-vector.svg`, import.meta.url), 'utf8');
  if (bg) svg = svg.replace('<svg', `<svg style="background:${bg}"`);
  const png = new Resvg(svg, {
    fitTo: { mode: 'width', value: w },
    background: bg || 'rgba(0,0,0,0)',
  }).render().asPng();
  await writeFile(outUrl, png);
  console.log(`OK ${outUrl.pathname.split('/').pop()} (${w}px)`);
}

const site = (p) => new URL(`../coicem-web/public/${p}`, import.meta.url);

// Logo del sitio (navbar/footer) — lockup completo, transparente, alta resolución
await raster('logo', 1600, site('images/coicem-logo.png'));
// Favicon e isotipo — emblema solo
await raster('emblema', 512, site('favicon.png'));
await raster('emblema', 512, new URL('./paquete-isotipo-vector-512.png', import.meta.url));
// OG 1200×630 sobre blanco
await raster('logo', 1100, new URL('./paquete-og-vector.png', import.meta.url), '#FFFFFF');

console.log('Assets del logo vectorizado generados.');
