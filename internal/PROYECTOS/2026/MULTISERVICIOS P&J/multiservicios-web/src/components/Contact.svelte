<!--
  Contact — Centered vertical layout with info cards + form
  MULTISERVICIOS P&J S.A.S
  Svelte 5 syntax with $state / $effect
-->

<script lang="ts">
  // Google reCAPTCHA v3 global object
  declare const grecaptcha: any;

  // --- reCAPTCHA v3 site key ---
  // TODO: Replace this TEST key with your real key from https://www.google.com/recaptcha/admin
  // The test key always passes and is for development only.
  const RECAPTCHA_SITE_KEY = '6LeIxAcTAAAAAJcZVRqyHh71UMIEGNQ_MXjiZKhI';

  // --- Form State ---
  let nombre = $state("");
  let email = $state("");
  let telefono = $state("");
  let servicio = $state("");
  let mensaje = $state("");

  let errors = $state<Record<string, string>>({});
  let submitted = $state(false);
  let sending = $state(false);

  // --- Reveal animation ---
  let sectionEl = $state<HTMLElement | null>(null);
  let revealed = $state(false);

  $effect(() => {
    if (!sectionEl) return;
    const observer = new IntersectionObserver(
      (entries) => {
        entries.forEach((entry) => {
          if (entry.isIntersecting) {
            revealed = true;
            observer.unobserve(entry.target);
          }
        });
      },
      { threshold: 0.08, rootMargin: "0px 0px -40px 0px" }
    );
    observer.observe(sectionEl);
    return () => observer.disconnect();
  });

  const servicios = [
    "Transporte de Carga por Carretera",
    "Obras Civiles y Mantenimiento Locativo",
    "Movimiento de Carga - Izaje",
    "Remediación Ambiental",
    "Transición Energética",
    "Alquiler de Maquinaria",
  ];

  function validate(): boolean {
    const newErrors: Record<string, string> = {};

    if (!nombre.trim()) newErrors.nombre = "El nombre es requerido.";
    if (!email.trim()) {
      newErrors.email = "El correo es requerido.";
    } else if (!/^[^\s@]+@[^\s@]+\.[^\s@]+$/.test(email)) {
      newErrors.email = "Ingrese un correo válido.";
    }
    if (!telefono.trim()) {
      newErrors.telefono = "El teléfono es requerido.";
    }
    if (!servicio) newErrors.servicio = "Seleccione un servicio.";
    if (mensaje.trim() && mensaje.trim().length < 10) {
      newErrors.mensaje = "El mensaje debe tener al menos 10 caracteres.";
    }

    errors = newErrors;
    return Object.keys(newErrors).length === 0;
  }

  let emailSent = $state(false);
  let sendMethod = $state<'email' | 'whatsapp' | ''>('');

  async function handleEmail(e: Event) {
    e.preventDefault();
    if (!validate()) return;

    sending = true;
    sendMethod = 'email';
    emailSent = false;

    try {
      const response = await fetch('/contact.php', {
        method: 'POST',
        headers: {
          'Content-Type': 'application/json',
          'Accept': 'application/json'
        },
        body: JSON.stringify({
          nombre,
          email,
          telefono,
          servicio,
          mensaje
        })
      });

      const result = await response.json();
      emailSent = result.success;
    } catch (error) {
      console.error('Email error:', error);
      emailSent = false;
    }

    sending = false;
    submitted = true;
    resetAfterDelay();
  }

  function handleWhatsApp(e: Event) {
    e.preventDefault();
    if (!validate()) return;

    sendMethod = 'whatsapp';
    const whatsappMessage = encodeURIComponent(
      `*Nueva Consulta - Multiservicios P&J*\n\n` +
      `*Nombre:* ${nombre}\n` +
      `*Email:* ${email}\n` +
      `*Teléfono:* ${telefono}\n` +
      `*Servicio:* ${servicio}\n` +
      `*Mensaje:* ${mensaje.trim() || 'Sin mensaje adicional'}`
    );
    window.open(`https://wa.me/573204464553?text=${whatsappMessage}`, '_blank');

    submitted = true;
    resetAfterDelay();
  }

  function resetAfterDelay() {
    setTimeout(() => {
      submitted = false;
      emailSent = false;
      sendMethod = '';
      nombre = "";
      email = "";
      telefono = "";
      servicio = "";
      mensaje = "";
      errors = {};
    }, 5000);
  }
</script>

<section
  id="contacto"
  class="section-padding bg-white"
  bind:this={sectionEl}
>
  <div class="section-container">

    <!-- Centered Header -->
    <div
      class="text-center max-w-2xl mx-auto mb-12 transition-all duration-600"
      class:opacity-0={!revealed}
      class:translate-y-6={!revealed}
      class:opacity-100={revealed}
      class:translate-y-0={revealed}
    >
      <span class="inline-block text-xs font-bold tracking-[0.2em] uppercase text-[#0089D0] mb-3">
        CONTÁCTENOS
      </span>
      <h2 class="heading-primary mt-1 mb-4">
        Tiene un Proyecto en Mente?
      </h2>
      <p class="text-body max-w-lg mx-auto">
        Cuéntenos sobre su proyecto y nuestro equipo de ingenieros le brindará
        una asesoría personalizada sin compromiso.
      </p>
    </div>

    <!-- Info Cards Row -->
    <div
      class="grid grid-cols-1 sm:grid-cols-2 lg:grid-cols-3 gap-4 mb-12 transition-all duration-600 delay-150"
      class:opacity-0={!revealed}
      class:translate-y-6={!revealed}
      class:opacity-100={revealed}
      class:translate-y-0={revealed}
    >
      <!-- Phone Card -->
      <div class="contact-card group">
        <div class="contact-card-icon">
          <svg xmlns="http://www.w3.org/2000/svg" class="w-5 h-5" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round">
            <path d="M22 16.92v3a2 2 0 0 1-2.18 2 19.79 19.79 0 0 1-8.63-3.07 19.5 19.5 0 0 1-6-6 19.79 19.79 0 0 1-3.07-8.67A2 2 0 0 1 4.11 2h3a2 2 0 0 1 2 1.72 12.84 12.84 0 0 0 .7 2.81 2 2 0 0 1-.45 2.11L8.09 9.91a16 16 0 0 0 6 6l1.27-1.27a2 2 0 0 1 2.11-.45 12.84 12.84 0 0 0 2.81.7A2 2 0 0 1 22 16.92z"/>
          </svg>
        </div>
        <h3 class="text-sm font-semibold text-[#005B32] mb-1">Teléfono</h3>
        <a href="tel:+573204464553" class="text-sm text-[#607D8B] hover:text-[#0089D0] transition-colors">
          +57 320 4464553
        </a>
      </div>

      <!-- Email Card -->
      <div class="contact-card group">
        <div class="contact-card-icon">
          <svg xmlns="http://www.w3.org/2000/svg" class="w-5 h-5" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round">
            <path d="M4 4h16c1.1 0 2 .9 2 2v12c0 1.1-.9 2-2 2H4c-1.1 0-2-.9-2-2V6c0-1.1.9-2 2-2z"/>
            <polyline points="22,6 12,13 2,6"/>
          </svg>
        </div>
        <h3 class="text-sm font-semibold text-[#005B32] mb-1">Correo</h3>
        <a href="mailto:multiserviciospjsas@gmail.com" class="text-sm text-[#607D8B] hover:text-[#0089D0] transition-colors break-all">
          multiserviciospjsas@gmail.com
        </a>
      </div>

      <!-- Location Card -->
      <div class="contact-card group">
        <div class="contact-card-icon">
          <svg xmlns="http://www.w3.org/2000/svg" class="w-5 h-5" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round">
            <path d="M21 10c0 7-9 13-9 13s-9-6-9-13a9 9 0 0 1 18 0z"/>
            <circle cx="12" cy="10" r="3"/>
          </svg>
        </div>
        <h3 class="text-sm font-semibold text-[#005B32] mb-1">Oficina</h3>
        <p class="text-sm text-[#607D8B]">Barrancabermeja, Corregimiento El Llanito</p>
      </div>

    </div>

    <!-- Centered Form -->
    <div
      class="max-w-[640px] mx-auto transition-all duration-600 delay-300"
      class:opacity-0={!revealed}
      class:translate-y-6={!revealed}
      class:opacity-100={revealed}
      class:translate-y-0={revealed}
    >
      <div class="bg-[#F5F7FA] rounded-2xl p-6 sm:p-8 lg:p-10">
        {#if submitted}
          <!-- Success State -->
          <div class="flex flex-col items-center justify-center py-12 text-center">
            <div class="w-16 h-16 rounded-full bg-[#0089D0]/10 flex items-center justify-center mb-4">
              <svg xmlns="http://www.w3.org/2000/svg" class="w-8 h-8 text-[#0089D0]" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.5" stroke-linecap="round" stroke-linejoin="round">
                <polyline points="20 6 9 17 4 12"/>
              </svg>
            </div>
            <h3 class="heading-secondary text-xl mb-2">
              {sendMethod === 'email' ? (emailSent ? '¡Correo Enviado!' : 'Error al Enviar') : '¡WhatsApp Abierto!'}
            </h3>
            <p class="text-body text-sm max-w-sm">
              {#if sendMethod === 'email' && emailSent}
                Su consulta fue enviada correctamente. Nuestro equipo le responderá a la brevedad.
              {:else if sendMethod === 'email' && !emailSent}
                Hubo un error al enviar el correo. Intente de nuevo o use WhatsApp.
              {:else}
                Se abrió WhatsApp para enviar su consulta. Si no se abrió automáticamente, verifique que no tenga bloqueadas las ventanas emergentes.
              {/if}
            </p>
          </div>
        {:else}
          <!-- Form -->
          <form onsubmit={handleEmail} novalidate class="space-y-5">

            <!-- Row 1: Nombre + Email -->
            <div class="grid grid-cols-1 sm:grid-cols-2 gap-4">
              <div>
                <label for="contact-nombre" class="block text-sm font-medium text-[#005B32] mb-1.5">
                  Nombre Completo <span class="text-red-500">*</span>
                </label>
                <input
                  id="contact-nombre"
                  type="text"
                  bind:value={nombre}
                  placeholder="Ingrese su nombre"
                  class="input-field"
                  class:error={errors.nombre}
                />
                {#if errors.nombre}
                  <p class="text-red-500 text-xs mt-1">{errors.nombre}</p>
                {/if}
              </div>

              <div>
                <label for="contact-email" class="block text-sm font-medium text-[#005B32] mb-1.5">
                  Correo Electrónico <span class="text-red-500">*</span>
                </label>
                <input
                  id="contact-email"
                  type="email"
                  bind:value={email}
                  placeholder="correo@ejemplo.com"
                  class="input-field"
                  class:error={errors.email}
                />
                {#if errors.email}
                  <p class="text-red-500 text-xs mt-1">{errors.email}</p>
                {/if}
              </div>
            </div>

            <!-- Row 2: Telefono + Servicio -->
            <div class="grid grid-cols-1 sm:grid-cols-2 gap-4">
              <div>
                <label for="contact-telefono" class="block text-sm font-medium text-[#005B32] mb-1.5">
                  Teléfono <span class="text-red-500">*</span>
                </label>
                <input
                  id="contact-telefono"
                  type="tel"
                  bind:value={telefono}
                  placeholder="+57 300 000 0000"
                  class="input-field"
                  class:error={errors.telefono}
                />
                {#if errors.telefono}
                  <p class="text-red-500 text-xs mt-1">{errors.telefono}</p>
                {/if}
              </div>

              <div>
                <label for="contact-servicio" class="block text-sm font-medium text-[#005B32] mb-1.5">
                  Servicio de Interés <span class="text-red-500">*</span>
                </label>
                <select
                  id="contact-servicio"
                  bind:value={servicio}
                  class="input-field appearance-none"
                  class:error={errors.servicio}
                  style="background-image: url(&quot;data:image/svg+xml,%3Csvg xmlns='http://www.w3.org/2000/svg' width='16' height='16' viewBox='0 0 24 24' fill='none' stroke='%23005B32' stroke-width='2' stroke-linecap='round' stroke-linejoin='round'%3E%3Cpolyline points='6 9 12 15 18 9'%3E%3C/polyline%3E%3C/svg%3E&quot;); background-repeat: no-repeat; background-position: right 12px center;"
                >
                  <option value="" disabled>Seleccione un servicio</option>
                  {#each servicios as s}
                    <option value={s}>{s}</option>
                  {/each}
                </select>
                {#if errors.servicio}
                  <p class="text-red-500 text-xs mt-1">{errors.servicio}</p>
                {/if}
              </div>
            </div>

            <!-- Full width: Mensaje -->
            <div>
              <label for="contact-mensaje" class="block text-sm font-medium text-[#005B32] mb-1.5">
                Mensaje <span class="text-[#9CA3AF] text-xs font-normal">(opcional)</span>
              </label>
              <textarea
                id="contact-mensaje"
                bind:value={mensaje}
                rows="4"
                placeholder="Describa brevemente su proyecto o consulta..."
                class="input-field resize-none"
                class:error={errors.mensaje}
              ></textarea>
              {#if errors.mensaje}
                <p class="text-red-500 text-xs mt-1">{errors.mensaje}</p>
              {/if}
            </div>

            <!-- Submit Buttons -->
            <div class="grid grid-cols-1 sm:grid-cols-2 gap-3">
              <!-- Email Button -->
              <button
                type="submit"
                disabled={sending}
                class="btn-primary disabled:opacity-60 disabled:cursor-not-allowed disabled:transform-none"
              >
                {#if sending}
                  <svg class="w-5 h-5 animate-spin" xmlns="http://www.w3.org/2000/svg" fill="none" viewBox="0 0 24 24">
                    <circle class="opacity-25" cx="12" cy="12" r="10" stroke="currentColor" stroke-width="4"/>
                    <path class="opacity-75" fill="currentColor" d="M4 12a8 8 0 018-8V0C5.373 0 0 5.373 0 12h4zm2 5.291A7.962 7.962 0 014 12H0c0 3.042 1.135 5.824 3 7.938l3-2.647z"/>
                  </svg>
                  Enviando...
                {:else}
                  <svg xmlns="http://www.w3.org/2000/svg" class="w-5 h-5" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round">
                    <path d="M4 4h16c1.1 0 2 .9 2 2v12c0 1.1-.9 2-2 2H4c-1.1 0-2-.9-2-2V6c0-1.1.9-2 2-2z"/>
                    <polyline points="22,6 12,13 2,6"/>
                  </svg>
                  Enviar por Correo
                {/if}
              </button>

              <!-- WhatsApp Button -->
              <button
                type="button"
                onclick={handleWhatsApp}
                disabled={sending}
                class="btn-whatsapp disabled:opacity-60 disabled:cursor-not-allowed"
              >
                <svg xmlns="http://www.w3.org/2000/svg" class="w-5 h-5" viewBox="0 0 32 32" fill="currentColor">
                  <path d="M16.01 0C7.17 0 0 7.17 0 16.01c0 2.82.74 5.58 2.14 8.01L0 32l8.2-2.15a15.94 15.94 0 0 0 7.81 2.04c8.84 0 16.01-7.17 16.01-16.01S24.85 0 16.01 0zm0 29.22c-2.5 0-4.96-.67-7.1-1.95l-.51-.3-4.87 1.28 1.3-4.75-.33-.53A13.2 13.2 0 0 1 2.67 16C2.67 8.64 8.64 2.67 16 2.67S29.34 8.64 29.34 16 23.37 29.22 16.01 29.22zm7.33-9.87c-.4-.2-2.37-1.17-2.74-1.3-.37-.14-.64-.2-.91.2s-1.04 1.3-1.28 1.57c-.23.27-.47.3-.87.1s-1.7-.63-3.23-2c-1.19-1.06-2-2.38-2.24-2.78s-.02-.62.18-.82c.18-.18.4-.47.6-.7.2-.24.27-.4.4-.67.14-.27.07-.5-.03-.7s-.91-2.2-1.25-3c-.33-.8-.66-.68-.91-.7h-.78c-.27 0-.7.1-1.07.5s-1.4 1.37-1.4 3.34 1.44 3.87 1.64 4.14c.2.27 2.83 4.32 6.86 6.05.96.41 1.71.66 2.29.84.96.31 1.84.26 2.53.16.77-.12 2.37-.97 2.71-1.9.33-.94.33-1.74.23-1.9-.1-.17-.37-.27-.77-.47z"/>
                </svg>
                Enviar por WhatsApp
              </button>
            </div>

            <!-- reCAPTCHA notice -->
            <p class="text-center text-[11px] text-[#9CA3AF] mt-3 leading-tight">
              Protegido por Google
              <a href="https://policies.google.com/privacy" target="_blank" rel="noopener noreferrer" class="underline hover:text-[#607D8B] transition-colors">reCAPTCHA</a>.
              Aplican
              <a href="https://policies.google.com/terms" target="_blank" rel="noopener noreferrer" class="underline hover:text-[#607D8B] transition-colors">Términos de Servicio</a>.
            </p>
          </form>
        {/if}
      </div>
    </div>

  </div>
</section>

<style>
  .contact-card {
    background: white;
    border: 1px solid #e8ecf0;
    border-radius: 1rem;
    padding: 1.5rem;
    text-align: center;
    display: flex;
    flex-direction: column;
    align-items: center;
    transition: all 0.25s ease;
  }

  .contact-card:hover {
    transform: translateY(-4px);
    box-shadow: 0 8px 24px rgba(0, 0, 0, 0.08);
    border-color: #0089D0;
  }

  .contact-card-icon {
    width: 3rem;
    height: 3rem;
    border-radius: 50%;
    background: #0089D0;
    color: white;
    display: flex;
    align-items: center;
    justify-content: center;
    margin-bottom: 0.75rem;
    transition: transform 0.25s ease;
  }

  .contact-card:hover .contact-card-icon {
    transform: scale(1.1);
  }

  /* WhatsApp button */
  .btn-whatsapp {
    display: inline-flex;
    align-items: center;
    justify-content: center;
    gap: 0.5rem;
    padding: 0.75rem 1.5rem;
    background-color: #25D366;
    color: white;
    font-family: 'Plus Jakarta Sans', sans-serif;
    font-weight: 600;
    font-size: 0.875rem;
    border-radius: 0.5rem;
    border: none;
    cursor: pointer;
    transition: all 0.25s ease;
    box-shadow: 0 2px 8px rgba(37, 211, 102, 0.3);
  }

  .btn-whatsapp:hover {
    background-color: #20bd5a;
    transform: translateY(-2px);
    box-shadow: 0 4px 16px rgba(37, 211, 102, 0.4);
  }

  .btn-whatsapp:active {
    transform: translateY(0);
  }

  /* Ensure touch-friendly tap targets */
  .contact-card :global(a) {
    min-height: 44px;
    display: inline-flex;
    align-items: center;
  }

  @media (hover: none) {
    .contact-card:hover {
      transform: none;
      box-shadow: none;
    }
  }

  @media (max-width: 640px) {
    .contact-card {
      padding: 1.25rem 1rem;
    }
  }
</style>
