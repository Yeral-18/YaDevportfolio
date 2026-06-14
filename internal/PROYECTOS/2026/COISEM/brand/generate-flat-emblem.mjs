/**
 * generate-flat-emblem.mjs — Rediseño FLAT profesional del emblema COICEM.
 * Vectores geométricos perfectos (bordes nítidos), paleta plana, conserva los
 * elementos del original: engranaje + edificios + herramientas cruzadas + arco
 * naranja + onda azul. Genera emblema + lockups (con wordmark tipográfico) + assets.
 */
import { Resvg } from '../coicem-web/node_modules/@resvg/resvg-js/index.js';
import { writeFileSync } from 'node:fs';

// ── Paleta plana ──────────────────────────────────────────────
const C = {
  blue:   '#025199', blueDk: '#013A6E', blueLt: '#2E7CC2',
  navy:   '#0B3D6B',
  orange: '#F79204', orangeDk: '#D87C00',
  gear:   '#46566E', gearDk: '#2E3B4E',
  steel:  '#5E7190',
  white:  '#FFFFFF', ink: '#0B0E14',
  metalL: '#6B7C90',
};

const R = (n) => Number(n.toFixed(2));
const P = (cx, cy, ang, r) => [R(cx + Math.cos(ang) * r), R(cy + Math.sin(ang) * r)];
const rad = (d) => (d * Math.PI) / 180;

// ── Engranaje: dientes trapezoidales finos y uniformes ────────
function gear(cx, cy, teeth, rOut, rIn, fill) {
  const pts = [];
  const step = (Math.PI * 2) / teeth;
  for (let i = 0; i < teeth; i++) {
    const a = i * step;
    pts.push(P(cx, cy, a + step * 0.06, rIn));
    pts.push(P(cx, cy, a + step * 0.20, rOut));
    pts.push(P(cx, cy, a + step * 0.30, rOut));
    pts.push(P(cx, cy, a + step * 0.44, rIn));
  }
  const d = pts.map((p, i) => (i ? 'L' : 'M') + p[0] + ' ' + p[1]).join(' ') + 'Z';
  return `<path d="${d}" fill="${fill}"/>`;
}

// ── Arco (swoosh) con extremos redondeados ────────────────────
function arc(cx, cy, r, w, a0, a1, color) {
  const [x0, y0] = P(cx, cy, rad(a0), r);
  const [x1, y1] = P(cx, cy, rad(a1), r);
  const large = Math.abs(a1 - a0) > 180 ? 1 : 0;
  return `<path d="M ${x0} ${y0} A ${r} ${r} 0 ${large} 1 ${x1} ${y1}" fill="none" stroke="${color}" stroke-width="${w}" stroke-linecap="round"/>`;
}

// ── Emblema ───────────────────────────────────────────────────
function emblem() {
  const cx = 120, cy = 120;
  const win = (x, y, w = 4, h = 4.6) => `<rect x="${x}" y="${y}" width="${w}" height="${h}" rx="0.6" fill="${C.white}"/>`;

  // Edificios (skyline) — 3 torres, apoyadas en línea base y=150
  const buildings = `
    <g>
      <rect x="88"  y="86"  width="20" height="64" fill="${C.blue}"/>
      <rect x="110" y="100" width="24" height="50" fill="${C.blueLt}"/>
      <rect x="136" y="112" width="17" height="38" fill="${C.blueDk}"/>
      ${[92, 102].flatMap(x => [92,102,112,122,132,142].map(y => win(x, y))).join('')}
      ${[114, 124].flatMap(x => [106,116,126,136].map(y => win(x, y))).join('')}
      ${[139].flatMap(x => [118,128,138].map(y => win(x, y))).join('')}
    </g>`;

  // Herramientas cruzadas (zona inferior, delante de la línea base — sin trepar
  // a los edificios). Compactas: cabezas gruesas abajo, vástagos cortos.
  const tools = `
    <g transform="translate(120 168)">
      <!-- llave inglesa (acero claro, contrasta con la onda navy) -->
      <g transform="rotate(-30)">
        <rect x="-5.5" y="-26" width="11" height="30" rx="5.5" fill="${C.steel}"/>
        <path fill-rule="evenodd" fill="${C.steel}" d="
          M 0 14 a 13 13 0 1 0 0.01 0 Z
          M 0 20 a 6.5 6.5 0 1 1 -0.01 0 Z
          M -6.5 9 L 6.5 9 L 6.5 20 L -6.5 20 Z"/>
      </g>
      <!-- destornillador (mango naranja, vástago acero, punta plana) -->
      <g transform="rotate(30)">
        <rect x="-7" y="2" width="14" height="26" rx="7" fill="${C.orange}"/>
        <rect x="-2.7" y="-24" width="5.4" height="26" fill="${C.gearDk}"/>
        <rect x="-4" y="-28" width="8" height="5" fill="${C.gearDk}"/>
      </g>
    </g>`;

  // Onda azul (la "hoja" del original) en la base
  const wave = `<path d="M 56 160 q 64 30 128 0 q -22 26 -64 26 q -42 0 -64 -26 Z" fill="${C.navy}"/>
    <path d="M 56 160 q 64 30 128 0" fill="none" stroke="${C.white}" stroke-width="3"/>`;

  return `
  <g>
    <!-- engranaje (con anillo interior para profundidad plana) -->
    ${gear(cx, cy, 16, 116, 103, C.gear)}
    <circle cx="${cx}" cy="${cy}" r="100" fill="${C.gearDk}"/>
    <circle cx="${cx}" cy="${cy}" r="92" fill="${C.white}"/>
    <!-- arco naranja superior-derecho -->
    ${arc(cx, cy, 88, 9, -126, 44, C.orange)}
    <clipPath id="disc"><circle cx="${cx}" cy="${cy}" r="92"/></clipPath>
    <g clip-path="url(#disc)">
      ${wave}
      ${buildings}
      <rect x="58" y="150" width="124" height="2.5" fill="${C.steel}"/>
      ${tools}
    </g>
  </g>`;
}

// ── Wordmark tipográfico (limpio) ─────────────────────────────
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

// ── Documentos ────────────────────────────────────────────────
const isotipo = () => `<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 240 240" width="240" height="240">${emblem()}</svg>`;
function lockup(bg, theme) {
  return `<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 800 220" width="800" height="220">
    ${bg ? `<rect width="800" height="220" fill="${bg}"/>` : ''}
    <g transform="translate(2 6) scale(0.88)">${emblem()}</g>
    ${wordmark(224, 122, theme)}
  </svg>`;
}

const png = (svg, w, bg) => new Resvg(svg, { fitTo: { mode: 'width', value: w }, background: bg || 'rgba(0,0,0,0)' }).render().asPng();
const here = (p) => new URL(`./${p}`, import.meta.url);
const site = (p) => new URL(`../coicem-web/public/${p}`, import.meta.url);

// OG 1200×630
const og = () => `<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 1200 630" width="1200" height="630">
  <rect width="1200" height="630" fill="#FFFFFF"/><rect width="1200" height="14" fill="${C.orange}"/>
  <g transform="translate(420 120) scale(1.6)">${emblem()}</g>
  <g transform="translate(232 470) scale(0.92)">${wordmark(212, 60, 'light')}</g></svg>`;

// Entregables
writeFileSync(here('emblema-flat.svg'), isotipo());
writeFileSync(here('emblema-flat.png'), png(isotipo(), 600));
writeFileSync(here('lockup-flat-claro.svg'), lockup(null, 'light'));
writeFileSync(here('lockup-flat-oscuro.svg'), lockup(null, 'dark'));
writeFileSync(here('lockup-flat-claro.png'), png(lockup('#FFFFFF', 'light'), 1600));
writeFileSync(here('lockup-flat-oscuro.png'), png(lockup('#0B0E14', 'dark'), 1600));

// Aplicar al sitio (navbar/footer oscuros → lockup oscuro; favicon = isotipo)
writeFileSync(site('images/coicem-logo.png'), png(lockup(null, 'dark'), 1600));
writeFileSync(site('favicon.png'), png(isotipo(), 256));
writeFileSync(here('og-flat.png'), png(og(), 1200));
console.log('OK emblema flat + lockups + assets del sitio (coicem-logo, favicon, og)');
