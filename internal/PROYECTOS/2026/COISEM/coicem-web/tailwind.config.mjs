/**
 * COICEM S.A.S — Tailwind config
 * Paleta PROVISIONAL v1 (extraída del logo JPEG — re-extraer con el original).
 * Brutalist: bordes duros, sin sombras blandas.
 */
import { fileURLToPath } from 'url';
const __dirname = fileURLToPath(new URL('.', import.meta.url)).replace(/\\/g, '/');

/** @type {import('tailwindcss').Config} */
export default {
  content: [`${__dirname}src/**/*.{astro,html,js,jsx,md,mdx,svelte,ts,tsx,vue}`],
  theme: {
    extend: {
      colors: {
        primary: {
          50:'#E8F1FA',100:'#C5DDF2',200:'#8EB9DC',300:'#4E90C8',400:'#1A6FB0',
          500:'#025199',600:'#023F7E',700:'#003069',800:'#002657',900:'#001A3C',950:'#000E27',
          DEFAULT:'#025199',
        },
        accent: {
          50:'#FFF4E3',100:'#FFE2B8',200:'#FFC97A',300:'#FFA222',400:'#F79204',
          500:'#F79204',600:'#E38325',700:'#B36400',800:'#8A4D00',900:'#5E3400',
          DEFAULT:'#F79204',
        },
        metal: { light:'#4B6881', DEFAULT:'#313F50', panel:'#161B22', base:'#0B0E14', black:'#000000' },
        dark:'#0B0E14', light:'#EDEDE8', surface:'#FFFFFF', highlight:'#F6FCFD',
        cta: { DEFAULT:'#F79204', hover:'#DB7E00' },
      },
      fontFamily: {
        display: ['Archivo Expanded', 'Archivo', 'system-ui', 'sans-serif'],
        body:    ['IBM Plex Sans', 'system-ui', 'sans-serif'],
        mono:    ['IBM Plex Mono', 'ui-monospace', 'monospace'],
      },
      // Brutalist: bordes duros.
      borderRadius: { none:'0px', sm:'2px', DEFAULT:'0px', md:'0px', lg:'0px', xl:'0px', full:'9999px' },
      // Sombras duras (offset, no blur suave) — estética técnica.
      boxShadow: {
        'hard':   '4px 4px 0 0 #000000',
        'hard-sm':'2px 2px 0 0 #000000',
        'accent': '4px 4px 0 0 #F79204',
      },
      transitionTimingFunction: {
        'quint': 'cubic-bezier(0.83, 0, 0.17, 1)',   // easeInOutQuint — firma COICEM
        'expo':  'cubic-bezier(0.16, 1, 0.3, 1)',     // easeOutExpo — reveals
        'sharp': 'cubic-bezier(0.4, 0, 0.2, 1)',
      },
      animation: {
        'fade-in':  'fadeIn 0.5s cubic-bezier(0.16,1,0.3,1) forwards',
        'rise':     'rise 0.6s cubic-bezier(0.16,1,0.3,1) forwards',
        'draw':     'draw 0.8s cubic-bezier(0.83,0,0.17,1) forwards',  // leader lines
      },
      keyframes: {
        fadeIn: { '0%':{opacity:'0'}, '100%':{opacity:'1'} },
        rise:   { '0%':{opacity:'0',transform:'translateY(18px)'}, '100%':{opacity:'1',transform:'translateY(0)'} },
        draw:   { '0%':{ strokeDashoffset:'1' }, '100%':{ strokeDashoffset:'0' } },
      },
    },
  },
  plugins: [require('@tailwindcss/typography')],
};
