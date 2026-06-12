/**
 * site-config.ts — PUNTO ÚNICO DE VERDAD para datos corporativos de COICEM.
 *
 * Regla CLAUDE.md "TOKENS SINCRONIZADOS": todo dato de contacto, telemetría y
 * marca vive aquí. Nunca se hardcodea en componentes, JSON-LD, contact.php ni footer.
 *
 * ⚠️ Marca = COICEM (el logo dice "COICEM SAS"). Dominio correcto = coicem.com.
 *    `coisem.com` fue un typo del cliente, en desuso.
 *
 * ⚠️ CAMPOS `pending`: deben confirmarse con el cliente ANTES de producción.
 *    `assertProductionReady()` (llamado desde astro.config con DEPLOY_TARGET=production)
 *    BLOQUEA el build mientras queden null. Cero datos inventados.
 */

export const siteConfig = {
  // ─── Identidad ───────────────────────────────────────────────
  legalName: 'COICEM S.A.S',
  shortName: 'COICEM',
  tagline: 'Servicio Mantenimiento Especializado',
  domain: 'https://coicem.com',
  sector: 'Mantenimiento industrial especializado · energía · petróleo/petroquímico · construcción · infraestructura',
  foundingDate: null,            // ❌ PENDIENTE cliente

  // ─── 5 áreas operativas (de misión/visión) ──────────────────
  areas: [
    { id: 'operacion',      name: 'Operación',      n: '01' },
    { id: 'mantenimiento',  name: 'Mantenimiento',  n: '02' },
    { id: 'construccion',   name: 'Construcción',   n: '03' },
    { id: 'energia',        name: 'Energía',        n: '04' },
    { id: 'infraestructura',name: 'Infraestructura',n: '05' },
  ],

  // ─── Contacto — TODO PENDIENTE (el cliente aún no lo entregó) ─
  // En dev/staging los componentes muestran "—/pendiente"; producción se bloquea.
  contact: {
    email:    null,   // ❌ PENDIENTE
    phone:    null,   // ❌ PENDIENTE (display)
    whatsapp: null,   // ❌ PENDIENTE (solo dígitos, para wa.me/)
    address:  null,   // ❌ PENDIENTE
    schedule: null,   // ❌ PENDIENTE
  },

  // ─── Telemetría del hero (idea de autor: panel de instrumentos) ─
  // ⚠️ CONDICIÓN #2: cero números inventados. Vienen de aquí o se muestran "—".
  telemetry: {
    continuidad:  null,  // ❌ % continuidad operativa
    mwMantenidos: null,  // ❌ MW mantenidos
    plantas:      null,  // ❌ plantas intervenidas
  },

  // ─── Pendientes P0 (NO ir a producción sin esto) ─────────────
  pending: {
    nit:           null,  // ❌ requerido para JSON-LD
    employeeCount: null,  // ❌
    contact:       null,  // ❌ email/tel/WhatsApp/dirección reales
    telemetry:     null,  // ❌ cifras reales del hero
    realProjects:  null,  // ❌ proyectos/clientes reales
    certifications:null,  // ❌ ¿ISO? confirmar
    /**
     * ❌ LOGO VECTORIAL — crítico para la idea de autor (despiece SVG).
     * Solo tenemos un JPEG de WhatsApp (mapa de bits → NO se puede despiezar).
     * ACCIÓN: pedir al cliente el archivo original del logo en .ai/.svg/.pdf.
     * Mientras llega, el despiece se PROTOTIPA con un SVG redibujado por YaDev,
     * marcado como reconstrucción aproximada — el cliente debe validarlo antes
     * de que sea el héroe del sitio.
     */
    logoVector:    null,  // ❌ archivo original .ai/.svg/.pdf — usando redibujo provisional
  },

  // ─── Atribución ──────────────────────────────────────────────
  credit: { dev: 'YaDev', url: 'https://yadevsistem.com' },
} as const;

// ─── Helpers ───────────────────────────────────────────────────

/** Dirección en una línea (o null si pendiente). */
export const addressLine: string | null = siteConfig.contact.address;

/** URL de WhatsApp (o null si pendiente). */
export function whatsappUrl(message?: string): string | null {
  if (!siteConfig.contact.whatsapp) return null;
  const base = `https://wa.me/${siteConfig.contact.whatsapp}`;
  return message ? `${base}?text=${encodeURIComponent(message)}` : base;
}

/**
 * Guard de producción: lanza si quedan campos PENDIENTE.
 * Llamar desde astro.config con DEPLOY_TARGET=production. Cierra B1-B4 + el riesgo
 * de publicar telemetría inventada o el logo sin validar.
 */
export function assertProductionReady(): void {
  const blockers: string[] = [];
  const p = siteConfig.pending;
  if (!p.nit)            blockers.push('NIT sin definir (JSON-LD)');
  if (!p.employeeCount)  blockers.push('N° empleados sin definir');
  if (!p.contact)        blockers.push('Contacto real (email/tel/WhatsApp/dirección) sin confirmar');
  if (!p.telemetry)      blockers.push('Telemetría del hero (continuidad/MW/plantas) sin confirmar');
  if (!p.realProjects)   blockers.push('Proyectos/clientes reales sin confirmar');
  if (!p.logoVector)     blockers.push('Logo vectorial original sin recibir — despiece usa redibujo NO validado por el cliente');

  if (blockers.length) {
    throw new Error(
      `\n🚫 COICEM NO ESTÁ LISTO PARA PRODUCCIÓN:\n` +
      blockers.map((b) => `   • ${b}`).join('\n') +
      `\n\nResolver en src/lib/site-config.ts antes de buildear para producción.\n`
    );
  }
}
