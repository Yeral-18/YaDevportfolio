/**
 * compose-lockup.mjs — Lockup final = emblema VECTORIZADO (real, limpio) +
 * wordmark TIPOGRÁFICO limpio (no el wordmark vectorizado con textura).
 * Genera el lockup para fondo claro y oscuro + isotipo + assets del sitio.
 */
import { Resvg } from '../coicem-web/node_modules/@resvg/resvg-js/index.js';
import { readFile, writeFile } from 'node:fs/promises';

const C = { blue: '#025199', orange: '#F79204', metalL: '#6B7C90' };

// Extrae viewBox + contenido interno del emblema vectorizado
const raw = await readFile(new URL('./emblema-vector.svg', import.meta.url), 'utf8');
const vb = (raw.match(/viewBox="([^"]+)"/) || [, '0 0 1000 1000'])[1];
const inner = raw.replace(/^[\s\S]*?<svg[^>]*>/, '').replace(/<\/svg>\s*$/, '');

// Wordmark tipográfico (mismas letras limpias de la versión A/B)
function wordmark(x, y, theme) {
  const coi = theme === 'dark' ? '#3B8FD9' : C.blue;
  const tag = theme === 'dark' ? '#8A99AB' : C.metalL;
  return `
  <g font-family="Arial, 'Archivo', sans-serif">
    <text x="${x}" y="${y}" font-size="62" font-weight="800" letter-spacing="1">
      <tspan fill="${coi}">COICEM</tspan><tspan fill="${C.orange}" dx="6">SAS</tspan>
    </text>
    <line x1="${x + 2}" y1="${y + 14}" x2="${x + 470}" y2="${y + 14}" stroke="${tag}" stroke-width="1.5"/>
    <text x="${x + 3}" y="${y + 33}" font-size="18.5" font-weight="600" letter-spacing="2.45" fill="${tag}">SERVICIO MANTENIMIENTO ESPECIALIZADO</text>
  </g>`;
}

// Emblema embebido como SVG anidado (cuadrado 200×200 a la izquierda)
function embEmbed(size, x, y) {
  return `<svg x="${x}" y="${y}" width="${size}" height="${size}" viewBox="${vb}" preserveAspectRatio="xMidYMid meet">${inner}</svg>`;
}

function lockup(bg, theme) {
  return `<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 800 210" width="800" height="210">
    ${bg ? `<rect width="800" height="210" fill="${bg}"/>` : ''}
    ${embEmbed(196, 4, 7)}
    ${wordmark(214, 116, theme)}
  </svg>`;
}
function isotipo() {
  return `<svg xmlns="http://www.w3.org/2000/svg" viewBox="${vb}" width="512" height="512">${inner}</svg>`;
}
function og() {
  return `<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 1200 630" width="1200" height="630">
    <rect width="1200" height="630" fill="#FFFFFF"/><rect width="1200" height="14" fill="${C.orange}"/>
    ${embEmbed(300, 450, 120)}
    <g transform="translate(232 440) scale(0.92)">${wordmark(212, 60, 'light')}</g>
  </svg>`;
}

const png = (svg, w, bg) => new Resvg(svg, { fitTo: { mode: 'width', value: w }, background: bg || 'rgba(0,0,0,0)' }).render().asPng();
const here = (p) => new URL(`./${p}`, import.meta.url);
const site = (p) => new URL(`../coicem-web/public/${p}`, import.meta.url);

// Entregables de marca
await writeFile(here('lockup-final-claro.svg'), lockup(null, 'light'));
await writeFile(here('lockup-final-oscuro.svg'), lockup(null, 'dark'));
await writeFile(here('lockup-final-claro.png'), png(lockup('#FFFFFF', 'light'), 1600));
await writeFile(here('lockup-final-oscuro.png'), png(lockup('#0B0E14', 'dark'), 1600));
await writeFile(here('isotipo-final.svg'), isotipo());
await writeFile(here('isotipo-final.png'), png(isotipo(), 512));
await writeFile(here('og-final.png'), png(og(), 1200));

// Aplicar al sitio (fondo oscuro → wordmark claro)
await writeFile(site('images/coicem-logo.png'), png(lockup(null, 'dark'), 1600));
await writeFile(site('favicon.png'), png(isotipo(), 256));
console.log('OK lockup final (emblema vectorizado + letras tipográficas) + assets del sitio');
