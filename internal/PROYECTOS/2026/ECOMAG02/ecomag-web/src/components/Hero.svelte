<script>
  import { onMount } from 'svelte';
  import { animate } from 'motion';

  let heroContent;
  let prefersReducedMotion = false;

  onMount(() => {
    prefersReducedMotion = window.matchMedia('(prefers-reduced-motion: reduce)').matches;

    if (!prefersReducedMotion && heroContent) {
      const elements = heroContent.querySelectorAll('[data-animate]');
      elements.forEach((el, i) => {
        el.style.opacity = '0';
        el.style.transform = 'translateY(24px)';
        animate(
          el,
          { opacity: [0, 1], transform: ['translateY(24px)', 'translateY(0)'] },
          { duration: 0.7, delay: 0.15 * i, easing: [0.22, 1, 0.36, 1] }
        );
      });
    }
  });
</script>

<section
  id="inicio"
  class="hero"
  aria-label="Inicio"
>
  <!-- Background leaves — much more visible and animated -->
  <div class="hero__leaves" aria-hidden="true">
    <!-- Leaf 1: Large, top-left, drifts right -->
    <svg class="leaf leaf--1" viewBox="0 0 80 100" xmlns="http://www.w3.org/2000/svg">
      <path d="M40 0C40 0 0 30 0 60C0 82 18 100 40 100C62 100 80 82 80 60C80 30 40 0 40 0Z" fill="currentColor"/>
      <path d="M40 15V85M40 40L20 55M40 55L60 45M40 70L25 75" stroke="rgba(255,255,255,0.4)" stroke-width="1.5" fill="none"/>
    </svg>
    <!-- Leaf 2: Medium, top-right, drifts left -->
    <svg class="leaf leaf--2" viewBox="0 0 80 100" xmlns="http://www.w3.org/2000/svg">
      <path d="M40 0C40 0 0 30 0 60C0 82 18 100 40 100C62 100 80 82 80 60C80 30 40 0 40 0Z" fill="currentColor"/>
      <path d="M40 15V85M40 40L20 55M40 55L60 45M40 70L25 75" stroke="rgba(255,255,255,0.4)" stroke-width="1.5" fill="none"/>
    </svg>
    <!-- Leaf 3: Small, mid-left, bobs up -->
    <svg class="leaf leaf--3" viewBox="0 0 80 100" xmlns="http://www.w3.org/2000/svg">
      <path d="M40 0C40 0 0 30 0 60C0 82 18 100 40 100C62 100 80 82 80 60C80 30 40 0 40 0Z" fill="currentColor"/>
      <path d="M40 15V85M40 40L20 55M40 55L60 45" stroke="rgba(255,255,255,0.4)" stroke-width="1.5" fill="none"/>
    </svg>
    <!-- Leaf 4: Large, bottom-right, slow float -->
    <svg class="leaf leaf--4" viewBox="0 0 80 100" xmlns="http://www.w3.org/2000/svg">
      <path d="M40 0C40 0 0 30 0 60C0 82 18 100 40 100C62 100 80 82 80 60C80 30 40 0 40 0Z" fill="currentColor"/>
      <path d="M40 15V85M40 40L20 55M40 55L60 45M40 70L25 75" stroke="rgba(255,255,255,0.4)" stroke-width="1.5" fill="none"/>
    </svg>
    <!-- Leaf 5: Medium, center-right -->
    <svg class="leaf leaf--5" viewBox="0 0 80 100" xmlns="http://www.w3.org/2000/svg">
      <path d="M40 0C40 0 0 30 0 60C0 82 18 100 40 100C62 100 80 82 80 60C80 30 40 0 40 0Z" fill="currentColor"/>
      <path d="M40 15V85M40 40L20 55M40 55L60 45" stroke="rgba(255,255,255,0.4)" stroke-width="1.5" fill="none"/>
    </svg>
    <!-- Leaf 6: Small, bottom-left -->
    <svg class="leaf leaf--6" viewBox="0 0 80 100" xmlns="http://www.w3.org/2000/svg">
      <path d="M40 0C40 0 0 30 0 60C0 82 18 100 40 100C62 100 80 82 80 60C80 30 40 0 40 0Z" fill="currentColor"/>
      <path d="M40 15V85M40 40L20 55M40 55L60 45M40 70L25 75" stroke="rgba(255,255,255,0.4)" stroke-width="1.5" fill="none"/>
    </svg>
    <!-- Leaf 7: Medium, lower-right -->
    <svg class="leaf leaf--7" viewBox="0 0 80 100" xmlns="http://www.w3.org/2000/svg">
      <path d="M40 0C40 0 0 30 0 60C0 82 18 100 40 100C62 100 80 82 80 60C80 30 40 0 40 0Z" fill="currentColor"/>
      <path d="M40 15V85M40 40L20 55M40 55L60 45" stroke="rgba(255,255,255,0.4)" stroke-width="1.5" fill="none"/>
    </svg>
  </div>

  <!-- Hero content -->
  <div class="hero__content section-container" bind:this={heroContent}>
    <div class="hero__inner">
      <span class="hero__badge" data-animate>
        Certificados ISO 9001 &middot; ISO 14001 &middot; ISO 45001
      </span>

      <h1 class="hero__title" data-animate>
        Construimos el futuro, protegemos el medio ambiente
      </h1>

      <p class="hero__subtitle" data-animate>
        Soluciones integrales en obra civil y gesti&oacute;n ambiental en toda Colombia.
        Innovaci&oacute;n, calidad y sostenibilidad en cada proyecto.
      </p>

      <div class="hero__cta" data-animate>
        <a href="#servicios" class="btn-primary">
          Nuestros Servicios
        </a>
        <a href="#contacto" class="btn-secondary btn-secondary--hero">
          Cont&aacute;ctanos
        </a>
      </div>
    </div>
  </div>
</section>

<style>
  .hero {
    position: relative;
    min-height: 100vh;
    min-height: 100dvh;
    display: flex;
    align-items: center;
    overflow: hidden;
    background:
      linear-gradient(135deg, rgba(27, 94, 32, 0.92) 0%, rgba(2, 119, 168, 0.7) 50%, rgba(27, 94, 32, 0.4) 100%),
      url('/hero-bg.jpg') center / cover no-repeat;
  }

  @media (max-width: 639px) {
    .hero {
      min-height: 85vh;
      min-height: 85dvh;
    }
  }

  /* ── Leaf SVGs — SUBTLE animations ── */
  .hero__leaves {
    position: absolute;
    inset: 0;
    pointer-events: none;
    z-index: 0;
  }

  @media (max-width: 639px) {
    .leaf--1 { width: 50px; opacity: 0.6; }
    .leaf--2 { width: 40px; opacity: 0.5; }
    .leaf--3 { width: 30px; opacity: 0.5; }
    .leaf--6 { width: 25px; opacity: 0.4; }
    .leaf--4, .leaf--5, .leaf--7 { display: none; }
  }

  .leaf {
    position: absolute;
    will-change: transform;
    filter: drop-shadow(0 2px 6px rgba(0,0,0,0.1));
    opacity: 0.7;
  }

  /* Leaf positions - más pequeñas y sutiles */
  .leaf--1 {
    width: 80px;
    top: 8%;
    left: 5%;
    color: rgba(124, 179, 66, 0.4);
    animation: leafFloat1 12s ease-in-out infinite;
  }

  .leaf--2 {
    width: 60px;
    top: 15%;
    right: 10%;
    color: rgba(27, 94, 32, 0.35);
    animation: leafFloat2 14s ease-in-out infinite;
    animation-delay: -3s;
  }

  .leaf--3 {
    width: 45px;
    top: 50%;
    left: 8%;
    color: rgba(76, 175, 80, 0.4);
    animation: leafFloat3 10s ease-in-out infinite;
    animation-delay: -2s;
  }

  .leaf--4 {
    width: 90px;
    bottom: 12%;
    right: 5%;
    color: rgba(27, 94, 32, 0.3);
    animation: leafFloat4 16s ease-in-out infinite;
    animation-delay: -5s;
  }

  .leaf--5 {
    width: 50px;
    top: 35%;
    left: 75%;
    color: rgba(124, 179, 66, 0.35);
    animation: leafFloat5 11s ease-in-out infinite;
    animation-delay: -1s;
  }

  .leaf--6 {
    width: 35px;
    bottom: 30%;
    left: 20%;
    color: rgba(76, 175, 80, 0.35);
    animation: leafFloat6 9s ease-in-out infinite;
    animation-delay: -4s;
  }

  .leaf--7 {
    width: 65px;
    top: 60%;
    right: 22%;
    color: rgba(27, 94, 32, 0.3);
    animation: leafFloat7 13s ease-in-out infinite;
    animation-delay: -2s;
  }

  /* ── Keyframes — SUBTLE, gentle movements ── */
  @keyframes leafFloat1 {
    0%, 100% { transform: translate(0, 0) rotate(-3deg); }
    50% { transform: translate(15px, -10px) rotate(3deg); }
  }

  @keyframes leafFloat2 {
    0%, 100% { transform: translate(0, 0) rotate(5deg); }
    50% { transform: translate(-12px, -8px) rotate(-2deg); }
  }

  @keyframes leafFloat3 {
    0%, 100% { transform: translateY(0) rotate(0deg); }
    50% { transform: translateY(-12px) rotate(4deg); }
  }

  @keyframes leafFloat4 {
    0%, 100% { transform: translate(0, 0) rotate(-2deg); }
    50% { transform: translate(-18px, -12px) rotate(4deg); }
  }

  @keyframes leafFloat5 {
    0%, 100% { transform: translate(0, 0) rotate(3deg); }
    50% { transform: translate(-10px, -8px) rotate(-3deg); }
  }

  @keyframes leafFloat6 {
    0%, 100% { transform: translate(0, 0) rotate(0deg); }
    50% { transform: translate(8px, -10px) rotate(5deg); }
  }

  @keyframes leafFloat7 {
    0%, 100% { transform: translate(0, 0) rotate(-2deg); }
    50% { transform: translate(12px, -10px) rotate(3deg); }
  }

  /* ── Content ── */
  .hero__content {
    position: relative;
    z-index: 1;
    width: 100%;
    padding-top: 6rem;
    padding-bottom: 4rem;
  }

  .hero__inner {
    max-width: 44rem;
  }

  .hero__badge {
    display: inline-block;
    padding: 0.5rem 1rem;
    border: 1px solid rgba(255, 255, 255, 0.25);
    border-radius: 9999px;
    font-family: var(--font-body);
    font-size: 0.75rem;
    font-weight: 500;
    color: rgba(255, 255, 255, 0.9);
    letter-spacing: 0.05em;
    backdrop-filter: blur(8px);
    background: rgba(255, 255, 255, 0.1);
    margin-bottom: 1.5rem;
  }

  .hero__title {
    font-family: var(--font-display);
    font-size: clamp(2rem, 5vw, 3.25rem);
    font-weight: 700;
    line-height: 1.1;
    letter-spacing: -0.03em;
    color: #fff;
    margin: 0 0 1.25rem;
  }

  .hero__subtitle {
    font-family: var(--font-body);
    font-size: clamp(1rem, 2vw, 1.125rem);
    line-height: 1.7;
    color: rgba(255, 255, 255, 0.8);
    margin: 0 0 2rem;
    max-width: 36rem;
  }

  .hero__cta {
    display: flex;
    flex-wrap: wrap;
    gap: 0.875rem;
  }

  @media (max-width: 639px) {
    .hero__content {
      padding-top: 5rem;
      padding-bottom: 3rem;
    }

    .hero__badge {
      font-size: 0.6875rem;
      padding: 0.375rem 0.75rem;
      margin-bottom: 1.25rem;
    }

    .hero__subtitle {
      margin-bottom: 1.5rem;
    }
  }

  @media (max-width: 400px) {
    .hero__cta {
      flex-direction: column;
    }

    .hero__cta :global(a) {
      width: 100%;
      text-align: center;
      justify-content: center;
    }
  }

  :global(.btn-secondary--hero) {
    border-color: rgba(255, 255, 255, 0.5) !important;
    color: #fff !important;
    background: rgba(255, 255, 255, 0.05);
  }

  :global(.btn-secondary--hero:hover) {
    background-color: rgba(255, 255, 255, 0.15) !important;
    border-color: rgba(255, 255, 255, 0.8) !important;
    color: #fff !important;
  }
</style>
