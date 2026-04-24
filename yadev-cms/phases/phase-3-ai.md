# Phase 3 — IA + Automatización

> Duración: **4 semanas** (20 días hábiles).
> Objetivo: agregar valor diferencial con IA de Anthropic. Onboardear PORON y COICEM (llegando a 4 tenants).
> Entra con Fase 2 estable.

---

## Principios IA en YaDev CMS

1. **Claude Haiku 4.5 por defecto** — rápido, barato, suficiente para 90% de tareas (rewrite, traducción, descripción corta).
2. **Claude Sonnet 4.6 solo cuando se requiere razonamiento** — SEO score, generación de schema.org, análisis de página completa.
3. **Prompt caching agresivo** — cachear system prompts + contexto del tenant + brand_voice. Ahorro ~50-70% esperado.
4. **Rate limits por tenant** — configurables por tenant (pricing y tiers: TBD post-MVP). Implementar como config `ai_monthly_quota` en `tenants` table para evitar abuse y permitir ajuste sin redeploy.
5. **Human-in-the-loop** — la IA sugiere, el usuario aprueba. Nunca auto-publicar contenido IA sin revisión.
6. **Logs + costs tracking** — `ai_usage` table por tenant: tokens_in, tokens_out, model, cost_usd.
7. **ADN de marca inviolable** — toda llamada a IA inyecta el `brand_voice` del tenant como system prompt cacheable. Claude NO produce contenido genérico: respeta tono, vocabulario preferido, vocabulario prohibido y sample texts del cliente.

---

## Semana 11 — Asistente de contenido

### Día 51-52: Anthropic SDK integration
- [ ] `composer require anthropic-ai/anthropic-sdk-php`.
- [ ] `config/anthropic.php` con API key de `/etc/yadev/secrets.env`.
- [ ] Wrapper service `App\Services\AI\ClaudeService`:
  ```php
  public function rewrite(string $text, string $tone, int $maxWords): string {
      return $this->call([
          'model' => 'claude-haiku-4-5',
          'max_tokens' => 500,
          'system' => [
              ['type' => 'text', 'text' => $this->systemPrompt(), 'cache_control' => ['type' => 'ephemeral']],
              ['type' => 'text', 'text' => $this->tenantContext()],
          ],
          'messages' => [
              ['role' => 'user', 'content' => "Reescribe este texto con tono $tone, max $maxWords palabras:\n\n$text"],
          ],
      ]);
  }
  ```
- [ ] `tenantContext()` devuelve: nombre empresa, industria, tone of voice, servicios principales. Todo se cachea con `cache_control: ephemeral`.

### Día 53-54: UI del asistente + brand_voice onboarding

**Brand Voice — ADN comercial del tenant (cierra gap vs Damos IA generativa):**

Antes de que la IA genere cualquier contenido, el tenant debe completar su perfil de voz. Se guarda en tabla `brand_voice` (ver tenant-schema.sql actualizado) y se inyecta como system prompt cacheable en TODAS las llamadas.

- [ ] Wizard `/studio/{tenant}/settings/brand-voice` con 4 pasos:
  1. **Tono de voz** — selector: profesional, cercano, autoritativo, técnico, cálido, aspiracional (multi-select, hasta 2).
  2. **Vocabulario preferido** — lista libre ("aliado estratégico", "ingeniería a medida", "Barrancabermeja"). Estos términos se sugieren proactivamente.
  3. **Vocabulario prohibido** — lista libre ("barato", "low cost", "experts"). La IA evita estos términos y los flaggea si aparecen en el texto de entrada.
  4. **Textos de referencia** — 2-3 párrafos reales del cliente (about us, servicio principal, tagline). La IA los usa como few-shot examples.
  5. **Contexto industria/audiencia** — dropdowns + campo libre (ej: "Industria: ingeniería civil. Audiencia: gerentes de proyectos de Ecopetrol, Cenit, Terpel").

- [ ] Endpoint `GET|PUT /v1/tenants/{tenant_id}/brand-voice`.
- [ ] System prompt builder `App\Services\AI\BrandVoiceSystemPrompt::build($tenant)` genera bloque de texto cacheable con `cache_control: ephemeral`.
- [ ] Cada llamada a IA: `system: [generic_yadev_prompt, brand_voice_block]` — ambos cacheados.
- [ ] Cache hit rate esperado: >70% (brand_voice cambia raramente, TTL de cache efectivo >5 min cubre ráfagas de edición).

**UI del asistente:**
- [ ] En cada textarea del editor de bloques, botón "Mejorar con IA".
- [ ] Modal con opciones:
  - Tono: usa los tonos configurados en brand_voice como default, permite override puntual.
  - Longitud: mantener, más corto, más largo.
  - Acción: reescribir, resumir, expandir, traducir, generar desde brief.
- [ ] Preview del resultado → aceptar o descartar.
- [ ] Histórial de sugerencias (últimas 5 por campo).
- [ ] Si el texto resultante contiene palabras del `vocabulary_avoid`, el UI marca en rojo y ofrece regenerar.

**Endpoint unificado de generación:**
- [ ] `POST /v1/tenants/{tenant_id}/ai/generate` — body `{ type: 'blog_post|service_description|meta_description|hero_copy|about_paragraph', context: {...}, constraints: { max_words, tone_override? } }`.
- [ ] Respuesta: `{ text, tokens_used, model, cache_hit_ratio }`.
- [ ] Tipos soportados y contexto requerido:
  - `blog_post`: `{ topic, target_keywords[], outline? }` → genera post 800-1200 palabras con headings H2/H3.
  - `service_description`: `{ service_name, features[], differentiators[] }` → párrafo largo + bullets.
  - `meta_description`: `{ page_title, page_context }` → 150-160 chars.
  - `hero_copy`: `{ page_purpose, target_action }` → headline + subhead + CTA.
  - `about_paragraph`: `{ company_history_short, values[] }` → 3-4 oraciones.

### Día 55: Endpoints + tests
- [ ] `POST /api/v1/ai/rewrite`.
- [ ] `POST /api/v1/ai/translate`.
- [ ] `POST /api/v1/ai/summarize`.
- [ ] `POST /api/v1/ai/expand`.
- [ ] Rate limit específico por tenant + plan.
- [ ] Tests: mockear responses, verificar tracking de tokens.

---

## Semana 12 — Auditor SEO/GEO en tiempo real + OG images

### Auditor SEO/GEO IA en tiempo real (cierra gap vs Damos "SEO + GEO")

Damos.co 2026 vende "optimización SEO + GEO" (GEO = Generative Engine Optimization, preparar contenido para SGE / Google AI Overviews / ChatGPT Search). Este módulo iguala y supera.

**Arquitectura:**

```
┌─────────────────────────┐
│  Studio (SvelteKit)     │
│  DOM Analyzer JS        │ ← onSave / onBlur de block editor
│  (extrae HTML parcial,  │
│   hace árbol de blocks) │
└──────────┬──────────────┘
           │ POST /v1/tenants/{t}/ai/audit
           ▼
┌─────────────────────────┐
│  API (Laravel)          │
│  SeoAuditService        │
│  ┌───────────────────┐  │
│  │ Brand voice cache │  │
│  │ Audit system prompt│ │
│  │ (ephemeral cache) │  │
│  └───────────────────┘  │
│          │              │
│          ▼              │
│  Claude Haiku 4.5       │
│  (con prompt caching)   │
└──────────┬──────────────┘
           │
           ▼
┌─────────────────────────┐
│  Response estructurada  │
│  Guardado en            │
│  seo_audits (tenant DB) │
└─────────────────────────┘
```

**Qué analiza:**

1. **SEO tradicional:**
   - Jerarquía H1/H2/H3 (un solo H1, H2 anidan correctamente).
   - Meta title: 50-60 chars, keyword principal al inicio.
   - Meta description: 150-160 chars, propuesta de valor + CTA verbal.
   - Schema.org: presencia de tipo correcto (LocalBusiness/Service/FAQPage/BreadcrumbList según la página), campos requeridos.
   - Open Graph: og:title, og:description, og:image, og:type, og:url presentes.
   - Twitter Cards.
   - Alt text en imágenes (ninguna `<img>` sin alt descriptivo).
   - Internal links: al menos 2 links salientes a otras páginas del sitio.
   - Keyword density: keyword principal entre 0.5% y 2.5%.
   - Canonical URL presente.
   - `lang="es-CO"`.

2. **GEO (Generative Engine Optimization):**
   - **Estructura de respuesta directa** — la página tiene un párrafo TL;DR de 40-60 palabras al inicio que un LLM puede citar como respuesta.
   - **Preguntas explícitas como H2/H3** — al menos 2-3 headings en forma de pregunta ("¿Qué es X?", "¿Cómo funciona Y?") porque SGE prioriza Q&A.
   - **Datos factuales citables** — números, fechas, ubicaciones, nombres propios claramente marcados (facilita extracción por LLM).
   - **FAQPage schema** — recomendación fuerte para páginas de servicio.
   - **Longitud de respuestas** — cada H2 tiene ≥100 palabras por debajo (suficiente para ser "chunk" extractable).
   - **Entidades reconocibles** — empresa, industria, ubicación mencionadas en los primeros 100 caracteres.
   - **Citabilidad (cite-worthiness)** — frases declarativas con autoridad ("ECOMAG S.A.S es una ingeniería civil con sede en Barrancabermeja desde 2010").

**Endpoint:**

- [ ] `POST /v1/tenants/{tenant_id}/ai/audit` — body `{ page_id, partial_html?, block_id? }`.
- [ ] Si `partial_html` viene, analiza ese fragmento (para audit inline en block editor). Si solo `page_id`, carga y analiza la página completa desde el content-tree.
- [ ] Runs en background (Horizon queue) si es página completa; síncrono si es block parcial (<2s).
- [ ] Guarda resultado en tabla `seo_audits` (ver schema actualizado).

**Respuesta estructurada:**
```json
{
  "score_seo": 82,
  "score_geo": 67,
  "score_overall": 74,
  "grade": "B",
  "issues": [
    {
      "id": "meta_desc_too_long",
      "severity": "high",
      "category": "seo",
      "message": "Meta description tiene 240 caracteres (max: 160).",
      "field_path": "seo.meta_description",
      "suggestion": "ECOMAG S.A.S: ingeniería civil y ambiental en Barrancabermeja con 15 años de experiencia. Proyectos llave en mano para Ecopetrol, Cenit y sector petrolero. Cotización en 24h."
    },
    {
      "id": "no_tldr_paragraph",
      "severity": "medium",
      "category": "geo",
      "message": "Falta párrafo TL;DR de 40-60 palabras al inicio (crítico para SGE).",
      "suggestion": "Agregar bajo el H1 un párrafo que resuma qué hace la empresa, dónde, y para quién."
    }
  ],
  "suggestions_inline": {
    "blocks": {
      "100": { "headline": "...", "description": "..." }
    }
  },
  "audited_at": "2026-04-22T15:40:00Z",
  "model": "claude-haiku-4-5",
  "cache_hit_ratio": 0.73
}
```

**UI en editor:**
- [ ] Panel lateral derecho colapsable "Auditor YaDev" con:
  - Score circular (SEO, GEO, Overall).
  - Lista de issues ordenada por severidad.
  - Click en issue → scroll al bloque/campo afectado + highlight.
  - Botón "Aplicar sugerencia" inline — reemplaza el campo con la sugerencia IA (requiere confirmación, human-in-the-loop).
- [ ] Re-audita en background al guardar (debounce 3s después de última edición).
- [ ] Último audit visible mientras se edita (no bloqueante).

**Respeto del brand_voice:**
Todas las sugerencias pasan por el system prompt con brand_voice del tenant. Si el tenant dice "tono cercano" y "evitar palabras corporativas", las sugerencias lo respetan. Esto es lo que diferencia de Damos (que usa IA genérica sin ADN del cliente).

### Generación de OG images con Nano Banana 2
- [ ] Integrar skill `nano-banana-2` via CLI inference.sh.
- [ ] Endpoint `POST /api/v1/ai/og-image`:
  - Input: `page_id`, `prompt?` (si no hay, generar desde title + brand).
  - Genera 1200x630 con logo del tenant + headline.
  - Upload a media, vincular a `seo_meta.og_image_id`.
- [ ] UI: botón "Generar OG image" en tab SEO.

### Schema.org IA
- [ ] Sonnet 4.6 sugiere JSON-LD adecuado al tipo de página:
  - Home → LocalBusiness + Organization + WebSite.
  - Service detail → Service + BreadcrumbList.
  - FAQ → FAQPage.
  - Team → Organization con miembros.
- [ ] User aprueba → se guarda en `seo_meta.schema_jsonld`.

---

## Semana 13 — Multi-idioma + automation

### i18n tenant-nivel con preservación de estructura

**Gap vs Damos:** Damos traduce texto plano. Nosotros traducimos blocks JSON preservando la estructura completa (Schema.org, alt text, URLs con slug traducido opcional, data-attributes).

- [ ] Settings: `locales = ['es-CO', 'en']` (o más). Default locale.
- [ ] Por cada bloque editable, tab de idiomas en la UI.
- [ ] Tabla `translations` con shape estructurada: `page_id`, `locale`, `translated_blocks` (JSON con misma forma que blocks originales pero traducidos), `translated_at`, `ai_generated` (bool para distinguir traducciones humanas).

**Endpoint estructurado:**
- [ ] `POST /v1/tenants/{tenant_id}/ai/translate` — body:
  ```json
  {
    "source_locale": "es-CO",
    "target_locale": "en",
    "blocks": [ { "id": 100, "type": "hero_split", "data": { ... } } ],
    "translate_slugs": false,
    "preserve_fields": ["urls", "emails", "phones", "logos", "schema_jsonld.sameAs"]
  }
  ```
- [ ] Respuesta: mismo array de blocks con `data` traducido, estructura byte-por-byte idéntica.
- [ ] El prompt instruye explícitamente a Claude:
  - Traducir solo strings destinadas a renderizar texto visible.
  - Preservar URLs, emails, hex colors, block IDs, enum values, keys JSON.
  - Respetar tono y vocabulario del `brand_voice` incluso al traducir.
  - Mantener longitud aproximada (±20% chars) para evitar overflow en UI.
  - Traducir `alt` attributes de imágenes (accesibilidad en el idioma destino).
  - Schema.org: traducir `description`, `name` cuando aplica, NO traducir URLs de `sameAs` ni `@type`.

**Bulk page translate:**
- [ ] Botón "Traducir toda la página al inglés" → encola job `TranslatePageJob`.
- [ ] Progreso visible en real time (Reverb): "Bloque 3/9 traducido...".
- [ ] Al terminar, abre diff view para que el usuario revise antes de aceptar.
- [ ] Post-aprobación, se guarda en `translations` y el build Astro genera subrutas.

**Build Astro multi-idioma:**
- [ ] Subrutas automáticas: `/en/inicio`, `/en/servicios`.
- [ ] Slug traducido opcional si `translate_slugs: true` → `/en/home`, `/en/services`.
- [ ] hreflang tags automáticos: `<link rel="alternate" hreflang="en" href="...">`.
- [ ] Language switcher renderizado automáticamente en navbar si `locales.length > 1`.

### Automation hooks
- [ ] Webhook handler cuando llega form submission:
  - Respuesta auto-generada con Haiku ("Gracias por contactarnos, {nombre}... nos contactaremos en las próximas 24h").
  - Enviada por email al lead.
  - Lead registrado en CRM si el tenant tiene integración (HubSpot, Mailchimp, etc.).
- [ ] Scheduled posts: programar un bloque para que cambie de estado en X fecha.
- [ ] Re-publishes programados: `schedule` skill de Claude Code para ejecutar `tenants:publish` cada semana (útil para blogs con fecha dinámica).

### Analytics IA
- [ ] Summary semanal por email al admin del tenant:
  - Publishes de la semana.
  - Form submissions (total + conversion rate).
  - Pages editadas.
  - "3 sugerencias IA para mejorar tu sitio esta semana" (generadas con Sonnet).

---

## Semana 14 — Onboarding PORON + COICEM

### Día 66-68: PORON S.A.S
- [ ] Discovery call con cliente → industria, servicios, estilo.
- [ ] Diseño único del sitio (usar skill `ui-ux-pro-max` + checklist de diseño único).
- [ ] Repo `site-poron`, desarrollo frontend en Astro.
- [ ] `tenants:create poron`, seed, publish.
- [ ] Handover + training.

### Día 69-70: COICEM
- [ ] Repetir flujo.
- [ ] Documentar cualquier fricción para actualizar playbook.

### Criterio
El onboarding debe tomar <16h cada uno (no 40h como Multiservicios tomó pre-CMS).

---

## Entregables Fase 3
- Asistente IA de contenido en cada textarea.
- SEO score + sugerencias IA.
- Generación de OG images con Nano Banana 2.
- Multi-idioma con traducción automática.
- Automation hooks (auto-respuesta leads, weekly summary).
- 4 tenants activos: Multiservicios, ECOMAG, PORON, COICEM.

## Métricas
- Ahorro de tiempo por cliente gracias a IA: >30% (medido vs Fase 2).
- Costo IA por tenant/mes: <$3 USD gracias a prompt caching.
- Clientes que usan IA al menos 1x/semana: >60%.
- NPS post-Fase 3: >50.

## Roadmap post-Fase 3 (ideas)
- Marketplace de templates pre-hechos por industria.
- Light-mode toggle por sitio (hoy todos dark-ish).
- A/B testing de CTAs con tracking nativo.
- Integración con Mercado Libre / WooCommerce para mini e-commerce.
- App móvil del CMS (React Native) para editar desde celular.
- IA agente autónomo que publica un artículo/mes por tenant (blog-as-a-service).
