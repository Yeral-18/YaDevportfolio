<script>
  import { onMount, onDestroy } from 'svelte';

  let progress = 0;
  let ticking = false;

  function onScroll() {
    if (!ticking) {
      requestAnimationFrame(() => {
        const scrollTop = window.scrollY || document.documentElement.scrollTop;
        const docHeight = document.documentElement.scrollHeight - document.documentElement.clientHeight;
        progress = docHeight > 0 ? scrollTop / docHeight : 0;
        ticking = false;
      });
      ticking = true;
    }
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

<div class="progress-bar-track">
  <div class="progress-bar-fill" style="transform: scaleX({progress})"></div>
</div>

<style>
  .progress-bar-track {
    position: fixed;
    top: 0;
    left: 0;
    width: 100%;
    height: 3px;
    background: transparent;
    z-index: 9999;
    pointer-events: none;
  }

  .progress-bar-fill {
    width: 100%;
    height: 100%;
    background: linear-gradient(to right, #1B5E20, #7CB342, #0277A8);
    transform-origin: left;
    transition: transform 0.15s ease-out;
  }
</style>
