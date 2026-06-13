<!--
  WhatsAppButton — botón flotante de SISTEMA (siempre se muestra al hacer scroll).
  brutalist técnico COICEM. El verde de marca WhatsApp (#25D366) se mantiene a propósito.
  ⚠️ siteConfig.contact.whatsapp PUEDE SER null → entonces NO se inventa número:
     el botón apunta a #contacto y el tooltip avisa "NÚMERO PENDIENTE".
-->
<script lang="ts">
  import { siteConfig } from '../lib/site-config';

  const MESSAGE = 'Hola, me interesa el servicio de mantenimiento de COICEM.';
  const num = siteConfig.contact.whatsapp;
  const hasNumber = Boolean(num);

  const href = hasNumber
    ? `https://wa.me/${num}?text=${encodeURIComponent(MESSAGE)}`
    : '#contacto';
  const label = hasNumber
    ? 'Escribir por WhatsApp a COICEM'
    : 'Ir a contacto (WhatsApp pendiente)';
  const tip = hasNumber ? 'WHATSAPP · ESCRÍBENOS' : 'WHATSAPP · NÚMERO PENDIENTE';

  let visible = $state(false);
  let reduced = $state(false);

  $effect(() => {
    if (typeof window === 'undefined') return;
    reduced = window.matchMedia('(prefers-reduced-motion: reduce)').matches;

    const onScroll = () => { visible = window.scrollY > 300; };
    onScroll();
    window.addEventListener('scroll', onScroll, { passive: true });
    return () => window.removeEventListener('scroll', onScroll);
  });
</script>

<a
  class="wa"
  class:visible
  class:reduced
  {href}
  aria-label={label}
  target={hasNumber ? '_blank' : undefined}
  rel={hasNumber ? 'noopener noreferrer' : undefined}
>
  <svg class="ico" viewBox="0 0 24 24" width="26" height="26" aria-hidden="true">
    <path
      fill="#fff"
      d="M.057 24l1.687-6.163a11.867 11.867 0 0 1-1.587-5.946C.16 5.335 5.495 0 12.05 0a11.82 11.82 0 0 1 8.413 3.488 11.824 11.824 0 0 1 3.48 8.414c-.003 6.557-5.338 11.892-11.893 11.892a11.9 11.9 0 0 1-5.688-1.448L.057 24zm6.597-3.807c1.676.995 3.276 1.591 5.392 1.592 5.448 0 9.886-4.434 9.889-9.885.002-5.462-4.415-9.89-9.881-9.892-5.452 0-9.887 4.434-9.889 9.884a9.86 9.86 0 0 0 1.51 5.26l-.999 3.648 3.978-1.207zm11.387-5.464c-.074-.124-.272-.198-.57-.347-.297-.149-1.758-.868-2.031-.967-.272-.099-.47-.149-.669.149-.198.297-.768.967-.941 1.165-.173.198-.347.223-.644.074-.297-.149-1.255-.462-2.39-1.475-.883-.788-1.48-1.761-1.653-2.059-.173-.297-.018-.458.13-.606.134-.133.297-.347.446-.521.151-.172.2-.296.3-.495.099-.198.05-.372-.025-.521-.075-.148-.669-1.611-.916-2.206-.242-.579-.487-.501-.669-.51l-.57-.01c-.198 0-.52.074-.792.372s-1.04 1.016-1.04 2.479 1.065 2.876 1.213 3.074c.149.198 2.095 3.2 5.076 4.487.71.306 1.263.489 1.694.626.712.226 1.36.194 1.872.118.571-.085 1.758-.719 2.006-1.413.247-.694.247-1.289.173-1.413z"
    />
  </svg>
  <span class="tip" aria-hidden="true">{tip}</span>
</a>

<style>
  .wa {
    position: fixed;
    right: 1.5rem;
    bottom: 1.5rem;
    z-index: 9000;
    display: grid;
    place-items: center;
    width: 56px;
    height: 56px;
    border-radius: 9999px;        /* única excepción de border-radius */
    background: #25D366;          /* verde de marca WhatsApp */
    border: 2px solid #000000;
    box-shadow: 4px 4px 0 #000000;
    pointer-events: none;
    opacity: 0;
    transform: translateY(12px);
    transition: opacity 320ms cubic-bezier(0.83, 0, 0.17, 1),
                transform 320ms cubic-bezier(0.83, 0, 0.17, 1);
  }
  .wa.visible {
    opacity: 1;
    transform: translateY(0);
    pointer-events: auto;
  }
  .wa:hover  { box-shadow: 2px 2px 0 #000000; transform: translate(2px, 2px); }
  .wa:active { box-shadow: 0 0 0 #000000;     transform: translate(4px, 4px); }
  .wa:focus-visible { outline: 2px solid #F79204; outline-offset: 3px; }

  .ico { display: block; }

  .tip {
    position: absolute;
    right: calc(100% + 12px);
    top: 50%;
    transform: translateY(-50%);
    white-space: nowrap;
    font-family: 'IBM Plex Mono', monospace;
    font-size: 10px;
    letter-spacing: 0.08em;
    color: #EDEDE8;
    background: #0B0E14;
    border: 1px solid #313F50;
    padding: 6px 9px;
    opacity: 0;
    pointer-events: none;
    transition: opacity 140ms ease;
  }
  .wa:hover .tip,
  .wa:focus-visible .tip { opacity: 1; }

  /* reduced-motion: sin animación de entrada ni desplazamiento */
  .wa.reduced {
    transition: none;
    transform: none;
  }
  .wa.reduced.visible { transform: none; }
  @media (prefers-reduced-motion: reduce) {
    .wa  { transition: none; transform: none; }
    .wa.visible { transform: none; }
    .wa:hover, .wa:active { transform: none; box-shadow: 4px 4px 0 #000000; }
    .tip { transition: none; }
  }
</style>
