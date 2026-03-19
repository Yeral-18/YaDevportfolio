<script>
  /**
   * Hero - MULTISERVICIOS P&J S.A.S
   * Split-screen layout (text left + visual right) with corporate identity colors
   * Azul Institucional (#0089D0), Verde Ambiental (#005B32), Verde Claro (#8CC63F)
   */

  let visible = $state(false);

  $effect(() => {
    const timer = setTimeout(() => { visible = true; }, 150);
    return () => clearTimeout(timer);
  });

  const stats = [
    { value: '6', label: 'Servicios Integrales' },
    { value: '3', label: 'Certificaciones ISO' },
    { value: '4+', label: 'Clientes en Santander' },
  ];

  const badges = [
    { label: 'Transporte', icon: 'building', x: '22%', y: '22%', delay: 400 },
    { label: 'Ambiental', icon: 'leaf', x: '65%', y: '35%', delay: 600 },
    { label: 'Energía Solar', icon: 'zap', x: '15%', y: '72%', delay: 800 },
    { label: 'Obras Civiles', icon: 'cog', x: '58%', y: '68%', delay: 1000 },
  ];
</script>

<section id="inicio" class="hero">
  <!-- LEFT: Content -->
  <div class="hero-left">
    <div class="hero-content" class:visible>
      <div class="hero-tag">
        <span class="tag-line"></span>
        Empresa de Ingeniería en Barrancabermeja
      </div>

      <h1 class="hero-heading">
        Transporte de Carga,<br>
        <span class="accent">Obras Civiles</span> y Remediación<br>
        Ambiental en Barrancabermeja
      </h1>

      <p class="hero-desc">
        Servicios integrales de transporte de carga, obras civiles, izaje de cargas,
        remediación ambiental y transición energética en Santander, Colombia.
        Empresa certificada ISO 9001, ISO 14001 e ISO 45001 con operaciones
        en Barrancabermeja y el Magdalena Medio.
      </p>

      <!-- Buttons: Corporate Blue -->
      <div class="hero-actions">
        <a href="#servicios" class="btn-hero-primary">
          Conocer Servicios
          <svg xmlns="http://www.w3.org/2000/svg" width="18" height="18" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round">
            <line x1="5" y1="12" x2="19" y2="12"></line>
            <polyline points="12 5 19 12 12 19"></polyline>
          </svg>
        </a>
        <a href="#contacto" class="btn-hero-ghost">
          Contactar
        </a>
      </div>

    </div>
  </div>

  <!-- RIGHT: Visual panel with gradient + geometric elements -->
  <div class="hero-right">
    <!-- Gradient background -->
    <div class="right-bg"></div>

    <!-- Geometric elements -->
    <div class="geo-elements">
      <!-- Large ring -->
      <div class="geo-ring geo-ring-lg"></div>
      <div class="geo-ring geo-ring-sm"></div>

      <!-- Grid pattern -->
      <div class="geo-grid"></div>

      <!-- Diagonal line -->
      <div class="geo-diagonal"></div>

      <!-- WATERMARK: Logo as subtle background -->
      <img
        src={`${import.meta.env.BASE_URL ?? '/multiservicios/'}logo-white.png`}
        alt=""
        aria-hidden="true"
        class="logo-watermark"
        class:visible
      />

      <!-- CENTER: Large crossed tools icon -->
      <div class="center-icon" class:visible>
        <svg xmlns="http://www.w3.org/2000/svg" width="120" height="120" viewBox="0 0 24 24" fill="none" stroke="rgba(255,255,255,0.15)" stroke-width="0.8" stroke-linecap="round" stroke-linejoin="round">
          <!-- Wrench -->
          <path d="M14.7 6.3a1 1 0 0 0 0 1.4l1.6 1.6a1 1 0 0 0 1.4 0l3.77-3.77a6 6 0 0 1-7.94 7.94l-6.91 6.91a2.12 2.12 0 0 1-3-3l6.91-6.91a6 6 0 0 1 7.94-7.94l-3.76 3.76z"/>
        </svg>
        <svg class="tool-2" xmlns="http://www.w3.org/2000/svg" width="100" height="100" viewBox="0 0 24 24" fill="none" stroke="rgba(255,255,255,0.1)" stroke-width="0.8" stroke-linecap="round" stroke-linejoin="round">
          <!-- Screwdriver / Settings -->
          <circle cx="12" cy="12" r="3"/>
          <path d="M12 1v4M12 19v4M4.22 4.22l2.83 2.83M16.95 16.95l2.83 2.83M1 12h4M19 12h4M4.22 19.78l2.83-2.83M16.95 7.05l2.83-2.83"/>
        </svg>
      </div>

      <!-- Floating service badges -->
      {#each badges as badge, i}
        <div
          class="float-badge"
          style="left: {badge.x}; top: {badge.y}; transition-delay: {badge.delay}ms"
          class:visible
        >
          {#if badge.icon === 'building'}
            <svg xmlns="http://www.w3.org/2000/svg" width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><rect x="4" y="2" width="16" height="20" rx="2" ry="2"/><path d="M9 22v-4h6v4"/><path d="M8 6h.01"/><path d="M16 6h.01"/><path d="M12 6h.01"/><path d="M12 10h.01"/><path d="M12 14h.01"/><path d="M16 10h.01"/><path d="M16 14h.01"/><path d="M8 10h.01"/><path d="M8 14h.01"/></svg>
          {:else if badge.icon === 'leaf'}
            <svg xmlns="http://www.w3.org/2000/svg" width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><path d="M11 20A7 7 0 0 1 9.8 6.9C15.5 4.9 20 .5 20 .5s-4.4 4.5-2.4 10.2A7 7 0 0 1 11 20z"/><path d="M2 21c0-3 1.85-5.36 5.08-6C9.5 14.52 12 13 13 12"/></svg>
          {:else if badge.icon === 'zap'}
            <svg xmlns="http://www.w3.org/2000/svg" width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><polygon points="13 2 3 14 12 14 11 22 21 10 12 10 13 2"/></svg>
          {:else}
            <svg xmlns="http://www.w3.org/2000/svg" width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><circle cx="12" cy="12" r="3"/><path d="M12 1v4M12 19v4M4.22 4.22l2.83 2.83M16.95 16.95l2.83 2.83M1 12h4M19 12h4M4.22 19.78l2.83-2.83M16.95 7.05l2.83-2.83"/></svg>
          {/if}
          <span>{badge.label}</span>
        </div>
      {/each}
    </div>

    <!-- Diagonal divider -->
    <div class="diagonal-clip"></div>
  </div>
</section>

<style>
  .hero {
    position: relative;
    min-height: 100vh;
    display: flex;
    overflow: hidden;
    /* Split-screen layout */
    background: linear-gradient(160deg, #1a2332 0%, #1e3040 50%, #1a3040 100%);
  }

  /* -- LEFT PANEL: Content -- */
  .hero-left {
    position: relative;
    z-index: 2;
    width: 55%;
    display: flex;
    align-items: center;
    padding: 7rem 3rem 4rem 0;
    padding-left: max(2rem, calc((100vw - 72rem) / 2 + 1rem));
  }

  .hero-content {
    max-width: 560px;
    opacity: 0;
    transform: translateY(24px);
    transition: opacity 0.7s cubic-bezier(0, 0, 0.2, 1),
                transform 0.7s cubic-bezier(0, 0, 0.2, 1);
  }

  .hero-content.visible {
    opacity: 1;
    transform: translateY(0);
  }

  /* Tag */
  .hero-tag {
    display: inline-flex;
    align-items: center;
    gap: 10px;
    font-size: 0.7rem;
    font-weight: 600;
    letter-spacing: 0.2em;
    text-transform: uppercase;
    color: rgba(140, 198, 63, 0.8);
    margin-bottom: 1.25rem;
  }

  .tag-line {
    display: block;
    width: 24px;
    height: 1px;
    background: rgba(140, 198, 63, 0.5);
  }

  /* Heading */
  .hero-heading {
    font-family: 'Plus Jakarta Sans', system-ui, sans-serif;
    font-size: clamp(2rem, 4.5vw, 3.5rem);
    font-weight: 800;
    line-height: 1.08;
    letter-spacing: -0.035em;
    color: white;
    margin-bottom: 1.25rem;
  }

  .hero-heading .accent {
    background: linear-gradient(135deg, #8AD7F8, #0089D0);
    -webkit-background-clip: text;
    -webkit-text-fill-color: transparent;
    background-clip: text;
  }

  /* Description */
  .hero-desc {
    font-size: clamp(0.9375rem, 1.2vw, 1.0625rem);
    color: rgba(255, 255, 255, 0.5);
    line-height: 1.7;
    margin-bottom: 2rem;
    max-width: 480px;
  }

  /* Buttons: Corporate Blue */
  .hero-actions {
    display: flex;
    align-items: center;
    gap: 1rem;
    margin-bottom: 2.5rem;
  }

  .btn-hero-primary {
    display: inline-flex;
    align-items: center;
    gap: 8px;
    padding: 13px 26px;
    background: #0089D0;
    color: white;
    font-size: 0.875rem;
    font-weight: 600;
    text-decoration: none;
    border-radius: 0;
    transition: all 0.3s cubic-bezier(0.34, 1.3, 0.64, 1);
    letter-spacing: 0.01em;
  }

  .btn-hero-primary:hover {
    background: #8AD7F8;
    color: #003F66;
    transform: translateY(-2px);
    box-shadow: 0 8px 24px rgba(0, 137, 208, 0.35);
  }

  .btn-hero-primary svg {
    transition: transform 0.2s ease;
  }

  .btn-hero-primary:hover svg {
    transform: translateX(3px);
  }

  .btn-hero-ghost {
    display: inline-flex;
    align-items: center;
    padding: 13px 26px;
    border: 1px solid rgba(255, 255, 255, 0.2);
    color: rgba(255, 255, 255, 0.75);
    font-size: 0.875rem;
    font-weight: 500;
    text-decoration: none;
    border-radius: 0;
    transition: all 0.3s ease;
  }

  .btn-hero-ghost:hover {
    border-color: rgba(255, 255, 255, 0.45);
    color: white;
    background: rgba(255, 255, 255, 0.05);
  }

  /* Stats */
  .hero-stats {
    display: flex;
    align-items: center;
    gap: 1.5rem;
  }

  .stat {
    display: flex;
    flex-direction: column;
    opacity: 0;
    transform: translateY(12px);
    transition: opacity 0.5s ease, transform 0.5s ease;
  }

  .stat.visible {
    opacity: 1;
    transform: translateY(0);
  }

  .stat-value {
    font-family: 'Plus Jakarta Sans', system-ui, sans-serif;
    font-size: 1.5rem;
    font-weight: 800;
    color: #8CC63F;
    letter-spacing: -0.02em;
  }

  .stat-label {
    font-size: 0.6875rem;
    color: rgba(255, 255, 255, 0.35);
    text-transform: uppercase;
    letter-spacing: 0.08em;
    font-weight: 500;
  }

  .stat-divider {
    width: 1px;
    height: 32px;
    background: rgba(255, 255, 255, 0.1);
  }

  /* -- RIGHT PANEL: Visual -- */
  .hero-right {
    position: relative;
    width: 45%;
    overflow: hidden;
  }

  .right-bg {
    position: absolute;
    inset: 0;
    background: linear-gradient(
      160deg,
      #003F66 0%,
      #0089D0 40%,
      #8AD7F8 100%
    );
  }

  /* Geometric elements on right panel */
  .geo-elements {
    position: absolute;
    inset: 0;
    z-index: 1;
  }

  .geo-ring {
    position: absolute;
    border: 1px solid rgba(255, 255, 255, 0.1);
    border-radius: 50%;
  }

  .geo-ring-lg {
    width: 500px;
    height: 500px;
    top: -80px;
    right: -120px;
  }

  .geo-ring-sm {
    width: 280px;
    height: 280px;
    bottom: 10%;
    left: -60px;
    border-color: rgba(255, 255, 255, 0.06);
  }

  .geo-grid {
    position: absolute;
    inset: 0;
    opacity: 0.04;
    background-image:
      linear-gradient(rgba(255,255,255,1) 1px, transparent 1px),
      linear-gradient(90deg, rgba(255,255,255,1) 1px, transparent 1px);
    background-size: 48px 48px;
  }

  /* Logo watermark */
  .logo-watermark {
    position: absolute;
    top: 50%;
    left: 50%;
    transform: translate(-50%, -50%) scale(1);
    width: 320px;
    height: auto;
    opacity: 0;
    mix-blend-mode: screen;
    filter: grayscale(1) brightness(1.5);
    pointer-events: none;
    z-index: 0;
    transition: opacity 1.2s ease 0.5s;
  }

  .logo-watermark.visible {
    opacity: 0.04;
  }

  .geo-diagonal {
    position: absolute;
    top: 0;
    bottom: 0;
    left: 30%;
    width: 1px;
    background: rgba(255, 255, 255, 0.06);
    transform: rotate(15deg);
    transform-origin: top;
  }

  /* Center icon: crossed tools */
  .center-icon {
    position: absolute;
    top: 50%;
    left: 50%;
    transform: translate(-50%, -50%);
    z-index: 1;
    display: flex;
    align-items: center;
    justify-content: center;
    opacity: 0;
    transition: opacity 1s ease 0.3s;
  }

  .center-icon.visible {
    opacity: 1;
  }

  .center-icon svg:first-child {
    animation: floatSlow 6s ease-in-out infinite;
  }

  .center-icon .tool-2 {
    position: absolute;
    transform: rotate(45deg);
    animation: floatSlow 6s ease-in-out infinite reverse;
  }

  @keyframes floatSlow {
    0%, 100% { transform: translate(-50%, -50%) rotate(0deg) scale(1); }
    25% { transform: translate(-50%, -48%) rotate(2deg) scale(1.02); }
    50% { transform: translate(-50%, -52%) rotate(0deg) scale(1); }
    75% { transform: translate(-50%, -49%) rotate(-2deg) scale(1.01); }
  }

  .center-icon svg:first-child {
    animation: breathe 6s ease-in-out infinite;
  }

  .center-icon .tool-2 {
    position: absolute;
    transform: rotate(45deg);
    animation: breatheReverse 8s ease-in-out infinite;
  }

  @keyframes breathe {
    0%, 100% { opacity: 1; transform: scale(1) rotate(0deg); }
    50% { opacity: 0.7; transform: scale(1.05) rotate(3deg); }
  }

  @keyframes breatheReverse {
    0%, 100% { opacity: 1; transform: rotate(45deg) scale(1); }
    50% { opacity: 0.6; transform: rotate(48deg) scale(1.08); }
  }

  /* Floating badges with animation */
  .float-badge {
    position: absolute;
    z-index: 3;
    display: inline-flex;
    align-items: center;
    gap: 8px;
    padding: 10px 16px;
    background: rgba(255, 255, 255, 0.12);
    backdrop-filter: blur(12px);
    border: 1px solid rgba(255, 255, 255, 0.15);
    border-radius: 0;
    color: white;
    font-size: 0.75rem;
    font-weight: 600;
    letter-spacing: 0.02em;
    opacity: 0;
    transform: translateY(16px);
    transition: opacity 0.6s ease, transform 0.6s ease;
  }

  .float-badge.visible {
    opacity: 1;
    transform: translateY(0);
    animation: badgeFloat 5s ease-in-out infinite;
  }

  /* Each badge gets a slightly different float animation */
  .float-badge:nth-child(5).visible {
    animation: badgeFloat 5s ease-in-out infinite;
  }

  .float-badge:nth-child(6).visible {
    animation: badgeFloat2 6s ease-in-out infinite;
  }

  .float-badge:nth-child(7).visible {
    animation: badgeFloat3 5.5s ease-in-out infinite;
  }

  .float-badge:nth-child(8).visible {
    animation: badgeFloat 7s ease-in-out infinite;
  }

  @keyframes badgeFloat {
    0%, 100% { transform: translateY(0); }
    50% { transform: translateY(-8px); }
  }

  @keyframes badgeFloat2 {
    0%, 100% { transform: translateY(0) translateX(0); }
    33% { transform: translateY(-6px) translateX(3px); }
    66% { transform: translateY(2px) translateX(-2px); }
  }

  @keyframes badgeFloat3 {
    0%, 100% { transform: translateY(0); }
    50% { transform: translateY(-10px); }
  }

  .float-badge svg {
    opacity: 0.8;
  }

  /* Diagonal clip (left edge of right panel) */
  .diagonal-clip {
    position: absolute;
    top: 0;
    bottom: 0;
    left: -1px;
    width: 80px;
    background: linear-gradient(160deg, #1a2332 0%, #1e3040 50%, #1a3040 100%);
    clip-path: polygon(0 0, 100% 8%, 0 100%);
    z-index: 2;
  }

  /* -- Responsive -- */
  @media (max-width: 1024px) {
    .hero {
      flex-direction: column;
    }

    .hero-left {
      width: 100%;
      padding: 7rem 1.5rem 3rem;
      text-align: center;
      align-items: center;
      justify-content: center;
    }

    .hero-content {
      max-width: 600px;
      margin: 0 auto;
    }

    .hero-tag {
      justify-content: center;
    }

    .hero-actions {
      justify-content: center;
    }

    .hero-stats {
      justify-content: center;
    }

    .hero-desc {
      margin-left: auto;
      margin-right: auto;
    }

    .hero-right {
      width: 100%;
      height: 300px;
    }

    .diagonal-clip {
      display: none;
    }
  }

  @media (max-width: 640px) {
    .hero-left {
      padding: 6rem 1rem 2rem;
    }

    .hero-heading {
      font-size: clamp(1.625rem, 6vw, 2rem);
    }

    .hero-actions {
      flex-direction: column;
      width: 100%;
    }

    .btn-hero-primary,
    .btn-hero-ghost {
      width: 100%;
      justify-content: center;
      padding: 14px 20px;
      min-height: 48px;
    }

    .hero-stats {
      gap: 1rem;
      flex-wrap: wrap;
    }

    .stat-value {
      font-size: 1.25rem;
    }

    .stat-label {
      font-size: 0.6rem;
    }

    .stat-divider {
      height: 24px;
    }

    .hero-right {
      height: 200px;
    }

    .float-badge {
      padding: 6px 10px;
      font-size: 0.625rem;
    }
  }

  @media (max-width: 360px) {
    .hero-left {
      padding: 5.5rem 0.75rem 1.5rem;
    }

    .hero-tag {
      font-size: 0.6rem;
    }

    .hero-desc {
      font-size: 0.875rem;
    }
  }
</style>
