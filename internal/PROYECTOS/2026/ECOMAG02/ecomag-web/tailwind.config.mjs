/** @type {import('tailwindcss').Config} */
export default {
  content: ['./src/**/*.{astro,html,js,jsx,md,mdx,svelte,ts,tsx,vue}'],
  theme: {
    extend: {
      colors: {
        primary: {
          50:  '#e8f5e9',
          100: '#c8e6c9',
          200: '#a5d6a7',
          300: '#81c784',
          400: '#66bb6a',
          500: '#1B5E20',
          600: '#165a1c',
          700: '#114d16',
          800: '#0d3f11',
          900: '#08310c',
          DEFAULT: '#1B5E20',
        },
        secondary: {
          50:  '#e0f2f7',
          100: '#b3e0ed',
          200: '#80cde2',
          300: '#4db9d6',
          400: '#26aacd',
          500: '#0277A8',
          600: '#026a97',
          700: '#015a80',
          800: '#014a6a',
          900: '#003a54',
          DEFAULT: '#0277A8',
        },
        accent: {
          50:  '#f1f8e9',
          100: '#dcedc8',
          200: '#c5e1a5',
          300: '#aed581',
          400: '#9ccc65',
          500: '#7CB342',
          600: '#6fa53b',
          700: '#5e9231',
          800: '#4e7f28',
          900: '#3e6c1f',
          DEFAULT: '#7CB342',
        },
        dark:    '#1a1a2e',
        light:   '#F5F7F2',
        surface: '#FFFFFF',
        cta:     '#E65100',
      },
      fontFamily: {
        display: ['Plus Jakarta Sans', 'system-ui', 'sans-serif'],
        body:    ['Inter', 'system-ui', 'sans-serif'],
      },
      // Premium shadows (Apple/Linear style)
      boxShadow: {
        'xs':   '0 1px 2px 0 rgb(0 0 0 / 0.03)',
        'sm':   '0 1px 3px 0 rgb(0 0 0 / 0.05), 0 1px 2px -1px rgb(0 0 0 / 0.05)',
        'DEFAULT': '0 4px 6px -1px rgb(0 0 0 / 0.07), 0 2px 4px -2px rgb(0 0 0 / 0.05)',
        'md':   '0 6px 12px -2px rgb(0 0 0 / 0.08), 0 3px 6px -3px rgb(0 0 0 / 0.05)',
        'lg':   '0 10px 25px -3px rgb(0 0 0 / 0.08), 0 4px 10px -4px rgb(0 0 0 / 0.04)',
        'xl':   '0 20px 40px -5px rgb(0 0 0 / 0.1), 0 8px 16px -6px rgb(0 0 0 / 0.05)',
        '2xl':  '0 25px 50px -12px rgb(0 0 0 / 0.15)',
        'primary': '0 8px 24px -4px rgb(27 94 32 / 0.2)',
        'accent':  '0 8px 24px -4px rgb(124 179 66 / 0.25)',
        'cta':     '0 8px 24px -4px rgb(230 81 0 / 0.25)',
      },
      // Subtle border radius scale
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
      // Transition timing functions
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
