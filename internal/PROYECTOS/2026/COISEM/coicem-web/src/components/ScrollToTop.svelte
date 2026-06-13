<!--
  ScrollToTop — botón cuadrado brutalist que vuelve al inicio.
  Se apila ENCIMA del WhatsApp (bottom 6rem). Aparece tras scrollY > 400.
  reduced-motion → scroll instantáneo y sin animación de entrada.
-->
<script lang="ts">
  import { siteConfig } from '../lib/site-config';
  // siteConfig importado por convención del proyecto (punto único de verdad).
  void siteConfig;

  let visible = $state(false);
  let reduced = $state(false);

  $effect(() => {
    if (typeof window === 'undefined') return;
    reduced = window.matchMedia('(prefers-reduced-motion: reduce)').matches;

    const onScroll = () => { visible = window.scrollY > 400; };
    onScroll();
    window.addEventListener('scroll', onScroll, { passive: true });
    return () => window.removeEventListener('scroll', onScroll);
  });

  function toTop() {
    window.scrollTo({ top: 0, behavior: reduced ? 'auto' : 'smooth' });
  }
</script>

<button
  class="top"
  class:visible
  class:reduced
  type="button"
  onclick={toTop}
  aria-label="Volver al inicio"
>
  <svg viewBox="0 0 24 24" width="20" height="20" aria-hidden="true">
    <path
      fill="none"
      stroke="#F79204"
      stroke-width="2"
      stroke-linecap="square"
      stroke-linejoin="miter"
      d="M6 14l6-6 6 6"
    />
  </svg>
</button>

<style>
  .top {
    position: fixed;
    right: 1.5rem;
    bottom: 6rem;
    z-index: 8999;
    display: grid;
    place-items: center;
    width: 44px;
    height: 44px;
    border-radius: 0;            /* brutalist: bordes duros */
    background: #0B0E14;
    border: 1px solid #313F50;
    cursor: pointer;
    pointer-events: none;
    opacity: 0;
    transform: translateY(10px);
    transition: opacity 280ms cubic-bezier(0.83, 0, 0.17, 1),
                transform 280ms cubic-bezier(0.83, 0, 0.17, 1),
                border-color 140ms ease;
  }
  .top.visible {
    opacity: 1;
    transform: translateY(0);
    pointer-events: auto;
  }
  .top:hover  { border-color: #F79204; }
  .top:focus-visible { outline: 2px solid #F79204; outline-offset: 3px; }

  /* reduced-motion: sin animación de entrada */
  .top.reduced { transition: border-color 140ms ease; transform: none; }
  .top.reduced.visible { transform: none; }
  @media (prefers-reduced-motion: reduce) {
    .top { transition: border-color 140ms ease; transform: none; }
    .top.visible { transform: none; }
  }
</style>
