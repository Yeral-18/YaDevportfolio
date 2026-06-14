<script lang="ts">
  import { siteConfig } from '../lib/site-config';

  // ─── Navegación horizontal: índice técnico arriba (datasheet header) ───
  // Brutalist: barra fija, fondo grafito sólido, borde duro 1px, mono.
  // NO glassy/blur (eso es de los otros proyectos) → mantiene ADN único.
  type Item = { label: string; href: string; n: string };

  const items: Item[] = [
    { label: 'Inicio',    href: '#inicio',    n: '00' },
    { label: 'Nosotros',  href: '#nosotros',  n: '01' },
    { label: 'Áreas',     href: '#areas',     n: '02' },
    { label: 'Contacto',  href: '#contacto',  n: '03' },
  ];

  const sectionIds = items.map((i) => i.href.slice(1));

  let open = $state(false);                          // overlay móvil
  let scrolled = $state(false);                      // sombra/estado al hacer scroll
  let activeId = $state(items[0].href.slice(1));     // scroll-spy

  // ─── Scroll-spy ──────────────────────────────────────────────
  $effect(() => {
    if (typeof document === 'undefined') return;
    const sections = sectionIds
      .map((id) => document.getElementById(id))
      .filter((el): el is HTMLElement => el !== null);
    if (sections.length === 0) return;

    const visible = new Map<string, number>();
    const observer = new IntersectionObserver(
      (entries) => {
        for (const entry of entries) {
          if (entry.isIntersecting) visible.set(entry.target.id, entry.intersectionRatio);
          else visible.delete(entry.target.id);
        }
        if (visible.size === 0) return;
        for (const id of sectionIds) {
          if (visible.has(id)) { activeId = id; break; }
        }
      },
      { rootMargin: '-50% 0px -50% 0px', threshold: [0, 0.25, 0.5, 0.75, 1] }
    );
    for (const s of sections) observer.observe(s);
    return () => observer.disconnect();
  });

  // ─── Sombra al hacer scroll ──────────────────────────────────
  $effect(() => {
    if (typeof window === 'undefined') return;
    const onScroll = () => { scrolled = window.scrollY > 8; };
    onScroll();
    window.addEventListener('scroll', onScroll, { passive: true });
    return () => window.removeEventListener('scroll', onScroll);
  });

  // ─── Bloqueo de scroll cuando el overlay está abierto ────────
  $effect(() => {
    if (typeof document === 'undefined') return;
    document.body.style.overflow = open ? 'hidden' : '';
    return () => { document.body.style.overflow = ''; };
  });

  function toggle() { open = !open; }
  function close()  { open = false; }
  function onKeydown(e: KeyboardEvent) {
    if (e.key === 'Escape' && open) { e.preventDefault(); close(); }
  }
</script>

<svelte:window on:keydown={onKeydown} />

<!-- ════════════════ NAVBAR HORIZONTAL FIJO ════════════════ -->
<header class="nav" class:scrolled role="banner">
  <div class="nav__inner">
    <!-- Logo -->
    <a class="nav__brand" href="#inicio" aria-label={`${siteConfig.shortName} S.A.S — inicio`}>
      <img class="nav__logo" src="/images/coicem-logo.png" alt={`${siteConfig.shortName} S.A.S`} />
    </a>

    <!-- Links (desktop) -->
    <nav class="nav__links" aria-label="Navegación principal">
      <ul class="nav__list">
        {#each items as item (item.href)}
          <li>
            <a
              class="nav__item"
              class:active={activeId === item.href.slice(1)}
              href={item.href}
              aria-current={activeId === item.href.slice(1) ? 'true' : undefined}
            >
              <span class="nav__n">{item.n}</span>
              <span class="nav__label">{item.label}</span>
            </a>
          </li>
        {/each}
      </ul>
    </nav>

    <!-- CTA (desktop) -->
    <a class="nav__cta" href="#contacto">Cotizar</a>

    <!-- Hamburguesa (móvil) -->
    <button
      class="nav__burger"
      type="button"
      aria-label="Abrir menú de navegación"
      aria-expanded={open}
      aria-controls="coicem-nav-overlay"
      onclick={toggle}
    >
      <span class="nav__burger-line"></span>
      <span class="nav__burger-line"></span>
      <span class="nav__burger-line"></span>
    </button>
  </div>
</header>

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
  <div class="overlay__head">
    <img class="overlay__logo" src="/images/coicem-logo.png" alt={`${siteConfig.shortName} S.A.S`} />
    <button class="overlay__close" type="button" aria-label="Cerrar menú" onclick={close}>
      <span aria-hidden="true">✕</span>
    </button>
  </div>

  <nav class="overlay__nav" aria-label="Navegación principal (móvil)">
    <ul class="overlay__list">
      {#each items as item (item.href)}
        <li>
          <a
            class="overlay__item"
            class:active={activeId === item.href.slice(1)}
            href={item.href}
            tabindex={open ? 0 : -1}
            onclick={close}
          >
            <span class="overlay__n">{item.n}</span>
            <span>{item.label}</span>
          </a>
        </li>
      {/each}
    </ul>
    <a class="overlay__cta" href="#contacto" tabindex={open ? 0 : -1} onclick={close}>Cotizar</a>
  </nav>
</div>

<style>
  :where(.nav, .overlay) {
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

  /* ═══════════ NAVBAR ═══════════ */
  .nav {
    position: fixed;
    top: 0; left: 0; right: 0;
    z-index: 60;
    background: var(--metal-base);
    border-bottom: 1px solid var(--metal-border);
    transition: box-shadow 160ms linear;
  }
  .nav.scrolled { box-shadow: 0 1px 0 0 var(--naranja); }

  .nav__inner {
    max-width: 1320px;
    margin: 0 auto;
    height: 72px;
    display: flex;
    align-items: center;
    gap: clamp(0.75rem, 2vw, 1.5rem);
    padding: 0 clamp(1rem, 4vw, 3rem);
  }

  .nav__brand { display: flex; align-items: center; text-decoration: none; flex-shrink: 0; min-width: 0; }
  .nav__logo { display: block; height: 52px; width: auto; max-width: 100%; }

  .nav__links { margin-left: auto; }
  .nav__list {
    list-style: none; margin: 0; padding: 0;
    display: flex; align-items: center; gap: 0.25rem;
  }
  .nav__item {
    display: inline-flex;
    align-items: baseline;
    gap: 0.5rem;
    padding: 0.55rem 0.9rem;
    text-decoration: none;
    border-bottom: 2px solid transparent;
    transition: color 160ms linear, border-color 160ms linear, background 160ms linear;
  }
  .nav__n {
    font-family: var(--font-mono);
    font-size: 0.62rem;
    color: var(--metal-light);
    transition: color 160ms linear;
  }
  .nav__label {
    font-family: var(--font-body);
    text-transform: uppercase;
    letter-spacing: 0.1em;
    font-size: 0.78rem;
    color: var(--texto);
    white-space: nowrap;
    transition: color 160ms linear;
  }
  .nav__item:hover { background: rgba(2, 81, 153, 0.16); }
  .nav__item.active { border-bottom-color: var(--naranja); }
  .nav__item.active .nav__n,
  .nav__item.active .nav__label { color: var(--naranja); }
  .nav__item:focus-visible { outline: 2px solid var(--naranja); outline-offset: -2px; }

  .nav__cta {
    flex-shrink: 0;
    display: inline-flex;
    align-items: center;
    min-height: 40px;
    padding: 0 1.3rem;
    background: var(--naranja);
    color: #000;
    font-family: var(--font-mono);
    text-transform: uppercase;
    letter-spacing: 0.12em;
    font-size: 0.76rem;
    font-weight: 600;
    text-decoration: none;
    border: 1px solid var(--naranja);
    transition: background 160ms linear;
  }
  .nav__cta:hover { background: #ffae3a; }
  .nav__cta:focus-visible { outline: 2px solid var(--texto); outline-offset: 2px; }

  /* Hamburguesa oculta en desktop */
  .nav__burger { display: none; }

  /* ═══════════ MÓVIL (<900px) ═══════════ */
  @media (max-width: 900px) {
    .nav__links, .nav__cta { display: none; }
    .nav__burger {
      display: flex;
      flex-direction: column;
      justify-content: center;
      gap: 5px;
      width: 44px; height: 44px;
      margin-left: auto;
      padding: 0 8px;
      background: transparent;
      border: 1px solid var(--metal-border);
      cursor: pointer;
    }
    .nav__burger-line { display: block; height: 2px; width: 100%; background: var(--texto); }
    .nav__burger:focus-visible { outline: 2px solid var(--naranja); outline-offset: 2px; }
  }

  /* ═══════════ OVERLAY FULLSCREEN ═══════════ */
  .overlay {
    position: fixed;
    inset: 0;
    z-index: 80;
    background: var(--metal-base);
    display: flex;
    flex-direction: column;
    clip-path: inset(0 0 100% 0);
    opacity: 0;
    pointer-events: none;
    transition:
      clip-path 320ms cubic-bezier(0.83, 0, 0.17, 1),
      opacity 320ms cubic-bezier(0.83, 0, 0.17, 1);
  }
  .overlay.open { clip-path: inset(0 0 0 0); opacity: 1; pointer-events: auto; }

  .overlay__head {
    display: flex; align-items: center; justify-content: space-between;
    height: 64px; padding: 0 16px;
    border-bottom: 1px solid var(--metal-border);
    flex-shrink: 0;
  }
  .overlay__logo { height: 38px; width: auto; }
  .overlay__close {
    display: flex; align-items: center; justify-content: center;
    width: 48px; height: 48px;
    background: transparent; border: 1px solid var(--metal-border);
    color: var(--texto); cursor: pointer;
    font-family: var(--font-mono); font-size: 1.25rem;
  }
  .overlay__close:focus-visible { outline: 2px solid var(--naranja); outline-offset: 2px; }

  .overlay__nav { flex: 1; overflow-y: auto; padding: 8px 0 24px; }
  .overlay__list { list-style: none; margin: 0; padding: 0; }
  .overlay__item {
    display: flex; align-items: baseline; gap: 16px;
    min-height: 56px; padding: 16px 24px;
    text-decoration: none;
    border-bottom: 1px solid rgba(49, 63, 80, 0.5);
    border-left: 3px solid transparent;
    font-family: var(--font-body);
    text-transform: uppercase;
    letter-spacing: 0.1em;
    font-size: 1.25rem;
    color: var(--texto);
  }
  .overlay__n { font-family: var(--font-mono); font-size: 1rem; color: var(--naranja); min-width: 1.6em; }
  .overlay__item.active { border-left-color: var(--naranja); background: rgba(2, 81, 153, 0.14); }
  .overlay__item.active, .overlay__item.active span { color: var(--naranja); }
  .overlay__item:focus-visible { outline: 2px solid var(--naranja); outline-offset: -2px; }

  .overlay__cta {
    display: flex; align-items: center; justify-content: center;
    margin: 24px; min-height: 52px;
    background: var(--naranja); color: #000;
    font-family: var(--font-mono); text-transform: uppercase;
    letter-spacing: 0.16em; font-size: 0.95rem; font-weight: 600;
    text-decoration: none;
  }
  .overlay__cta:focus-visible { outline: 2px solid var(--texto); outline-offset: 2px; }

  @media (prefers-reduced-motion: reduce) {
    .overlay { transition: none; }
    .nav, .nav__item, .nav__n, .nav__label { transition: none; }
  }
</style>
