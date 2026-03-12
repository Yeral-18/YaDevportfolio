/**
 * ECOMAG S.A.S — Design Tokens
 * Sistema de diseño centralizado inspirado en Apple, Linear, Vercel
 *
 * Uso: Importar tokens en componentes para mantener consistencia
 */

// ═══════════════════════════════════════════════════════════════
// COLORS
// ═══════════════════════════════════════════════════════════════

export const colors = {
  // Primary — Verde corporativo
  primary: {
    50:  '#e8f5e9',
    100: '#c8e6c9',
    200: '#a5d6a7',
    300: '#81c784',
    400: '#66bb6a',
    500: '#1B5E20', // DEFAULT
    600: '#165a1c',
    700: '#114d16',
    800: '#0d3f11',
    900: '#08310c',
  },

  // Secondary — Azul profesional
  secondary: {
    50:  '#e0f2f7',
    100: '#b3e0ed',
    200: '#80cde2',
    300: '#4db9d6',
    400: '#26aacd',
    500: '#0277A8', // DEFAULT
    600: '#026a97',
    700: '#015a80',
    800: '#014a6a',
    900: '#003a54',
  },

  // Accent — Verde lima
  accent: {
    50:  '#f1f8e9',
    100: '#dcedc8',
    200: '#c5e1a5',
    300: '#aed581',
    400: '#9ccc65',
    500: '#7CB342', // DEFAULT
    600: '#6fa53b',
    700: '#5e9231',
    800: '#4e7f28',
    900: '#3e6c1f',
  },

  // CTA — Naranja energético
  cta: {
    DEFAULT: '#E65100',
    hover: '#d84a00',
    active: '#c44300',
  },

  // Neutrals
  dark: '#1a1a2e',
  light: '#F5F7F2',
  surface: '#FFFFFF',

  // Grays (para texto y bordes)
  gray: {
    50:  '#f9fafb',
    100: '#f3f4f6',
    200: '#e5e7eb',
    300: '#d1d5db',
    400: '#9ca3af',
    500: '#6b7280',
    600: '#4b5563',
    700: '#374151',
    800: '#1f2937',
    900: '#111827',
  },
} as const;

// ═══════════════════════════════════════════════════════════════
// SPACING — Sistema 4px base
// ═══════════════════════════════════════════════════════════════

export const spacing = {
  px: '1px',
  0:   '0',
  0.5: '0.125rem',  // 2px
  1:   '0.25rem',   // 4px
  1.5: '0.375rem',  // 6px
  2:   '0.5rem',    // 8px
  2.5: '0.625rem',  // 10px
  3:   '0.75rem',   // 12px
  4:   '1rem',      // 16px
  5:   '1.25rem',   // 20px
  6:   '1.5rem',    // 24px
  8:   '2rem',      // 32px
  10:  '2.5rem',    // 40px
  12:  '3rem',      // 48px
  16:  '4rem',      // 64px
  20:  '5rem',      // 80px
  24:  '6rem',      // 96px
} as const;

// ═══════════════════════════════════════════════════════════════
// BORDER RADIUS — Escala consistente
// ═══════════════════════════════════════════════════════════════

export const radius = {
  none: '0',
  sm:   '0.25rem',   // 4px — inputs pequeños
  DEFAULT: '0.5rem', // 8px — botones, inputs
  md:   '0.625rem',  // 10px
  lg:   '0.75rem',   // 12px — cards pequeñas
  xl:   '1rem',      // 16px — cards medianas
  '2xl': '1.25rem',  // 20px — cards grandes
  '3xl': '1.5rem',   // 24px — modals
  full: '9999px',    // pills, badges
} as const;

// ═══════════════════════════════════════════════════════════════
// SHADOWS — Estilo Apple/Linear (suaves y elegantes)
// ═══════════════════════════════════════════════════════════════

export const shadows = {
  // Sombras sutiles para elevación
  xs:   '0 1px 2px 0 rgb(0 0 0 / 0.03)',
  sm:   '0 1px 3px 0 rgb(0 0 0 / 0.05), 0 1px 2px -1px rgb(0 0 0 / 0.05)',
  DEFAULT: '0 4px 6px -1px rgb(0 0 0 / 0.07), 0 2px 4px -2px rgb(0 0 0 / 0.05)',
  md:   '0 6px 12px -2px rgb(0 0 0 / 0.08), 0 3px 6px -3px rgb(0 0 0 / 0.05)',
  lg:   '0 10px 25px -3px rgb(0 0 0 / 0.08), 0 4px 10px -4px rgb(0 0 0 / 0.04)',
  xl:   '0 20px 40px -5px rgb(0 0 0 / 0.1), 0 8px 16px -6px rgb(0 0 0 / 0.05)',
  '2xl': '0 25px 50px -12px rgb(0 0 0 / 0.15)',

  // Sombras con color (para hovers)
  primary: '0 8px 24px -4px rgb(27 94 32 / 0.2)',
  accent:  '0 8px 24px -4px rgb(124 179 66 / 0.25)',
  cta:     '0 8px 24px -4px rgb(230 81 0 / 0.3)',

  // Inner shadow para inputs focus
  inner: 'inset 0 1px 2px rgb(0 0 0 / 0.05)',

  none: 'none',
} as const;

// ═══════════════════════════════════════════════════════════════
// TYPOGRAPHY
// ═══════════════════════════════════════════════════════════════

export const typography = {
  fonts: {
    display: "'Plus Jakarta Sans', system-ui, sans-serif",
    body: "'Inter', system-ui, sans-serif",
  },

  // Tamaños con line-height incluido
  sizes: {
    xs:   { size: '0.75rem',   lineHeight: '1rem' },      // 12px
    sm:   { size: '0.875rem',  lineHeight: '1.25rem' },   // 14px
    base: { size: '1rem',      lineHeight: '1.5rem' },    // 16px
    lg:   { size: '1.125rem',  lineHeight: '1.75rem' },   // 18px
    xl:   { size: '1.25rem',   lineHeight: '1.75rem' },   // 20px
    '2xl': { size: '1.5rem',   lineHeight: '2rem' },      // 24px
    '3xl': { size: '1.875rem', lineHeight: '2.25rem' },   // 30px
    '4xl': { size: '2.25rem',  lineHeight: '2.5rem' },    // 36px
    '5xl': { size: '3rem',     lineHeight: '1.1' },       // 48px
    '6xl': { size: '3.75rem',  lineHeight: '1.05' },      // 60px
  },

  weights: {
    normal:   '400',
    medium:   '500',
    semibold: '600',
    bold:     '700',
    extrabold: '800',
  },

  letterSpacing: {
    tighter: '-0.05em',
    tight:   '-0.025em',
    normal:  '0',
    wide:    '0.025em',
    wider:   '0.05em',
    widest:  '0.1em',
  },
} as const;

// ═══════════════════════════════════════════════════════════════
// MOTION — Transiciones y animaciones (estilo Linear/Vercel)
// ═══════════════════════════════════════════════════════════════

export const motion = {
  // Duraciones
  duration: {
    instant: '50ms',
    fast:    '150ms',
    normal:  '250ms',
    slow:    '400ms',
    slower:  '600ms',
  },

  // Easings premium (sutiles, no bouncy)
  easing: {
    // Estándar — para la mayoría de transiciones
    default: 'cubic-bezier(0.4, 0, 0.2, 1)',

    // Entrada — elementos que aparecen
    easeOut: 'cubic-bezier(0, 0, 0.2, 1)',

    // Salida — elementos que desaparecen
    easeIn: 'cubic-bezier(0.4, 0, 1, 1)',

    // Spring sutil — para hovers (NO exagerado)
    spring: 'cubic-bezier(0.34, 1.3, 0.64, 1)',

    // Smooth — para transforms suaves
    smooth: 'cubic-bezier(0.25, 0.46, 0.45, 0.94)',
  },

  // Transiciones predefinidas
  transitions: {
    // Para colores y opacidad
    colors: 'color 150ms ease, background-color 150ms ease, border-color 150ms ease',

    // Para transforms (hover scale, translate)
    transform: 'transform 250ms cubic-bezier(0.4, 0, 0.2, 1)',

    // Para sombras
    shadow: 'box-shadow 250ms cubic-bezier(0.4, 0, 0.2, 1)',

    // Combo para cards/botones
    interactive: 'transform 250ms cubic-bezier(0.34, 1.3, 0.64, 1), box-shadow 250ms ease, opacity 200ms ease',

    // Para elementos que aparecen (scroll reveal)
    reveal: 'opacity 500ms cubic-bezier(0, 0, 0.2, 1), transform 500ms cubic-bezier(0, 0, 0.2, 1)',
  },
} as const;

// ═══════════════════════════════════════════════════════════════
// HOVER STATES — Valores consistentes
// ═══════════════════════════════════════════════════════════════

export const hover = {
  // Scale sutil (NO exagerado)
  scale: {
    subtle: 1.01,    // Para cards grandes
    default: 1.02,   // Para cards medianas
    button: 1.03,    // Para botones
  },

  // Translate vertical
  lift: {
    subtle: '-2px',
    default: '-4px',
    elevated: '-6px',
  },

  // Opacidad para overlays
  overlay: {
    light: 0.05,
    medium: 0.1,
    strong: 0.15,
  },
} as const;

// ═══════════════════════════════════════════════════════════════
// Z-INDEX — Escala ordenada
// ═══════════════════════════════════════════════════════════════

export const zIndex = {
  behind: -1,
  base: 0,
  dropdown: 10,
  sticky: 20,
  fixed: 30,
  modalBackdrop: 40,
  modal: 50,
  popover: 60,
  tooltip: 70,
  toast: 80,
  max: 9999,
} as const;

// ═══════════════════════════════════════════════════════════════
// BREAKPOINTS
// ═══════════════════════════════════════════════════════════════

export const breakpoints = {
  sm: '640px',
  md: '768px',
  lg: '1024px',
  xl: '1280px',
  '2xl': '1536px',
} as const;

// ═══════════════════════════════════════════════════════════════
// CSS CUSTOM PROPERTIES (para usar en CSS)
// ═══════════════════════════════════════════════════════════════

export const cssVariables = `
  :root {
    /* Colors */
    --color-primary: ${colors.primary[500]};
    --color-primary-light: ${colors.primary[100]};
    --color-secondary: ${colors.secondary[500]};
    --color-accent: ${colors.accent[500]};
    --color-cta: ${colors.cta.DEFAULT};
    --color-dark: ${colors.dark};
    --color-light: ${colors.light};

    /* Typography */
    --font-display: ${typography.fonts.display};
    --font-body: ${typography.fonts.body};

    /* Shadows */
    --shadow-sm: ${shadows.sm};
    --shadow-md: ${shadows.md};
    --shadow-lg: ${shadows.lg};
    --shadow-primary: ${shadows.primary};

    /* Motion */
    --ease-default: ${motion.easing.default};
    --ease-spring: ${motion.easing.spring};
    --duration-fast: ${motion.duration.fast};
    --duration-normal: ${motion.duration.normal};
  }
`;
