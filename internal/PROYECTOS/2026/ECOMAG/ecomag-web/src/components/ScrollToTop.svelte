<script>
  import { onMount, onDestroy } from 'svelte';

  let visible = false;
  let ticking = false;

  function onScroll() {
    if (!ticking) {
      requestAnimationFrame(() => {
        visible = window.scrollY > 400;
        ticking = false;
      });
      ticking = true;
    }
  }

  function scrollToTop() {
    window.scrollTo({ top: 0, behavior: 'smooth' });
  }

  onMount(() => {
    window.addEventListener('scroll', onScroll, { passive: true });
    onScroll();
  });

  onDestroy(() => {
    if (typeof window !== 'undefined') {
      window.removeEventListener('scroll', onScroll);
    }
  });
</script>

<button
  class="scroll-to-top"
  class:visible
  on:click={scrollToTop}
  aria-label="Volver al inicio"
>
  <svg
    xmlns="http://www.w3.org/2000/svg"
    width="22"
    height="22"
    viewBox="0 0 24 24"
    fill="none"
    stroke="#1B5E20"
    stroke-width="2.5"
    stroke-linecap="round"
    stroke-linejoin="round"
  >
    <polyline points="18 15 12 9 6 15" />
  </svg>
</button>

<style>
  .scroll-to-top {
    position: fixed;
    bottom: 6rem;
    right: 1.25rem;
    z-index: 45;
    width: 44px;
    height: 44px;
    border-radius: 50%;
    border: 2px solid rgba(27, 94, 32, 0.35);
    background: rgba(255, 255, 255, 0.95);
    box-shadow: 0 2px 10px rgba(27, 94, 32, 0.2), 0 0 0 0 rgba(27, 94, 32, 0.15);
    cursor: pointer;
    display: flex;
    align-items: center;
    justify-content: center;
    opacity: 0;
    transform: scale(0.8);
    pointer-events: none;
    transition: opacity 0.3s ease, transform 0.3s ease, box-shadow 0.2s ease, border-color 0.2s ease;
  }

  .scroll-to-top.visible {
    opacity: 1;
    transform: scale(1);
    pointer-events: auto;
    animation: scrollTopPulse 2.5s ease-in-out infinite;
  }

  @keyframes scrollTopPulse {
    0%, 100% { box-shadow: 0 2px 10px rgba(27, 94, 32, 0.2), 0 0 0 0 rgba(27, 94, 32, 0.15); }
    50% { box-shadow: 0 2px 10px rgba(27, 94, 32, 0.2), 0 0 0 6px rgba(27, 94, 32, 0); }
  }

  @media (min-width: 640px) {
    .scroll-to-top {
      bottom: 8rem;
      right: 2rem;
      width: 44px;
      height: 44px;
    }
  }

  .scroll-to-top:hover {
    transform: scale(1.1);
    box-shadow: 0 4px 16px rgba(27, 94, 32, 0.35);
    border-color: rgba(27, 94, 32, 0.5);
    animation: none;
  }
</style>
