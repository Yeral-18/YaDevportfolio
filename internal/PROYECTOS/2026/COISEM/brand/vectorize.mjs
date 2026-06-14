/**
 * vectorize.mjs — Vectoriza el EMBLEMA preprocesado (emblema-pre.png) con params
 * de máxima limpieza (menos capas, splines, corner alto) para evitar texturas.
 */
import { vectorize, ColorMode, Hierarchical, PathSimplifyMode } from '../coicem-web/node_modules/@neplex/vectorizer/index.js';
import { Resvg } from '../coicem-web/node_modules/@resvg/resvg-js/index.js';
import { readFile, writeFile } from 'node:fs/promises';

const opts = {
  colorMode: ColorMode.Color,
  colorPrecision: 6,        // preserva grises metálicos
  filterSpeckle: 20,        // borra motas de borde sin comer detalle
  spliceThreshold: 65,
  cornerThreshold: 88,      // bordes suaves
  hierarchical: Hierarchical.Stacked,
  mode: PathSimplifyMode.Spline,
  layerDifference: 26,
  lengthThreshold: 8,
  maxIterations: 10,
  pathPrecision: 5,
};

const src = await readFile(new URL('./emblema-pre.png', import.meta.url));
const svg = await vectorize(src, opts);
await writeFile(new URL('./emblema-vector.svg', import.meta.url), svg);
const png = new Resvg(svg, { fitTo: { mode: 'width', value: 600 } }).render().asPng();
await writeFile(new URL('./emblema-vector.png', import.meta.url), png);
console.log(`OK emblema-vector.svg (${(svg.length / 1024).toFixed(0)} KB)`);
