<!--
  CrosshairCursor — cursor de marca COICEM: retícula/calibre técnico con lectura
  de coordenadas en mono. NO es el cursor engranaje (prohibido, es de Multiservicios).
  Oculto en touch; reduced-motion → sin lerp (sigue directo).
-->
<script lang="ts">
  let x = $state(-100);
  let y = $state(-100);
  let tx = -100, ty = -100;
  let active = $state(false);
  let enabled = $state(false);

  $effect(() => {
    if (typeof window === 'undefined') return;
    const fine = window.matchMedia('(pointer: fine)').matches;
    if (!fine) return;                 // touch → sin cursor custom
    enabled = true;
    document.documentElement.classList.add('has-crosshair');

    const reduced = window.matchMedia('(prefers-reduced-motion: reduce)').matches;
    let raf = 0;

    const onMove = (e: PointerEvent) => {
      tx = e.clientX; ty = e.clientY;
      active = true;
      if (reduced) { x = tx; y = ty; }
    };
    const onDown = () => document.documentElement.classList.add('cursor-down');
    const onUp   = () => document.documentElement.classList.remove('cursor-down');
    const onLeave = () => (active = false);

    const loop = () => {
      x += (tx - x) * 0.22;            // lerp
      y += (ty - y) * 0.22;
      raf = requestAnimationFrame(loop);
    };
    if (!reduced) raf = requestAnimationFrame(loop);

    window.addEventListener('pointermove', onMove, { passive: true });
    window.addEventListener('pointerdown', onDown);
    window.addEventListener('pointerup', onUp);
    document.addEventListener('mouseleave', onLeave);

    return () => {
      cancelAnimationFrame(raf);
      window.removeEventListener('pointermove', onMove);
      window.removeEventListener('pointerdown', onDown);
      window.removeEventListener('pointerup', onUp);
      document.removeEventListener('mouseleave', onLeave);
      document.documentElement.classList.remove('has-crosshair', 'cursor-down');
    };
  });
</script>

{#if enabled}
  <div class="cross" class:active style:left={`${x}px`} style:top={`${y}px`} aria-hidden="true">
    <span class="h"></span>
    <span class="v"></span>
    <span class="dot"></span>
    <span class="coord">{Math.round(x)},{Math.round(y)}</span>
  </div>
{/if}

<style>
  :global(html.has-crosshair),
  :global(html.has-crosshair *) { cursor: none; }

  .cross {
    position: fixed; top: 0; left: 0; z-index: 9000;
    width: 0; height: 0; pointer-events: none;
    opacity: 0; transition: opacity 160ms ease;
  }
  .cross.active { opacity: 1; }

  .cross .h, .cross .v { position: absolute; background: #F79204; }
  .cross .h { width: 26px; height: 1px; transform: translate(-13px, 0); }
  .cross .v { width: 1px; height: 26px; transform: translate(0, -13px); }
  .cross .dot {
    position: absolute; width: 5px; height: 5px;
    border: 1px solid #F79204; transform: translate(-2.5px, -2.5px);
  }
  .cross .coord {
    position: absolute; left: 12px; top: 12px;
    font-family: 'IBM Plex Mono', monospace; font-size: 10px;
    color: #4B6881; white-space: nowrap; letter-spacing: 0.02em;
  }
  :global(html.cursor-down) .cross .dot { background: #F79204; }

  @media (prefers-reduced-motion: reduce) {
    .cross { transition: none; }
  }
</style>
