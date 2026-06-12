#!/usr/bin/env node
/**
 * check-dna.mjs — Verificación programática de colisión de ADN visual.
 * Parsea la TABLA MAESTRA de .claude/PROJECT_DNA_LOG.md y valida que la
 * combinación propuesta no repita tripletas ni use ejes saturados.
 *
 * Uso:
 *   node scripts/check-dna.mjs --director "Apple" --composicion "Editorial" \
 *     --movimiento "Cinemático" --navegacion "Sidebar" [--easing "0.34,1.3"] [--body-font "Inter"]
 *
 * Salidas (exit codes):
 *   0  OK         — combinación válida
 *   1  COLISIÓN   — tripleta Director+Composición+Movimiento ya usada
 *   2  SATURADO   — eje secundario saturado (navegación/easing/tipografía)
 *   3  ERROR      — log no encontrado o argumentos inválidos
 */
import { readFileSync, existsSync } from 'node:fs';
import { join } from 'node:path';

// ── Argumentos ──────────────────────────────────────────────
const args = {};
const argv = process.argv.slice(2);
for (let i = 0; i < argv.length; i += 2) {
  if (argv[i]?.startsWith('--')) args[argv[i].slice(2)] = argv[i + 1] ?? '';
}

const required = ['director', 'composicion', 'movimiento'];
const missing = required.filter((k) => !args[k]);
if (missing.length) {
  console.error(`ERROR: faltan argumentos: ${missing.map((m) => '--' + m).join(', ')}`);
  console.error('Uso: node scripts/check-dna.mjs --director X --composicion Y --movimiento Z [--navegacion W] [--easing E] [--body-font F]');
  process.exit(3);
}

// ── Localizar el log ────────────────────────────────────────
const candidates = [
  join(process.cwd(), '.claude', 'PROJECT_DNA_LOG.md'),
  join(process.cwd(), 'PROJECT_DNA_LOG.md'),
  join(process.cwd(), '..', '.claude', 'PROJECT_DNA_LOG.md'),
];
const logPath = candidates.find((p) => existsSync(p));
if (!logPath) {
  console.error('ERROR: no se encontró PROJECT_DNA_LOG.md (buscado en .claude/ y raíz)');
  process.exit(3);
}
const log = readFileSync(logPath, 'utf8');

// ── Parsear la TABLA MAESTRA ────────────────────────────────
// Busca la sección "TABLA MAESTRA" y extrae filas markdown de la tabla.
const norm = (s) =>
  s.toLowerCase()
    .normalize('NFD').replace(/[\u0300-\u036f]/g, '') // sin tildes
    .replace(/\*\*/g, '').replace(/\s+/g, ' ').trim();

const section = log.split(/##\s+TABLA MAESTRA/i)[1]?.split(/\n##\s/)[0] ?? '';
const rows = section
  .split('\n')
  .filter((l) => l.trim().startsWith('|') && !/^\|[-\s|]+\|$/.test(l.trim()))
  .map((l) => l.split('|').map((c) => norm(c)).filter(Boolean))
  .filter((cells) => cells.length >= 6 && cells[0] !== 'cliente'); // salta header

if (!rows.length) {
  console.error('ERROR: no pude parsear filas de la TABLA MAESTRA en el log.');
  process.exit(3);
}

// ── Matcher difuso: la celda contiene la palabra clave ──────
// "split-screen 55/45" debe matchear propuesta "Split-screen".
const matches = (cell, proposal) => {
  const c = norm(cell);
  const p = norm(proposal);
  if (!p) return false;
  return c.includes(p) || p.includes(c.split(' ')[0]) || c.split(/[\s/(]/)[0] === p.split(/[\s/(]/)[0];
};

// ── 1. Verificar colisión de tripleta ───────────────────────
console.log(`\n── check-dna · log: ${logPath.replace(process.cwd(), '.')} ──\n`);
console.log(`Propuesta: ${args.director} + ${args.composicion} + ${args.movimiento}` +
  (args.navegacion ? ` · nav: ${args.navegacion}` : '') + '\n');

let collision = null;
for (const cells of rows) {
  const [cliente, director, composicion, movimiento] = cells;
  if (
    matches(director, args.director) &&
    matches(composicion, args.composicion) &&
    matches(movimiento, args.movimiento)
  ) {
    collision = cliente;
    break;
  }
}

if (collision) {
  console.error(`✗ COLISIÓN: la tripleta ya la usa "${collision}".`);
  console.error('  → Regenerar: cambia al menos UNO de los 3 ejes principales.\n');
  process.exit(1);
}
console.log('✓ Tripleta única — no colisiona con ningún proyecto del log.');

// ── 2. Verificar saturación de ejes secundarios ─────────────
// Cuenta usos en la tabla; umbral: si el valor propuesto ya aparece en
// TODOS los proyectos existentes (o ≥3 veces), está saturado.
let saturated = [];
const countAxis = (idx, proposal) =>
  rows.filter((cells) => matches(cells[idx] ?? '', proposal)).length;

if (args.navegacion) {
  const n = countAxis(4, args.navegacion); // col 4 = Navegación
  if (n >= 3 || (rows.length >= 2 && n === rows.length)) {
    saturated.push(`Navegación "${args.navegacion}" usada ${n}× — elegir otra (floating pill, sidebar, overlay, dock…)`);
  } else {
    console.log(`✓ Navegación "${args.navegacion}" — ${n} uso(s) previo(s), aceptable.`);
  }
}

// Saturaciones declaradas en el texto del log (sección RESERVA / warnings 🔴)
const declared = log.match(/🔴[^\n]*/g) ?? [];
for (const d of declared) {
  const dn = norm(d);
  for (const [key, val] of Object.entries(args)) {
    if (val && dn.includes(norm(val)) && !saturated.some((s) => s.includes(val))) {
      saturated.push(`El log marca saturado: "${d.trim()}" y tu propuesta usa "${val}" (--${key}).`);
    }
  }
}

if (args.easing && /0\.34\s*,\s*1\.3/.test(args.easing)) {
  saturated.push('Easing spring cubic-bezier(0.34,1.3,…) ya usado en los 3 proyectos — variar la curva.');
}
if (args['body-font'] && norm(args['body-font']) === 'inter' && rows.length >= 3) {
  saturated.push('Tipografía body "Inter" usada en los 3 proyectos — considerar variar (no bloqueante si es decisión de marca).');
}

if (saturated.length) {
  console.error('\n✗ SATURADO:');
  saturated.forEach((s) => console.error(`  • ${s}`));
  console.error('');
  process.exit(2);
}

console.log('\n✅ OK — combinación válida. Registrar en PROJECT_DNA_LOG.md antes de codear.\n');
process.exit(0);
