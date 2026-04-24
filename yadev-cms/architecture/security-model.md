# Security Model — YaDev CMS

> Seguridad first. Cada endpoint debe autorizar por tenant. Un cliente jamás debe leer datos de otro.

---

## 1. Threat model

### Actores
| Actor | Acceso legítimo | Acceso prohibido |
|-------|-----------------|------------------|
| YaDev super-admin (Yeral) | Todos los tenants, impersonar, provisioning | Commitear `.env` a repo público |
| Admin cliente | Su tenant: pages, blocks, media, forms, publish | Otros tenants, billing, impersonación |
| Editor cliente | Su tenant: pages, blocks (sin publicar ni borrar) | Users management, settings globales, publish |
| Usuario anónimo | Formularios públicos (submissions vía API pública con rate limit) | Cualquier otra cosa |
| Atacante externo | Ninguno | Todo |

### Amenazas principales
1. **Cross-tenant data leak** — un usuario del tenant A logra leer recursos del tenant B. (CRÍTICO)
2. **Privilege escalation** — un editor logra hacer publish o crear users.
3. **Token leak** — token Sanctum robado vía XSS o localStorage.
4. **SQL injection** — usuario inyecta SQL en un campo.
5. **XSS en editor WYSIWYG** — cliente pega HTML malicioso que se renderiza a otros visitantes.
6. **File upload abuso** — cliente sube PHP ejecutable o payload reverse-shell.
7. **Form spam** — bot envía miles de form submissions.
8. **Brute force login** — atacante prueba passwords.
9. **Man-in-the-middle** — tráfico interceptado entre panel y API.
10. **Backup leak** — dump SQL cae en manos equivocadas.

---

## 2. Roles y permisos (spatie/laravel-permission)

### Roles
- `yadev_super_admin` (global, vive en central.users) — todo. Solo Yeral.
- `tenant_admin` (por tenant) — todo dentro de SU tenant.
- `tenant_editor` (por tenant) — editar y guardar borradores, NO publicar ni configurar ni gestionar users.
- `tenant_viewer` (por tenant) — read-only, útil para que YaDev audite con permiso del cliente.

### Permisos granulares (ejemplos)
- `pages.view`, `pages.create`, `pages.update`, `pages.delete`, `pages.publish`
- `blocks.view`, `blocks.update`, `blocks.delete`
- `media.view`, `media.upload`, `media.delete`
- `forms.view`, `forms.submissions.read`, `forms.submissions.export`, `forms.submissions.delete`
- `settings.view`, `settings.update`
- `users.view`, `users.invite`, `users.update`, `users.delete`
- `site.publish`
- `site.export` (solo tenant_admin)

### Matriz
| Permiso | super_admin | tenant_admin | editor | viewer |
|---------|:-:|:-:|:-:|:-:|
| pages.* | ✅ | ✅ | update only | view only |
| blocks.* | ✅ | ✅ | ✅ | view only |
| media.* | ✅ | ✅ | view + upload | view only |
| forms.submissions.* | ✅ | ✅ | view only | view only |
| settings.update | ✅ | ✅ | ❌ | ❌ |
| users.* | ✅ | ✅ | ❌ | ❌ |
| site.publish | ✅ | ✅ | ❌ | ❌ |
| site.export | ✅ | ✅ | ❌ | ❌ |
| tenants.* | ✅ | ❌ | ❌ | ❌ |

---

## 3. Autenticación

### Laravel Sanctum (token-based)
- Login devuelve token con expiración 7 días (refreshable con cada request vía middleware custom `RefreshTokenExpiry`).
- Token se guarda client-side en **cookie HttpOnly + Secure + SameSite=Lax** (recomendado) o localStorage si el frontend vive en mismo dominio.
- Logout invalida el token server-side (borra de `personal_access_tokens`).

### Password policy
- Mínimo 10 caracteres.
- Al menos 1 letra, 1 número.
- Hashed con Bcrypt cost=12.
- Rotación no forzada (anti-pattern OWASP moderno) salvo breach detected.

### 2FA (Fase 2)
- TOTP vía `pragmarx/google2fa-laravel`.
- Obligatorio para `tenant_admin` y `yadev_super_admin`.
- Backup codes descargables.

### Brute force protection
- `ThrottleRequests` middleware: 5 login attempts por IP+email en 15 min.
- Después de 5 fallos → cuenta bloqueada 30 min + email al admin del tenant.
- Si hay 50+ intentos desde misma IP en 1h → ban automático vía fail2ban en VPS.

---

## 4. Autorización por tenant

### Patrón obligatorio
Todos los modelos eloquent del tenant extienden `TenantModel` que:
```php
abstract class TenantModel extends Model
{
    protected $connection = 'tenant'; // Siempre usa la conexión del tenant activo

    // Scope global que verifica que hay tenant activo
    protected static function booted()
    {
        static::addGlobalScope('tenancy', function (Builder $builder) {
            if (!tenant()) {
                throw new NoTenantContextException();
            }
        });
    }
}
```

### Policies (spatie/laravel-permission)
Todo Controller → usa Form Request con `authorize()`:
```php
// App/Http/Requests/UpdateBlockRequest.php
public function authorize(): bool
{
    return $this->user()->can('blocks.update')
        && Block::find($this->route('id'))?->exists();  // exists() confirma que es del tenant activo
}
```

### Tests obligatorios
```php
// tests/Feature/CrossTenantIsolationTest.php
it('prevents user from tenant A reading block of tenant B', function () {
    $tenantA = Tenant::factory()->create();
    $tenantB = Tenant::factory()->create();

    $blockB = tenancy()->initialize($tenantB)
        && Block::factory()->create();
    $tokenA = tenancy()->initialize($tenantA)
        && User::factory()->create()->createToken('test')->plainTextToken;

    $this->withToken($tokenA)
        ->getJson("/api/v1/blocks/{$blockB->id}")
        ->assertStatus(404);
});
```

---

## 5. Validación de input

### Form Requests (obligatorio)
Cada endpoint que acepta body = Form Request con rules estrictas.

Ejemplo bloque Hero:
```php
// App/Http/Requests/UpdateBlockRequest.php
public function rules(): array
{
    $block = Block::findOrFail($this->route('id'));
    return match ($block->type) {
        'hero_split' => [
            'data.eyebrow' => 'string|max:100',
            'data.headline' => 'required|string|max:200',
            'data.description' => 'required|string|max:800',
            'data.primary_cta.label' => 'required|string|max:50',
            'data.primary_cta.href' => 'required|string|regex:/^(https?:\/\/|\/|#)/',
        ],
        'services_zigzag' => [ ... ],
        default => throw new UnsupportedBlockTypeException(),
    };
}
```

### Rich text sanitization (TipTap)
- Server-side whitelist con `HTMLPurifier`:
  - Allowed tags: `p, h2, h3, h4, ul, ol, li, strong, em, a, br, blockquote, img`.
  - Attrs: `href` (solo http/https/mailto), `target="_blank"` auto con `rel="noopener noreferrer"`, `src` (solo URLs del tenant media domain).
  - `<script>`, `<iframe>`, `on*` handlers: rechazados.

---

## 6. Upload de archivos (media)

### Validaciones
- Tipos permitidos: `jpg, jpeg, png, webp, svg, gif, pdf, mp4, webm`.
- Size max: 10 MB imágenes, 50 MB video, 20 MB pdf.
- `image/svg+xml` → sanitizar con `DOMPurify server-side` (remover `<script>`).
- MIME type verificado con `file_mime_content_type()` (no confiar en Content-Type del cliente).
- Extensión doble (`malicious.jpg.php`) → rechazar si última extensión no está en whitelist.

### Storage
- Filesystem: `/srv/yadev-cms/storage/tenants/{tenant_slug}/media/`.
- Nombre de archivo: `hash(content + timestamp)` → evita sobrescribir, permite dedup.
- Nginx sirve desde `/media/{tenant_slug}/...` con cache headers 1 año + `Content-Disposition: inline` para imágenes.
- NUNCA servir archivos con `X-Content-Type-Options: nosniff` ausente.
- NUNCA permitir ejecución de PHP en `/media/`.

### Nginx location block (media)
```nginx
location ^~ /media/ {
    alias /srv/yadev-cms/storage/tenants/;
    add_header X-Content-Type-Options "nosniff";
    add_header Content-Security-Policy "default-src 'none'";
    location ~ \.(php|phtml|py|pl|cgi)$ { deny all; }
    expires 1y;
    access_log off;
}
```

---

## 7. CORS

El API (`api.yadev.co`) expone dos **categorías de orígenes permitidos**, manejadas por middleware dinámico (no static config):

### A) Panel admin (siempre permitido)

**Producción:**
```
Access-Control-Allow-Origin: https://studio.yadev.co
Access-Control-Allow-Methods: GET, POST, PUT, PATCH, DELETE
Access-Control-Allow-Headers: Authorization, Content-Type, X-Requested-With
Access-Control-Allow-Credentials: true
Access-Control-Max-Age: 3600
```

**Local-first (Fase 0-2, dev only):**
```
Access-Control-Allow-Origin: http://studio.yadev.local:5173
# Adicional: permitir cualquier http://*.yadev.local:* con regex (solo APP_ENV=local)
# Ejemplo Laravel config/cors.php → paths: ['v1/*'], allowed_origins_patterns:
#   [ '#^http://[a-z0-9-]+\.yadev\.local(:\d+)?$#' ]
Access-Control-Allow-Methods: GET, POST, PUT, PATCH, DELETE
Access-Control-Allow-Headers: Authorization, Content-Type, X-Requested-With
Access-Control-Allow-Credentials: true
Access-Control-Max-Age: 3600
```

En `APP_ENV=local` aceptar los dos. En `APP_ENV=production` descartar cualquier origin que matchee `.yadev.local` — nunca debería aparecer en prod pero defense-in-depth.

### B) Sitios de cliente (whitelist por tenant, dinámico)
Cada tenant tiene filas en `yadev_central.domains` con sus dominios autorizados. El middleware `DynamicCors` hace:

```php
$origin = $request->header('Origin');
$tenantFromRoute = $request->route('tenant_id');

// Solo permitir si el origin está registrado como dominio del tenant
$allowed = Domain::where('hostname', parse_url($origin, PHP_URL_HOST))
    ->where('tenant_id', $tenantFromRoute)
    ->exists();

if ($allowed) {
    return $response
        ->header('Access-Control-Allow-Origin', $origin)
        ->header('Vary', 'Origin');
}
```

**Garantía:** el sitio cliente A **nunca** puede consumir endpoints del tenant B desde el navegador — aunque alguien inyecte JS malicioso, el CORS lo bloquea porque el Origin del sitio A solo está whitelisted para el tenant A.

**Nota importante:** los builds de Astro se ejecutan **server-side en el runner del VPS**, no en el navegador del cliente. El runner se autentica con HMAC, no con CORS. Por lo tanto los fetchs de build time no pasan por este middleware — van por HMAC validation. CORS solo importa para fetchs desde el navegador (forms públicos, widgets, etc.).

### Reglas absolutas
- Nunca `Access-Control-Allow-Origin: *` en endpoints autenticados.
- Nunca hardcodear dominios de cliente en nginx — la whitelist vive en DB, se actualiza cuando se registra un tenant nuevo.
- Preflight cacheable 1h.

---

## 8. Rate limiting

| Contexto | Límite | Por |
|----------|--------|-----|
| Login | 5/15min | IP + email |
| Password reset | 3/1h | IP + email |
| API authenticated | 60/min | token |
| API anonymous | 20/min | IP |
| Form submission público | 3/10min | IP + form_id |
| Media upload | 30/10min | token |
| Publish | 10/1h | token (no spamear rebuilds) |

---

## 9. Secrets management

- `.env` NUNCA committeado.
- Secrets en VPS: archivo `/etc/yadev/secrets.env` con permisos 600, owner www-data.
- Rotación: `APP_KEY` cada 12 meses. Sanctum tokens se invalidan si APP_KEY rota → logout forzado de todos los usuarios.
- DB passwords: generados aleatoriamente en `tenants:create`.
- Webhook HMAC secret: único por tenant.

---

## 10. Headers de seguridad (Nginx → Laravel)

```nginx
add_header Strict-Transport-Security "max-age=31536000; includeSubDomains; preload" always;
add_header X-Content-Type-Options "nosniff" always;
add_header X-Frame-Options "DENY" always;
add_header Referrer-Policy "strict-origin-when-cross-origin" always;
add_header Permissions-Policy "geolocation=(), microphone=(), camera=()" always;

# CSP para el panel admin (NO para la API que devuelve JSON)
add_header Content-Security-Policy
  "default-src 'self';
   script-src 'self' 'unsafe-inline' https://www.google.com https://www.gstatic.com;
   style-src 'self' 'unsafe-inline' https://fonts.googleapis.com;
   font-src 'self' https://fonts.gstatic.com;
   img-src 'self' data: blob: https:;
   connect-src 'self' https://api.yadev.co;
   frame-ancestors 'none';"
  always;
```

Nota: los **sitios públicos en Hostinger shared NO usan CSP** porque Hostinger la sobreescribe (ver CLAUDE.md raíz, problema #3).

---

## 11. Logging y auditoría

- Todo evento write (create/update/delete) se registra en `activity_log`:
  - `actor_id`, `actor_type`, `action`, `subject_type`, `subject_id`, `before`, `after`, `ip`, `user_agent`, `at`.
- Retention: 6 meses en DB, archivado a S3 después.
- Alertas (Fase 2): `publish.failed` → email a super-admin. `login.suspicious` (5+ countries en 1h) → alerta.
- NO loggear passwords, tokens, card numbers. Sanitizar request body antes de log.

---

## 12. Backups y cifrado

- Dumps MySQL diarios → cifrados con `openssl enc -aes-256-cbc` antes de subir a BackBlaze B2.
- Key de cifrado guardada en 1Password de Yeral + copia offline.
- Test de restore mensual: tomar dump cifrado, descifrar, importar a VPS staging, verificar que API arranca.

---

## 13. Disclosure y respuesta a incidentes

- Página `yadev.co/security` con email `security@yadev.co`.
- SLA respuesta: 24h para críticos.
- Si breach confirmado: notificar clientes afectados dentro de 72h (GDPR-like, aunque Colombia no lo exija legalmente, es buena práctica).

---

## 14. Checklist pre-producción (antes de cada deploy mayor)

- [ ] Tests `CrossTenantIsolationTest` verdes.
- [ ] `php artisan security:check` (composer audit + node audit) sin high/critical.
- [ ] Headers de seguridad verificados con securityheaders.com (A+).
- [ ] CSP sin `unsafe-eval`.
- [ ] Nginx no sirve `/storage` ni `/.env`.
- [ ] SSL cubre `studio.yadev.co` + `api.yadev.co` con HSTS.
- [ ] Backup de producción probado en staging esta semana.
- [ ] 2FA activo en cuenta super-admin.
