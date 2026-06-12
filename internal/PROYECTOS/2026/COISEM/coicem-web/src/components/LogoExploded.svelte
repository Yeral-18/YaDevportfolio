<!--
  LogoExploded — RECONSTRUCCIÓN APROXIMADA del logo COICEM en SVG por piezas.
  ⚠️ PROTOTIPO: redibujado desde el JPEG (no es el original). Pendiente de validación
     del cliente + del logo vectorial real (ver site-config.pending.logoVector).
  Idea de autor: despiece (explode) → re-ensamblado al entrar en vista; toggle por click.
  Móvil/touch: click. reduced-motion: ensamblado estático. Fallback: SVG siempre visible.
-->
<script lang="ts">
  let assembled = $state(false);   // entra ensamblándose
  let exploded  = $state(false);   // toggle manual
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

  // 12 dientes del engranaje
  const teeth = Array.from({ length: 12 }, (_, i) => i * 30);

  // Piezas: offset de despiece (x,y) + número de parte + etiqueta
  const parts = [
    { id: 'gear',  n: '01', label: 'ENGRANAJE',    ex: 0,   ey: -54 },
    { id: 'build', n: '02', label: 'INFRAESTRUCT', ex: -60, ey: 18 },
    { id: 'wrench',n: '03', label: 'LLAVE',         ex: 58,  ey: 22 },
    { id: 'screw', n: '04', label: 'DESTORNILLADOR',ex: 30,  ey: 62 },
    { id: 'arc',   n: '05', label: 'ARCO',          ex: 64,  ey: -22 },
  ];
  const off = (id: string) => {
    const show = exploded;
    const p = parts.find((q) => q.id === id)!;
    return show ? `translate(${p.ex}px, ${p.ey}px)` : 'translate(0,0)';
  };
</script>

<div
  class="despiece"
  class:assembled
  class:exploded
  bind:this={host}
  role="img"
  aria-label="Logo de COICEM: engranaje con herramientas (reconstrucción)"
  title="Click para despiezar / ensamblar"
  onclick={() => (exploded = !exploded)}
  onkeydown={(e) => { if (e.key === 'Enter' || e.key === ' ') { e.preventDefault(); exploded = !exploded; } }}
  tabindex="0"
>
  <svg viewBox="0 0 400 400" xmlns="http://www.w3.org/2000/svg" aria-hidden="true">
    <!-- 05 arco naranja -->
    <g class="part" style:transform={off('arc')}>
      <path d="M 300 120 A 110 110 0 0 1 300 280" fill="none" stroke="#F79204" stroke-width="14" stroke-linecap="round" opacity="0.95"/>
    </g>

    <!-- 01 engranaje (anillo + dientes) -->
    <g class="part" style:transform={off('gear')}>
      <g transform="translate(200,200)">
        {#each teeth as a}
          <rect x="-9" y="-148" width="18" height="34" rx="2" fill="#313F50" transform={`rotate(${a})`} />
        {/each}
        <circle r="124" fill="none" stroke="#4B6881" stroke-width="20" />
        <circle r="104" fill="#0B0E14" stroke="#313F50" stroke-width="3" />
      </g>
    </g>

    <!-- 02 edificios (azul) -->
    <g class="part" style:transform={off('build')}>
      <g transform="translate(150,168)">
        <rect x="0"  y="20" width="26" height="70" fill="#025199" />
        <rect x="30" y="0"  width="26" height="90" fill="#1A6FB0" />
        <rect x="60" y="34" width="22" height="56" fill="#023F7E" />
      </g>
    </g>

    <!-- 03 llave (metal) -->
    <g class="part" style:transform={off('wrench')}>
      <g transform="translate(214,150) rotate(38)">
        <rect x="-7" y="0" width="14" height="120" rx="5" fill="#8EB9DC" />
        <path d="M -16 -6 a 20 20 0 1 0 32 0 l -7 10 a 9 9 0 1 1 -18 0 z" fill="#8EB9DC" />
      </g>
    </g>

    <!-- 04 destornillador (mango naranja) -->
    <g class="part" style:transform={off('screw')}>
      <g transform="translate(176,150) rotate(40)">
        <rect x="-9" y="0"   width="18" height="64" rx="6" fill="#F79204" />
        <rect x="-4" y="62"  width="8"  height="60" fill="#8EB9DC" />
        <rect x="-3" y="120" width="6"  height="14" fill="#4B6881" />
      </g>
    </g>

    <!-- leader lines + part numbers (visibles al despiezar) -->
    {#each parts as p}
      <g class="leader" style:transform={off(p.id)}>
        <text x={200 + p.ex * 0.0} y={200} font-family="'IBM Plex Mono', monospace" font-size="0"></text>
      </g>
    {/each}
  </svg>

  <!-- Etiquetas de parte (HTML, mono) — sólo visibles al despiezar -->
  <ul class="legend" aria-hidden={!exploded}>
    {#each parts as p}
      <li><span class="num">{p.n}</span> {p.label}</li>
    {/each}
  </ul>

  <span class="proto-tag">RECONSTRUCCIÓN · PENDIENTE VALIDACIÓN</span>
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

  /* Estado inicial: piezas ligeramente separadas + transparentes; al "assembled" convergen */
  .part {
    transform-box: fill-box;
    transform-origin: center;
    transition: transform 700ms cubic-bezier(0.83, 0, 0.17, 1), opacity 500ms ease;
    opacity: 0;
  }
  .assembled .part { opacity: 1; }

  /* En reposo (assembled, no exploded) las piezas están en su sitio (translate 0).
     El style:transform inline maneja explode; aquí sólo la entrada. */
  .despiece:not(.assembled) .part { opacity: 0; }

  .leader { transition: transform 700ms cubic-bezier(0.83,0,0.17,1); }

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
    .part, .leader, .legend { transition: none; }
  }
</style>
