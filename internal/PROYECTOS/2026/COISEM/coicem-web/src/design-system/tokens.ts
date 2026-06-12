/**
 * ══════════════════════════════════════════════════════════════════
 * COICEM S.A.S — Design Tokens
 * ADN: Brutalist · Editorial/columnas · Tipográfico · Sidebar · Datos/autoridad
 * ══════════════════════════════════════════════════════════════════
 *
 * ⚠️ PALETA PROVISIONAL v1 — extraída pixel a pixel del LOGO JPEG de WhatsApp
 *    (PIL, no de memoria). PERO WhatsApp recomprime y altera el color sutilmente.
 *    → Cuando llegue el logo ORIGINAL (.ai/.svg/.pdf, ver site-config.pending.logoVector),
 *      RE-EXTRAER estos hex y actualizar este archivo + tailwind.config.mjs + brandbook.
 *
 *    Verificado: el fondo del logo es #000000 puro. El "#000E27" extraído NO es color
 *    de marca (es sombra/gradiente del logo) → la base oscura es una decisión de diseño
 *    (grafito/negro brutalista), no un token de marca.
 *
 * Tipografía: Archivo Expanded (display, señalética industrial) + IBM Plex Sans (body)
 *             + IBM Plex Mono (specs/part-numbers). NO Inter.
 * Motion:     easeInOutQuint cubic-bezier(0.83,0,0.17,1) — snap maquinado, SIN rebote.
 * ══════════════════════════════════════════════════════════════════
 */

export const colors = {
  // PRIMARY — Azul de marca (wordmark "COICEM"). Estructural, autoridad. ~80%.
  primary: {
    50:  '#E8F1FA',
    100: '#C5DDF2',
    200: '#8EB9DC',  // tint extraído del logo
    300: '#4E90C8',
    400: '#1A6FB0',
    500: '#025199',  // ★ azul primario extraído
    600: '#023F7E',  // extraído (gradiente medio)
    700: '#003069',  // extraído
    800: '#002657',  // extraído (oscuro)
    900: '#001A3C',
    950: '#000E27',  // sombra del logo (NO marca pura) — útil como tinta profunda
    DEFAULT: '#025199',
  },

  // ACCENT / CTA — Naranja hi-vis (wordmark "SAS" + destornillador). ~10%, seguridad.
  accent: {
    50:  '#FFF4E3',
    100: '#FFE2B8',
    200: '#FFC97A',
    300: '#FFA222',  // naranja claro extraído
    400: '#F79204',  // ★ naranja primario extraído
    500: '#F79204',
    600: '#E38325',  // ámbar/arco extraído
    700: '#B36400',
    800: '#8A4D00',
    900: '#5E3400',
    DEFAULT: '#F79204',
  },

  // CTA = el naranja de seguridad (conversión, hi-vis).
  cta: { DEFAULT: '#F79204', hover: '#DB7E00' },

  // METAL / GRAFITO — engranaje del logo + superficies brutalistas oscuras.
  metal: {
    light: '#4B6881',  // metal claro extraído
    DEFAULT: '#313F50', // metal oscuro extraído
    panel:  '#161B22',  // panel/bloque brutalista
    base:   '#0B0E14',  // base grafito (decisión de diseño)
    black:  '#000000',  // fondo del logo — el negro ES on-brand
  },

  // NEUTRALS
  dark:    '#0B0E14',   // base oscura (texto sobre claro / fondo dark)
  light:   '#EDEDE8',   // off-white concreto (brutalist, no blanco puro)
  surface: '#FFFFFF',
  highlight:'#F6FCFD',  // blancos del logo (edificios/llave)
} as const;

export const typography = {
  fonts: {
    // Archivo no tiene "Expanded" en Google Fonts directo → usar 'Archivo' con
    // font-stretch:expanded / variación, o 'Archivo Expanded' si se autohospeda.
    display: "'Archivo Expanded', 'Archivo', system-ui, sans-serif",
    body:    "'IBM Plex Sans', system-ui, sans-serif",
    mono:    "'IBM Plex Mono', ui-monospace, monospace",
  },
  weights: { regular: '400', medium: '500', semibold: '600', bold: '700', black: '900' },
  tracking: { tight: '-0.02em', normal: '0em', wide: '0.04em', widest: '0.12em' },
} as const;

export const motion = {
  easing: {
    // ★ Firma de COICEM — sin rebote, snap maquinado (NO el spring 0.34,1.3 saturado).
    quint:  'cubic-bezier(0.83, 0, 0.17, 1)',  // easeInOutQuint
    out:    'cubic-bezier(0.16, 1, 0.3, 1)',   // easeOutExpo — reveals
    sharp:  'cubic-bezier(0.4, 0, 0.2, 1)',
  },
  duration: { fast: '160ms', normal: '320ms', slow: '560ms' },
} as const;

// BRUTALIST — bordes duros. Radio mínimo o cero; sin sombras blandas.
export const borderRadius = {
  none: '0px', sm: '2px', DEFAULT: '0px', md: '0px', lg: '0px', full: '9999px',
} as const;

export const breakpoints = {
  sm: '640px', md: '768px', lg: '1024px', xl: '1280px', '2xl': '1536px',
} as const;

export type ColorName = keyof typeof colors;
