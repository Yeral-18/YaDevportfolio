# Phase 1 — MVP (Multiservicios PoC)

> Duración: **4 semanas** (20 días hábiles).
> Objetivo: Multiservicios P&J 100% editable desde el panel. Arquitectura multi-tenant establecida aunque haya 1 solo cliente.
> Criterio de éxito: la clienta (gerencia@multiserviciospj.com) edita el título del hero, sube una foto al servicio "Transporte", presiona Publicar, y en <2min el cambio está live sin que Yeral toque nada.

---

## Semana 1 — Scaffolding Laravel multi-tenant

### Día 1-2: Repo + Laravel base
- [ ] Los 3 repos de la org `yadevOs/` están clonados en `yadev-cms/{api,studio,infra}/`. Verificar `git remote -v` en cada uno apunta a `https://github.com/yadevOs/yadev-cms-{api,studio,infra}.git`.
  ```
  yadev-cms/
    api/        (clone de yadevOs/yadev-cms-api — Laravel)
    studio/     (clone de yadevOs/yadev-cms-studio — SvelteKit)
    infra/      (clone de yadevOs/yadev-cms-infra — docker-compose, scripts)
  ```
- [ ] `cd api && composer create-project laravel/laravel . "^11.0"` (scaffold in-place sobre el repo clonado — ajustar `--remove-vcs` para no borrar `.git/`).
- [ ] Commit inicial + push al repo `yadevOs/yadev-cms-api`.
- [ ] Test local con SQLite + `php artisan serve`.
- [ ] Configurar `phpunit.xml` para correr tests en sqlite memory.

### Día 3: stancl/tenancy
- [ ] `composer require stancl/tenancy:^3.9`.
- [ ] `php artisan tenancy:install`.
- [ ] Configurar `config/tenancy.php`:
  - `bootstrappers` → `DatabaseTenancyBootstrapper`, `CacheTenancyBootstrapper`, `FilesystemTenancyBootstrapper`, `QueueTenancyBootstrapper`, `RedisTenancyBootstrapper`.
  - `database.prefix` → `tenant_`.
  - `central_domains` → `['api.yadev.co','studio.yadev.co','api.yadev.local','studio.yadev.local','localhost']` (incluir `.yadev.local` para desarrollo local-first; los `.yadev.co` aplican post Fase VPS-migration).
- [ ] Migrar schema central (adaptar `database/central-schema.sql` a Laravel migrations en `database/migrations/`).
- [ ] Migraciones de tenant en `database/migrations/tenant/` (adaptar `tenant-schema.sql`).

### Día 4: Sanctum + roles
- [ ] `composer require laravel/sanctum`.
- [ ] `composer require spatie/laravel-permission`.
- [ ] Publicar y ejecutar migraciones de ambos.
- [ ] Crear middleware `InitializeTenancyByToken` que lee el `tenant` claim del token y switchea la conexión.
- [ ] Seed central: 1 super-admin Yeral.

### Día 5: Tests foundation
- [ ] Test `TenancyTestCase` base con setUp que crea tenant de prueba.
- [ ] Test `CrossTenantIsolationTest` — primera validación de seguridad (puede estar rojo hasta tener endpoints, pero establecer shape).
- [ ] CI: GitHub Actions corre `php artisan test` en PR.

### Entregable semana 1
`php artisan tenants:create multiservicios --domain=multiserviciospj.com --admin-email=gerencia@multiserviciospj.com` debe:
1. Crear DB `tenant_multiservicios`.
2. Correr migraciones tenant en ella.
3. Crear admin user + rol `tenant_admin`.
4. Ser idempotente-seguro.

---

## Semana 2 — Schema tenant + API CRUD básico

### Día 6-7: Modelos + API bloques básicos
- [ ] Modelos tenant: `User`, `Page`, `Section`, `Block`, `Media`, `Form`, `FormSubmission`, `Setting`, `Menu`, `MenuItem`, `SeoMeta`, `Publish`, `ActivityLog`, `BlockVersion`, `Redirect`.
- [ ] Todos extienden `TenantModel` abstract con global scope de seguridad.
- [ ] Factories + seeders para cada modelo.
- [ ] Resources API (`BlockResource`, `PageResource`, etc.).

### Día 8-9: Block types y schemas (fase 1 subset)
Implementar schema + validación para 5 bloques core (suficiente para Multiservicios):
- [ ] `hero_split`
- [ ] `services_zigzag`
- [ ] `about_three_cards`
- [ ] `contact_form`
- [ ] `rich_text`

Estructura:
```php
// api/app/Blocks/HeroSplit.php
class HeroSplit implements BlockContract {
    public function schema(): array { return [
        'eyebrow' => 'nullable|string|max:100',
        'headline_parts' => 'required|array|min:1',
        'headline_parts.*.text' => 'required|string|max:200',
        'headline_parts.*.style' => 'in:default,accent',
        'description' => 'required|string|max:800',
        'primary_cta.label' => 'required|string|max:50',
        'primary_cta.href' => 'required|string|regex:/^(https?:\/\/|\/|#)/',
        // ...
    ]; }
    public function defaultData(): array { return [ ... ]; }
    public function astroComponent(): string { return 'Hero.svelte'; }
}
```

Registro en `config/blocks.php`:
```php
return [
    'hero_split' => \App\Blocks\HeroSplit::class,
    'services_zigzag' => \App\Blocks\ServicesZigzag::class,
    // ...
];
```

### Día 10: Endpoints CRUD
- [ ] `POST /api/v1/auth/login` + `POST /api/v1/auth/logout` + `GET /api/v1/auth/me`.
- [ ] `GET|POST|PUT|DELETE /api/v1/pages`.
- [ ] `GET|POST|PUT|DELETE /api/v1/blocks`.
- [ ] `POST /api/v1/media` (upload) + `GET /api/v1/media` + `DELETE /api/v1/media/{id}`.
- [ ] `GET /api/v1/settings` + `PUT /api/v1/settings`.

Cada endpoint:
- Form Request con validación.
- Policy con spatie/permission.
- ActivityLog escrito automáticamente (event listener `LogActivityEvent`).
- Test feature.

### Entregable semana 2
Con Postman/curl:
1. Login como gerencia@multiserviciospj.com → recibe token.
2. GET /pages → lista con 1 página ("Inicio").
3. PUT /blocks/{id} → actualiza título del hero, versión incrementa.
4. GET /activity-log → muestra el cambio.
5. Intentar acceder a `/pages` con token de OTRO tenant ficticio → 404.

---

## Semana 3 — Panel SvelteKit

### Día 11-12: Scaffold SvelteKit
- [ ] `pnpm create svelte@latest admin` (TypeScript, ESLint, Prettier, Vitest).
- [ ] Configurar Tailwind + `shadcn-svelte` init.
- [ ] Setup tokens YaDev: `#0a0a0b` base, Space Grotesk + Inter, indigo primary.
- [ ] Estructura de rutas:
  ```
  admin/src/routes/
    (auth)/login/+page.svelte
    (app)/dashboard/+page.svelte
    (app)/pages/+page.svelte
    (app)/pages/[id]/+page.svelte
    (app)/media/+page.svelte
    (app)/forms/+page.svelte
    (app)/settings/+page.svelte
    +layout.svelte  (sidebar + topbar + auth guard)
  ```
- [ ] Store auth con `$state` (token, user, tenant).
- [ ] Interceptor fetch: auto-agregar `Authorization: Bearer`, manejar 401.

### Día 13-14: Editor visual de bloques
- [ ] Componente `<BlockEditor type="hero_split" data={...} onUpdate={...} />`.
- [ ] Por cada block type, un componente Svelte en `admin/src/lib/blocks/{name}/Editor.svelte`.
- [ ] Inputs con validación Zod client-side (espejo del schema backend).
- [ ] Debounce autosave (2s inactivo → PUT).
- [ ] Preview lateral live con iframe apuntando a `https://preview.yadev.co/{tenant}/{page-slug}?token=...` (Fase 2 real, en MVP mostrar solo un render simplificado inline).

### Día 15: Mediateca + editor fotográfico integrado
- [ ] Grid de media con thumbnails.
- [ ] Drag-drop upload (dropzone svelte).
- [ ] Modal "Seleccionar imagen" usable desde cualquier editor de bloque.
- [ ] Edit alt text + title.

**Editor fotográfico (cierra gap vs Damos WYSIWYG + photo editor):**

Stack: **Cropper.js** (client-side, recorte/rotación) + **Intervention Image** (server-side PHP, filtros/resize/compresión/WebP).

- [ ] Modal "Editar imagen" abribl desde cualquier tarjeta de media.
- [ ] Tabs del modal:
  - **Recortar** — Cropper.js con relaciones predefinidas (libre, 1:1, 4:3, 16:9, 1200×630 OG).
  - **Rotar** — botones 90° izquierda/derecha + flip horizontal/vertical.
  - **Filtros** — sliders brillo (−100/+100), contraste, saturación, sharpness. Preview live.
  - **Exportar** — selector formato (JPG/PNG/WebP) + slider calidad (50-100) + opción "reemplazar original" vs "guardar como copia".
- [ ] Endpoint `POST /v1/media/{id}/transform` — body `{ crop: {x,y,w,h}, rotate: deg, filters: {...}, format, quality, mode: 'replace'|'copy' }`.
- [ ] Server aplica Intervention Image, regenera thumbnails + webp, actualiza `media.url` (si mode=replace) o crea row nuevo (si mode=copy).
- [ ] Justificación de anticipar a Fase 1 (no Fase 2): la mediateca llega en semana 2 y sin editor básico el cliente envía por WhatsApp fotos sin recortar. Forma parte del loop de edición diaria, no es feature avanzada.

Documentado en `architecture/api-contract.md` bajo Media > transform.

### Entregable semana 3
Flujo UX completo:
1. Login → dashboard.
2. Click "Páginas" → ver "Inicio".
3. Click Inicio → editor con los 9 bloques visibles en orden.
4. Editar campo del hero → se guarda solo (debounce).
5. Click "Publicar" → muestra loading → éxito.

(En este momento, "publicar" aún NO rebuildea el sitio real — eso es semana 4.)

---

## Semana 4 — Webhook runner + deploy + migración Multiservicios

### Día 16: Runner Node
- [ ] Crear `runner/` con Fastify + PM2.
- [ ] Endpoint `POST /webhook/rebuild` con HMAC validation.
- [ ] Lógica:
  ```js
  // runner/src/build.js
  async function rebuild({ tenant, content_url, hmac }) {
    verifyHmac(...);
    const buildDir = `/srv/builds/${tenant}`;
    await exec(`cd ${buildDir} && git pull`);
    const content = await fetch(content_url, { headers: { Authorization: `Bearer ${SERVICE_TOKEN}` }}).then(r => r.json());
    await fs.writeFile(`${buildDir}/src/content/site.json`, JSON.stringify(content, null, 2));
    await exec(`cd ${buildDir} && pnpm install --frozen-lockfile && pnpm build`);
    await exec(`rsync -az --delete ${buildDir}/dist/ ${DEPLOY_TARGETS[tenant]}`);
    return { status: 'success', duration_ms: Date.now() - start };
  }
  ```
- [ ] `pm2 start runner/src/server.js --name yadev-runner`.

### Día 17: Refactor Astro Multiservicios para consumir JSON
- [ ] Crear rama `cms-compatible` del repo `site-multiservicios` (NO tocar main en producción).
- [ ] Crear `src/content/site.json` con estructura que matchea el API.
- [ ] Refactor `Hero.svelte`, `AboutUs.astro`, `Services.astro`, etc., para recibir props en vez de arrays hardcodeados:
  ```astro
  ---
  import site from '../content/site.json';
  const heroBlock = site.pages.find(p => p.slug === 'inicio').sections
    .find(s => s.type === 'hero').blocks.find(b => b.type === 'hero_split');
  ---
  <Hero data={heroBlock.data} client:load />
  ```
- [ ] Verificar que `pnpm build` genera dist/ idéntico al actual.
- [ ] Merge a main SOLO después de validar que el build local funciona.

### Día 18: Integración Laravel → Runner
- [ ] Job `PublishSite($tenant_id)`:
  ```php
  public function handle() {
      $publish = Publish::create(['status' => 'queued']);
      $contentUrl = route('api.v1.internal.content-snapshot', ['tenant' => $tenant]);
      Http::post('http://127.0.0.1:8080/webhook/rebuild', [
          'tenant' => $tenant->id,
          'content_url' => $contentUrl,
          'publish_id' => $publish->id,
          'hmac' => hash_hmac('sha256', $tenant->id, config('yadev.runner_secret')),
      ]);
      $publish->update(['status' => 'building', 'started_at' => now()]);
  }
  ```
- [ ] Endpoint `GET /api/v1/internal/content-snapshot/{tenant}` que genera JSON completo del tenant (solo accesible desde localhost).
- [ ] Endpoint `POST /api/v1/publish/{id}/complete` que el runner llama al terminar.
- [ ] Broadcast via Laravel Reverb al panel (toast "Publicado en 1m 34s").

### Día 19: Deploy real Multiservicios
- [ ] `php artisan tenants:create multiservicios ...`
- [ ] Importar `seed-multiservicios.sql` → validar que los bloques match con el render.
- [ ] Setup `/srv/builds/multiservicios/` con clone del repo y rama `cms-compatible`.
- [ ] Test publish end-to-end → verificar que `multiserviciospj.com` sigue idéntico.

### Día 20: QA + cutover
- [ ] QA manual por Yeral: cambiar cada uno de los 9 bloques desde el panel y ver que se refleja.
- [ ] Credenciales reales a gerencia@multiserviciospj.com con password temporal.
- [ ] Sesión de onboarding 30 min por video llamada — enseñar a la clienta el flujo.
- [ ] Monitoreo de publishes en Horizon por 1 semana antes de declarar "estable".

---

## Entregable Fase 1
- `api.yadev.co/v1/*` operativo con auth, CRUD, publish.
- `studio.yadev.co` panel con login + editor + mediateca + publish.
- Multiservicios editable, publicable, live en multiserviciospj.com.
- 0 downtime en el sitio original durante el cutover.
- Documentación para usuario final en `/admin` → ayuda contextual en cada sección.

## Métricas de éxito
- Tiempo de publicación: <120s promedio.
- Tiempo de edición bloque Hero: <30s desde login.
- Error rate en publishes: <5%.
- Clienta Multiservicios publica al menos 2 cambios sin ayuda en la primera semana.

## Riesgos Fase 1 (ver `risks-and-tradeoffs.md`)
- Refactor Astro mal hecho rompe el sitio live → se mitiga con branch separado + test de build antes de cutover.
- Clienta no entiende el panel → onboarding video + ayuda contextual.
- Runner falla silenciosamente → Horizon monitor + alerta si publish >5min sin callback.
