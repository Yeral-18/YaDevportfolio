# Auth Mode Decision — Token Bearer for Phase 1

> Decisión tomada el 2026-04-24 tras la auditoría del `security-auditor` (findings MEDIUM sobre incoherencia entre `SANCTUM_STATEFUL_DOMAINS` en `.env.example` y `auth.svelte.ts` usando `Authorization: Bearer ${token}`).
> Resuelve: Q-SEC-3 del security-audit-post-v4.md sección 6.
> Estado: **RESUELTA**.

---

## Decisión

**Fase 1 (MVP) — Todos los consumidores del API usan Sanctum Personal Access Tokens (bearer)** almacenados en `localStorage` en el studio. Sin cookies stateful, sin CSRF dance.

**Fase 2 (hardening) — El studio migra a Sanctum SPA con cookies HttpOnly + CSRF** con `SESSION_DOMAIN=.yadev.co` cuando exista el dominio real. El runner y los builds Astro siguen con bearer tokens (server-to-server).

---

## Contexto

El usuario confirmó:

- **Q-SEC-1** (datos sensibles) — Ningún cliente actual maneja datos de salud / financieros / niños. Habeas Data Ley 1581 CO aplica en modo estándar (datos corporativos: emails, teléfonos, razón social), no en modo agravado.
- **Q-SEC-2** (BitLocker) — La laptop tiene BitLocker disponible pero sin activar por ahora. Los dumps locales plain text quedan como riesgo aceptado hasta que el usuario active FDE **manualmente**. **Claude NO debe activar BitLocker automáticamente** — requiere guardar la clave de recuperación en un medio externo (USB dedicado, password manager, impreso en físico) antes de cifrar, y esa gestión de claves es responsabilidad exclusiva del usuario. El sistema solo debe recordarle al llegar al trigger documentado, no ejecutar.
- **Q-SEC-3** (Sanctum mode) — Pidió recomendación.

---

## Trade-offs considerados

| Criterio | Token Bearer | SPA Cookies |
|----------|--------------|-------------|
| Setup local-first HTTP | Trivial | Requiere `Secure=(env !== 'local')` + `SESSION_DOMAIN=.yadev.local` |
| Runner Node (server-to-server) | Nativo | No soporta |
| Builds Astro (build-time fetch) | Nativo | No soporta |
| CORS config | 1 header | `credentials: include` + origin explícito + CSRF preflight |
| XSS → token theft | Vulnerable (mitigable con CSP) | Inmune (HttpOnly) |
| Revocación server-side | Requiere `last_used_at` check | Trivial (invalidar sesión) |
| Mobile/CLI futuro | Compatible | Necesita endpoint bearer paralelo |
| Código ya scaffoldeado (studio + api) | Alineado | Requiere rewrite |

Peso decisivo: **el runner y los builds Astro NO PUEDEN usar cookies**. Mantener dos mecanismos paralelos en MVP es complejidad no justificada.

---

## Mitigaciones del riesgo XSS (compensa la elección de bearer + localStorage)

### En el studio (SvelteKit)

1. **CSP estricto** en `src/app.html` como meta tag:
   ```html
   <meta http-equiv="Content-Security-Policy"
         content="default-src 'self';
                  script-src 'self';
                  style-src 'self' 'unsafe-inline' https://fonts.googleapis.com;
                  font-src 'self' https://fonts.gstatic.com;
                  img-src 'self' data: http://api.yadev.local:8000 http://127.0.0.1:19000;
                  connect-src 'self' http://api.yadev.local:8000 ws://studio.yadev.local:5173;
                  object-src 'none';
                  frame-ancestors 'none';
                  base-uri 'self';
                  form-action 'self';">
   ```
   En producción reemplazar orígenes `.local` por `.yadev.co`.

2. **Zero `{@html}`** en componentes del studio. Único caso permitido: renderizar output de TipTap que ya fue sanitizado con `enshrined/svg-sanitize` + DOMPurify server-side. Todo `{@html}` requiere comentario justificando + test que valida el sanitizer.

3. **`innerHTML` prohibido**. ESLint rule `no-inner-html` activada.

4. **Subresource Integrity (SRI)** para todo script externo (hoy ninguno, pero enforced para el futuro).

### En el API (Laravel)

1. **Tokens con expiración corta**:
   ```php
   // config/sanctum.php
   'expiration' => 120, // minutos (2h)
   ```

2. **Token rotation** en el login: cada login genera un nuevo PAT y revoca los anteriores del mismo device_name.

3. **Scope obligatorio por token**:
   - Super-admin: `['*']`
   - Tenant admin: `['tenant:{id}:*']`
   - Editor: `['tenant:{id}:pages:read', 'tenant:{id}:pages:write', 'tenant:{id}:media:*']`
   - Runner/Build: `['tenant:{id}:publish:read']` — solo lectura del content tree

4. **Headers de seguridad server-side** via middleware `SecurityHeaders`:
   ```php
   // bootstrap/app.php
   $response->headers->set('X-Content-Type-Options', 'nosniff');
   $response->headers->set('X-Frame-Options', 'DENY');
   $response->headers->set('Referrer-Policy', 'strict-origin-when-cross-origin');
   // Solo en prod:
   if (app()->environment('production')) {
       $response->headers->set('Strict-Transport-Security', 'max-age=31536000; includeSubDomains');
   }
   ```

5. **Rate limit agresivo en `/v1/auth/login`**:
   ```php
   RateLimiter::for('login', fn ($req) => [
       Limit::perMinute(5)->by($req->ip()),
       Limit::perMinute(3)->by($req->input('email')),
   ]);
   ```

6. **Lockout progresivo** después de 5 intentos fallidos: backoff exponencial 30s → 1m → 5m → 15m → 1h.

---

## Impacto en archivos existentes

### Cambios requeridos (aplicar tras cierre del agente C)

| Archivo | Cambio |
|---------|--------|
| `api/.env.example` | Remover `SANCTUM_STATEFUL_DOMAINS`. Agregar `SANCTUM_TOKEN_EXPIRATION=120` |
| `api/config/sanctum.php` | `'expiration' => env('SANCTUM_TOKEN_EXPIRATION', 120)` |
| `api/bootstrap/app.php` | Middleware `SecurityHeaders` global para todas las respuestas |
| `api/app/Http/Middleware/SecurityHeaders.php` | Crear |
| `api/app/Providers/RouteServiceProvider.php` (o `bootstrap/app.php`) | Rate limiter `login` |
| `api/routes/api.php` | `Route::post('/auth/login', ...)->middleware('throttle:login')` |
| `studio/src/app.html` | Agregar meta CSP (bloque arriba) |
| `studio/.env.example` | Sin cambios (ya tiene `VITE_API_URL`) |
| `studio/src/lib/stores/auth.svelte.ts` | Agregar `tokenExpiresAt` al estado + auto-logout cuando expira |
| `studio/eslint.config.js` | Regla `no-inner-html` + regla custom contra `{@html}` sin `// sanitized:` encima |
| `architecture/security-model.md` | §3 reescribir "Authentication" con la decisión explícita. Eliminar mención a cookies stateful. Agregar sección 3.5 "Token scopes & rotation" |
| `architecture/multi-tenancy-strategy.md` | §3 actualizar: `tenant_id` viaja en el **scope** del token (`tenant:{id}:*`), no como claim JWT |
| `architecture/api-contract.md` | §2 "Authentication" actualizar: remover `/sanctum/csrf-cookie`, agregar rotación de token en `/auth/login` response |

### Sin cambios (ya alineados)

- `studio/src/lib/api/client.ts` — ya usa `Authorization: Bearer` ✅
- `studio/src/lib/stores/auth.svelte.ts` — ya usa localStorage ✅
- `studio/src/routes/login/+page.svelte` — ya usa email+password ✅

---

## Migración a Fase 2 (documentada, no ejecutada)

Cuando el studio migre a cookies stateful (Fase 2 semana X):

1. Agregar en `api/.env` (prod): `SANCTUM_STATEFUL_DOMAINS=studio.yadev.co`, `SESSION_DOMAIN=.yadev.co`, `SESSION_SECURE_COOKIE=true`, `SESSION_SAME_SITE=lax`
2. En studio: cambiar `api/client.ts` a `fetch(url, { credentials: 'include' })` + preflight `POST /sanctum/csrf-cookie` antes del login
3. Revocar `localStorage.token` + migrar al cookie-based session en el mismo request de login (backward-compat de 1 semana)
4. Runner y builds Astro **siguen con bearer PAT** via `POST /v1/auth/tokens` endpoint admin-only

Esfuerzo estimado: 2-3 días de dev + 1 día de test cross-browser.

---

## Rationale final

Elegimos **pragmatismo sobre idealismo**:

- MVP necesita envío rápido. Token bearer baja la complejidad ~40% en auth.
- XSS en un panel admin es grave, pero el studio es un SPA cerrado sin contenido generado por usuarios públicos (TipTap solo renderiza texto que otros admins escribieron). Surface area controlable.
- CSP + ESLint rules + zero `innerHTML` bajan el riesgo residual a aceptable para Fase 1.
- En Fase 2, cuando existan datos reales de 3+ tenants y haya presión regulatoria real, migrar a cookies es un refactor aislado de 2-3 días.

**Owner de la migración Fase 2:** el usuario + agente code-reviewer.
**Trigger de la migración:** primer cliente que manifieste preocupación de compliance, o 3+ tenants activos, lo que ocurra primero.
