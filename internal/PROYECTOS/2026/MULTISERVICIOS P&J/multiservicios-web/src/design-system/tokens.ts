/**
 * MULTISERVICIOS P&J S.A.S — Design Tokens
 * Corporate Identity: Azul Institucional / Verde Ambiental / Azul CTA
 */

export const colors = {
  primary: {
    50:  '#e6f4fb',
    100: '#b3ddf3',
    200: '#8AD7F8',
    300: '#4db8e8',
    400: '#1aa3de',
    500: '#0089D0',
    600: '#0077B5',
    700: '#006BA3',
    800: '#005588',
    900: '#003F66',
    950: '#002D4D',
  },
  secondary: {
    50:  '#e6f0eb',
    100: '#b3d4c3',
    200: '#80b89b',
    300: '#4d9c73',
    400: '#007A45',
    500: '#005B32',
    600: '#004F2C',
    700: '#003D22',
    800: '#002E19',
    900: '#001F11',
  },
  accent: {
    50:  '#f4fae8',
    100: '#dff0be',
    200: '#c9e694',
    300: '#A8D86A',
    400: '#8CC63F',
    500: '#8CC63F',
    600: '#7AB535',
    700: '#6BA32E',
    800: '#5A8F26',
    900: '#3F6A1A',
  },
  cta: {
    DEFAULT: '#0089D0',
    hover: '#006BA3',
    active: '#005588',
  },
  dark: '#1a1a2e',
  light: '#F5F7FA',
  surface: '#FFFFFF',
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

export const spacing = {
  px: '1px',
  0:   '0',
  0.5: '0.125rem',
  1:   '0.25rem',
  1.5: '0.375rem',
  2:   '0.5rem',
  2.5: '0.625rem',
  3:   '0.75rem',
  4:   '1rem',
  5:   '1.25rem',
  6:   '1.5rem',
  8:   '2rem',
  10:  '2.5rem',
  12:  '3rem',
  16:  '4rem',
  20:  '5rem',
  24:  '6rem',
} as const;

export const radius = {
  none: '0',
  sm:   '0.25rem',
  DEFAULT: '0.5rem',
  md:   '0.625rem',
  lg:   '0.75rem',
  xl:   '1rem',
  '2xl': '1.25rem',
  '3xl': '1.5rem',
  full: '9999px',
} as const;

export const shadows = {
  xs:   '0 1px 2px 0 rgb(0 0 0 / 0.03)',
  sm:   '0 1px 3px 0 rgb(0 0 0 / 0.05), 0 1px 2px -1px rgb(0 0 0 / 0.05)',
  DEFAULT: '0 4px 6px -1px rgb(0 0 0 / 0.07), 0 2px 4px -2px rgb(0 0 0 / 0.05)',
  md:   '0 6px 12px -2px rgb(0 0 0 / 0.08), 0 3px 6px -3px rgb(0 0 0 / 0.05)',
  lg:   '0 10px 25px -3px rgb(0 0 0 / 0.08), 0 4px 10px -4px rgb(0 0 0 / 0.04)',
  xl:   '0 20px 40px -5px rgb(0 0 0 / 0.1), 0 8px 16px -6px rgb(0 0 0 / 0.05)',
  '2xl': '0 25px 50px -12px rgb(0 0 0 / 0.15)',
  primary: '0 8px 24px -4px rgb(0 137 208 / 0.25)',
  accent:  '0 8px 24px -4px rgb(140 198 63 / 0.25)',
  cta:     '0 8px 24px -4px rgb(0 137 208 / 0.3)',
  inner: 'inset 0 1px 2px rgb(0 0 0 / 0.05)',
  none: 'none',
} as const;

export const typography = {
  fonts: {
    display: "'Plus Jakarta Sans', system-ui, sans-serif",
    body: "'Inter', system-ui, sans-serif",
  },
  sizes: {
    xs:   { size: '0.75rem',   lineHeight: '1rem' },
    sm:   { size: '0.875rem',  lineHeight: '1.25rem' },
    base: { size: '1rem',      lineHeight: '1.5rem' },
    lg:   { size: '1.125rem',  lineHeight: '1.75rem' },
    xl:   { size: '1.25rem',   lineHeight: '1.75rem' },
    '2xl': { size: '1.5rem',   lineHeight: '2rem' },
    '3xl': { size: '1.875rem', lineHeight: '2.25rem' },
    '4xl': { size: '2.25rem',  lineHeight: '2.5rem' },
    '5xl': { size: '3rem',     lineHeight: '1.1' },
    '6xl': { size: '3.75rem',  lineHeight: '1.05' },
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

export const motion = {
  duration: {
    instant: '50ms',
    fast:    '150ms',
    normal:  '250ms',
    slow:    '400ms',
    slower:  '600ms',
  },
  easing: {
    default: 'cubic-bezier(0.4, 0, 0.2, 1)',
    easeOut: 'cubic-bezier(0, 0, 0.2, 1)',
    easeIn: 'cubic-bezier(0.4, 0, 1, 1)',
    spring: 'cubic-bezier(0.34, 1.3, 0.64, 1)',
    smooth: 'cubic-bezier(0.25, 0.46, 0.45, 0.94)',
  },
  transitions: {
    colors: 'color 150ms ease, background-color 150ms ease, border-color 150ms ease',
    transform: 'transform 250ms cubic-bezier(0.4, 0, 0.2, 1)',
    shadow: 'box-shadow 250ms cubic-bezier(0.4, 0, 0.2, 1)',
    interactive: 'transform 250ms cubic-bezier(0.34, 1.3, 0.64, 1), box-shadow 250ms ease, opacity 200ms ease',
    reveal: 'opacity 500ms cubic-bezier(0, 0, 0.2, 1), transform 500ms cubic-bezier(0, 0, 0.2, 1)',
  },
} as const;

export const hover = {
  scale: {
    subtle: 1.01,
    default: 1.02,
    button: 1.03,
  },
  lift: {
    subtle: '-2px',
    default: '-4px',
    elevated: '-6px',
  },
  overlay: {
    light: 0.05,
    medium: 0.1,
    strong: 0.15,
  },
} as const;

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

export const breakpoints = {
  sm: '640px',
  md: '768px',
  lg: '1024px',
  xl: '1280px',
  '2xl': '1536px',
} as const;
