import { fileURLToPath } from 'url';

const __dirname = fileURLToPath(new URL('.', import.meta.url)).replace(/\\/g, '/');

/** @type {import('tailwindcss').Config} */
export default {
  content: [`${__dirname}src/**/*.{astro,html,js,jsx,md,mdx,svelte,ts,tsx,vue}`],
  theme: {
    extend: {
      colors: {
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
          DEFAULT: '#0089D0',
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
          DEFAULT: '#005B32',
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
          DEFAULT: '#8CC63F',
        },
        dark:    '#1a1a2e',
        light:   '#F5F7FA',
        surface: '#FFFFFF',
        cta: {
          DEFAULT: '#0089D0',
          hover:   '#006BA3',
        },
      },
      fontFamily: {
        display: ['Plus Jakarta Sans', 'system-ui', 'sans-serif'],
        body:    ['Inter', 'system-ui', 'sans-serif'],
      },
      boxShadow: {
        'xs':   '0 1px 2px 0 rgb(0 0 0 / 0.03)',
        'sm':   '0 1px 3px 0 rgb(0 0 0 / 0.05), 0 1px 2px -1px rgb(0 0 0 / 0.05)',
        'DEFAULT': '0 4px 6px -1px rgb(0 0 0 / 0.07), 0 2px 4px -2px rgb(0 0 0 / 0.05)',
        'md':   '0 6px 12px -2px rgb(0 0 0 / 0.08), 0 3px 6px -3px rgb(0 0 0 / 0.05)',
        'lg':   '0 10px 25px -3px rgb(0 0 0 / 0.08), 0 4px 10px -4px rgb(0 0 0 / 0.04)',
        'xl':   '0 20px 40px -5px rgb(0 0 0 / 0.1), 0 8px 16px -6px rgb(0 0 0 / 0.05)',
        '2xl':  '0 25px 50px -12px rgb(0 0 0 / 0.15)',
        'primary': '0 8px 24px -4px rgb(0 137 208 / 0.25)',
        'accent':  '0 8px 24px -4px rgb(140 198 63 / 0.25)',
        'cta':     '0 8px 24px -4px rgb(0 137 208 / 0.25)',
      },
      borderRadius: {
        'sm':  '0.25rem',
        DEFAULT: '0.5rem',
        'md':  '0.625rem',
        'lg':  '0.75rem',
        'xl':  '1rem',
        '2xl': '1.25rem',
        '3xl': '1.5rem',
      },
      animation: {
        'wave':        'waveMove 10s ease-in-out infinite',
        'pulse-ring':  'pulseRing 2.5s ease-out infinite',
        'float':       'float 4s ease-in-out infinite',
        'fade-in':     'fadeIn 0.5s ease-out',
      },
      keyframes: {
        waveMove: {
          '0%, 100%': { transform: 'translateX(0)' },
          '50%':      { transform: 'translateX(-20px)' },
        },
        pulseRing: {
          '0%':   { transform: 'scale(1)', opacity: '0.5' },
          '100%': { transform: 'scale(2)', opacity: '0' },
        },
        float: {
          '0%, 100%': { transform: 'translateY(0)' },
          '50%':      { transform: 'translateY(-8px)' },
        },
        fadeIn: {
          '0%':   { opacity: '0', transform: 'translateY(10px)' },
          '100%': { opacity: '1', transform: 'translateY(0)' },
        },
      },
      transitionTimingFunction: {
        'spring': 'cubic-bezier(0.34, 1.3, 0.64, 1)',
        'smooth': 'cubic-bezier(0.25, 0.46, 0.45, 0.94)',
      },
    },
  },
  plugins: [
    require('@tailwindcss/typography'),
  ],
};
