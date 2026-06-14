<script lang="ts">
  import { siteConfig } from '../lib/site-config';

  // ─── Índice numerado: Inicio (00) + 5 áreas + Contacto (06) ───
  type Item = { label: string; href: string; n: string };

  const items: Item[] = [
    { label: 'Inicio', href: '#inicio', n: '00' },
    ...siteConfig.areas.map((a) => ({ label: a.name, href: '#' + a.id, n: a.n })),
    { label: 'Contacto', href: '#contacto', n: '06' },
  ];

  // ─── Estado (Svelte 5 runes) ─────────────────────────────────
  let open = $state(false);          // overlay móvil
  let activeId = $state(items[0].href.slice(1)); // id de la sección activa (scroll-spy)

  const sectionIds = items.map((i) => i.href.slice(1));

  // ─── Scroll-spy con IntersectionObserver ─────────────────────
  $effect(() => {
    if (typeof document === 'undefined') return;

    const sections = sectionIds
      .map((id) => document.getElementById(id))
      .filter((el): el is HTMLElement => el !== null);

    if (sections.length === 0) return;

    // La sección "más visible / más arriba" marca el item activo.
    const visible = new Map<string, number>();

    const observer = new IntersectionObserver(
      (entries) => {
        for (const entry of entries) {
          if (entry.isIntersecting) visible.set(entry.target.id, entry.intersectionRatio);
          else visible.delete(entry.target.id);
        }
        if (visible.size === 0) return;
        // Elige la sección visible que aparezca primero en el orden del índice.
        for (const id of sectionIds) {
          if (visible.has(id)) {
            activeId = id;
            break;
          }
        }
      },
      { rootMargin: '-45% 0px -45% 0px', threshold: [0, 0.25, 0.5, 0.75, 1] }
    );

    for (const s of sections) observer.observe(s);

    return () => observer.disconnect();
  });

  // ─── Bloqueo de scroll del body cuando el overlay está abierto ─
  $effect(() => {
    if (typeof document === 'undefined') return;
    document.body.style.overflow = open ? 'hidden' : '';
    return () => {
      document.body.style.overflow = '';
    };
  });

  function toggle() {
    open = !open;
  }

  function close() {
    open = false;
  }

  function onItemClick() {
    // Al navegar desde el overlay, ciérralo.
    close();
  }

  function onKeydown(e: KeyboardEvent) {
    if (e.key === 'Escape' && open) {
      e.preventDefault();
      close();
    }
  }
</script>

<svelte:window on:keydown={onKeydown} />

<!-- ════════════════ RIEL VERTICAL FIJO (DESKTOP ≥1024px) ════════════════ -->
<nav class="rail" aria-label="Índice de navegación principal">
  <a class="rail-head" href="#inicio" aria-label={`${siteConfig.shortName} S.A.S — inicio`}>
    <img class="rail-logo" src="/images/coicem-logo.png" alt={`${siteConfig.shortName} S.A.S`} />
  </a>

  <ul class="rail-list">
    {#each items as item (item.href)}
      <li>
        <a
          class="rail-item"
          class:active={activeId === item.href.slice(1)}
          href={item.href}
          aria-current={activeId === item.href.slice(1) ? 'true' : undefined}
        >
          <span class="num">{item.n}</span>
          <span class="label">{item.label}</span>
        </a>
      </li>
    {/each}
  </ul>
</nav>

<!-- ════════════════ TOP-BAR SLIM (MÓVIL <1024px) ════════════════ -->
<div class="topbar">
  <img class="bar-logo" src="/images/coicem-logo.png" alt={`${siteConfig.shortName} S.A.S`} />
  <button
    class="burger"
    type="button"
    aria-label="Abrir menú de navegación"
    aria-expanded={open}
    aria-controls="coicem-nav-overlay"
    onclick={toggle}
  >
    <span class="burger-line"></span>
    <span class="burger-line"></span>
    <span class="burger-line"></span>
  </button>
</div>

<!-- ════════════════ OVERLAY FULLSCREEN (MÓVIL) ════════════════ -->
<div
  id="coicem-nav-overlay"
  class="overlay"
  class:open
  role="dialog"
  aria-modal="true"
  aria-label="Navegación principal"
  aria-hidden={!open}
>
  <div class="overlay-head">
    <img class="bar-logo" src="/images/coicem-logo.png" alt={`${siteConfig.shortName} S.A.S`} />
    <button class="close" type="button" aria-label="Cerrar menú" onclick={close}>
      <span class="close-x" aria-hidden="true">✕</span>
    </button>
  </div>

  <nav class="overlay-nav" aria-label="Índice de navegación (móvil)">
    <ul class="overlay-list">
      {#each items as item (item.href)}
        <li>
          <a
            class="overlay-item"
            class:active={activeId === item.href.slice(1)}
            href={item.href}
            tabindex={open ? 0 : -1}
            onclick={onItemClick}
          >
            <span class="num">{item.n}</span>
            <span class="label">{item.label}</span>
          </a>
        </li>
      {/each}
    </ul>
  </nav>
</div>

<!-- ════════════════ CTA INFERIOR FIJO (MÓVIL — SISTEMA) ════════════════ -->
<div class="bottom-cta">
  <a class="cta-btn" href="#contacto">Cotizar</a>
</div>

<style>
  /* ─── Tokens locales ─────────────────────────────────────── */
  :where(.rail, .topbar, .overlay, .bottom-cta) {
    --metal-base: #0b0e14;
    --metal-border: #313f50;
    --metal-light: #4b6881;
    --azul: #025199;
    --naranja: #f79204;
    --texto: #edede8;
    --font-display: 'Archivo Expanded', 'Archivo', sans-serif;
    --font-body: 'IBM Plex Sans', sans-serif;
    --font-mono: 'IBM Plex Mono', monospace;
  }

  /* ═══════════ RIEL VERTICAL (DESKTOP) ═══════════ */
  .rail {
    display: none;
  }

  @media (min-width: 1024px) {
    .rail {
      display: flex;
      flex-direction: column;
      position: fixed;
      top: 0;
      left: 0;
      width: 210px;
      height: 100vh;
      background: var(--metal-base);
      border-right: 1px solid var(--metal-border);
      z-index: 50;
      overflow-y: auto;
    }
    /* Ocultar elementos móviles en desktop */
    .topbar,
    .overlay,
    .bottom-cta {
      display: none !important;
    }
  }

  .rail-head {
    display: flex;
    flex-direction: column;
    padding: 24px 20px 20px;
    border-bottom: 1px solid var(--metal-border);
  }

  .rail-head { display: block; text-decoration: none; }
  .rail-logo { display: block; width: 100%; max-width: 160px; height: auto; }
  .bar-logo { display: block; height: 30px; width: auto; }
  .overlay-head .bar-logo { height: 34px; }

  .rail-list {
    list-style: none;
    margin: 0;
    padding: 12px 0;
  }

  .rail-item {
    display: flex;
    align-items: baseline;
    gap: 12px;
    padding: 11px 20px;
    text-decoration: none;
    border-left: 3px solid transparent;
    transition: color 160ms linear, border-color 160ms linear, background 160ms linear;
  }

  .rail-item .num {
    font-family: var(--font-mono);
    font-size: 0.75rem;
    color: var(--metal-light);
    min-width: 1.4em;
    transition: color 160ms linear;
  }

  .rail-item .label {
    font-family: var(--font-body);
    text-transform: uppercase;
    letter-spacing: 0.12em;
    font-size: 0.8rem;
    color: var(--texto);
    transition: color 160ms linear;
  }

  .rail-item:hover {
    background: rgba(2, 81, 153, 0.14);
  }

  .rail-item.active {
    border-left-color: var(--naranja);
  }

  .rail-item.active .num,
  .rail-item.active .label {
    color: var(--naranja);
  }

  .rail-item:focus-visible {
    outline: 2px solid var(--naranja);
    outline-offset: -2px;
  }

  /* ═══════════ TOP-BAR SLIM (MÓVIL) ═══════════ */
  .topbar {
    position: fixed;
    top: 0;
    left: 0;
    right: 0;
    height: 52px;
    display: flex;
    align-items: center;
    justify-content: space-between;
    padding: 0 16px;
    background: var(--metal-base);
    border-bottom: 1px solid var(--metal-border);
    z-index: 60;
  }

  .burger {
    display: flex;
    flex-direction: column;
    justify-content: center;
    gap: 5px;
    width: 44px;
    height: 44px;
    padding: 0 8px;
    background: transparent;
    border: 1px solid var(--metal-border);
    cursor: pointer;
  }

  .burger-line {
    display: block;
    height: 2px;
    width: 100%;
    background: var(--texto);
  }

  .burger:focus-visible {
    outline: 2px solid var(--naranja);
    outline-offset: 2px;
  }

  /* ═══════════ OVERLAY FULLSCREEN (MÓVIL) ═══════════ */
  .overlay {
    position: fixed;
    inset: 0;
    z-index: 80;
    background: var(--metal-base);
    display: flex;
    flex-direction: column;
    /* Estado cerrado: clip + translate, no interactivo */
    clip-path: inset(0 0 100% 0);
    transform: translateY(-8px);
    opacity: 0;
    pointer-events: none;
    transition:
      clip-path 320ms cubic-bezier(0.83, 0, 0.17, 1),
      transform 320ms cubic-bezier(0.83, 0, 0.17, 1),
      opacity 320ms cubic-bezier(0.83, 0, 0.17, 1);
  }

  .overlay.open {
    clip-path: inset(0 0 0 0);
    transform: translateY(0);
    opacity: 1;
    pointer-events: auto;
  }

  .overlay-head {
    display: flex;
    align-items: center;
    justify-content: space-between;
    height: 52px;
    padding: 0 16px;
    border-bottom: 1px solid var(--metal-border);
    flex-shrink: 0;
  }

  .close {
    display: flex;
    align-items: center;
    justify-content: center;
    width: 48px;
    height: 48px;
    background: transparent;
    border: 1px solid var(--metal-border);
    color: var(--texto);
    cursor: pointer;
  }

  .close-x {
    font-family: var(--font-mono);
    font-size: 1.25rem;
    line-height: 1;
  }

  .close:focus-visible {
    outline: 2px solid var(--naranja);
    outline-offset: 2px;
  }

  .overlay-nav {
    flex: 1;
    overflow-y: auto;
  }

  .overlay-list {
    list-style: none;
    margin: 0;
    padding: 8px 0;
  }

  .overlay-item {
    display: flex;
    align-items: baseline;
    gap: 16px;
    min-height: 48px;
    padding: 14px 24px;
    text-decoration: none;
    border-bottom: 1px solid rgba(49, 63, 80, 0.5);
    border-left: 3px solid transparent;
  }

  .overlay-item .num {
    font-family: var(--font-mono);
    font-size: 1rem;
    color: var(--naranja);
    min-width: 1.6em;
  }

  .overlay-item .label {
    font-family: var(--font-body);
    text-transform: uppercase;
    letter-spacing: 0.1em;
    font-size: 1.25rem;
    color: var(--texto);
  }

  .overlay-item.active {
    border-left-color: var(--naranja);
    background: rgba(2, 81, 153, 0.14);
  }

  .overlay-item:focus-visible {
    outline: 2px solid var(--naranja);
    outline-offset: -2px;
  }

  /* ═══════════ CTA INFERIOR FIJO (MÓVIL) ═══════════ */
  .bottom-cta {
    position: fixed;
    bottom: 0;
    left: 0;
    right: 0;
    z-index: 70;
    padding: 8px;
    background: var(--metal-base);
    border-top: 1px solid var(--metal-border);
  }

  .cta-btn {
    display: flex;
    align-items: center;
    justify-content: center;
    width: 100%;
    min-height: 48px;
    background: var(--naranja);
    color: #000;
    font-family: var(--font-mono);
    text-transform: uppercase;
    letter-spacing: 0.16em;
    font-size: 0.9rem;
    font-weight: 600;
    text-decoration: none;
  }

  .cta-btn:focus-visible {
    outline: 2px solid var(--texto);
    outline-offset: 2px;
  }

  /* ═══════════ PREFERS-REDUCED-MOTION ═══════════ */
  @media (prefers-reduced-motion: reduce) {
    .overlay {
      transition: none;
    }
    .rail-item,
    .rail-item .num,
    .rail-item .label {
      transition: none;
    }
  }
</style>
