<!--
  LogoExploded — Despiece del logo COICEM (emblema reconstruido Versión B).
  Misma geometría que brand/generate-logo.mjs: engranaje 14 dientes + skyline +
  línea base + herramientas cruzadas + arco naranja. Coherente con navbar/footer.
  Idea de autor: las piezas entran ensamblándose y se despiezan (explode) al click.
  Móvil/touch: click. reduced-motion: estático. Fallback: SVG siempre visible.
-->
<script lang="ts">
  let assembled = $state(false);
  let exploded  = $state(false);
  let host = $state<HTMLElement | null>(null);

  const reduced = typeof window !== 'undefined'
    && window.matchMedia?.('(prefers-reduced-motion: reduce)').matches;

  $effect(() => {
    if (!host) return;
    if (reduced) { assembled = true; return; }
    const io = new IntersectionObserver((es) => {
      es.forEach((e) => { if (e.isIntersecting) { assembled = true; io.unobserve(e.target); } });
    }, { threshold: 0.3 });
    io.observe(host);
    return () => io.disconnect();
  });

  // ─── Geometría del emblema B (igual que generate-logo.mjs) ───
  function gearPath(cx: number, cy: number, teeth: number, rOut: number, rIn: number): string {
    const pts: [number, number][] = [];
    const step = (Math.PI * 2) / teeth;
    for (let i = 0; i < teeth; i++) {
      const a = i * step;
      pts.push([a + step * 0.00, rIn]);
      pts.push([a + step * 0.18, rOut]);
      pts.push([a + step * 0.32, rOut]);
      pts.push([a + step * 0.50, rIn]);
    }
    return pts.map(([ang, r], i) =>
      (i === 0 ? 'M' : 'L') + (cx + Math.cos(ang) * r).toFixed(2) + ' ' + (cy + Math.sin(ang) * r).toFixed(2)
    ).join(' ') + 'Z';
  }
  function arcPath(cx: number, cy: number, r: number, w: number, a0: number, a1: number): string {
    const rad = (d: number) => (d * Math.PI) / 180;
    const p = (ang: number, rr: number): [string, string] =>
      [(cx + Math.cos(ang) * rr).toFixed(2), (cy + Math.sin(ang) * rr).toFixed(2)];
    const [x0, y0] = p(rad(a0), r), [x1, y1] = p(rad(a1), r);
    const [x2, y2] = p(rad(a1), r - w), [x3, y3] = p(rad(a0), r - w);
    const large = Math.abs(a1 - a0) > 180 ? 1 : 0;
    return `M ${x0} ${y0} A ${r} ${r} 0 ${large} 1 ${x1} ${y1} L ${x2} ${y2} A ${r - w} ${r - w} 0 ${large} 0 ${x3} ${y3} Z`;
  }

  const GEAR = gearPath(100, 100, 14, 98, 87);
  const ARC  = arcPath(100, 100, 74, 8, -102, 34);

  // Ventanas de los edificios (mismas posiciones que el emblema)
  const win: [number, number][] = [];
  for (const y of [62, 70, 78, 86, 94]) { win.push([79, y]); win.push([85, y]); }
  for (const y of [76, 84, 92, 100]) { win.push([96, y]); win.push([103, y]); }
  for (const y of [86, 94, 102]) { win.push([116, y]); }

  // ─── Despiece: offset por pieza + nº de parte ───
  const parts = [
    { id: 'gear',  n: '01', label: 'ENGRANAJE',     ex: 0,   ey: -30 },
    { id: 'build', n: '02', label: 'INFRAESTRUCT.',  ex: -30, ey: 6  },
    { id: 'wrench',n: '03', label: 'LLAVE',          ex: 30,  ey: 14 },
    { id: 'screw', n: '04', label: 'DESTORNILLADOR', ex: 14,  ey: 32 },
    { id: 'arc',   n: '05', label: 'ARCO',           ex: 30,  ey: -16 },
  ];
  const off = (id: string) => {
    const p = parts.find((q) => q.id === id)!;
    return exploded ? `translate(${p.ex}px, ${p.ey}px)` : 'translate(0,0)';
  };
</script>

<div
  class="despiece"
  class:assembled
  class:exploded
  bind:this={host}
  role="img"
  aria-label="Logo de COICEM: engranaje con edificios y herramientas (reconstrucción)"
  title="Click para despiezar / ensamblar"
  onclick={() => (exploded = !exploded)}
  onkeydown={(e) => { if (e.key === 'Enter' || e.key === ' ') { e.preventDefault(); exploded = !exploded; } }}
  tabindex="0"
>
  <svg viewBox="0 0 200 200" xmlns="http://www.w3.org/2000/svg" aria-hidden="true">
    <!-- 01 engranaje + anillo + cara -->
    <g class="part" style:transform={off('gear')}>
      <path d={GEAR} fill="#313F50" />
      <circle cx="100" cy="100" r="82" fill="#26303D" />
      <circle cx="100" cy="100" r="76" fill="#FFFFFF" />
    </g>

    <!-- 05 arco naranja -->
    <g class="part" style:transform={off('arc')}>
      <path d={ARC} fill="#F79204" />
    </g>

    <!-- 03 llave (zona inferior) -->
    <g class="part" style:transform={off('wrench')}>
      <g transform="translate(100 134) rotate(-34)" fill="#313F50">
        <rect x="-3.2" y="-26" width="6.4" height="30" rx="3.2" />
        <path fill-rule="evenodd" d="M 0 14 a 10 10 0 1 0 0.01 0 Z M 0 19 a 4.6 4.6 0 1 1 -0.01 0 Z M -4.8 10 L 4.8 10 L 4.8 19 L -4.8 19 Z" />
      </g>
    </g>

    <!-- 04 destornillador (mango naranja) -->
    <g class="part" style:transform={off('screw')}>
      <g transform="translate(100 134) rotate(34)">
        <rect x="-4" y="6" width="8" height="20" rx="4" fill="#F79204" />
        <rect x="-2.1" y="-22" width="4.2" height="28" fill="#26303D" />
        <rect x="-3" y="-26" width="6" height="4.5" fill="#26303D" />
      </g>
    </g>

    <!-- 02 edificios + línea base (encima, zona superior) -->
    <g class="part" style:transform={off('build')}>
      <rect x="44" y="108" width="112" height="2" fill="#6B7C90" />
      <rect x="76" y="56" width="14" height="53" fill="#025199" />
      <rect x="92" y="70" width="18" height="39" fill="#025199" />
      <rect x="112" y="80" width="12" height="29" fill="#025199" />
      {#each win as [x, y]}
        <rect x={x} y={y} width="3" height="3.4" fill="#FFFFFF" />
      {/each}
    </g>
  </svg>

  <!-- Etiquetas de parte (sólo al despiezar) -->
  <ul class="legend" aria-hidden={!exploded}>
    {#each parts as p}
      <li><span class="num">{p.n}</span> {p.label}</li>
    {/each}
  </ul>

  <span class="proto-tag">RECONSTRUCCIÓN B · PENDIENTE VALIDACIÓN</span>
</div>

<style>
  .despiece {
    position: relative;
    width: 100%;
    max-width: 420px;
    margin: 0 auto;
    cursor: pointer;
    outline: none;
  }
  .despiece:focus-visible { outline: 2px solid #F79204; outline-offset: 4px; }

  svg { width: 100%; height: auto; display: block; }

  .part {
    transform-box: fill-box;
    transform-origin: center;
    transition: transform 700ms cubic-bezier(0.83, 0, 0.17, 1), opacity 500ms ease;
    opacity: 0;
  }
  .assembled .part { opacity: 1; }
  .despiece:not(.assembled) .part { opacity: 0; }

  .legend {
    list-style: none; margin: 14px 0 0; padding: 0;
    display: grid; grid-template-columns: repeat(2, 1fr); gap: 4px 14px;
    font-family: 'IBM Plex Mono', monospace; font-size: 11px;
    color: #4B6881; text-transform: uppercase; letter-spacing: 0.04em;
    opacity: 0; transition: opacity 300ms ease; pointer-events: none;
  }
  .exploded .legend { opacity: 1; }
  .legend .num { color: #F79204; }

  .proto-tag {
    display: block; margin-top: 10px;
    font-family: 'IBM Plex Mono', monospace; font-size: 9.5px;
    letter-spacing: 0.12em; color: #4B6881; text-transform: uppercase;
    border-top: 1px solid #313F50; padding-top: 6px;
  }

  @media (prefers-reduced-motion: reduce) {
    .part, .legend { transition: none; }
  }
</style>
