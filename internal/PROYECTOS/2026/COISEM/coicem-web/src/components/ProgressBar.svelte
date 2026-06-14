<!--
  ProgressBar — COICEM S.A.S
  SISTEMA (estándar YaDev §1): barra fija top 3px, % de scroll.
  Estilo brutalist: naranja hi-vis sólido (sin gradiente blando), borde duro.
-->
<script lang="ts">
  let progress = $state(0);

  $effect(() => {
    const updateProgress = () => {
      const scrollTop = window.scrollY;
      const docHeight = document.documentElement.scrollHeight - window.innerHeight;
      progress = docHeight > 0 ? (scrollTop / docHeight) * 100 : 0;
    };
    updateProgress();
    window.addEventListener('scroll', updateProgress, { passive: true });
    window.addEventListener('resize', updateProgress, { passive: true });
    return () => {
      window.removeEventListener('scroll', updateProgress);
      window.removeEventListener('resize', updateProgress);
    };
  });
</script>

<div
  class="progress-bar"
  role="progressbar"
  aria-valuenow={Math.round(progress)}
  aria-valuemin={0}
  aria-valuemax={100}
  aria-label="Progreso de lectura de la página"
  style="width: {progress}%"
></div>

<style>
  .progress-bar {
    position: fixed;
    top: 0;
    left: 0;
    height: 3px;
    background: #f79204;          /* hi-vis seguridad — sólido, sin gradiente */
    z-index: 9999;
    transition: width 0.1s linear;
    will-change: width;
    transform-origin: left;
  }

  @media (prefers-reduced-motion: reduce) {
    .progress-bar { transition: none; }
  }
</style>
