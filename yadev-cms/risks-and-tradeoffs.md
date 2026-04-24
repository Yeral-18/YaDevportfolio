# Risks & Trade-offs — YaDev CMS

> Análisis frío de qué puede salir mal, probabilidad, impacto y cómo mitigarlo.
> Esta doc se revisa al cerrar cada fase.

---

## Riesgos técnicos

### R1. Latencia de rebuild frustra al cliente
- **Síntoma:** cliente edita título, presiona publicar, espera 5 minutos, cree que no funcionó.
- **Probabilidad:** Media-alta en Fase 1.
- **Impacto:** Alto (mal UX → pierden confianza en el producto).
- **Causa raíz:** Astro build completo toma 60-120s sin cache. Instalación `pnpm` toma 30-60s adicionales.
- **Mitigación:**
  1. Cachear `node_modules/` entre builds (pnpm con lockfile no reinstala si no cambió).
  2. Cachear la carpeta `.astro/` (compila incremental).
  3. Solo rebuild si cambió contenido (skip si hash igual).
  4. Indicador progreso real en UI: "Building... 45s" + preview del cambio antes de que termine (optimistic update).
  5. Si >3min → alertar al super-admin, no sólo al cliente.
- **Medición:** p95 duration de publishes debe ser <90s post-Fase 1.

### R2. VPS $8 insuficiente para 20 clientes
- **Síntoma:** MySQL slow queries, Horizon con backlog, respuestas 500ms+.
- **Probabilidad:** Baja en corto plazo (hoy 2 clientes), media a mediano plazo.
- **Impacto:** Medio (degradación UX, no outage).
- **Mitigación:**
  1. Horizon dashboard monitoreado, ver p99 cada semana.
  2. Alertas si CPU promedio >60% durante 15min o RAM >75%.
  3. Plan claro de upgrade: $8 → $16 → $32 según crecimiento.
  4. Opcional: mover queue workers a un VPS separado de $4 si scaling vertical no alcanza.
- **Trigger de upgrade:** 10+ clientes activos o CPU sustained >60%.

### R3. Cliente rompe layout con rich text
- **Síntoma:** Cliente pega HTML de Word con estilos inline → el sitio se ve mal.
- **Probabilidad:** Alta.
- **Impacto:** Medio (cosmético, no downtime, pero reputación).
- **Mitigación:**
  1. TipTap con schema restringido (solo p, h2-h4, ul, ol, li, strong, em, a, blockquote).
  2. Paste handler que limpia estilos inline.
  3. Preview obligatorio antes de publicar en vista "Mobile" y "Desktop".
  4. Server-side HTMLPurifier como segunda línea.
  5. Button "Deshacer" siempre a 1 clic con `activity_log`.

### R4. Pérdida de DB tenant = cliente pierde todo
- **Síntoma:** disk failure VPS, script destructivo, o hackeo.
- **Probabilidad:** Baja.
- **Impacto:** **Crítico** (pierdes cliente y reputación).
- **Mitigación:**
  1. Backup diario cifrado a BackBlaze B2 (off-site, otro proveedor).
  2. Retention 30 días granular + 12 meses mensual.
  3. Test de restore MENSUAL en staging (no opcional, cron-forced con alerta si falla).
  4. Before any destructive op (`DROP DATABASE`, `migrate:fresh`, etc.) → confirmar tenant name + requerir password super-admin 2FA.
  5. No hard-delete tenant en central por 90 días (soft-delete + resguardar dump).

### R5. Cross-tenant data leak
- **Síntoma:** cliente A logra leer datos de cliente B.
- **Probabilidad:** Media (un bug, un query mal escrito).
- **Impacto:** **Crítico** (breach legal, brand damage irreparable).
- **Mitigación:**
  1. `TenantModel` abstract con scope global que bloquea queries sin tenant context.
  2. Test `CrossTenantIsolationTest` obligatorio en CI, bloqueante.
  3. Code review con checklist específico para cualquier query.
  4. Penetration test manual antes de cada fase.
  5. Nginx vhost separado por tenant si alguna vez usamos un sitio público con datos sensibles.

### R6. Colisión de webhook simultáneo
- **Síntoma:** cliente publica, y mientras, otro usuario del mismo tenant también publica → runner corre 2x, posible corrupción de dist/.
- **Probabilidad:** Media.
- **Impacto:** Bajo (un publish queda desactualizado, no daña datos).
- **Mitigación:**
  1. Queue con `unique lock` por tenant_id (Laravel ShouldBeUnique interface).
  2. Si llega nuevo publish mientras otro en curso → coalescer en uno solo (último gana, pero builds intermedios se skip).
  3. Lock en rsync: archivo `.lock` en `/srv/builds/{tenant}/` durante build.

### R7. Hostinger shared bloquea el rsync deploy
- **Síntoma:** rsync falla con "connection closed" o "permission denied".
- **Probabilidad:** Baja (Hostinger soporta SSH).
- **Impacto:** Alto (ningún publish funciona).
- **Mitigación:**
  1. Validación al crear tenant: probar SSH al deploy target antes de marcar "activo".
  2. Fallback a SFTP via `curl --upload-file` si rsync bloqueado.
  3. Whitelist de IP del VPS en el firewall de Hostinger.
  4. Health check semanal: `php artisan deploy-target:verify --all`.

### R8. Dependencia de paquetes third-party
- **Síntoma:** stancl/tenancy deja de ser mantenido, Sanctum tiene CVE grave, etc.
- **Probabilidad:** Baja.
- **Impacto:** Medio.
- **Mitigación:**
  1. Dependabot activo en GitHub → PRs semanales con updates.
  2. `composer audit` + `pnpm audit` en CI, bloqueante en HIGH o CRITICAL.
  3. Stack boring por diseño: usar solo paquetes con 1000+ stars y maintenance activo.
  4. Alternativa identificada para cada paquete crítico (ej: `tenancy-for-laravel` si stancl muere).

### R9. Problema de costo Anthropic IA
- **Síntoma:** Un tenant abusa del asistente IA, factura del mes sube a $200 inesperados.
- **Probabilidad:** Media si no hay límites.
- **Impacto:** Bajo económicamente, medio por cash flow.
- **Mitigación:**
  1. Rate limit IA por tenant (configurable en `tenants` table, no hardcoded).
  2. Monthly quota en USD de coste IA (valores concretos: TBD post-MVP cuando haya data real de uso por cliente).
  3. Si exceed → auto-disable features IA hasta siguiente ciclo, alerta al admin.
  4. Prompt caching agresivo para bajar costo 50%.
  5. Dashboard costos IA visible para super-admin.

### R10. Runner silencioso (jobs se pierden)
- **Síntoma:** Job encolado pero nunca ejecutado, panel queda "publishing..." infinito.
- **Probabilidad:** Media.
- **Impacto:** Medio.
- **Mitigación:**
  1. Timeout agresivo: si runner no responde en 5min → marcar failed + retry.
  2. Horizon watchdog alerta si un job queda >10min sin empezar.
  3. PM2 autorestart si runner crashea.
  4. Uptime monitor a `/webhook/health`.

---

## Riesgos de producto

### R11. Cliente no entiende el panel
- **Síntoma:** Soporte saturado con preguntas básicas.
- **Probabilidad:** Alta al inicio.
- **Impacto:** Alto (churn si se sienten frustrados).
- **Mitigación:**
  1. Onboarding video 30min con cada cliente nuevo.
  2. Tooltips contextuales en todos los campos.
  3. Videos cortos (30s c/u) por acción clave: "Cómo cambiar una foto", "Cómo publicar", "Cómo ver formularios".
  4. Chat de soporte WhatsApp con respuesta <4h.
  5. Feedback loop: entrevistar a los primeros 5 clientes cada mes.

### R12. Features feature-creep
- **Síntoma:** Yeral o clientes piden features avanzados (ej: e-commerce) que escapan del core.
- **Probabilidad:** Alta.
- **Impacto:** Medio (retrasa roadmap).
- **Mitigación:**
  1. Roadmap público con milestones.
  2. Feature requests en GitHub issues → priorización por votos del cliente.
  3. Decir NO explícito en features out-of-scope. Sugerir Shopify/Stripe/etc.
  4. Pricing refleja complejidad: features avanzadas se gatean por plan cuando los tiers se definan post-MVP.

### R13. Cliente se va a competencia
- **Síntoma:** Cliente cancela mantenimiento, pide exportar.
- **Probabilidad:** Media a largo plazo.
- **Impacto:** Bajo (mejor cliente honesto que cliente atado).
- **Mitigación:**
  1. Export tool en 1 clic desde el panel: SQL dump + media zip + instrucciones README.
  2. No vendor lock-in artificial.
  3. Contrato anual con descuento para reducir churn.
  4. Net Promoter Score trimestral, actuar si <30.

### R14. Yeral como único ingeniero = bus factor 1
- **Síntoma:** Yeral se enferma, viaja, o se cansa. Todo el sistema depende de él.
- **Probabilidad:** Media.
- **Impacto:** Alto.
- **Mitigación:**
  1. Documentación obsesiva (este mismo Blueprint es ejemplo).
  2. README.md en cada subcarpeta.
  3. Runbooks para operaciones críticas (deploy, restore, tenant:create).
  4. Considerar contratar part-time junior en Fase 3.
  5. Claude Code como "pair programmer" permanente acelera y documenta.

---

## Trade-offs aceptados explícitamente

### T1. Panel SvelteKit custom vs Filament
- **Elegido:** SvelteKit custom.
- **Pagamos:** ~30% más tiempo de desarrollo.
- **Ganamos:** look YaDev coherente, reusabilidad de conocimiento Svelte, no lock-in a Laravel ecosystem.

### T2. DB-per-tenant vs single-DB multi-tenant
- **Elegido:** DB-per-tenant.
- **Pagamos:** más complejidad operacional, migraciones en loop, cross-tenant reporting requiere ETL.
- **Ganamos:** aislamiento real, portabilidad, compliance robusto, queries más rápidas.

### T3. Astro estático + rebuild vs SSR Laravel+Blade
- **Elegido:** Astro estático con rebuild por webhook.
- **Pagamos:** latencia de "publish" de 1-2 min, complejidad del runner.
- **Ganamos:** sitios ultra-rápidos (100/100 Lighthouse), $0 hosting adicional por cliente, no hay que migrar código existente.

### T4. VPS Hostinger vs cloud grande (AWS/GCP)
- **Elegido:** Hostinger VPS $8.
- **Pagamos:** menos herramientas administrativas (no RDS managed, no S3, no Lambda).
- **Ganamos:** costo 10x menor al inicio, un solo vendor para web+DB+mail, UI en español.

### T5. Roles fijos vs permisos fine-grained
- **Elegido:** 3-4 roles preconfigurados (admin/editor/viewer) con posibilidad de permisos granulares en Fase 2.
- **Pagamos:** flexibilidad limitada inicialmente.
- **Ganamos:** UX simple, menos bugs, setup inmediato.

### T6. PHP mail() en sitios públicos vs Resend
- **Elegido:** PHP mail() en los sitios estáticos (formulario de contacto), Resend en API para notificaciones del CMS.
- **Pagamos:** pobre deliverability a veces desde Hostinger shared.
- **Ganamos:** costo cero, simple, ya funciona.
- **Plan:** migrar contact forms del cliente a usar el API YaDev (vía JS) para ganar deliverability en Fase 2.

### T7. No 2FA en Fase 1
- **Elegido:** 2FA en Fase 2.
- **Pagamos:** ventana de riesgo si token roba.
- **Mitigado:** tokens cortos (7d), rate limit fuerte en login, logging de IP sospechosa.

### T8. Editor WYSIWYG (TipTap) vs Markdown puro
- **Elegido:** TipTap WYSIWYG.
- **Pagamos:** más bundle JS en panel, más superficie de ataque (XSS potencial).
- **Ganamos:** UX accesible para no-técnicos. Markdown asusta a 80% de los clientes colombianos.

---

## Monitoring & alerting (Fase 1+)

| Métrica | Threshold | Alerta |
|---------|-----------|--------|
| API p99 latency | >2000ms por 5min | Slack + email |
| Publish duration | >180s | Panel toast + log |
| Publish failures | >3 en 1h | Email super-admin |
| CPU VPS | >80% sustained 15min | Email + SMS |
| RAM VPS | >85% sustained 15min | Email + SMS |
| Disk VPS | >75% | Email |
| MySQL slow queries | >10/min | Log para review |
| Failed login | >50 intentos 1h (total) | Alerta security |
| Cross-tenant violation | 1+ | INMEDIATA SMS super-admin |
| Backup failure | 1+ | Email + bloqueo nuevo publish hasta resolver |

---

## Incident response playbook

### Severity 1 (crítico)
Ejemplos: breach, data loss, sitio público down.
- Respuesta: <15 min.
- Acción: acknowledge, comunicar al cliente, mitigar, post-mortem en 48h.

### Severity 2 (alto)
Ejemplos: publishes fallando para 1 tenant, API degradada.
- Respuesta: <2h.
- Acción: troubleshoot, rollback si necesario, notificar cliente afectado.

### Severity 3 (medio)
Ejemplos: bug UI, feature no funciona.
- Respuesta: próximo día hábil.
- Acción: bug report en GitHub issues, planificar fix.

### Severity 4 (bajo)
Ejemplos: tipografía mal alineada, copy-paste error.
- Respuesta: próximo sprint.
