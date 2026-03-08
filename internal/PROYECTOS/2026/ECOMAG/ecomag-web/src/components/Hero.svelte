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

  /* Mobile: reduce min-height so hero fits better on small screens */
  @media (max-width: 639px) {
    .hero {
      min-height: 85vh;
      min-height: 85dvh;
    }
  }

  /* ── Leaf SVGs — VISIBLE & ANIMATED ── */
  .hero__leaves {
    position: absolute;
    inset: 0;
    pointer-events: none;
    z-index: 0;
  }

  /* Mobile: hide some leaves and shrink others to reduce clutter */
  @media (max-width: 639px) {
    .leaf--1 { width: 60px; }
    .leaf--2 { width: 45px; }
    .leaf--3 { width: 35px; }
    .leaf--6 { width: 30px; }
    .leaf--4,
    .leaf--5,
    .leaf--7 {
      display: none;
    }
  }

  .leaf {
    position: absolute;
    will-change: transform;
    filter: drop-shadow(0 2px 8px rgba(0,0,0,0.15));
  }

  /* Leaf 1: Large, top-left — sway + drift right */
  .leaf--1 {
    width: 110px;
    top: 5%;
    left: 3%;
    color: rgba(124, 179, 66, 0.5);
    animation: leafFloat1 8s ease-in-out infinite;
  }

  /* Leaf 2: Medium, top-right — sway + drift left */
  .leaf--2 {
    width: 80px;
    top: 12%;
    right: 8%;
    color: rgba(27, 94, 32, 0.45);
    animation: leafFloat2 9s ease-in-out infinite;
    animation-delay: -2s;
  }

  /* Leaf 3: Small, mid-left — bouncy bob */
  .leaf--3 {
    width: 55px;
    top: 50%;
    left: 6%;
    color: rgba(76, 175, 80, 0.55);
    animation: leafFloat3 6s ease-in-out infinite;
    animation-delay: -1s;
  }

  /* Leaf 4: Large, bottom-right — slow majestic float */
  .leaf--4 {
    width: 130px;
    bottom: 10%;
    right: 3%;
    color: rgba(27, 94, 32, 0.35);
    animation: leafFloat4 12s ease-in-out infinite;
    animation-delay: -4s;
  }

  /* Leaf 5: Medium, center-right — gentle sway */
  .leaf--5 {
    width: 65px;
    top: 32%;
    left: 72%;
    color: rgba(124, 179, 66, 0.5);
    animation: leafFloat5 7s ease-in-out infinite;
    animation-delay: -0.5s;
  }

  /* Leaf 6: Small, bottom-left — quick flutter */
  .leaf--6 {
    width: 48px;
    bottom: 25%;
    left: 18%;
    color: rgba(76, 175, 80, 0.45);
    animation: leafFloat6 5s ease-in-out infinite;
    animation-delay: -3s;
  }

  /* Leaf 7: Medium, lower-center-right */
  .leaf--7 {
    width: 90px;
    top: 65%;
    right: 20%;
    color: rgba(27, 94, 32, 0.4);
    animation: leafFloat7 10s ease-in-out infinite;
    animation-delay: -1.5s;
  }

  /* ── Keyframes — big, dramatic, clearly visible movements ── */

  /* Float1: sway wide + drift right + bob up */
  @keyframes leafFloat1 {
    0%   { transform: translate(0, 0) rotate(-8deg) scale(1); }
    25%  { transform: translate(30px, -20px) rotate(5deg) scale(1.05); }
    50%  { transform: translate(50px, -5px) rotate(12deg) scale(1); }
    75%  { transform: translate(20px, -25px) rotate(-3deg) scale(1.03); }
    100% { transform: translate(0, 0) rotate(-8deg) scale(1); }
  }

  /* Float2: drift left + tilt + scale pulse */
  @keyframes leafFloat2 {
    0%   { transform: translate(0, 0) rotate(10deg) scale(1); }
    33%  { transform: translate(-40px, -15px) rotate(-8deg) scale(1.08); }
    66%  { transform: translate(-20px, 10px) rotate(5deg) scale(0.95); }
    100% { transform: translate(0, 0) rotate(10deg) scale(1); }
  }

  /* Float3: bouncy vertical bob + wiggle */
  @keyframes leafFloat3 {
    0%, 100% { transform: translateY(0) rotate(0deg); }
    20%  { transform: translateY(-30px) rotate(10deg); }
    40%  { transform: translateY(-10px) rotate(-5deg); }
    60%  { transform: translateY(-35px) rotate(8deg); }
    80%  { transform: translateY(-12px) rotate(-3deg); }
  }

  /* Float4: slow majestic arc */
  @keyframes leafFloat4 {
    0%   { transform: translate(0, 0) rotate(-5deg) scale(1); }
    25%  { transform: translate(-35px, -30px) rotate(8deg) scale(1.06); }
    50%  { transform: translate(-60px, -10px) rotate(-10deg) scale(1); }
    75%  { transform: translate(-25px, -40px) rotate(5deg) scale(1.04); }
    100% { transform: translate(0, 0) rotate(-5deg) scale(1); }
  }

  /* Float5: gentle side-to-side + up */
  @keyframes leafFloat5 {
    0%, 100% { transform: translate(0, 0) rotate(5deg); }
    50%  { transform: translate(-25px, -20px) rotate(-10deg); }
  }

  /* Float6: quick flutter — fast wiggle */
  @keyframes leafFloat6 {
    0%   { transform: translate(0, 0) rotate(0deg); }
    15%  { transform: translate(10px, -15px) rotate(15deg); }
    30%  { transform: translate(-5px, -25px) rotate(-10deg); }
    50%  { transform: translate(15px, -10px) rotate(12deg); }
    70%  { transform: translate(-8px, -20px) rotate(-8deg); }
    85%  { transform: translate(5px, -5px) rotate(6deg); }
    100% { transform: translate(0, 0) rotate(0deg); }
  }

  /* Float7: slow diagonal drift */
  @keyframes leafFloat7 {
    0%   { transform: translate(0, 0) rotate(-3deg) scale(1); }
    33%  { transform: translate(25px, -20px) rotate(10deg) scale(1.05); }
    66%  { transform: translate(-15px, -35px) rotate(-7deg) scale(0.97); }
    100% { transform: translate(0, 0) rotate(-3deg) scale(1); }
  }

  /* prefers-reduced-motion: animations will be disabled via JS if user prefers */

  /* ── Content ── */
  .hero__content {
    position: relative;
    z-index: 1;
    width: 100%;
    padding-top: 6rem;
    padding-bottom: 4rem;
  }

  .hero__inner {
    max-width: 48rem;
  }

  .hero__badge {
    display: inline-block;
    padding: 0.375rem 1rem;
    border: 1px solid rgba(255, 255, 255, 0.35);
    border-radius: 9999px;
    font-family: var(--font-body);
    font-size: 0.8125rem;
    font-weight: 500;
    color: rgba(255, 255, 255, 0.9);
    letter-spacing: 0.025em;
    backdrop-filter: blur(4px);
    background: rgba(255, 255, 255, 0.08);
    margin-bottom: 1.5rem;
  }

  .hero__title {
    font-family: var(--font-display);
    font-size: clamp(2rem, 5vw, 3.5rem);
    font-weight: 800;
    line-height: 1.1;
    letter-spacing: -0.025em;
    color: #fff;
    margin: 0 0 1.25rem;
  }

  .hero__subtitle {
    font-family: var(--font-body);
    font-size: clamp(1rem, 2vw, 1.25rem);
    line-height: 1.7;
    color: rgba(255, 255, 255, 0.85);
    margin: 0 0 2.5rem;
    max-width: 38rem;
  }

  .hero__cta {
    display: flex;
    flex-wrap: wrap;
    gap: 1rem;
  }

  /* Mobile: reduce padding, adjust badge size, stack CTA buttons on very small screens */
  @media (max-width: 639px) {
    .hero__content {
      padding-top: 4.5rem;
      padding-bottom: 2.5rem;
    }

    .hero__badge {
      font-size: 0.6875rem;
      padding: 0.25rem 0.75rem;
      margin-bottom: 1rem;
    }

    .hero__subtitle {
      margin-bottom: 1.75rem;
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
    border-color: rgba(255, 255, 255, 0.6) !important;
    color: #fff !important;
  }
  :global(.btn-secondary--hero:hover) {
    background-color: rgba(255, 255, 255, 0.15) !important;
    border-color: #fff !important;
    color: #fff !important;
  }
</style>
