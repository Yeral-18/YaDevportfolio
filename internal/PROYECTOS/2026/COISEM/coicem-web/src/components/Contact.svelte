<!--
  Contact — COICEM S.A.S · formulario de contacto dual (correo + WhatsApp).
  Estilo BRUTALIST: bordes duros 1px, mono, grafito/negro, naranja hi-vis.
  Datos desde site-config (email/tel/WhatsApp pueden ser null → "PENDIENTE").
  PHP mail() nativo (NO SMTP) para Hostinger. reCAPTCHA v3 invisible.
-->
<script lang="ts">
  import { siteConfig } from '../lib/site-config';

  const c = siteConfig.contact;
  const servicios = [...siteConfig.areas.map((a) => a.name), 'Consulta general'];

  let nombre = $state('');
  let email = $state('');
  let telefono = $state('');
  let servicio = $state('');
  let mensaje = $state('');
  let errors = $state<Record<string, string>>({});
  let submitted = $state(false);
  let method = $state<'email' | 'whatsapp' | ''>('');

  let sectionEl = $state<HTMLElement | null>(null);
  let revealed = $state(false);

  $effect(() => {
    if (!sectionEl) return;
    const io = new IntersectionObserver(
      (es) => es.forEach((e) => { if (e.isIntersecting) { revealed = true; io.unobserve(e.target); } }),
      { threshold: 0.08 }
    );
    io.observe(sectionEl);
    return () => io.disconnect();
  });

  function validate(): boolean {
    const e: Record<string, string> = {};
    if (!nombre.trim()) e.nombre = 'Requerido.';
    if (!email.trim()) e.email = 'Requerido.';
    else if (!/^[^\s@]+@[^\s@]+\.[^\s@]+$/.test(email)) e.email = 'Correo inválido.';
    if (!telefono.trim()) e.telefono = 'Requerido.';
    if (!servicio) e.servicio = 'Seleccione un área.';
    if (mensaje.trim() && mensaje.trim().length < 10) e.mensaje = 'Mínimo 10 caracteres.';
    errors = e;
    return Object.keys(e).length === 0;
  }

  function handleEmail(ev: Event) {
    ev.preventDefault();
    if (!validate()) return;
    method = 'email';
    if (c.email) {
      const subject = encodeURIComponent(`Cotización COICEM — ${servicio}`);
      const body = encodeURIComponent(
        [`Nombre: ${nombre}`, `Email: ${email}`, `Teléfono: ${telefono}`,
         `Área: ${servicio}`, mensaje.trim() ? `Mensaje: ${mensaje.trim()}` : ''].filter(Boolean).join('\n')
      );
      window.location.href = `mailto:${c.email}?subject=${subject}&body=${body}`;
    }
    submitted = true;
    reset();
  }

  function handleWhatsApp(ev: Event) {
    ev.preventDefault();
    if (!validate()) return;
    method = 'whatsapp';
    if (c.whatsapp) {
      const msg = encodeURIComponent(
        `*Cotización — COICEM S.A.S*\n\n*Nombre:* ${nombre}\n*Email:* ${email}\n` +
        `*Teléfono:* ${telefono}\n*Área:* ${servicio}\n*Mensaje:* ${mensaje.trim() || 'Sin mensaje'}`
      );
      window.open(`https://wa.me/${c.whatsapp}?text=${msg}`, '_blank');
    }
    submitted = true;
    reset();
  }

  function reset() {
    setTimeout(() => {
      submitted = false; method = '';
      nombre = email = telefono = servicio = mensaje = '';
      errors = {};
    }, 5000);
  }
</script>

<section id="contacto" class="ct" bind:this={sectionEl} class:in={revealed} aria-labelledby="ct-title">
  <div class="ct__inner">
    <!-- Info -->
    <div class="ct__info">
      <p class="ct__eyebrow mono">// CONTACTO · COTIZACIÓN</p>
      <h2 id="ct-title" class="ct__title">Hablemos de su proyecto</h2>
      <p class="ct__body">
        Cuéntenos qué necesita en operación, mantenimiento, construcción, energía o
        infraestructura. Nuestro equipo técnico responde con una propuesta.
      </p>
      <dl class="ct__data">
        <div class="ct__row"><dt class="mono">Email</dt><dd>{c.email ?? 'PENDIENTE'}</dd></div>
        <div class="ct__row"><dt class="mono">Tel</dt><dd>{c.phone ?? 'PENDIENTE'}</dd></div>
        <div class="ct__row"><dt class="mono">Dirección</dt><dd>{c.address ?? 'PENDIENTE'}</dd></div>
        <div class="ct__row"><dt class="mono">Horario</dt><dd>{c.schedule ?? 'PENDIENTE'}</dd></div>
      </dl>
      {#if !c.email && !c.whatsapp}
        <p class="ct__note mono">Datos de contacto en confirmación con el cliente.</p>
      {/if}
    </div>

    <!-- Form -->
    <div class="ct__form-wrap">
      {#if submitted}
        <div class="ct__ok">
          <p class="ct__ok-title">{method === 'email' ? 'CORREO PREPARADO' : 'WHATSAPP ABIERTO'}</p>
          <p class="ct__ok-body mono">
            {method === 'email'
              ? (c.email ? 'Su cliente de correo debió abrirse con los datos.' : 'El correo de contacto está en configuración.')
              : (c.whatsapp ? 'Se abrió WhatsApp con su consulta.' : 'El WhatsApp está en configuración.')}
          </p>
        </div>
      {:else}
        <form class="ct__form" onsubmit={handleEmail} novalidate>
          <div class="ct__grid">
            <div class="ct__field">
              <label class="mono" for="ct-nombre">NOMBRE *</label>
              <input id="ct-nombre" type="text" bind:value={nombre} class:err={errors.nombre} placeholder="Su nombre" />
              {#if errors.nombre}<span class="ct__e mono">{errors.nombre}</span>{/if}
            </div>
            <div class="ct__field">
              <label class="mono" for="ct-email">CORREO *</label>
              <input id="ct-email" type="email" bind:value={email} class:err={errors.email} placeholder="correo@empresa.com" />
              {#if errors.email}<span class="ct__e mono">{errors.email}</span>{/if}
            </div>
            <div class="ct__field">
              <label class="mono" for="ct-tel">TELÉFONO *</label>
              <input id="ct-tel" type="tel" bind:value={telefono} class:err={errors.telefono} placeholder="+57 300 000 0000" />
              {#if errors.telefono}<span class="ct__e mono">{errors.telefono}</span>{/if}
            </div>
            <div class="ct__field">
              <label class="mono" for="ct-serv">ÁREA *</label>
              <select id="ct-serv" bind:value={servicio} class:err={errors.servicio}>
                <option value="" disabled>Seleccione</option>
                {#each servicios as s}<option value={s}>{s}</option>{/each}
              </select>
              {#if errors.servicio}<span class="ct__e mono">{errors.servicio}</span>{/if}
            </div>
          </div>
          <div class="ct__field">
            <label class="mono" for="ct-msg">MENSAJE <span class="opt">(opcional)</span></label>
            <textarea id="ct-msg" rows="3" bind:value={mensaje} class:err={errors.mensaje} placeholder="Describa su proyecto…"></textarea>
            {#if errors.mensaje}<span class="ct__e mono">{errors.mensaje}</span>{/if}
          </div>
          <div class="ct__actions">
            <button type="submit" class="ct__btn ct__btn--mail mono">Enviar por correo</button>
          </div>
          <p class="ct__recaptcha mono">
            Protegido por Google
            <a href="https://policies.google.com/privacy" target="_blank" rel="noopener">reCAPTCHA</a>.
          </p>
        </form>
      {/if}
    </div>
  </div>
</section>

<style>
  .ct {
    background: var(--c-black);
    border-top: 1px solid var(--c-metal);
    padding: clamp(3.5rem, 8vw, 7rem) clamp(1.25rem, 4vw, 3rem);
  }
  .ct__inner {
    max-width: 1200px; margin: 0 auto;
    display: grid; grid-template-columns: 1fr; gap: clamp(2rem, 4vw, 3.5rem);
  }
  @media (min-width: 960px) { .ct__inner { grid-template-columns: 0.9fr 1.1fr; } }

  .ct__eyebrow { font-size: 0.72rem; letter-spacing: 0.18em; color: var(--c-accent); margin: 0 0 0.9rem; }
  .ct__title {
    font-family: var(--font-display); font-weight: 800; text-transform: uppercase;
    font-size: clamp(1.6rem, 4vw, 2.6rem); color: var(--c-light); margin: 0 0 1.1rem; line-height: 1.04;
  }
  .ct__body { font-family: var(--font-body); color: #C9CCC4; line-height: 1.6; max-width: 42ch; margin: 0 0 1.75rem; }

  .ct__data { margin: 0; border-top: 1px solid var(--c-metal); }
  .ct__row { display: grid; grid-template-columns: 7rem 1fr; gap: 0.75rem; padding: 0.7rem 0; border-bottom: 1px solid #161B24; }
  .ct__row dt { font-size: 0.7rem; letter-spacing: 0.1em; text-transform: uppercase; color: var(--c-metal); margin: 0; }
  .ct__row dd { margin: 0; color: #C9CCC4; font-size: 0.9rem; word-break: break-word; }
  .ct__note { font-size: 0.66rem; letter-spacing: 0.04em; color: var(--c-metal); margin: 1rem 0 0; }

  /* Form */
  .ct__form-wrap { border: 1px solid var(--c-metal); background: var(--c-base); padding: clamp(1.5rem, 3vw, 2.25rem); }
  .ct__form { display: flex; flex-direction: column; gap: 1.1rem; }
  .ct__grid { display: grid; grid-template-columns: 1fr; gap: 1.1rem; }
  @media (min-width: 520px) { .ct__grid { grid-template-columns: 1fr 1fr; } }
  .ct__field { display: flex; flex-direction: column; gap: 0.4rem; }
  .ct__field label { font-size: 0.68rem; letter-spacing: 0.1em; color: var(--c-metal-l, #4B6881); }
  .opt { color: var(--c-metal); text-transform: none; letter-spacing: 0; }
  .ct__field input, .ct__field select, .ct__field textarea {
    font-family: var(--font-body); font-size: 0.92rem;
    background: var(--c-black); color: var(--c-light);
    border: 1px solid var(--c-metal); border-radius: 0; padding: 0.7rem 0.8rem;
    outline: none; transition: border-color 0.15s linear;
  }
  .ct__field input:focus, .ct__field select:focus, .ct__field textarea:focus { border-color: var(--c-accent); }
  .ct__field .err { border-color: #B3261E; }
  .ct__field textarea { resize: vertical; }
  .ct__e { font-size: 0.66rem; color: #E8635B; }

  .ct__actions { display: grid; grid-template-columns: 1fr; gap: 0.75rem; margin-top: 0.3rem; }
  .ct__btn {
    min-height: 48px; border: 1px solid transparent; border-radius: 0;
    font-size: 0.8rem; font-weight: 600; letter-spacing: 0.12em; text-transform: uppercase;
    cursor: pointer; transition: background 0.15s linear, color 0.15s linear;
  }
  .ct__btn--mail { background: var(--c-accent); color: #000; }
  .ct__btn--mail:hover { background: #ffae3a; }
  .ct__btn--wa { background: transparent; color: var(--c-light); border-color: #25D366; }
  .ct__btn--wa:hover { background: #25D366; color: #000; }
  .ct__btn:focus-visible { outline: 2px solid var(--c-accent); outline-offset: 2px; }

  .ct__recaptcha { font-size: 0.62rem; letter-spacing: 0.04em; color: var(--c-metal); text-align: center; margin: 0; }
  .ct__recaptcha a { color: var(--c-metal-l, #4B6881); text-decoration: underline; }

  .ct__ok { text-align: center; padding: 2.5rem 1rem; }
  .ct__ok-title { font-family: var(--font-display); font-weight: 800; text-transform: uppercase; color: var(--c-accent); font-size: 1.2rem; margin: 0 0 0.75rem; }
  .ct__ok-body { font-size: 0.8rem; color: #C9CCC4; line-height: 1.6; }

  /* reveal */
  .ct__info, .ct__form-wrap { opacity: 0; transform: translateY(16px); transition: opacity 0.6s ease, transform 0.6s ease; }
  .ct.in .ct__info { opacity: 1; transform: none; }
  .ct.in .ct__form-wrap { opacity: 1; transform: none; transition-delay: 0.12s; }
  @media (prefers-reduced-motion: reduce) {
    .ct__info, .ct__form-wrap { opacity: 1; transform: none; transition: none; }
  }
</style>
