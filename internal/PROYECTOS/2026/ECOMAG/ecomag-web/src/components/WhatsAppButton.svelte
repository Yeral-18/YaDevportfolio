<script>
  import { onMount } from 'svelte';

  let visible = false;
  let showTooltip = false;
  let prefersReducedMotion = false;

  onMount(() => {
    prefersReducedMotion = window.matchMedia('(prefers-reduced-motion: reduce)').matches;
    const timer = setTimeout(() => { visible = true; }, 1500);
    return () => clearTimeout(timer);
  });
</script>

{#if visible}
  <div
    class="whatsapp-fixed"
    on:mouseenter={() => showTooltip = true}
    on:mouseleave={() => showTooltip = false}
    role="presentation"
  >
    <!-- Tooltip -->
    {#if showTooltip}
      <span class="whatsapp-tooltip">
        &iquest;Necesitas ayuda?
      </span>
    {/if}

    <!-- Button container — rings are positioned relative to this -->
    <div class="whatsapp-btn-container">
      <!-- Pulse rings -->
      <span class="whatsapp-ring whatsapp-ring--1" aria-hidden="true"></span>
      <span class="whatsapp-ring whatsapp-ring--2" aria-hidden="true"></span>
      <span class="whatsapp-ring whatsapp-ring--3" aria-hidden="true"></span>

      <!-- Actual button -->
      <a
        href="https://wa.me/57XXXXXXXXXX"
        target="_blank"
        rel="noopener noreferrer"
        class="whatsapp-btn"
        aria-label="Contactanos por WhatsApp"
      >
        <svg
          xmlns="http://www.w3.org/2000/svg"
          width="28"
          height="28"
          viewBox="0 0 24 24"
          fill="#fff"
          aria-hidden="true"
        >
          <path d="M17.472 14.382c-.297-.149-1.758-.867-2.03-.967-.273-.099-.471-.148-.67.15-.197.297-.767.966-.94 1.164-.173.199-.347.223-.644.075-.297-.15-1.255-.463-2.39-1.475-.883-.788-1.48-1.761-1.653-2.059-.173-.297-.018-.458.13-.606.134-.133.298-.347.446-.52.149-.174.198-.298.298-.497.099-.198.05-.371-.025-.52-.075-.149-.669-1.612-.916-2.207-.242-.579-.487-.5-.669-.51-.173-.008-.371-.01-.57-.01-.198 0-.52.074-.792.372-.272.297-1.04 1.016-1.04 2.479 0 1.462 1.065 2.875 1.213 3.074.149.198 2.096 3.2 5.077 4.487.709.306 1.262.489 1.694.625.712.227 1.36.195 1.871.118.571-.085 1.758-.719 2.006-1.413.248-.694.248-1.289.173-1.413-.074-.124-.272-.198-.57-.347m-5.421 7.403h-.004a9.87 9.87 0 0 1-5.031-1.378l-.361-.214-3.741.982.998-3.648-.235-.374a9.86 9.86 0 0 1-1.51-5.26c.001-5.45 4.436-9.884 9.888-9.884 2.64 0 5.122 1.03 6.988 2.898a9.825 9.825 0 0 1 2.893 6.994c-.003 5.45-4.437 9.884-9.885 9.884m8.413-18.297A11.815 11.815 0 0 0 12.05 0C5.495 0 .16 5.335.157 11.892c0 2.096.547 4.142 1.588 5.945L.057 24l6.305-1.654a11.882 11.882 0 0 0 5.683 1.448h.005c6.554 0 11.89-5.335 11.893-11.893a11.821 11.821 0 0 0-3.48-8.413z"/>
        </svg>
      </a>
    </div>
  </div>
{/if}

<style>
  .whatsapp-fixed {
    position: fixed;
    bottom: 1.25rem;
    right: 1.25rem;
    z-index: 50;
    display: flex;
    align-items: center;
  }

  @media (min-width: 640px) {
    .whatsapp-fixed {
      bottom: 1.5rem;
      right: 1.5rem;
    }
  }

  /* ── Tooltip — hidden on small touch screens ── */
  @media (max-width: 639px) {
    .whatsapp-tooltip {
      display: none;
    }
  }

  .whatsapp-tooltip {
    position: absolute;
    right: calc(100% + 0.75rem);
    top: 50%;
    transform: translateY(-50%);
    white-space: nowrap;
    background: #fff;
    color: #1a1a2e;
    font-family: var(--font-body);
    font-size: 0.8125rem;
    font-weight: 500;
    padding: 0.5rem 0.875rem;
    border-radius: 0.5rem;
    box-shadow: 0 4px 16px rgba(0, 0, 0, 0.15);
    pointer-events: none;
    animation: tooltipFade 0.25s ease-out forwards;
  }

  .whatsapp-tooltip::after {
    content: '';
    position: absolute;
    top: 50%;
    right: -6px;
    transform: translateY(-50%);
    border: 6px solid transparent;
    border-left-color: #fff;
    border-right: 0;
  }

  @keyframes tooltipFade {
    from { opacity: 0; transform: translateY(-50%) translateX(8px); }
    to   { opacity: 1; transform: translateY(-50%) translateX(0); }
  }

  /* ── Button container — anchor for rings ── */
  .whatsapp-btn-container {
    position: relative;
    width: 60px;
    height: 60px;
  }

  @media (min-width: 640px) {
    .whatsapp-btn-container {
      width: 68px;
      height: 68px;
    }
  }

  /* ── Button ── */
  .whatsapp-btn {
    position: absolute;
    inset: 0;
    display: flex;
    align-items: center;
    justify-content: center;
    border-radius: 9999px;
    background-color: #25D366;
    box-shadow: 0 4px 20px rgba(37, 211, 102, 0.45);
    transition: transform 0.3s cubic-bezier(0.34, 1.56, 0.64, 1), box-shadow 0.3s ease;
    z-index: 2;
  }

  @media (min-width: 640px) {
    .whatsapp-btn svg {
      width: 32px;
      height: 32px;
    }
  }

  .whatsapp-btn:hover {
    transform: scale(1.12);
    box-shadow: 0 6px 28px rgba(37, 211, 102, 0.55);
  }

  .whatsapp-btn:focus-visible {
    outline: 2px solid #25D366;
    outline-offset: 4px;
  }

  /* ── Pulse rings — centered on the button ── */
  .whatsapp-ring {
    position: absolute;
    inset: 0;
    border-radius: 9999px;
    border: 3px solid #25D366;
    z-index: 1;
    pointer-events: none;
    will-change: transform, opacity;
  }

  .whatsapp-ring--1 {
    animation: pulseWave 2.4s cubic-bezier(0.215, 0.61, 0.355, 1) infinite;
  }

  .whatsapp-ring--2 {
    animation: pulseWave 2.4s cubic-bezier(0.215, 0.61, 0.355, 1) infinite;
    animation-delay: 0.8s;
  }

  .whatsapp-ring--3 {
    animation: pulseWave 2.4s cubic-bezier(0.215, 0.61, 0.355, 1) infinite;
    animation-delay: 1.6s;
  }

  @keyframes pulseWave {
    0% {
      transform: scale(1);
      opacity: 0.6;
    }
    50% {
      opacity: 0.25;
    }
    100% {
      transform: scale(1.35);
      opacity: 0;
    }
  }

  @media (min-width: 640px) {
    @keyframes pulseWave {
      0% {
        transform: scale(1);
        opacity: 0.6;
      }
      50% {
        opacity: 0.25;
      }
      100% {
        transform: scale(1.5);
        opacity: 0;
      }
    }
  }

  /* prefers-reduced-motion handled via JS */
</style>
