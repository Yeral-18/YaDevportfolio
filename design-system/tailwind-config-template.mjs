/**
 * ══════════════════════════════════════════════════════════════════
 * YaDev Design System — Tailwind Config Template
 * ══════════════════════════════════════════════════════════════════
 *
 * SETUP:
 *   1. Copy to: tailwind.config.mjs (project root)
 *   2. Replace all PLACEHOLDER color values with client brand hex.
 *   3. Keep fontFamily as-is unless the project uses different fonts.
 *   4. Adjust animations/keyframes to match the site personality.
 *
 * PATH FIX:
 *   The content array uses fileURLToPath(__dirname) + a template
 *   literal to build an absolute path. This is required when the
 *   project folder contains special characters on Windows.
 *   The .replace(/\\/g, '/') normalizes backslashes to forward
 *   slashes, which Tailwind's glob engine requires.
 *
 * ══════════════════════════════════════════════════════════════════
 */

import { fileURLToPath } from 'url';

/**
 * Resolve __dirname equivalent in ESM.
 * Using URL + fileURLToPath gives us a clean absolute path that
 * works on both Windows and Linux, even with special chars in path.
 */
const __dirname = fileURLToPath(new URL('.', import.meta.url)).replace(/\\/g, '/');

/** @type {import('tailwindcss').Config} */
export default {
  /**
   * Content — tells Tailwind which files to scan for class names.
   * Using an absolute path (${__dirname}src/**) avoids Tailwind
   * failing to find classes when the CWD is different from the
   * project root (common on Windows with pnpm/yarn workspaces).
   */
  content: [
    `${__dirname}src/**/*.{astro,html,js,jsx,md,mdx,svelte,ts,tsx,vue}`,
  ],

  theme: {
    extend: {

      /* ── Colors ──────────────────────────────────────────────── */
      /*
       * [PLACEHOLDER] Replace all hex values with client brand colors.
       *
       * Generating a full scale from a single hex:
       *   https://uicolors.app/create
       *   https://www.tailwindshades.com/
       *
       * Scale guide:
       *   50   = almost white (backgrounds, badges)
       *   100  = very light (selection, scrollbar)
       *   200  = light tint
       *   300  = medium-light
       *   400  = medium
       *   500  = base (DEFAULT — most used)
       *   600  = medium-dark
       *   700  = dark (hover fills for secondary btn)
       *   800  = very dark
       *   900  = near-black
       *   950  = deepest (footer text on dark backgrounds)
       */
      colors: {
        primary: {
          50:      '#PLACEHOLDER_PRIMARY_50',
          100:     '#PLACEHOLDER_PRIMARY_100',
          200:     '#PLACEHOLDER_PRIMARY_200',
          300:     '#PLACEHOLDER_PRIMARY_300',
          400:     '#PLACEHOLDER_PRIMARY_400',
          500:     '#PLACEHOLDER_PRIMARY_500',
          600:     '#PLACEHOLDER_PRIMARY_600',
          700:     '#PLACEHOLDER_PRIMARY_700',
          800:     '#PLACEHOLDER_PRIMARY_800',
          900:     '#PLACEHOLDER_PRIMARY_900',
          950:     '#PLACEHOLDER_PRIMARY_950',
          DEFAULT: '#PLACEHOLDER_PRIMARY_500',
        },
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

        /* Semantic tokens */
        dark:    '#PLACEHOLDER_DARK',   /* body text, footer bg */
        light:   '#PLACEHOLDER_LIGHT',  /* page background */
        surface: '#FFFFFF',             /* card / input bg */

        /* CTA as object to support .cta and .cta-hover in Tailwind */
        cta: {
          DEFAULT: '#PLACEHOLDER_CTA',
          hover:   '#PLACEHOLDER_CTA_HOVER',
        },
      },

      /* ── Font Families ───────────────────────────────────────── */
      /*
       * Default pairing: Plus Jakarta Sans (display) + Inter (body).
       *
       * IMPORTANT: Each client project should ideally use a
       * different font pairing to ensure visual uniqueness.
       *
       * Alternative pairings to consider:
       *   Tech/Dark:        'Space Grotesk' + 'DM Sans'
       *   Luxury/Corporate: 'Cormorant Garamond' + 'Lato'
       *   Playful/Creative: 'Clash Display' + 'Satoshi'
       *   Editorial:        'Fraunces' + 'Source Serif 4'
       *   Minimal/Swiss:    'DM Sans' + 'DM Mono'
       *   Professional:     'Sora' + 'Nunito Sans'
       */
      fontFamily: {
        display: ['Plus Jakarta Sans', 'system-ui', 'sans-serif'],
        body:    ['Inter', 'system-ui', 'sans-serif'],
        mono:    ['JetBrains Mono', 'Fira Code', 'ui-monospace', 'monospace'],
      },

      /* ── Shadows ─────────────────────────────────────────────── */
      /*
       * Neutral scale uses black at low opacity (subtle, modern).
       * Colored shadows use brand colors for button/card glows.
       *
       * [PLACEHOLDER] For colored shadows, decompose the hex into
       * R G B integers and replace values in the rgb() functions.
       *
       * Example: #0089D0 → rgb(0 137 208)
       */
      boxShadow: {
        'xs':      '0 1px 2px 0 rgb(0 0 0 / 0.03)',
        'sm':      '0 1px 3px 0 rgb(0 0 0 / 0.05), 0 1px 2px -1px rgb(0 0 0 / 0.05)',
        'DEFAULT': '0 4px 6px -1px rgb(0 0 0 / 0.07), 0 2px 4px -2px rgb(0 0 0 / 0.05)',
        'md':      '0 6px 12px -2px rgb(0 0 0 / 0.08), 0 3px 6px -3px rgb(0 0 0 / 0.05)',
        'lg':      '0 10px 25px -3px rgb(0 0 0 / 0.08), 0 4px 10px -4px rgb(0 0 0 / 0.04)',
        'xl':      '0 20px 40px -5px rgb(0 0 0 / 0.1), 0 8px 16px -6px rgb(0 0 0 / 0.05)',
        '2xl':     '0 25px 50px -12px rgb(0 0 0 / 0.15)',
        /* [PLACEHOLDER] Colored glow shadows — replace R G B */
        'primary': '0 8px 24px -4px rgb(PLACEHOLDER_PR PLACEHOLDER_PG PLACEHOLDER_PB / 0.25)',
        'accent':  '0 8px 24px -4px rgb(PLACEHOLDER_AR PLACEHOLDER_AG PLACEHOLDER_AB / 0.25)',
        'cta':     '0 8px 24px -4px rgb(PLACEHOLDER_CR PLACEHOLDER_CG PLACEHOLDER_CB / 0.25)',
      },

      /* ── Border Radius ───────────────────────────────────────── */
      borderRadius: {
        'none':    '0px',
        'sm':      '0.25rem',
        'DEFAULT': '0.5rem',
        'md':      '0.625rem',
        'lg':      '0.75rem',
        'xl':      '1rem',
        '2xl':     '1.25rem',
        '3xl':     '1.5rem',
        'full':    '9999px',
      },

      /* ── Animations ──────────────────────────────────────────── */
      /*
       * These are utility animations for decorative elements.
       * Component-level transitions should use CSS variables
       * (--ease-spring, --duration-normal) via inline styles.
       *
       * Customize per project personality:
       *   - Remove 'leaf-sway' for non-nature projects
       *   - Add 'ticker' for news/scrolling elements
       *   - Add 'shimmer' for skeleton loaders
       */
      animation: {
        /* Gentle ambient motion for decorative elements */
        'float':       'float 4s ease-in-out infinite',
        'float-slow':  'float 6s ease-in-out infinite',
        'pulse-ring':  'pulseRing 2.5s ease-out infinite',

        /* UI feedback animations */
        'fade-in':     'fadeIn 0.5s ease-out forwards',
        'slide-up':    'slideUp 0.4s ease-out forwards',
        'scale-in':    'scaleIn 0.3s cubic-bezier(0.34, 1.3, 0.64, 1) forwards',

        /* Loader animations */
        'spin-slow':   'spin 3s linear infinite',
        'shimmer':     'shimmer 1.5s ease-in-out infinite',

        /* Background animations */
        'wave':        'waveMove 10s ease-in-out infinite',
        'wave-slow':   'waveMove 14s ease-in-out infinite',

        /* [PLACEHOLDER] Add project-specific animations here */
        /* 'leaf-sway': 'leafSway 6s ease-in-out infinite', */
      },

      keyframes: {
        float: {
          '0%, 100%': { transform: 'translateY(0)' },
          '50%':      { transform: 'translateY(-10px)' },
        },
        pulseRing: {
          '0%':   { transform: 'scale(1)', opacity: '0.5' },
          '100%': { transform: 'scale(2.2)', opacity: '0' },
        },
        fadeIn: {
          '0%':   { opacity: '0', transform: 'translateY(10px)' },
          '100%': { opacity: '1', transform: 'translateY(0)' },
        },
        slideUp: {
          '0%':   { opacity: '0', transform: 'translateY(24px)' },
          '100%': { opacity: '1', transform: 'translateY(0)' },
        },
        scaleIn: {
          '0%':   { opacity: '0', transform: 'scale(0.9)' },
          '100%': { opacity: '1', transform: 'scale(1)' },
        },
        shimmer: {
          '0%':   { backgroundPosition: '-200% center' },
          '100%': { backgroundPosition: '200% center' },
        },
        waveMove: {
          '0%, 100%': { transform: 'translateX(0)' },
          '50%':      { transform: 'translateX(-20px)' },
        },
        /* [PLACEHOLDER] Project-specific keyframes */
        /* leafSway: {
          '0%, 100%': { transform: 'rotate(-3deg) translateY(0)' },
          '50%':      { transform: 'rotate(3deg) translateY(-8px)' },
        }, */
      },

      /* ── Easing Functions ────────────────────────────────────── */
      /*
       * Named easing functions for use with Tailwind's duration
       * utilities: duration-150 ease-spring
       */
      transitionTimingFunction: {
        'spring':  'cubic-bezier(0.34, 1.3, 0.64, 1)',
        'smooth':  'cubic-bezier(0.25, 0.46, 0.45, 0.94)',
        'bounce':  'cubic-bezier(0.68, -0.55, 0.265, 1.55)',
      },
    },
  },

  plugins: [
    /**
     * @tailwindcss/typography — adds .prose class for rich text.
     * Used in blog posts, long descriptions, terms/privacy pages.
     * Install: npm install @tailwindcss/typography
     */
    require('@tailwindcss/typography'),
  ],
};
