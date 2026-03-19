/**
 * ══════════════════════════════════════════════════════════════════
 * YaDev Design System — Tokens Template
 * ══════════════════════════════════════════════════════════════════
 *
 * USAGE:
 *   1. Copy this file to your project: src/design-system/tokens.ts
 *   2. Replace every value marked with [PLACEHOLDER] with the
 *      client's actual brand values.
 *   3. Run generateCSSVars() in your Layout.astro <head> if you
 *      prefer JS-driven injection, OR keep the :root block in
 *      global.css in sync with these values manually.
 *
 * NAMING CONVENTION:
 *   Colors follow a 50–950 scale (light → dark).
 *   DEFAULT is the primary usage value (usually 500).
 *
 * ══════════════════════════════════════════════════════════════════
 */

// ─────────────────────────────────────────────────────────────────
// COLOR TOKENS
// Replace hex values with client brand colors.
// Tip: Use https://uicolors.app to generate a full scale from
//      a single brand color.
// ─────────────────────────────────────────────────────────────────

export const colors = {

  /**
   * PRIMARY — The dominant brand color.
   * Used for: nav active states, headings on dark, icon boxes,
   *           secondary button border/text, focus rings.
   * [PLACEHOLDER] — Replace with client's main brand color.
   */
  primary: {
    50:      '#PLACEHOLDER_PRIMARY_50',   // lightest tint (bg, badges, input focus ring)
    100:     '#PLACEHOLDER_PRIMARY_100',  // light tint (selection highlight, scrollbar)
    200:     '#PLACEHOLDER_PRIMARY_200',
    300:     '#PLACEHOLDER_PRIMARY_300',
    400:     '#PLACEHOLDER_PRIMARY_400',
    500:     '#PLACEHOLDER_PRIMARY_500',  // base — DEFAULT
    600:     '#PLACEHOLDER_PRIMARY_600',
    700:     '#PLACEHOLDER_PRIMARY_700',  // hover state for secondary btn fill
    800:     '#PLACEHOLDER_PRIMARY_800',
    900:     '#PLACEHOLDER_PRIMARY_900',
    950:     '#PLACEHOLDER_PRIMARY_950',  // darkest — use for footer text on dark bg
    DEFAULT: '#PLACEHOLDER_PRIMARY_500',
  },

  /**
   * SECONDARY — Supporting brand color.
   * Used for: feature labels, dividers, complementary sections,
   *           gradient pairs with primary.
   * [PLACEHOLDER] — Replace with client's secondary color.
   */
  secondary: {
    50:      '#PLACEHOLDER_SECONDARY_50',
    100:     '#PLACEHOLDER_SECONDARY_100',
    200:     '#PLACEHOLDER_SECONDARY_200',
    300:     '#PLACEHOLDER_SECONDARY_300',
    400:     '#PLACEHOLDER_SECONDARY_400',
    500:     '#PLACEHOLDER_SECONDARY_500',
    600:     '#PLACEHOLDER_SECONDARY_600',
    700:     '#PLACEHOLDER_SECONDARY_700',
    800:     '#PLACEHOLDER_SECONDARY_800',
    900:     '#PLACEHOLDER_SECONDARY_900',
    DEFAULT: '#PLACEHOLDER_SECONDARY_500',
  },

  /**
   * ACCENT — Highlight / tag / spark color.
   * Used for: section labels, badge dots, icon highlights,
   *           decorative elements, chart colors.
   * This can be a vibrant contrasting color.
   * [PLACEHOLDER] — Replace with client's accent color.
   */
  accent: {
    50:      '#PLACEHOLDER_ACCENT_50',
    100:     '#PLACEHOLDER_ACCENT_100',
    200:     '#PLACEHOLDER_ACCENT_200',
    300:     '#PLACEHOLDER_ACCENT_300',
    400:     '#PLACEHOLDER_ACCENT_400',
    500:     '#PLACEHOLDER_ACCENT_500',
    600:     '#PLACEHOLDER_ACCENT_600',
    700:     '#PLACEHOLDER_ACCENT_700',
    800:     '#PLACEHOLDER_ACCENT_800',
    900:     '#PLACEHOLDER_ACCENT_900',
    DEFAULT: '#PLACEHOLDER_ACCENT_500',
  },

  /**
   * CTA — Call-to-action button color.
   * Can be the same as primary or a dedicated conversion color.
   * Often slightly more vibrant/warm than the main brand.
   * [PLACEHOLDER] — Replace with client's CTA color.
   *
   * Examples from past projects:
   *   ECOMAG:         #E65100 (deep orange, energetic contrast to green)
   *   Multiservicios: #0089D0 (same as primary — CTA IS the brand color)
   */
  cta: {
    DEFAULT: '#PLACEHOLDER_CTA',
    hover:   '#PLACEHOLDER_CTA_HOVER',  // ~10% darker than DEFAULT
  },

  /**
   * NEUTRALS — Dark and light surface colors.
   * dark:    Used for body text, headings, footer background.
   * light:   Used for page background (near-white, slightly tinted).
   * surface: Pure white for cards, modals, inputs.
   */
  dark:    '#PLACEHOLDER_DARK',    // e.g. #1a1a2e (near-black, slightly warm/cool)
  light:   '#PLACEHOLDER_LIGHT',   // e.g. #F5F7FA (off-white page background)
  surface: '#FFFFFF',              // card / input background — usually pure white

} as const;


// ─────────────────────────────────────────────────────────────────
// SPACING — 4px base grid
// All spacing values are multiples of 4px.
// These map to Tailwind's default spacing scale.
// ─────────────────────────────────────────────────────────────────

export const spacing = {
  0:    '0px',
  1:    '4px',
  2:    '8px',
  3:    '12px',
  4:    '16px',
  5:    '20px',
  6:    '24px',
  8:    '32px',
  10:   '40px',
  12:   '48px',
  16:   '64px',
  20:   '80px',
  24:   '96px',
  section: {
    sm:  '64px',   // py-16 — mobile sections
    md:  '96px',   // py-24 — standard desktop sections
    lg:  '128px',  // py-32 — hero / feature emphasis sections
  },
} as const;


// ─────────────────────────────────────────────────────────────────
// BORDER RADIUS
// ─────────────────────────────────────────────────────────────────

export const borderRadius = {
  none:    '0px',
  sm:      '0.25rem',   // 4px — tight elements
  DEFAULT: '0.5rem',    // 8px — standard inputs, small cards
  md:      '0.625rem',  // 10px
  lg:      '0.75rem',   // 12px — standard cards
  xl:      '1rem',      // 16px — prominent cards, modals
  '2xl':   '1.25rem',   // 20px — hero sections, overlapping UI
  '3xl':   '1.5rem',    // 24px — large feature cards
  full:    '9999px',    // pill badges, avatar circles
} as const;


// ─────────────────────────────────────────────────────────────────
// SHADOWS — Neutral scale + colored brand variants
// Neutral shadows use black at low opacity (subtle, modern).
// Colored shadows use the primary/cta color (glow effect on hover).
// ─────────────────────────────────────────────────────────────────

export const shadows = {
  // Neutral depth scale
  xs:  '0 1px 2px 0 rgb(0 0 0 / 0.03)',
  sm:  '0 1px 3px 0 rgb(0 0 0 / 0.05), 0 1px 2px -1px rgb(0 0 0 / 0.05)',
  md:  '0 4px 6px -1px rgb(0 0 0 / 0.07), 0 2px 4px -2px rgb(0 0 0 / 0.05)',
  lg:  '0 10px 25px -3px rgb(0 0 0 / 0.08), 0 4px 10px -4px rgb(0 0 0 / 0.04)',
  xl:  '0 20px 40px -5px rgb(0 0 0 / 0.1), 0 8px 16px -6px rgb(0 0 0 / 0.05)',
  '2xl': '0 25px 50px -12px rgb(0 0 0 / 0.15)',

  /**
   * Colored glow shadows — replace R G B values.
   * Formula: 0 8px 24px -4px rgb(R G B / 0.25)
   *
   * [PLACEHOLDER] Replace the rgb values below with the
   * primary and cta colors decomposed as R G B integers.
   *
   * Examples:
   *   primary: #0089D0 → rgb(0 137 208 / 0.25)
   *   primary: #1B5E20 → rgb(27 94 32 / 0.2)
   *   cta:     #E65100 → rgb(230 81 0 / 0.25)
   */
  primary: '0 8px 24px -4px rgb(PLACEHOLDER_R PLACEHOLDER_G PLACEHOLDER_B / 0.25)',
  accent:  '0 8px 24px -4px rgb(PLACEHOLDER_AR PLACEHOLDER_AG PLACEHOLDER_AB / 0.25)',
  cta:     '0 8px 24px -4px rgb(PLACEHOLDER_CR PLACEHOLDER_CG PLACEHOLDER_CB / 0.25)',
} as const;


// ─────────────────────────────────────────────────────────────────
// TYPOGRAPHY
// Using Google Fonts: Plus Jakarta Sans + Inter
// Add to <head>:
//   <link rel="preconnect" href="https://fonts.googleapis.com">
//   <link href="https://fonts.googleapis.com/css2?family=Plus+Jakarta+Sans:wght@400;500;600;700;800&family=Inter:wght@400;500;600&display=swap" rel="stylesheet">
// ─────────────────────────────────────────────────────────────────

export const typography = {
  fonts: {
    display: "'Plus Jakarta Sans', system-ui, sans-serif",
    body:    "'Inter', system-ui, sans-serif",
    mono:    "'JetBrains Mono', 'Fira Code', ui-monospace, monospace",
  },
  sizes: {
    // Fluid scale using clamp()
    xs:   'clamp(0.75rem, 1vw, 0.875rem)',      // 12–14px
    sm:   'clamp(0.875rem, 1.2vw, 1rem)',        // 14–16px
    base: 'clamp(0.9375rem, 1.5vw, 1.0625rem)', // 15–17px body text
    lg:   'clamp(1.0625rem, 2vw, 1.25rem)',      // 17–20px
    xl:   'clamp(1.125rem, 2.5vw, 1.5rem)',      // 18–24px
    '2xl': 'clamp(1.25rem, 2.5vw, 1.75rem)',     // 20–28px heading-secondary
    '3xl': 'clamp(1.5rem, 3vw, 2.25rem)',        // 24–36px
    '4xl': 'clamp(1.75rem, 4vw, 3rem)',          // 28–48px heading-primary
    '5xl': 'clamp(2rem, 5vw, 4rem)',             // 32–64px hero headline
  },
  weights: {
    regular:   '400',
    medium:    '500',
    semibold:  '600',
    bold:      '700',
    extrabold: '800',
  },
  leading: {
    tight:   '1.15',   // headings
    snug:    '1.25',   // subheadings
    normal:  '1.5',    // labels, buttons
    relaxed: '1.6',    // body paragraphs
    loose:   '1.8',    // long-form prose
  },
  tracking: {
    tight:     '-0.025em',  // headings
    normal:    '0em',
    wide:      '0.025em',
    wider:     '0.05em',
    widest:    '0.1em',     // uppercase labels
  },
} as const;


// ─────────────────────────────────────────────────────────────────
// MOTION — Duration + Easing
// Philosophy: fast enough to feel responsive, slow enough to feel
// intentional. Spring easing for interactive elements, smooth for
// decorative animations.
// ─────────────────────────────────────────────────────────────────

export const motion = {
  duration: {
    instant:  '100ms',  // micro interactions (checkbox tick, icon swap)
    fast:     '150ms',  // hover state changes (bg, border, color)
    normal:   '250ms',  // standard transitions (card hover, modal open)
    slow:     '400ms',  // scroll reveals, page-level transitions
    verySlow: '600ms',  // hero entrance, splash screen
  },
  easing: {
    // Standard Material-inspired curves
    default: 'cubic-bezier(0.4, 0, 0.2, 1)',      // standard: ease in+out
    in:      'cubic-bezier(0.4, 0, 1, 1)',          // accelerate
    out:     'cubic-bezier(0, 0, 0.2, 1)',          // decelerate (reveals)
    // Custom premium curves
    spring:  'cubic-bezier(0.34, 1.3, 0.64, 1)',   // slight overshoot — button lifts
    smooth:  'cubic-bezier(0.25, 0.46, 0.45, 0.94)', // very smooth — image zooms
    bounce:  'cubic-bezier(0.68, -0.55, 0.265, 1.55)', // bounce — playful elements only
  },
  transitions: {
    // Ready-to-use transition shorthand strings
    base:       'all 150ms cubic-bezier(0.4, 0, 0.2, 1)',
    hover:      'transform 250ms cubic-bezier(0.34, 1.3, 0.64, 1), box-shadow 250ms cubic-bezier(0.4, 0, 0.2, 1)',
    color:      'background-color 150ms cubic-bezier(0.4, 0, 0.2, 1), color 150ms cubic-bezier(0.4, 0, 0.2, 1)',
    reveal:     'opacity 400ms cubic-bezier(0, 0, 0.2, 1), transform 400ms cubic-bezier(0, 0, 0.2, 1)',
    imageZoom:  'transform 400ms cubic-bezier(0.25, 0.46, 0.45, 0.94)',
  },
} as const;


// ─────────────────────────────────────────────────────────────────
// Z-INDEX STACK
// Named layers prevent magic numbers scattered across components.
// ─────────────────────────────────────────────────────────────────

export const zIndex = {
  hide:     -1,    // behind everything
  base:      0,
  raised:   10,    // cards on hover, tooltips
  dropdown: 20,    // dropdowns, popovers
  sticky:   30,    // sticky headers, sidebars
  overlay:  40,    // modal backdrop
  modal:    50,    // modal dialog
  toast:    60,    // toast notifications
  tooltip:  70,    // tooltips over modals
  cursor:   80,    // custom cursor
  top:      9999,  // absolute highest — accessibility skip links
} as const;


// ─────────────────────────────────────────────────────────────────
// BREAKPOINTS — Tailwind-aligned
// ─────────────────────────────────────────────────────────────────

export const breakpoints = {
  sm:  '640px',   // >= small phone landscape
  md:  '768px',   // >= tablet portrait
  lg:  '1024px',  // >= tablet landscape / small laptop
  xl:  '1280px',  // >= standard desktop
  '2xl': '1536px', // >= wide desktop
} as const;


// ─────────────────────────────────────────────────────────────────
// CSS VARIABLES EXPORT
// Inject these into your Astro Layout's <head> via a <style> block,
// or keep global.css :root in sync manually.
//
// Usage in Layout.astro:
//   ---
//   import { generateCSSVars } from '../design-system/tokens';
//   const cssVars = generateCSSVars();
//   ---
//   <style set:html={cssVars}></style>
// ─────────────────────────────────────────────────────────────────

export function generateCSSVars(): string {
  return `
    :root {
      /* Colors */
      --color-primary:       ${colors.primary.DEFAULT};
      --color-primary-50:    ${colors.primary[50]};
      --color-primary-100:   ${colors.primary[100]};
      --color-primary-light: ${colors.primary[200]};
      --color-primary-dark:  ${colors.primary[700]};
      --color-secondary:     ${colors.secondary.DEFAULT};
      --color-secondary-50:  ${colors.secondary[50]};
      --color-accent:        ${colors.accent.DEFAULT};
      --color-accent-50:     ${colors.accent[50]};
      --color-dark:          ${colors.dark};
      --color-light:         ${colors.light};
      --color-surface:       ${colors.surface};
      --color-cta:           ${colors.cta.DEFAULT};
      --color-cta-hover:     ${colors.cta.hover};

      /* Typography */
      --font-display: ${typography.fonts.display};
      --font-body:    ${typography.fonts.body};
      --font-mono:    ${typography.fonts.mono};

      /* Shadows */
      --shadow-xs:      ${shadows.xs};
      --shadow-sm:      ${shadows.sm};
      --shadow-md:      ${shadows.md};
      --shadow-lg:      ${shadows.lg};
      --shadow-xl:      ${shadows.xl};
      --shadow-primary: ${shadows.primary};
      --shadow-accent:  ${shadows.accent};
      --shadow-cta:     ${shadows.cta};

      /* Motion */
      --ease-default: ${motion.easing.default};
      --ease-out:     ${motion.easing.out};
      --ease-spring:  ${motion.easing.spring};
      --ease-smooth:  ${motion.easing.smooth};
      --duration-fast:   ${motion.duration.fast};
      --duration-normal: ${motion.duration.normal};
      --duration-slow:   ${motion.duration.slow};

      /* Radius */
      --radius-sm:  ${borderRadius.sm};
      --radius-md:  ${borderRadius.md};
      --radius-lg:  ${borderRadius.lg};
      --radius-xl:  ${borderRadius.xl};
      --radius-2xl: ${borderRadius['2xl']};
    }
  `;
}


// ─────────────────────────────────────────────────────────────────
// TYPE EXPORTS
// Use these in component TypeScript interfaces.
// ─────────────────────────────────────────────────────────────────

export type ColorScale = typeof colors.primary;
export type ColorName = keyof typeof colors;
export type ShadowName = keyof typeof shadows;
export type MotionDuration = keyof typeof motion.duration;
export type MotionEasing = keyof typeof motion.easing;
export type ZIndexLayer = keyof typeof zIndex;
export type Breakpoint = keyof typeof breakpoints;
