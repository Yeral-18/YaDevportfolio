/**
 * generate-logo.mjs — LOGO_ENGINE · COICEM S.A.S
 * Reconstrucción vectorial del logo (JPEG WhatsApp → SVG limpio).
 *   Versión A (fiel):    conserva el look original (engranaje metálico, hoja azul,
 *                        gradientes) pero regulariza dientes y limpia ruido.
 *   Versión B (mejorada):flat-design moderno, escalable a favicon, mismos elementos
 *                        (engranaje + edificios + herramientas + arco naranja),
 *                        sin bevels 3D ni degradados sucios.
 *
 * Paleta extraída del logo real: azul #025199 · naranja #F79204 · metal #313F50.
 * Genera SVG + PNG (vía @resvg/resvg-js) en esta carpeta.
 */
import { Resvg } from '../coicem-web/node_modules/@resvg/resvg-js/index.js';
import { writeFileSync } from 'node:fs';

// ─── Paleta ──────────────────────────────────────────────────────
const C = {
  blue: '#025199', blueD: '#013366', blueL: '#1E6FB8',
  orange: '#F79204', orangeD: '#D87C00',
  metal: '#3A4A5E', metalD: '#26303D', metalL: '#6B7C90',
  white: '#FFFFFF', ink: '#0B0E14',
};

// ─── Engranaje regular (geometría exacta) ────────────────────────
function gearPath(cx, cy, teeth, rOut, rIn) {
  const pts = [];
  const step = (Math.PI * 2) / teeth;
  for (let i = 0; i < teeth; i++) {
    const a = i * step;
    // 4 vértices por diente: valle → subida → cresta → bajada
    pts.push([a + step * 0.00, rIn]);
    pts.push([a + step * 0.18, rOut]);
    pts.push([a + step * 0.32, rOut]);
    pts.push([a + step * 0.50, rIn]);
  }
  let d = '';
  pts.forEach(([ang, r], i) => {
    const x = (cx + Math.cos(ang) * r).toFixed(2);
    const y = (cy + Math.sin(ang) * r).toFixed(2);
    d += (i === 0 ? 'M' : 'L') + x + ' ' + y + ' ';
  });
  return d + 'Z';
}

// ─── Edificios (2 torres con ventanas) ───────────────────────────
function buildings(fill, win) {
  return `
    <g>
      <rect x="62" y="64" width="17" height="44" rx="1.5" fill="${fill}"/>
      <rect x="81" y="76" width="14" height="32" rx="1.5" fill="${fill}"/>
      <g fill="${win}">
        <rect x="65.5" y="69" width="3.5" height="3.5"/><rect x="72" y="69" width="3.5" height="3.5"/>
        <rect x="65.5" y="77" width="3.5" height="3.5"/><rect x="72" y="77" width="3.5" height="3.5"/>
        <rect x="65.5" y="85" width="3.5" height="3.5"/><rect x="72" y="85" width="3.5" height="3.5"/>
        <rect x="65.5" y="93" width="3.5" height="3.5"/><rect x="72" y="93" width="3.5" height="3.5"/>
        <rect x="84" y="81" width="3" height="3"/><rect x="89.5" y="81" width="3" height="3"/>
        <rect x="84" y="88" width="3" height="3"/><rect x="89.5" y="88" width="3" height="3"/>
        <rect x="84" y="95" width="3" height="3"/><rect x="89.5" y="95" width="3" height="3"/>
      </g>
    </g>`;
}

// ─── Llave inglesa + destornillador cruzados ─────────────────────
function tools(wrenchFill, driverHandle, driverShaft) {
  return `
    <!-- Llave inglesa: cabeza abierta (anillo con boca) arriba-izq, mango abajo-der -->
    <g transform="translate(104 102) rotate(-42)" fill="${wrenchFill}">
      <rect x="-4.5" y="-2" width="9" height="40" rx="4.5"/>
      <path fill-rule="evenodd" d="
        M 0 -26 a 13 13 0 1 0 0.01 0 Z
        M 0 -19 a 6 6 0 1 1 -0.01 0 Z
        M -6 -30 L 6 -30 L 6 -19 L -6 -19 Z"/>
    </g>
    <!-- Destornillador: mango naranja abajo-izq, punta plana arriba-der -->
    <g transform="translate(96 104) rotate(42)">
      <rect x="-6" y="6" width="12" height="22" rx="6" fill="${driverHandle}"/>
      <rect x="-2.6" y="-16" width="5.2" height="24" fill="${driverShaft}"/>
      <rect x="-3.6" y="-20" width="7.2" height="5" rx="1" fill="${driverShaft}"/>
    </g>`;
}

// ─── Arco naranja (swoosh superior) ──────────────────────────────
function arc(cx, cy, r, w, a0, a1, fill) {
  const p = (ang, rr) => [(cx + Math.cos(ang) * rr).toFixed(2), (cy + Math.sin(ang) * rr).toFixed(2)];
  const rad = (d) => (d * Math.PI) / 180;
  const [x0, y0] = p(rad(a0), r), [x1, y1] = p(rad(a1), r);
  const [x2, y2] = p(rad(a1), r - w), [x3, y3] = p(rad(a0), r - w);
  const large = Math.abs(a1 - a0) > 180 ? 1 : 0;
  return `<path d="M ${x0} ${y0} A ${r} ${r} 0 ${large} 1 ${x1} ${y1} L ${x2} ${y2} A ${r - w} ${r - w} 0 ${large} 0 ${x3} ${y3} Z" fill="${fill}"/>`;
}

// ─── Onda/hoja azul de la base (solo versión A — fiel) ───────────
const wave = `<path d="M 36 126 q 64 26 128 0 q -20 22 -64 22 q -44 0 -64 -22 Z" fill="${C.blueD}" stroke="${C.white}" stroke-width="2"/>`;

// ─── Emblema ─────────────────────────────────────────────────────
function emblem(variant) {
  const flat = variant === 'B';
  const gearFill = flat ? C.metal : 'url(#gMetal)';
  const faceFill = C.white;
  const arcFill = flat ? C.orange : 'url(#gOrange)';
  const bFill = flat ? C.blue : 'url(#gBlue)';

  return `
  <g>
    ${flat ? '' : `
      <radialGradient id="gMetal" cx="40%" cy="30%" r="80%">
        <stop offset="0%" stop-color="${C.metalL}"/><stop offset="100%" stop-color="${C.metalD}"/>
      </radialGradient>
      <linearGradient id="gOrange" x1="0" y1="0" x2="1" y2="1">
        <stop offset="0%" stop-color="#FFB13D"/><stop offset="100%" stop-color="${C.orangeD}"/>
      </linearGradient>
      <linearGradient id="gBlue" x1="0" y1="0" x2="0" y2="1">
        <stop offset="0%" stop-color="${C.blueL}"/><stop offset="100%" stop-color="${C.blueD}"/>
      </linearGradient>`}

    <!-- Engranaje -->
    <path d="${gearPath(100, 100, 12, 98, 82)}" fill="${gearFill}"/>
    <circle cx="100" cy="100" r="80" fill="${flat ? C.metalD : '#1A2230'}"/>
    <!-- Cara -->
    <circle cx="100" cy="100" r="74" fill="${faceFill}"/>
    <!-- Arco naranja superior -->
    ${arc(100, 100, 72, 11, -42, 128, arcFill)}
    <!-- Onda azul (solo A) -->
    ${flat ? '' : `<clipPath id="face"><circle cx="100" cy="100" r="74"/></clipPath><g clip-path="url(#face)">${wave}</g>`}
    <!-- Edificios -->
    ${buildings(bFill, C.white)}
    <!-- Herramientas cruzadas -->
    ${tools(flat ? C.metal : C.metalL, C.orange, flat ? C.metalL : '#C9CCC4')}
  </g>`;
}

// ─── Wordmark (theme: 'light' = texto azul p/ fondo claro · 'dark' = texto claro p/ fondo oscuro) ──
function wordmark(x, y, theme = 'light') {
  const coiColor = theme === 'dark' ? '#3B8FD9' : C.blue;
  const tagColor = theme === 'dark' ? '#8A99AB' : C.metalL;
  return `
  <g font-family="Arial, 'Archivo', sans-serif">
    <text x="${x}" y="${y}" font-size="62" font-weight="800" letter-spacing="1">
      <tspan fill="${coiColor}">COICEM</tspan><tspan fill="${C.orange}" dx="6">SAS</tspan>
    </text>
    <line x1="${x + 2}" y1="${y + 14}" x2="${x + 470}" y2="${y + 14}" stroke="${tagColor}" stroke-width="1.5"/>
    <text x="${x + 3}" y="${y + 33}" font-size="18.5" font-weight="600" letter-spacing="2.45" fill="${tagColor}">SERVICIO MANTENIMIENTO ESPECIALIZADO</text>
  </g>`;
}

// ─── Documentos SVG ──────────────────────────────────────────────
function isotipoSVG(variant) {
  return `<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 200 200" width="200" height="200">${emblem(variant)}</svg>`;
}
function lockupSVG(variant, bg, theme = 'light') {
  return `<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 800 200" width="800" height="200">
    ${bg ? `<rect width="800" height="200" fill="${bg}"/>` : ''}
    <g transform="translate(0 4) scale(0.96)">${emblem(variant)}</g>
    ${wordmark(212, 110, theme)}
  </svg>`;
}
// OG 1200×630 — isotipo + wordmark centrados sobre fondo claro
function ogSVG(variant) {
  return `<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 1200 630" width="1200" height="630">
    <rect width="1200" height="630" fill="#FFFFFF"/>
    <rect x="0" y="0" width="1200" height="14" fill="${C.orange}"/>
    <g transform="translate(355 150) scale(1.6)">${emblem(variant)}</g>
    <g transform="translate(232 430) scale(0.92)">${wordmark(212, 60, 'light')}</g>
  </svg>`;
}

// ─── Render ──────────────────────────────────────────────────────
function png(svg, w) {
  const r = new Resvg(svg, { fitTo: { mode: 'width', value: w } });
  return r.render().asPng();
}

// ─── Comparativa A/B (ambas versiones, para que el cliente elija) ──
for (const v of ['A', 'B']) {
  writeFileSync(new URL(`./logo-${v}-isotipo.svg`, import.meta.url), isotipoSVG(v));
  writeFileSync(new URL(`./logo-${v}-lockup.svg`, import.meta.url), lockupSVG(v));
  writeFileSync(new URL(`./logo-${v}-isotipo.png`, import.meta.url), png(isotipoSVG(v), 512));
  writeFileSync(new URL(`./logo-${v}-lockup-light.png`, import.meta.url), png(lockupSVG(v, '#FFFFFF'), 1100));
  writeFileSync(new URL(`./logo-${v}-lockup-dark.png`, import.meta.url), png(lockupSVG(v, '#0B0E14', 'dark'), 1100));
  console.log(`✓ Versión ${v} generada (isotipo + lockup claro/oscuro)`);
}

// ─── PAQUETE DE MARCA — versión elegida: B (flat) ─────────────────
const CHOSEN = 'B';
const out = (name) => new URL(`./paquete-${name}`, import.meta.url);

// Isotipo (transparente) — favicon/app/sello
writeFileSync(out('isotipo.svg'), isotipoSVG(CHOSEN));
writeFileSync(out('isotipo-512.png'), png(isotipoSVG(CHOSEN), 512));
writeFileSync(out('favicon-180.png'), png(isotipoSVG(CHOSEN), 180));
writeFileSync(out('favicon-32.png'), png(isotipoSVG(CHOSEN), 32));

// Lockup horizontal (transparente) — claro y oscuro
writeFileSync(out('lockup-claro.svg'), lockupSVG(CHOSEN, null, 'light'));
writeFileSync(out('lockup-oscuro.svg'), lockupSVG(CHOSEN, null, 'dark'));
writeFileSync(out('lockup-claro.png'), png(lockupSVG(CHOSEN, null, 'light'), 1600));
writeFileSync(out('lockup-oscuro.png'), png(lockupSVG(CHOSEN, null, 'dark'), 1600));

// OG 1200×630
writeFileSync(out('og-image.png'), png(ogSVG(CHOSEN), 1200));

console.log('✓ Paquete de marca B generado (isotipo, favicons, lockups, OG)');

// ─── Reemplazo del logo en el sitio (JPEG recortado → vector limpio) ──
// El sitio es oscuro → usar el lockup "para fondo oscuro".
const siteLogo = new URL('../coicem-web/public/images/coicem-logo.png', import.meta.url);
writeFileSync(siteLogo, png(lockupSVG(CHOSEN, null, 'dark'), 1100));
const siteFav = new URL('../coicem-web/public/favicon.png', import.meta.url);
writeFileSync(siteFav, png(isotipoSVG(CHOSEN), 256));
console.log('✓ Logo del sitio reemplazado por reconstrucción B (navbar/footer/favicon)');

// Comparativa lado a lado A vs B (sobre claro y oscuro)
function compare(bg, label) {
  return `<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 900 520" width="900" height="520">
    <rect width="900" height="520" fill="${bg}"/>
    <text x="40" y="50" font-family="Arial" font-size="26" font-weight="800" fill="${bg === '#FFFFFF' ? '#0B0E14' : '#FFFFFF'}">RECONSTRUCCIÓN LOGO COICEM — ${label}</text>
    <text x="40" y="110" font-family="Arial" font-size="20" font-weight="700" fill="${C.orange}">VERSIÓN A — Fiel</text>
    <g transform="translate(40 130) scale(0.55)">${emblem('A')}</g>
    <g transform="translate(250 175) scale(0.42)">${emblem('A')}</g>
    <text x="40" y="330" font-family="Arial" font-size="20" font-weight="700" fill="${C.orange}">VERSIÓN B — Mejorada (flat)</text>
    <g transform="translate(40 350) scale(0.55)">${emblem('B')}</g>
    <g transform="translate(250 395) scale(0.42)">${emblem('B')}</g>
    <text x="470" y="160" font-family="Arial" font-size="15" fill="${bg === '#FFFFFF' ? '#444' : '#AAA'}">Conserva engranaje metálico,</text>
    <text x="470" y="182" font-family="Arial" font-size="15" fill="${bg === '#FFFFFF' ? '#444' : '#AAA'}">onda azul y degradados — limpios.</text>
    <text x="470" y="380" font-family="Arial" font-size="15" fill="${bg === '#FFFFFF' ? '#444' : '#AAA'}">Plano, alto contraste, escala a</text>
    <text x="470" y="402" font-family="Arial" font-size="15" fill="${bg === '#FFFFFF' ? '#444' : '#AAA'}">favicon. Sin bevels 3D ni ruido.</text>
  </svg>`;
}
writeFileSync(new URL('./compare-AB-light.png', import.meta.url), png(compare('#FFFFFF', 'sobre claro'), 1100));
writeFileSync(new URL('./compare-AB-dark.png', import.meta.url), png(compare('#0B0E14', 'sobre oscuro'), 1100));
console.log('✓ Comparativas A/B generadas');
