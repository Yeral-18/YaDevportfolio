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
      animation: {
        'leaf-sway':   'leafSway 6s ease-in-out infinite',
        'wave':        'waveMove 8s ease-in-out infinite',
        'pulse-ring':  'pulseRing 2s ease-out infinite',
        'float':       'float 3s ease-in-out infinite',
      },
      keyframes: {
        leafSway: {
          '0%, 100%': { transform: 'rotate(-3deg) translateY(0)' },
          '50%':      { transform: 'rotate(3deg) translateY(-8px)' },
        },
        waveMove: {
          '0%, 100%': { transform: 'translateX(0)' },
          '50%':      { transform: 'translateX(-25px)' },
        },
        pulseRing: {
          '0%':   { transform: 'scale(1)', opacity: '0.6' },
          '100%': { transform: 'scale(2.2)', opacity: '0' },
        },
        float: {
          '0%, 100%': { transform: 'translateY(0)' },
          '50%':      { transform: 'translateY(-10px)' },
        },
      },
    },
  },
  plugins: [
    require('@tailwindcss/typography'),
  ],
};
