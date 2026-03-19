<script>
  const phoneNumber = '573204464553';

  let isOpen = $state(false);
  let nombre = $state('');
  let servicio = $state('');
  let mensaje = $state('');

  const servicios = [
    'Transporte de Carga por Carretera',
    'Obras Civiles y Mantenimiento Locativo',
    'Movimiento de Carga - Izaje',
    'Remediación Ambiental',
    'Transición Energética',
    'Alquiler de Maquinaria',
  ];

  function toggleCard() {
    isOpen = !isOpen;
  }

  function closeCard() {
    isOpen = false;
  }

  function handleSubmit(e) {
    e.preventDefault();

    const mensajeFinal = mensaje.trim() || 'Sin mensaje adicional';
    const text =
      `*Nueva Consulta - Multiservicios P&J*\n\n` +
      `*Nombre:* ${nombre}\n` +
      `*Servicio:* ${servicio}\n` +
      `*Mensaje:* ${mensajeFinal}`;

    const url = `https://wa.me/${phoneNumber}?text=${encodeURIComponent(text)}`;
    window.open(url, '_blank', 'noopener,noreferrer');
    closeCard();
  }
</script>

<!-- Popup card -->
{#if isOpen}
  <!-- Backdrop (transparent, closes on click outside on mobile) -->
  <div
    class="backdrop"
    onclick={closeCard}
    aria-hidden="true"
  ></div>
{/if}

<div class="card-wrapper" class:card-visible={isOpen} aria-live="polite">
  <div class="card" role="dialog" aria-modal="true" aria-label="Formulario de contacto WhatsApp">
    <!-- Header -->
    <div class="card-header">
      <div class="header-avatar">
        <svg viewBox="0 0 32 32" width="22" height="22" fill="#fff" aria-hidden="true">
          <path d="M16.004 0C7.165 0 0 7.163 0 16.001c0 2.822.737 5.58 2.139 8.008L.074 32l8.2-2.148A15.93 15.93 0 0 0 16.004 32C24.838 32 32 24.837 32 16.001 32 7.163 24.838 0 16.004 0zm0 29.32a13.27 13.27 0 0 1-7.172-2.096l-.514-.306-5.33 1.398 1.423-5.2-.335-.533A13.21 13.21 0 0 1 2.68 16.001c0-7.35 5.98-13.32 13.324-13.32 7.346 0 13.316 5.97 13.316 13.32 0 7.35-5.97 13.32-13.316 13.32zm7.304-9.975c-.4-.2-2.367-1.168-2.734-1.301-.367-.134-.634-.2-.9.2-.268.4-1.034 1.3-1.268 1.568-.234.267-.467.3-.867.1-.4-.2-1.69-.623-3.218-1.987-1.189-1.062-1.993-2.374-2.227-2.774-.234-.4-.025-.616.176-.815.18-.18.4-.467.6-.7.2-.234.267-.4.4-.668.134-.267.067-.5-.033-.7-.1-.2-.9-2.168-1.234-2.968-.325-.78-.655-.674-.9-.687l-.767-.012c-.267 0-.7.1-1.067.5-.367.4-1.4 1.368-1.4 3.336 0 1.967 1.434 3.868 1.634 4.134.2.268 2.823 4.31 6.84 6.043.955.413 1.7.659 2.282.844.959.305 1.832.262 2.522.159.77-.115 2.367-.968 2.7-1.903.334-.934.334-1.734.234-1.902-.1-.167-.367-.267-.767-.467z"/>
        </svg>
      </div>
      <div class="header-text">
        <span class="header-title">Te asesoramos en línea</span>
        <span class="header-subtitle">Comunícate con nosotros ¡Te brindamos asesoría personalizada!</span>
      </div>
      <button
        class="close-btn"
        onclick={closeCard}
        aria-label="Cerrar formulario de contacto"
        type="button"
      >
        <svg viewBox="0 0 24 24" width="18" height="18" fill="none" stroke="#fff" stroke-width="2.5" stroke-linecap="round" aria-hidden="true">
          <line x1="18" y1="6" x2="6" y2="18"/>
          <line x1="6" y1="6" x2="18" y2="18"/>
        </svg>
      </button>
    </div>

    <!-- Form body -->
    <form class="card-body" onsubmit={handleSubmit} novalidate>
      <div class="field">
        <label for="wa-nombre" class="field-label">Nombre <span class="required" aria-hidden="true">*</span></label>
        <input
          id="wa-nombre"
          type="text"
          class="field-input"
          placeholder="Tu nombre completo"
          bind:value={nombre}
          required
          autocomplete="name"
        />
      </div>

      <div class="field">
        <label for="wa-servicio" class="field-label">Servicio de Interés <span class="required" aria-hidden="true">*</span></label>
        <select
          id="wa-servicio"
          class="field-input field-select"
          bind:value={servicio}
          required
        >
          <option value="" disabled selected>Selecciona un servicio</option>
          {#each servicios as s}
            <option value={s}>{s}</option>
          {/each}
        </select>
      </div>

      <div class="field">
        <label for="wa-mensaje" class="field-label">Mensaje <span class="optional">(opcional)</span></label>
        <textarea
          id="wa-mensaje"
          class="field-input field-textarea"
          placeholder="Cuéntanos más sobre lo que necesitas..."
          bind:value={mensaje}
          rows="3"
        ></textarea>
      </div>

      <button type="submit" class="submit-btn" disabled={!nombre.trim() || !servicio}>
        <svg viewBox="0 0 32 32" width="18" height="18" fill="#fff" aria-hidden="true">
          <path d="M16.004 0C7.165 0 0 7.163 0 16.001c0 2.822.737 5.58 2.139 8.008L.074 32l8.2-2.148A15.93 15.93 0 0 0 16.004 32C24.838 32 32 24.837 32 16.001 32 7.163 24.838 0 16.004 0zm0 29.32a13.27 13.27 0 0 1-7.172-2.096l-.514-.306-5.33 1.398 1.423-5.2-.335-.533A13.21 13.21 0 0 1 2.68 16.001c0-7.35 5.98-13.32 13.324-13.32 7.346 0 13.316 5.97 13.316 13.32 0 7.35-5.97 13.32-13.316 13.32zm7.304-9.975c-.4-.2-2.367-1.168-2.734-1.301-.367-.134-.634-.2-.9.2-.268.4-1.034 1.3-1.268 1.568-.234.267-.467.3-.867.1-.4-.2-1.69-.623-3.218-1.987-1.189-1.062-1.993-2.374-2.227-2.774-.234-.4-.025-.616.176-.815.18-.18.4-.467.6-.7.2-.234.267-.4.4-.668.134-.267.067-.5-.033-.7-.1-.2-.9-2.168-1.234-2.968-.325-.78-.655-.674-.9-.687l-.767-.012c-.267 0-.7.1-1.067.5-.367.4-1.4 1.368-1.4 3.336 0 1.967 1.434 3.868 1.634 4.134.2.268 2.823 4.31 6.84 6.043.955.413 1.7.659 2.282.844.959.305 1.832.262 2.522.159.77-.115 2.367-.968 2.7-1.903.334-.934.334-1.734.234-1.902-.1-.167-.367-.267-.767-.467z"/>
        </svg>
        Enviar por WhatsApp
      </button>
    </form>
  </div>
</div>

<!-- Floating trigger button -->
<button
  class="whatsapp-button"
  onclick={toggleCard}
  aria-label={isOpen ? 'Cerrar chat de WhatsApp' : 'Abrir chat de WhatsApp'}
  aria-expanded={isOpen}
  type="button"
>
  {#if !isOpen}
    <span class="pulse-ring" aria-hidden="true"></span>
  {/if}

  {#if isOpen}
    <!-- X icon when open -->
    <svg viewBox="0 0 24 24" width="24" height="24" fill="none" stroke="#fff" stroke-width="2.5" stroke-linecap="round" aria-hidden="true">
      <line x1="18" y1="6" x2="6" y2="18"/>
      <line x1="6" y1="6" x2="18" y2="18"/>
    </svg>
  {:else}
    <!-- WhatsApp icon when closed -->
    <svg viewBox="0 0 32 32" width="28" height="28" fill="#fff" aria-hidden="true">
      <path d="M16.004 0C7.165 0 0 7.163 0 16.001c0 2.822.737 5.58 2.139 8.008L.074 32l8.2-2.148A15.93 15.93 0 0 0 16.004 32C24.838 32 32 24.837 32 16.001 32 7.163 24.838 0 16.004 0zm0 29.32a13.27 13.27 0 0 1-7.172-2.096l-.514-.306-5.33 1.398 1.423-5.2-.335-.533A13.21 13.21 0 0 1 2.68 16.001c0-7.35 5.98-13.32 13.324-13.32 7.346 0 13.316 5.97 13.316 13.32 0 7.35-5.97 13.32-13.316 13.32zm7.304-9.975c-.4-.2-2.367-1.168-2.734-1.301-.367-.134-.634-.2-.9.2-.268.4-1.034 1.3-1.268 1.568-.234.267-.467.3-.867.1-.4-.2-1.69-.623-3.218-1.987-1.189-1.062-1.993-2.374-2.227-2.774-.234-.4-.025-.616.176-.815.18-.18.4-.467.6-.7.2-.234.267-.4.4-.668.134-.267.067-.5-.033-.7-.1-.2-.9-2.168-1.234-2.968-.325-.78-.655-.674-.9-.687l-.767-.012c-.267 0-.7.1-1.067.5-.367.4-1.4 1.368-1.4 3.336 0 1.967 1.434 3.868 1.634 4.134.2.268 2.823 4.31 6.84 6.043.955.413 1.7.659 2.282.844.959.305 1.832.262 2.522.159.77-.115 2.367-.968 2.7-1.903.334-.934.334-1.734.234-1.902-.1-.167-.367-.267-.767-.467z"/>
    </svg>
  {/if}
</button>

<style>
  /* ── Floating trigger button ── */
  .whatsapp-button {
    position: fixed;
    right: 1.5rem;
    bottom: 1.5rem;
    z-index: 1000;
    width: 56px;
    height: 56px;
    border-radius: 50%;
    background-color: #25D366;
    border: none;
    cursor: pointer;
    display: flex;
    align-items: center;
    justify-content: center;
    box-shadow: 0 4px 14px rgba(37, 211, 102, 0.45);
    transition: transform 0.2s ease, box-shadow 0.2s ease, background-color 0.2s ease;
    outline-offset: 3px;
  }

  .whatsapp-button:hover {
    transform: scale(1.08);
    box-shadow: 0 6px 20px rgba(37, 211, 102, 0.55);
  }

  .whatsapp-button:focus-visible {
    outline: 2px solid #25D366;
  }

  /* ── Pulse ring ── */
  .pulse-ring {
    position: absolute;
    width: 100%;
    height: 100%;
    border-radius: 50%;
    border: 2px solid #25D366;
    animation: pulse 2s ease-out infinite;
    pointer-events: none;
  }

  @keyframes pulse {
    0% { transform: scale(1); opacity: 0.6; }
    100% { transform: scale(1.65); opacity: 0; }
  }

  /* ── Transparent backdrop (closes card on outside click) ── */
  .backdrop {
    position: fixed;
    inset: 0;
    z-index: 998;
    background: transparent;
  }

  /* ── Card wrapper – handles slide-up + fade animation ── */
  .card-wrapper {
    position: fixed;
    right: 1.5rem;
    bottom: calc(56px + 1.5rem + 12px); /* button height + bottom offset + gap */
    z-index: 999;
    width: 320px;

    /* Hidden state */
    opacity: 0;
    pointer-events: none;
    transform: translateY(16px) scale(0.97);
    transform-origin: bottom right;
    transition:
      opacity 0.22s cubic-bezier(0.4, 0, 0.2, 1),
      transform 0.22s cubic-bezier(0.4, 0, 0.2, 1);
  }

  .card-wrapper.card-visible {
    opacity: 1;
    pointer-events: auto;
    transform: translateY(0) scale(1);
  }

  /* ── Card shell ── */
  .card {
    background: #ffffff;
    border-radius: 16px;
    box-shadow:
      0 8px 32px rgba(0, 0, 0, 0.14),
      0 2px 8px rgba(0, 0, 0, 0.08);
    overflow: hidden;
    border: 1px solid rgba(0, 0, 0, 0.06);
  }

  /* ── Card header ── */
  .card-header {
    background-color: #25D366;
    padding: 14px 16px;
    display: flex;
    align-items: flex-start;
    gap: 10px;
  }

  .header-avatar {
    flex-shrink: 0;
    width: 36px;
    height: 36px;
    border-radius: 50%;
    background-color: rgba(255, 255, 255, 0.2);
    display: flex;
    align-items: center;
    justify-content: center;
    margin-top: 2px;
  }

  .header-text {
    flex: 1;
    display: flex;
    flex-direction: column;
    gap: 2px;
    min-width: 0;
  }

  .header-title {
    font-size: 0.9rem;
    font-weight: 700;
    color: #ffffff;
    line-height: 1.2;
    letter-spacing: 0.01em;
  }

  .header-subtitle {
    font-size: 0.72rem;
    color: rgba(255, 255, 255, 0.88);
    line-height: 1.35;
  }

  .close-btn {
    flex-shrink: 0;
    width: 28px;
    height: 28px;
    border-radius: 50%;
    border: none;
    background: rgba(255, 255, 255, 0.18);
    cursor: pointer;
    display: flex;
    align-items: center;
    justify-content: center;
    transition: background 0.15s ease;
    padding: 0;
  }

  .close-btn:hover {
    background: rgba(255, 255, 255, 0.32);
  }

  .close-btn:focus-visible {
    outline: 2px solid #fff;
    outline-offset: 2px;
  }

  /* ── Card body / form ── */
  .card-body {
    padding: 18px 16px 16px;
    display: flex;
    flex-direction: column;
    gap: 13px;
  }

  .field {
    display: flex;
    flex-direction: column;
    gap: 5px;
  }

  .field-label {
    font-size: 0.75rem;
    font-weight: 600;
    color: #374151;
    letter-spacing: 0.02em;
    text-transform: uppercase;
  }

  .required {
    color: #ef4444;
    margin-left: 2px;
  }

  .optional {
    font-weight: 400;
    color: #9ca3af;
    text-transform: none;
    font-size: 0.72rem;
    letter-spacing: 0;
  }

  .field-input {
    width: 100%;
    padding: 9px 12px;
    border: 1.5px solid #e5e7eb;
    border-radius: 8px;
    font-size: 0.82rem;
    color: #111827;
    background: #f9fafb;
    transition: border-color 0.15s ease, box-shadow 0.15s ease;
    box-sizing: border-box;
    font-family: inherit;
    outline: none;
  }

  .field-input::placeholder {
    color: #9ca3af;
  }

  .field-input:focus {
    border-color: #25D366;
    box-shadow: 0 0 0 3px rgba(37, 211, 102, 0.14);
    background: #fff;
  }

  .field-select {
    cursor: pointer;
    appearance: none;
    background-image: url("data:image/svg+xml,%3Csvg xmlns='http://www.w3.org/2000/svg' width='12' height='8' viewBox='0 0 12 8'%3E%3Cpath d='M1 1l5 5 5-5' stroke='%236b7280' stroke-width='1.8' fill='none' stroke-linecap='round' stroke-linejoin='round'/%3E%3C/svg%3E");
    background-repeat: no-repeat;
    background-position: right 11px center;
    padding-right: 30px;
  }

  .field-textarea {
    resize: vertical;
    min-height: 70px;
    line-height: 1.45;
  }

  /* ── Submit button ── */
  .submit-btn {
    display: flex;
    align-items: center;
    justify-content: center;
    gap: 8px;
    width: 100%;
    padding: 11px 16px;
    background-color: #25D366;
    color: #fff;
    border: none;
    border-radius: 10px;
    font-size: 0.85rem;
    font-weight: 700;
    cursor: pointer;
    letter-spacing: 0.02em;
    transition: background-color 0.18s ease, transform 0.15s ease, opacity 0.18s ease;
    font-family: inherit;
    margin-top: 2px;
  }

  .submit-btn:hover:not(:disabled) {
    background-color: #1ebe5d;
    transform: translateY(-1px);
  }

  .submit-btn:active:not(:disabled) {
    transform: translateY(0);
  }

  .submit-btn:disabled {
    opacity: 0.48;
    cursor: not-allowed;
  }

  .submit-btn:focus-visible {
    outline: 2px solid #25D366;
    outline-offset: 3px;
  }

  /* ── Mobile: full-width card ── */
  @media (max-width: 420px) {
    .card-wrapper {
      right: 12px;
      left: 12px;
      width: auto;
      bottom: calc(56px + 1.5rem + 12px);
    }

    .whatsapp-button {
      right: 1rem;
      bottom: 1rem;
    }
  }
</style>
