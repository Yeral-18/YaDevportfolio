/**
 * compose-envato.mjs — Lockup = emblema de ENVATO (el que gustó, vector limpio) +
 * wordmark TIPOGRÁFICO COICEM SAS. Genera lockups claro/oscuro + assets del sitio.
 */
import { Resvg } from '../coicem-web/node_modules/@resvg/resvg-js/index.js';
import { readFileSync, writeFileSync } from 'node:fs';

const C = { blue: '#025199', orange: '#F79204', metalL: '#6B7C90' };
const embB64 = readFileSync(new URL('./emblema-envato-clean.png', import.meta.url)).toString('base64');
const EMB = (x, y, s) => `<image x="${x}" y="${y}" width="${s}" height="${s}" href="data:image/png;base64,${embB64}" preserveAspectRatio="xMidYMid meet"/>`;

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

const isotipo = () => `<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 220 220" width="220" height="220">${EMB(6, 6, 208)}</svg>`;
function lockup(bg, theme) {
  return `<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 800 220" width="800" height="220">
    ${bg ? `<rect width="800" height="220" fill="${bg}"/>` : ''}
    ${EMB(0, 8, 204)}
    ${wordmark(224, 122, theme)}
  </svg>`;
}
function og() {
  return `<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 1200 630" width="1200" height="630">
    <rect width="1200" height="630" fill="#FFFFFF"/><rect width="1200" height="14" fill="${C.orange}"/>
    ${EMB(440, 110, 320)}
    <g transform="translate(232 470) scale(0.92)">${wordmark(212, 60, 'light')}</g></svg>`;
}

const png = (svg, w, bg) => new Resvg(svg, { fitTo: { mode: 'width', value: w }, background: bg || 'rgba(0,0,0,0)' }).render().asPng();
const here = (p) => new URL(`./${p}`, import.meta.url);
const site = (p) => new URL(`../coicem-web/public/${p}`, import.meta.url);

writeFileSync(here('lockup-envato-claro.png'), png(lockup('#FFFFFF', 'light'), 1600));
writeFileSync(here('lockup-envato-oscuro.png'), png(lockup('#0B0E14', 'dark'), 1600));
console.log('OK lockup envato (emblema que gustó + wordmark tipográfico)');

if (process.argv[2] === 'apply') {
  writeFileSync(here('lockup-envato-claro.svg'), lockup(null, 'light'));
  writeFileSync(here('lockup-envato-oscuro.svg'), lockup(null, 'dark'));
  writeFileSync(here('isotipo-envato.svg'), isotipo());
  writeFileSync(site('images/coicem-logo.png'), png(lockup(null, 'dark'), 1600));
  writeFileSync(site('favicon.png'), png(isotipo(), 256));
  writeFileSync(here('og-envato.png'), png(og(), 1200));
  console.log('APLICADO al sitio (coicem-logo, favicon, og)');
}
