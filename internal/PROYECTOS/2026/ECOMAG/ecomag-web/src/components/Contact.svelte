<script>
  import { onMount } from 'svelte';

  // ── Form state ──
  let nombre = '';
  let empresa = '';
  let telefono = '';
  let email = '';
  let mensaje = '';
  let honeypot = '';

  // ── Validation state ──
  let errors = {
    nombre: '',
    telefono: '',
    email: '',
    mensaje: '',
  };
  let touched = {
    nombre: false,
    telefono: false,
    email: false,
    mensaje: false,
  };

  // ── Submission state ──
  let submitting = false;
  let submitSuccess = false;
  let submitError = false;
  let submitErrorMsg = '';

  // ── Validators ──
  const emailRegex = /^[^\s@]+@[^\s@]+\.[^\s@]+$/;
  const phoneRegex = /^(\+57\s?)?[0-9\s\-()]{7,15}$/;

  function validateField(field) {
    switch (field) {
      case 'nombre':
        errors.nombre = nombre.trim() === '' ? 'El nombre es obligatorio.' : '';
        break;
      case 'telefono':
        if (telefono.trim() === '') {
          errors.telefono = 'El telefono es obligatorio.';
        } else if (!phoneRegex.test(telefono.trim())) {
          errors.telefono = 'Ingrese un numero valido (ej: +57 300 123 4567).';
        } else {
          errors.telefono = '';
        }
        break;
      case 'email':
        if (email.trim() === '') {
          errors.email = 'El email es obligatorio.';
        } else if (!emailRegex.test(email.trim())) {
          errors.email = 'Ingrese un email valido.';
        } else {
          errors.email = '';
        }
        break;
      case 'mensaje':
        if (mensaje.trim() === '') {
          errors.mensaje = 'El mensaje es obligatorio.';
        } else if (mensaje.trim().length < 10) {
          errors.mensaje = 'El mensaje debe tener al menos 10 caracteres.';
        } else {
          errors.mensaje = '';
        }
        break;
    }
  }

  function handleBlur(field) {
    touched[field] = true;
    validateField(field);
  }

  function validateAll() {
    const fields = ['nombre', 'telefono', 'email', 'mensaje'];
    fields.forEach((f) => {
      touched[f] = true;
      validateField(f);
    });
    return fields.every((f) => errors[f] === '');
  }

  function resetForm() {
    nombre = '';
    empresa = '';
    telefono = '';
    email = '';
    mensaje = '';
    honeypot = '';
    errors = { nombre: '', telefono: '', email: '', mensaje: '' };
    touched = { nombre: false, telefono: false, email: false, mensaje: false };
  }

  async function handleSubmit() {
    if (!validateAll()) return;
    if (honeypot) return; // Bot detected

    submitting = true;
    submitSuccess = false;
    submitError = false;
    submitErrorMsg = '';

    try {
      const res = await fetch('/api/contact', {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify({
          nombre: nombre.trim(),
          empresa: empresa.trim(),
          telefono: telefono.trim(),
          email: email.trim(),
          mensaje: mensaje.trim(),
          _gotcha: honeypot,
        }),
      });

      if (res.ok) {
        submitSuccess = true;
        resetForm();
      } else {
        const data = await res.json().catch(() => ({}));
        submitErrorMsg = data.message || 'Error al enviar el mensaje. Intente nuevamente.';
        submitError = true;
      }
    } catch (err) {
      submitErrorMsg = 'Error de conexion. Verifique su internet e intente nuevamente.';
      submitError = true;
    } finally {
      submitting = false;
    }
  }

  function retrySubmit() {
    submitError = false;
    submitErrorMsg = '';
  }

  // ── Scroll animations ──
  onMount(() => {
    const section = document.getElementById('contacto');
    if (!section) return;

    const header = section.querySelector('.contact__header');
    const infoCard = section.querySelector('.contact__info');
    const formCard = section.querySelector('.contact__form-wrapper');
    const details = section.querySelectorAll('.contact__detail');

    // Set initial states
    if (header) {
      header.style.opacity = '0';
      header.style.transform = 'translate3d(0, 50px, 0)';
      header.style.willChange = 'transform, opacity';
    }
    if (infoCard) {
      infoCard.style.opacity = '0';
      infoCard.style.transform = 'translate3d(-40px, 0, 0)';
      infoCard.style.willChange = 'transform, opacity';
    }
    if (formCard) {
      formCard.style.opacity = '0';
      formCard.style.transform = 'translate3d(40px, 0, 0)';
      formCard.style.willChange = 'transform, opacity';
    }
    details.forEach((detail) => {
      detail.style.opacity = '0';
      detail.style.transform = 'translate3d(0, 20px, 0)';
      detail.style.willChange = 'transform, opacity';
    });

    const observer = new IntersectionObserver(
      (entries) => {
        entries.forEach((entry) => {
          if (entry.isIntersecting) {
            // Header fade up
            if (header) {
              header.style.transition = 'opacity 0.7s cubic-bezier(0.34, 1.56, 0.64, 1), transform 0.7s cubic-bezier(0.34, 1.56, 0.64, 1)';
              header.style.opacity = '1';
              header.style.transform = 'translate3d(0, 0, 0)';
            }

            // Info card slide from left
            if (infoCard) {
              setTimeout(() => {
                infoCard.style.transition = 'opacity 0.7s cubic-bezier(0.34, 1.56, 0.64, 1), transform 0.7s cubic-bezier(0.34, 1.56, 0.64, 1)';
                infoCard.style.opacity = '1';
                infoCard.style.transform = 'translate3d(0, 0, 0)';
              }, 200);
            }

            // Form card slide from right
            if (formCard) {
              setTimeout(() => {
                formCard.style.transition = 'opacity 0.7s cubic-bezier(0.34, 1.56, 0.64, 1), transform 0.7s cubic-bezier(0.34, 1.56, 0.64, 1)';
                formCard.style.opacity = '1';
                formCard.style.transform = 'translate3d(0, 0, 0)';
              }, 300);
            }

            // Stagger contact details
            details.forEach((detail, i) => {
              setTimeout(() => {
                detail.style.transition = 'opacity 0.5s cubic-bezier(0.34, 1.56, 0.64, 1), transform 0.5s cubic-bezier(0.34, 1.56, 0.64, 1)';
                detail.style.opacity = '1';
                detail.style.transform = 'translate3d(0, 0, 0)';
              }, 400 + i * 100);
            });

            observer.unobserve(entry.target);
          }
        });
      },
      { threshold: 0.15 }
    );

    observer.observe(section);
  });
</script>

<section id="contacto" class="contact" aria-label="Contacto">
  <div class="section-container section-padding">
    <!-- Section header -->
    <div class="contact__header">
      <span class="contact__tag">Contacto</span>
      <h2 class="heading-primary">
        &iquest;Listo para iniciar su proyecto?
      </h2>
      <p class="text-body contact__intro">
        Estamos listos para ayudarle a hacer realidad su proyecto. Cuentenos su necesidad
        y le responderemos en menos de 24 horas.
      </p>
    </div>

    <div class="contact__grid">
      <!-- ── Left column: Contact info ── -->
      <div class="contact__info">
        <div class="contact__info-card">
          <!-- Phone -->
          <div class="contact__detail">
            <div class="contact__icon" aria-hidden="true">
              <svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" width="22" height="22">
                <path d="M22 16.92v3a2 2 0 01-2.18 2 19.79 19.79 0 01-8.63-3.07 19.5 19.5 0 01-6-6A19.79 19.79 0 012.12 4.18 2 2 0 014.11 2h3a2 2 0 012 1.72c.127.96.361 1.903.7 2.81a2 2 0 01-.45 2.11L8.09 9.91a16 16 0 006 6l1.27-1.27a2 2 0 012.11-.45c.907.339 1.85.573 2.81.7A2 2 0 0122 16.92z"/>
              </svg>
            </div>
            <div>
              <h3 class="contact__detail-title">Telefono</h3>
              <a href="tel:+57XXXXXXXXXX" class="contact__detail-value">+57 XXX XXX XXXX</a>
            </div>
          </div>

          <!-- Email -->
          <div class="contact__detail">
            <div class="contact__icon" aria-hidden="true">
              <svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" width="22" height="22">
                <rect x="2" y="4" width="20" height="16" rx="2"/>
                <path d="M22 7l-8.97 5.7a1.94 1.94 0 01-2.06 0L2 7"/>
              </svg>
            </div>
            <div>
              <h3 class="contact__detail-title">Email</h3>
              <a href="mailto:info@ecomagsas.com" class="contact__detail-value">info@ecomagsas.com</a>
            </div>
          </div>

          <!-- Address -->
          <div class="contact__detail">
            <div class="contact__icon" aria-hidden="true">
              <svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" width="22" height="22">
                <path d="M21 10c0 7-9 13-9 13s-9-6-9-13a9 9 0 0118 0z"/>
                <circle cx="12" cy="10" r="3"/>
              </svg>
            </div>
            <div>
              <h3 class="contact__detail-title">Direccion</h3>
              <p class="contact__detail-value">Calle 72 # 19 - 42<br/>Barrancabermeja, Santander</p>
            </div>
          </div>

          <!-- Schedule -->
          <div class="contact__detail">
            <div class="contact__icon" aria-hidden="true">
              <svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" width="22" height="22">
                <circle cx="12" cy="12" r="10"/>
                <polyline points="12 6 12 12 16 14"/>
              </svg>
            </div>
            <div>
              <h3 class="contact__detail-title">Horario</h3>
              <p class="contact__detail-value">Lun - Vie: 8:00 AM - 6:00 PM</p>
            </div>
          </div>
        </div>

        <!-- Google Maps placeholder -->
        <div class="contact__map-placeholder">
          <!--
            Google Maps Embed: Replace YOUR_API_KEY and coordinates with actual values.
            <iframe
              src="https://www.google.com/maps/embed/v1/place?key=YOUR_API_KEY&q=Calle+72+19-42,Barrancabermeja,Santander,Colombia"
              width="100%"
              height="200"
              style="border:0; border-radius: 0.75rem;"
              allowfullscreen=""
              loading="lazy"
              referrerpolicy="no-referrer-when-downgrade"
              title="Ubicacion de ECOMAG S.A.S en el mapa"
            ></iframe>
          -->
          <div class="contact__map-stub" aria-hidden="true">
            <svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.5" width="32" height="32">
              <path d="M21 10c0 7-9 13-9 13s-9-6-9-13a9 9 0 0118 0z"/>
              <circle cx="12" cy="10" r="3"/>
            </svg>
            <span>Mapa de Google (por configurar)</span>
          </div>
        </div>
      </div>

      <!-- ── Right column: Form ── -->
      <div class="contact__form-wrapper">
        {#if submitSuccess}
          <div class="contact__success" role="alert">
            <svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.5" width="48" height="48">
              <circle cx="12" cy="12" r="10"/>
              <path d="M9 12l2 2 4-4"/>
            </svg>
            <h3>Mensaje enviado exitosamente</h3>
            <p>Gracias por contactarnos. Nos comunicaremos con usted en las proximas 24 horas.</p>
            <button class="btn-primary" on:click={() => { submitSuccess = false; }}>
              Enviar otro mensaje
            </button>
          </div>
        {:else}
          <form
            on:submit|preventDefault={handleSubmit}
            novalidate
            class="contact__form"
          >
            <!-- Nombre -->
            <div class="form-group">
              <label for="contact-nombre" class="form-label">
                Nombre completo <span class="form-required" aria-hidden="true">*</span>
              </label>
              <input
                id="contact-nombre"
                type="text"
                bind:value={nombre}
                on:blur={() => handleBlur('nombre')}
                class="form-input"
                class:form-input--error={touched.nombre && errors.nombre}
                placeholder="Ej: Juan Perez"
                required
                aria-required="true"
                aria-invalid={touched.nombre && !!errors.nombre}
                aria-describedby={errors.nombre ? 'error-nombre' : undefined}
              />
              {#if touched.nombre && errors.nombre}
                <p id="error-nombre" class="form-error" aria-live="polite">{errors.nombre}</p>
              {/if}
            </div>

            <!-- Empresa -->
            <div class="form-group">
              <label for="contact-empresa" class="form-label">
                Empresa <span class="form-optional">(opcional)</span>
              </label>
              <input
                id="contact-empresa"
                type="text"
                bind:value={empresa}
                class="form-input"
                placeholder="Nombre de la empresa"
              />
            </div>

            <!-- Telefono + Email row -->
            <div class="form-row">
              <div class="form-group">
                <label for="contact-telefono" class="form-label">
                  Telefono <span class="form-required" aria-hidden="true">*</span>
                </label>
                <input
                  id="contact-telefono"
                  type="tel"
                  bind:value={telefono}
                  on:blur={() => handleBlur('telefono')}
                  class="form-input"
                  class:form-input--error={touched.telefono && errors.telefono}
                  placeholder="+57 300 123 4567"
                  required
                  aria-required="true"
                  aria-invalid={touched.telefono && !!errors.telefono}
                  aria-describedby={errors.telefono ? 'error-telefono' : undefined}
                  pattern="(\+57\s?)?[0-9\s\-()]{7,15}"
                />
                {#if touched.telefono && errors.telefono}
                  <p id="error-telefono" class="form-error" aria-live="polite">{errors.telefono}</p>
                {/if}
              </div>

              <div class="form-group">
                <label for="contact-email" class="form-label">
                  Email <span class="form-required" aria-hidden="true">*</span>
                </label>
                <input
                  id="contact-email"
                  type="email"
                  bind:value={email}
                  on:blur={() => handleBlur('email')}
                  class="form-input"
                  class:form-input--error={touched.email && errors.email}
                  placeholder="correo@ejemplo.com"
                  required
                  aria-required="true"
                  aria-invalid={touched.email && !!errors.email}
                  aria-describedby={errors.email ? 'error-email' : undefined}
                />
                {#if touched.email && errors.email}
                  <p id="error-email" class="form-error" aria-live="polite">{errors.email}</p>
                {/if}
              </div>
            </div>

            <!-- Mensaje -->
            <div class="form-group">
              <label for="contact-mensaje" class="form-label">
                Mensaje <span class="form-required" aria-hidden="true">*</span>
              </label>
              <textarea
                id="contact-mensaje"
                bind:value={mensaje}
                on:blur={() => handleBlur('mensaje')}
                class="form-input form-textarea"
                class:form-input--error={touched.mensaje && errors.mensaje}
                placeholder="Describanos su proyecto o consulta..."
                rows="5"
                required
                aria-required="true"
                aria-invalid={touched.mensaje && !!errors.mensaje}
                aria-describedby={errors.mensaje ? 'error-mensaje' : undefined}
                minlength="10"
              ></textarea>
              {#if touched.mensaje && errors.mensaje}
                <p id="error-mensaje" class="form-error" aria-live="polite">{errors.mensaje}</p>
              {/if}
            </div>

            <!-- Honeypot (hidden from humans) -->
            <div class="form-honeypot" aria-hidden="true" tabindex="-1">
              <label for="contact-gotcha">No llenar</label>
              <input
                id="contact-gotcha"
                type="text"
                name="_gotcha"
                bind:value={honeypot}
                autocomplete="off"
                tabindex="-1"
              />
            </div>

            <!-- Error message -->
            {#if submitError}
              <div class="contact__error" role="alert">
                <svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" width="20" height="20">
                  <circle cx="12" cy="12" r="10"/>
                  <line x1="15" y1="9" x2="9" y2="15"/>
                  <line x1="9" y1="9" x2="15" y2="15"/>
                </svg>
                <span>{submitErrorMsg}</span>
                <button type="button" class="contact__retry" on:click={retrySubmit}>
                  Reintentar
                </button>
              </div>
            {/if}

            <!-- Submit button -->
            <button
              type="submit"
              class="btn-primary contact__submit"
              disabled={submitting}
            >
              {#if submitting}
                <svg class="contact__spinner" xmlns="http://www.w3.org/2000/svg" fill="none" viewBox="0 0 24 24" width="20" height="20">
                  <circle cx="12" cy="12" r="10" stroke="currentColor" stroke-width="4" opacity="0.25"/>
                  <path fill="currentColor" d="M4 12a8 8 0 018-8V0C5.373 0 0 5.373 0 12h4z"/>
                </svg>
                Enviando...
              {:else}
                Enviar mensaje
                <svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" width="18" height="18">
                  <line x1="22" y1="2" x2="11" y2="13"/>
                  <polygon points="22 2 15 22 11 13 2 9 22 2"/>
                </svg>
              {/if}
            </button>
          </form>
        {/if}
      </div>
    </div>
  </div>
</section>

<style>
  .contact {
    background: linear-gradient(180deg, #D8E6D0 0%, #CDDCC4 50%, #D8E6D0 100%);
  }

  .contact__header {
    text-align: center;
    max-width: 40rem;
    margin: 0 auto 2rem;
  }

  @media (min-width: 768px) {
    .contact__header {
      margin: 0 auto 3rem;
    }
  }

  .contact__tag {
    display: inline-block;
    padding: 0.25rem 0.75rem;
    border-radius: 9999px;
    font-size: 0.8125rem;
    font-weight: 600;
    color: var(--color-primary);
    background: rgba(27, 94, 32, 0.1);
    margin-bottom: 1rem;
    letter-spacing: 0.025em;
    text-transform: uppercase;
  }

  .contact__intro {
    margin-top: 1rem;
  }

  .contact__grid {
    display: grid;
    grid-template-columns: 1fr;
    gap: 2.5rem;
  }

  @media (min-width: 768px) {
    .contact__grid {
      grid-template-columns: 5fr 7fr;
      gap: 3rem;
    }
  }

  /* ── Left column ── */
  .contact__info-card {
    display: flex;
    flex-direction: column;
    gap: 1.25rem;
    background: white;
    border-radius: 1rem;
    padding: 1.25rem;
    box-shadow: 0 1px 3px rgba(0, 0, 0, 0.08);
  }

  @media (min-width: 640px) {
    .contact__info-card {
      gap: 1.5rem;
      padding: 2rem;
    }
  }

  .contact__detail {
    display: flex;
    align-items: flex-start;
    gap: 1rem;
  }

  .contact__icon {
    flex-shrink: 0;
    width: 2.75rem;
    height: 2.75rem;
    display: flex;
    align-items: center;
    justify-content: center;
    border-radius: 0.75rem;
    background: rgba(27, 94, 32, 0.08);
    color: var(--color-primary);
  }

  .contact__detail-title {
    font-family: var(--font-display);
    font-size: 0.8125rem;
    font-weight: 600;
    color: #6b7280;
    text-transform: uppercase;
    letter-spacing: 0.05em;
    margin: 0 0 0.125rem;
  }

  .contact__detail-value {
    font-family: var(--font-body);
    font-size: 0.9375rem;
    color: var(--color-dark);
    text-decoration: none;
    line-height: 1.5;
  }

  a.contact__detail-value:hover {
    color: var(--color-primary);
  }

  .contact__map-placeholder {
    margin-top: 1.5rem;
  }

  .contact__map-stub {
    display: flex;
    flex-direction: column;
    align-items: center;
    justify-content: center;
    gap: 0.5rem;
    height: 100px;
    border-radius: 0.75rem;
    background: rgba(27, 94, 32, 0.05);
    border: 2px dashed rgba(27, 94, 32, 0.15);
    color: #9ca3af;
    font-size: 0.8125rem;
  }

  @media (min-width: 768px) {
    .contact__map-stub {
      height: 140px;
    }
  }

  /* ── Form ── */
  .contact__form-wrapper {
    background: white;
    border-radius: 1rem;
    padding: 1.25rem;
    box-shadow: 0 1px 3px rgba(0, 0, 0, 0.08);
  }

  @media (min-width: 640px) {
    .contact__form-wrapper {
      padding: 2rem;
    }
  }

  .contact__form {
    display: flex;
    flex-direction: column;
    gap: 1.25rem;
  }

  .form-row {
    display: grid;
    grid-template-columns: 1fr;
    gap: 1.25rem;
  }

  @media (min-width: 640px) {
    .form-row {
      grid-template-columns: 1fr 1fr;
    }
  }

  .form-group {
    display: flex;
    flex-direction: column;
    gap: 0.375rem;
  }

  .form-label {
    font-family: var(--font-body);
    font-size: 0.875rem;
    font-weight: 500;
    color: var(--color-dark);
  }

  .form-required {
    color: #dc2626;
  }

  .form-optional {
    font-weight: 400;
    color: #9ca3af;
    font-size: 0.8125rem;
  }

  .form-input {
    width: 100%;
    padding: 0.75rem 0.875rem;
    border: 1px solid #d1d5db;
    border-radius: 0.5rem;
    font-family: var(--font-body);
    font-size: 1rem;
    color: var(--color-dark);
    background: white;
    transition: border-color 0.2s, box-shadow 0.2s;
    outline: none;
    min-height: 44px;
  }

  @media (min-width: 640px) {
    .form-input {
      padding: 0.625rem 0.875rem;
      font-size: 0.9375rem;
      min-height: unset;
    }
  }

  .form-input::placeholder {
    color: #9ca3af;
  }

  .form-input:focus {
    border-color: var(--color-primary);
    box-shadow: 0 0 0 3px rgba(27, 94, 32, 0.15);
  }

  .form-input--error {
    border-color: #dc2626;
  }

  .form-input--error:focus {
    border-color: #dc2626;
    box-shadow: 0 0 0 3px rgba(220, 38, 38, 0.15);
  }

  .form-textarea {
    resize: vertical;
    min-height: 120px;
  }

  .form-error {
    font-size: 0.8125rem;
    color: #dc2626;
    margin: 0;
    display: flex;
    align-items: center;
    gap: 0.25rem;
  }

  .form-honeypot {
    position: absolute;
    left: -9999px;
    width: 1px;
    height: 1px;
    overflow: hidden;
    opacity: 0;
  }

  /* ── Submit button ── */
  .contact__submit {
    width: 100%;
    gap: 0.5rem;
    margin-top: 0.5rem;
    font-size: 1rem;
    padding: 0.75rem 1.5rem;
    min-height: 48px;
  }

  .contact__submit:disabled {
    opacity: 0.7;
    cursor: not-allowed;
  }

  .contact__spinner {
    animation: spin 0.8s linear infinite;
  }

  @keyframes spin {
    to { transform: rotate(360deg); }
  }

  /* ── Success / Error ── */
  .contact__success {
    display: flex;
    flex-direction: column;
    align-items: center;
    justify-content: center;
    text-align: center;
    gap: 1rem;
    padding: 3rem 2rem;
    color: var(--color-primary);
  }

  .contact__success h3 {
    font-family: var(--font-display);
    font-size: 1.25rem;
    font-weight: 700;
    color: var(--color-primary);
    margin: 0;
  }

  .contact__success p {
    font-size: 0.9375rem;
    color: #4b5563;
    margin: 0;
    max-width: 24rem;
  }

  .contact__error {
    display: flex;
    align-items: center;
    gap: 0.5rem;
    padding: 0.75rem 1rem;
    border-radius: 0.5rem;
    background: #fef2f2;
    border: 1px solid #fecaca;
    color: #dc2626;
    font-size: 0.875rem;
    flex-wrap: wrap;
  }

  .contact__retry {
    background: none;
    border: none;
    color: #dc2626;
    font-weight: 600;
    text-decoration: underline;
    cursor: pointer;
    font-size: 0.875rem;
    padding: 0;
    margin-left: auto;
  }

  .contact__retry:hover {
    color: #b91c1c;
  }
</style>
