<script>
  import { onMount, onDestroy } from 'svelte';

  let cursorEl;
  let active = false;
  let animId;

  // Current and target positions
  let tx = -100, ty = -100;
  let cx = -100, cy = -100;

  // Lerp factor — lower = smoother/slower
  const LERP = 0.15;

  function lerp(a, b, t) {
    return a + (b - a) * t;
  }

  function onMouseMove(e) {
    tx = e.clientX;
    ty = e.clientY;
  }

  function loop() {
    cx = lerp(cx, tx, LERP);
    cy = lerp(cy, ty, LERP);

    if (cursorEl) {
      // Calculate rotation based on movement direction
      const dx = tx - cx;
      const dy = ty - cy;
      const angle = Math.atan2(dy, dx) * (180 / Math.PI);
      cursorEl.style.transform = `translate3d(${cx - 12}px, ${cy - 12}px, 0) rotate(${angle + 45}deg)`;
    }

    animId = requestAnimationFrame(loop);
  }

  onMount(() => {
    // Only activate on devices with fine pointer (desktop)
    const hasPointer = window.matchMedia('(pointer: fine)').matches;
    const prefersReducedMotion = window.matchMedia('(prefers-reduced-motion: reduce)').matches;

    if (!hasPointer || prefersReducedMotion) return;

    active = true;
    document.body.style.cursor = 'none';
    document.addEventListener('mousemove', onMouseMove, { passive: true });
    animId = requestAnimationFrame(loop);
  });

  onDestroy(() => {
    if (!active) return;
    document.body.style.cursor = '';
    document.removeEventListener('mousemove', onMouseMove);
    if (animId) cancelAnimationFrame(animId);
  });
</script>

{#if active}
  <div class="leaf-cursor" bind:this={cursorEl} aria-hidden="true">
    <svg
      width="24"
      height="24"
      viewBox="0 0 24 24"
      fill="none"
      xmlns="http://www.w3.org/2000/svg"
    >
      <path
        d="M17 8C8 10 5.9 16.17 3.82 21.34l1.89.66.95-2.3c.48.17.98.3 1.34.3C19 20 22 3 22 3c-1 2-8 2.25-13 3.25S2 11.5 2 13.5s1.75 3.75 1.75 3.75"
        fill="#1B5E20"
        stroke="#1B5E20"
        stroke-width="0.5"
        stroke-linecap="round"
        stroke-linejoin="round"
      />
    </svg>
  </div>
{/if}

<style>
  .leaf-cursor {
    position: fixed;
    top: 0;
    left: 0;
    width: 24px;
    height: 24px;
    pointer-events: none;
    z-index: 9999;
    will-change: transform;
  }
</style>
