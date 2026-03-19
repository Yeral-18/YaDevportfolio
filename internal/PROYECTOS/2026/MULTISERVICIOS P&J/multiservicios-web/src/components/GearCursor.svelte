<script>
  /**
   * GearCursor - Custom cursor for MULTISERVICIOS P&J
   * Industrial gear/cog that follows the mouse with smooth animation
   * Similar approach to ECOMAG's leaf but completely different visual
   */

  let cursorEl = $state(null);
  let active = $state(false);

  $effect(() => {
    // Only on desktop with fine pointer, respect reduced motion
    const isFinePointer = window.matchMedia('(pointer: fine)').matches;
    const prefersReducedMotion = window.matchMedia('(prefers-reduced-motion: reduce)').matches;

    if (!isFinePointer || prefersReducedMotion) return;

    active = true;
    document.body.style.cursor = 'none';

    let mouseX = 0;
    let mouseY = 0;
    let curX = 0;
    let curY = 0;
    let rotation = 0;
    let speed = 0;
    let prevX = 0;
    let prevY = 0;
    let animFrame;

    const onMouseMove = (e) => {
      mouseX = e.clientX;
      mouseY = e.clientY;
    };

    const lerp = (a, b, t) => a + (b - a) * t;

    const animate = () => {
      // Calculate speed for rotation
      const dx = mouseX - prevX;
      const dy = mouseY - prevY;
      speed = Math.sqrt(dx * dx + dy * dy);
      prevX = mouseX;
      prevY = mouseY;

      // Smooth follow
      curX = lerp(curX, mouseX, 0.15);
      curY = lerp(curY, mouseY, 0.15);

      // Gear rotates based on movement speed (industrial feel)
      rotation += speed * 0.8;

      if (cursorEl) {
        cursorEl.style.transform = `translate(${curX - 12}px, ${curY - 12}px) rotate(${rotation}deg)`;
      }

      animFrame = requestAnimationFrame(animate);
    };

    window.addEventListener('mousemove', onMouseMove, { passive: true });
    animFrame = requestAnimationFrame(animate);

    // Hide on interactive elements
    const addHoverListeners = () => {
      const interactives = document.querySelectorAll('a, button, input, textarea, select, [role="button"]');
      interactives.forEach((el) => {
        el.addEventListener('mouseenter', () => {
          if (cursorEl) cursorEl.style.opacity = '0.4';
          if (cursorEl) cursorEl.style.transform += ' scale(0.6)';
        });
        el.addEventListener('mouseleave', () => {
          if (cursorEl) cursorEl.style.opacity = '1';
        });
      });
    };

    // Run after DOM is ready
    setTimeout(addHoverListeners, 500);

    return () => {
      window.removeEventListener('mousemove', onMouseMove);
      cancelAnimationFrame(animFrame);
      document.body.style.cursor = '';
    };
  });
</script>

{#if active}
  <div class="gear-cursor" bind:this={cursorEl}>
    <svg
      xmlns="http://www.w3.org/2000/svg"
      width="24"
      height="24"
      viewBox="0 0 24 24"
      fill="none"
    >
      <!-- Gear/Cog shape - industrial identity -->
      <path
        d="M12 15a3 3 0 1 0 0-6 3 3 0 0 0 0 6Z"
        fill="#0089D0"
        fill-opacity="0.9"
      />
      <path
        d="M19.4 15a1.65 1.65 0 0 0 .33 1.82l.06.06a2 2 0 0 1-2.83 2.83l-.06-.06a1.65 1.65 0 0 0-1.82-.33 1.65 1.65 0 0 0-1 1.51V21a2 2 0 0 1-4 0v-.09A1.65 1.65 0 0 0 9 19.4a1.65 1.65 0 0 0-1.82.33l-.06.06a2 2 0 0 1-2.83-2.83l.06-.06A1.65 1.65 0 0 0 4.68 15a1.65 1.65 0 0 0-1.51-1H3a2 2 0 0 1 0-4h.09A1.65 1.65 0 0 0 4.6 9a1.65 1.65 0 0 0-.33-1.82l-.06-.06a2 2 0 0 1 2.83-2.83l.06.06A1.65 1.65 0 0 0 9 4.68a1.65 1.65 0 0 0 1-1.51V3a2 2 0 0 1 4 0v.09a1.65 1.65 0 0 0 1 1.51 1.65 1.65 0 0 0 1.82-.33l.06-.06a2 2 0 0 1 2.83 2.83l-.06.06A1.65 1.65 0 0 0 19.4 9a1.65 1.65 0 0 0 1.51 1H21a2 2 0 0 1 0 4h-.09a1.65 1.65 0 0 0-1.51 1Z"
        fill="#0089D0"
        fill-opacity="0.6"
        stroke="#0089D0"
        stroke-width="0.5"
        stroke-opacity="0.8"
      />
    </svg>
  </div>
{/if}

<style>
  .gear-cursor {
    position: fixed;
    top: 0;
    left: 0;
    width: 24px;
    height: 24px;
    pointer-events: none;
    z-index: 9999;
    will-change: transform;
    transition: opacity 0.2s ease;
  }

  /* Hide cursor on all elements globally */
  :global(body.gear-active),
  :global(body.gear-active *) {
    cursor: none !important;
  }
</style>
