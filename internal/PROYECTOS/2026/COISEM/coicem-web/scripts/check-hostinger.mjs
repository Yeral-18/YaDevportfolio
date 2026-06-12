#!/usr/bin/env node
/**
 * check-hostinger.mjs — Validador de las reglas no-obvias de Hostinger.
 * Convierte la checklist mental del CLAUDE.md en un gate automático.
 * Uso:  node scripts/check-hostinger.mjs
 * Falla (exit 1) si alguna regla crítica no se cumple.
 */
import { readFileSync, existsSync, readdirSync, statSync } from 'node:fs';
import { join, extname } from 'node:path';

const ROOT = process.cwd();
let errors = 0;
let warnings = 0;

const fail = (msg) => { console.error(`  ✗ ${msg}`); errors++; };
const warn = (msg) => { console.warn(`  ⚠ ${msg}`); warnings++; };
const ok   = (msg) => { console.log(`  ✓ ${msg}`); };
const read = (p) => existsSync(p) ? readFileSync(p, 'utf8') : null;

console.log('\n── Validación Hostinger ──────────────────────\n');

// 1. astro.config.mjs → build.assets = 'assets'
const astroCfg = read(join(ROOT, 'astro.config.mjs'));
if (!astroCfg) {
  warn('No se encontró astro.config.mjs (¿estás en la raíz del proyecto?)');
} else if (/assets\s*:\s*['"]assets['"]/.test(astroCfg)) {
  ok("astro.config.mjs usa build.assets: 'assets' (no _astro/)");
} else {
  fail("astro.config.mjs NO define build.assets:'assets' → Hostinger bloqueará el CSS");
}

// 2. fileURLToPath fix (si la ruta tiene & o espacios)
if (astroCfg && /[&\s]/.test(ROOT)) {
  if (/fileURLToPath/.test(astroCfg)) ok('Ruta con & o espacio + fileURLToPath presente');
  else fail('Ruta con & o espacio pero falta fileURLToPath → Vite no resolverá Tailwind');
}

// 3. .htaccess sin CSP, con MIME types
const htaccess = read(join(ROOT, 'public', '.htaccess')) || read(join(ROOT, 'dist', '.htaccess'));
if (!htaccess) {
  warn('No se encontró .htaccess en public/ ni dist/');
} else {
  // Ignorar comentarios Apache (líneas que empiezan con #); solo una directiva REAL bloquea.
  const htaccessCode = htaccess.split('\n').filter((l) => !/^\s*#/.test(l)).join('\n');
  if (/Header\s+(always\s+set|set|add|append)\s+["']?Content-Security-Policy/i.test(htaccessCode))
    fail('.htaccess define un header Content-Security-Policy → bloqueará Google Fonts/CSS. Quitarlo.');
  else ok('.htaccess sin header Content-Security-Policy');
  if (/AddType\s+text\/css\s+\.css/i.test(htaccessCode)) ok('.htaccess declara MIME text/css');
  else fail('.htaccess sin "AddType text/css .css" → Hostinger puede servir CSS como text/plain');
}

// 4. contact.php usa mail(), no SMTP
const contactPhp = read(join(ROOT, 'public', 'contact.php')) || read(join(ROOT, 'dist', 'contact.php'));
if (contactPhp) {
  // Quitar comentarios PHP (/* */, //, # al inicio) para no castigar la documentación
  // del boilerplate ("PHP mail() nativo — NO SMTP (puerto 587 bloqueado)").
  const phpCode = contactPhp
    .replace(/\/\*[\s\S]*?\*\//g, '')         // bloques /* ... */
    .replace(/(^|[^:])\/\/.*$/gm, '$1')        // líneas // (sin romper https://)
    .replace(/^\s*#.*$/gm, '');                // líneas # al inicio
  const usesMail = /\bmail\s*\(/.test(phpCode);
  // USO real de SMTP: isSMTP(), new PHPMailer, fsockopen a 587/465, Port = 587/465.
  const usesSmtp = /->\s*isSMTP\s*\(|new\s+PHPMailer|fsockopen\s*\([^)]*\b(?:587|465)\b|Port\s*=\s*['"]?(?:587|465)\b/i.test(phpCode);
  if (usesMail && !usesSmtp) ok('contact.php usa mail() nativo (sin SMTP)');
  else if (usesSmtp) fail('contact.php usa SMTP → puerto bloqueado en Hostinger. Usar mail().');
  else warn('contact.php no contiene mail() — verificar manualmente');
} else {
  warn('No se encontró contact.php');
}

// 5. Logo PNG (no SVG) en navbar — heurística sobre dist/build
const publicDir = existsSync(join(ROOT, 'public')) ? join(ROOT, 'public') : null;
if (publicDir) {
  const files = walk(publicDir);
  const hasLogoPng = files.some(f => /logo.*\.png$/i.test(f));
  const hasLogoSvg = files.some(f => /logo.*\.svg$/i.test(f));
  if (hasLogoPng) ok('Existe logo .png');
  else if (hasLogoSvg) warn('Solo hay logo .svg → OG de WhatsApp no lo renderiza. Generar PNG.');
  else warn('No se detectó archivo de logo');
}

// 6/7. Imágenes pesadas (>100KB) y logos pequeños — aviso
if (publicDir) {
  const imgs = walk(publicDir).filter(f => /\.(jpg|jpeg|png|webp)$/i.test(f));
  const heavy = imgs.filter(f => statSync(f).size > 100 * 1024 && !/og|hero/i.test(f));
  if (heavy.length) warn(`${heavy.length} imagen(es) >100KB (excl. hero/og): ${heavy.slice(0,3).map(f=>f.replace(ROOT,'.')).join(', ')}${heavy.length>3?'…':''}`);
  else ok('Ninguna imagen de contenido supera 100KB');
}

// 8. reCAPTCHA test key de Google (clave pública de prueba — NUNCA en producción)
// Detectada en Luqra (P1-E6) y pendiente en Multiservicios.
const GOOGLE_TEST_KEY = '6LeIxAcTAAAAA'; // prefijo de las claves de prueba oficiales
const searchDirs = ['src', 'public', 'dist'].map(d => join(ROOT, d)).filter(existsSync);
let testKeyHits = [];
for (const dir of searchDirs) {
  for (const f of walk(dir)) {
    if (!/\.(astro|svelte|html|js|mjs|ts|php)$/i.test(f)) continue;
    const content = read(f);
    if (content && content.includes(GOOGLE_TEST_KEY)) testKeyHits.push(f.replace(ROOT, '.'));
  }
}
if (testKeyHits.length) fail(`reCAPTCHA TEST KEY de Google detectada (no protege nada) en: ${testKeyHits.join(', ')} → generar clave real en google.com/recaptcha`);
else ok('Sin reCAPTCHA test key');

// 9. Strings TODO / placeholder en el build final (bloqueadores tipo B1-B4 de Luqra)
// TODO y PLACEHOLDER solo en MAYÚSCULAS exactas (\b...\b, SIN flag i): así no matchea
// la palabra española "todo/todos/método". Lorem ipsum y "+57 XXX" se mantienen.
// Se excluye internal/ (bloqueado en robots.txt + tokens de plantilla en los generadores).
const PLACEHOLDER_RE = /\bTODO\b|\bPLACEHOLDER\b|\+57\s*XXX|[Ll]orem [Ii]psum/g;
const distDir = join(ROOT, 'dist');
if (existsSync(distDir)) {
  let todoHits = [];
  for (const f of walk(distDir)) {
    if (!/\.(html|php|xml|txt|json)$/i.test(f)) continue;
    // Excluir SOLO dist/internal/ (panel YaDev, no indexable). Se prueba la ruta
    // RELATIVA a ROOT: el propio monorepo vive bajo .../internal/PROYECTOS/..., así
    // que probar el path absoluto excluiría TODO. (bug encontrado en proyecto real)
    if (/[\\/]internal[\\/]/i.test(f.replace(ROOT, ''))) continue;
    const content = read(f);
    if (!content) continue;
    const m = content.match(PLACEHOLDER_RE);
    if (m) todoHits.push(`${f.replace(ROOT, '.')} (${[...new Set(m)].join(', ')})`);
  }
  if (todoHits.length) {
    fail(`Placeholders en el build (Google los indexaría):`);
    todoHits.slice(0, 6).forEach(h => console.error(`      ${h}`));
    if (todoHits.length > 6) console.error(`      … y ${todoHits.length - 6} más`);
  } else ok('dist/ sin TODOs ni placeholders');
} else {
  warn('No existe dist/ — correr npm run build antes de validar placeholders');
}

// Resumen
console.log('\n──────────────────────────────────────────────');
console.log(`  ${errors} error(es), ${warnings} advertencia(s)\n`);
if (errors > 0) {
  console.error('❌ DEPLOY BLOQUEADO — corregir errores antes de subir a Hostinger.\n');
  process.exit(1);
} else {
  console.log('✅ Reglas críticas Hostinger OK.\n');
}

function walk(dir) {
  const out = [];
  for (const entry of readdirSync(dir)) {
    const p = join(dir, entry);
    const s = statSync(p);
    if (s.isDirectory()) out.push(...walk(p));
    else out.push(p);
  }
  return out;
}
