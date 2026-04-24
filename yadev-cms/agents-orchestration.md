# Agents & Skills Orchestration — YaDev CMS

> Mapeo de qué agente/skill usa Claude Code en cada tarea del proyecto, en qué orden, y qué puede paralelizarse.
> Referencia: ver `.claude/agents/` (root) y skills disponibles en la sesión.

---

## Roster disponible

### Agentes (root del portfolio + built-in)
| Agente | Fortaleza |
|--------|-----------|
| `project-orchestrator` (este) | Cerebro principal, divide tareas, coordina |
| `Explore` | Leer código existente sin modificar |
| `Plan` | Diseñar cambios grandes antes de ejecutar |
| `general-purpose` | Ejecutar múltiples cambios paralelos |
| `frontend-developer` | Componentes, CSS, layouts |
| `code-reviewer` | Revisión de PRs / calidad de código |
| `security-auditor` | Vulnerabilidades, headers, permisos |
| `seo-specialist` | Schema.org, meta tags, keywords |
| `devops-engineer` | CI/CD, infra, Docker, deploy |
| `content-marketer` | Copy, textos SEO |

### Skills
| Skill | Fortaleza |
|-------|-----------|
| `simplify` | Limpieza/refactor de código |
| `review` | Review estructurado de PR |
| `security-review` | Audit de branch actual |
| `ui-ux-pro-max` | Decisiones de diseño (paletas, tipografía, layouts) |
| `nano-banana-2` | Generación de imágenes (OG, hero, mockups) |
| `claude-api` | Build apps Anthropic con prompt caching |
| `init` | CLAUDE.md initialization |
| `loop` | Ejecutar prompts recurrentes |
| `schedule` | Cron de agentes remotos |

---

## Fase 0 — Setup VPS

### Tareas y asignaciones

| Tarea | Agente/Skill | Paraleliza? | Notas |
|-------|-------------|-------------|-------|
| Diseñar arquitectura VPS | `Plan` | — | Ya hecho en `phases/phase-0-setup.md` |
| Redactar scripts bash hardening | `devops-engineer` | ❌ secuencial | Validar cada paso |
| Configurar Nginx sites | `devops-engineer` | ❌ | SSL después de reachability |
| Emitir SSL certbot | `devops-engineer` | ❌ | Depende DNS propagated |
| Script de backups B2 | `devops-engineer` | ✅ paralelo a Nginx | Independiente |
| Workflow GitHub Actions | `devops-engineer` | ✅ paralelo a backups | Independiente |
| Revisar seguridad del setup | `security-auditor` + skill `security-review` | ❌ al final | Despues de todo lo anterior |

**Orquestación sugerida:**
```
1. project-orchestrator → Plan del setup
2. devops-engineer → scripts en orden secuencial (hardening → stack → Nginx → SSL)
3. PARALELO:
   - devops-engineer → backups
   - devops-engineer → CI/CD
4. security-auditor → audit final
5. code-reviewer → valida scripts antes de merge
```

---

## Fase 1 — MVP

### Semana 1: Scaffolding Laravel

| Tarea | Agente/Skill | Paraleliza? |
|-------|-------------|-------------|
| Crear repo monorepo | `devops-engineer` | — |
| Explorar Laravel 11 docs + stancl/tenancy | `Explore` | ✅ con scaffolding |
| Setup Laravel + packages | `general-purpose` | — |
| Adaptar central-schema.sql a migrations | `general-purpose` | ✅ con tenant-schema |
| Adaptar tenant-schema.sql a migrations | `general-purpose` | ✅ con central |
| Middleware + tests foundation | `frontend-developer` (backend variant) | ❌ después de migrations |

### Semana 2: API CRUD

| Tarea | Agente/Skill | Paraleliza? |
|-------|-------------|-------------|
| Diseñar API contract (si hay cambios) | `Plan` | — |
| Modelos + resources | `general-purpose` (dispara 3-4 en paralelo) | ✅ |
| Block types 1-5 | `general-purpose` (1 por block) | ✅ 5 paralelos |
| Endpoints auth | `general-purpose` | ✅ con block types |
| Endpoints pages/blocks CRUD | `general-purpose` | ❌ necesita block types ready |
| Tests feature | `general-purpose` | ✅ mientras otro escribe endpoints |
| Security review de endpoints | `security-auditor` + skill `security-review` | ❌ al final de la semana |

### Semana 3: Panel SvelteKit

| Tarea | Agente/Skill | Paraleliza? |
|-------|-------------|-------------|
| Diseño visual del panel | skill `ui-ux-pro-max` + `frontend-developer` | — |
| Scaffold SvelteKit + Tailwind | `frontend-developer` | — |
| shadcn-svelte setup + tokens YaDev | `frontend-developer` | ❌ después de scaffold |
| Auth pages + store | `frontend-developer` | ✅ con shadcn |
| Editor bloques (5 types) | `general-purpose` (1 por block editor) | ✅ 5 paralelos |
| Mediateca UI | `frontend-developer` | ✅ con block editors |
| Code review | `code-reviewer` + skill `review` | ❌ al final |

### Semana 4: Runner + deploy

| Tarea | Agente/Skill | Paraleliza? |
|-------|-------------|-------------|
| Runner Node (Fastify) | `devops-engineer` | — |
| Refactor Astro Multiservicios | `frontend-developer` | ✅ con runner |
| Transformers JSON → Astro | `frontend-developer` | ❌ después de Astro refactor |
| Integración Laravel → runner | `devops-engineer` | ❌ después runner + Astro |
| QA end-to-end | `project-orchestrator` (coordina) | — |
| Simplify antes de merge | skill `simplify` | ❌ al final |

---

## Fase 2 — Paridad

### Semana 5: Bloques avanzados

Cada nuevo block type tiene 4 tareas independientes. Ejecutar muchas en paralelo:

```
general-purpose (wave 1, parallel):
  - stats_bar (schema + editor + transformer + test)
  - benefits_grid (schema + editor + transformer + test)
  - bento_projects (schema + editor + transformer + test)

general-purpose (wave 2, parallel):
  - clients_carousel
  - cta_banner
  - footer_mega

general-purpose (wave 3, parallel):
  - image_gallery
  - faq
  - timeline

general-purpose (wave 4, parallel):
  - team_grid
  - testimonials_slider
  - pricing_table

code-reviewer → al cierre de cada wave
```

### Semana 6: Forms

| Tarea | Agente/Skill | Paraleliza? |
|-------|-------------|-------------|
| UI form builder | `frontend-developer` + skill `ui-ux-pro-max` | — |
| Backend validación + storage submissions | `general-purpose` | ✅ con UI |
| Resend integration (email) | `devops-engineer` | ✅ con backend |
| Meta Cloud API integration (WhatsApp) | `devops-engineer` | ✅ con Resend |
| Anti-spam (honeypot + reCAPTCHA) | `security-auditor` | ❌ al final de la semana |
| Export CSV | `general-purpose` | ✅ con todo lo demás |

### Semana 7: SEO + Menús + Popups

| Tarea | Agente/Skill | Paraleliza? |
|-------|-------------|-------------|
| SEO editor UI + logic | `seo-specialist` + `frontend-developer` | — |
| Menú editor drag-drop | `frontend-developer` | ✅ con SEO |
| Popups UI + trigger logic | `frontend-developer` | ✅ con menús |
| Redirects simple UI | `general-purpose` | ✅ |
| Content marketer revisa que los textos editables sean SEO-friendly | `content-marketer` | ❌ al final |

### Semana 8: Mediateca + Activity

| Tarea | Agente/Skill | Paraleliza? |
|-------|-------------|-------------|
| Folders + tags | `general-purpose` | — |
| Conversiones async (thumb/webp/og) | `devops-engineer` | ✅ |
| Usage tracker | `general-purpose` | ✅ |
| Cloudflare R2 adapter | `devops-engineer` | ✅ con el resto |
| Activity log UI | `frontend-developer` | ✅ |
| Version restore | `general-purpose` | ✅ |

### Semana 9: Users + 2FA + Collab

| Tarea | Agente/Skill | Paraleliza? |
|-------|-------------|-------------|
| Users CRUD | `general-purpose` | — |
| 2FA TOTP flow | `security-auditor` + `frontend-developer` | ✅ con users |
| Invite via email | `devops-engineer` | ✅ |
| Collaboration via Reverb | `frontend-developer` | ✅ |
| Security review consolidada | `security-auditor` + skill `security-review` | ❌ al cierre |

### Semana 10: Onboarding ECOMAG

| Tarea | Agente/Skill | Paraleliza? |
|-------|-------------|-------------|
| Explore componentes actuales ECOMAG | `Explore` | — |
| Mapear a bloques CMS | `Plan` | ❌ después Explore |
| Bloques nuevos si hacen falta | `general-purpose` | ✅ |
| Seed ecomag.sql | `content-marketer` + `general-purpose` | ✅ |
| Refactor Astro ECOMAG | `frontend-developer` | ❌ |
| Cutover QA | `code-reviewer` + project-orchestrator | ❌ al final |

---

## Fase 3 — IA

### Semana 11: Asistente de contenido

| Tarea | Agente/Skill | Paraleliza? |
|-------|-------------|-------------|
| Anthropic SDK setup + prompt caching | skill `claude-api` | — |
| ClaudeService wrapper | `general-purpose` | — |
| Endpoints rewrite/translate/etc | `general-purpose` | ✅ con UI |
| UI del asistente (modal) | `frontend-developer` | ✅ |
| Rate limiting por tenant | `security-auditor` | ❌ al final |
| Tracking de tokens/costos | `devops-engineer` | ✅ |

### Semana 12: SEO IA + OG images

| Tarea | Agente/Skill | Paraleliza? |
|-------|-------------|-------------|
| SEO score endpoint (Sonnet) | `seo-specialist` + skill `claude-api` | — |
| UI SEO score | `frontend-developer` | ✅ con endpoint |
| Integración Nano Banana 2 | skill `nano-banana-2` | ✅ |
| Endpoint OG image | `general-purpose` + skill `nano-banana-2` | ❌ después de nano setup |
| Schema.org generator | `seo-specialist` + skill `claude-api` | ✅ |

### Semana 13: i18n + automation

| Tarea | Agente/Skill | Paraleliza? |
|-------|-------------|-------------|
| Migration `translations` table + logic | `general-purpose` | — |
| Build Astro multi-locale | `frontend-developer` | ✅ con translations logic |
| Tab idiomas en editor | `frontend-developer` | ✅ |
| Bulk translate async | `general-purpose` + skill `claude-api` | ✅ |
| Automation hooks | `devops-engineer` | ✅ |
| Weekly summary email | `content-marketer` + skill `claude-api` | ✅ |
| Cron scheduling | skill `schedule` | ❌ al final |

### Semana 14: Onboarding PORON + COICEM

Mismo patrón que ECOMAG en semana 10.

---

## Orchestration reglas generales

### Cuándo usar `Explore`
- Antes de modificar cualquier archivo que no creaste (p.ej. componentes de Multiservicios).
- Cuando el usuario pregunta "¿cómo funciona X?" en el codebase.

### Cuándo usar `Plan`
- Cuando una tarea afecta 4+ archivos relacionados.
- Cuando hay que decidir entre 2+ enfoques técnicos (documenta trade-offs).

### Cuándo usar `general-purpose` (en paralelo)
- Múltiples archivos independientes que se pueden escribir simultáneamente.
- Tests que van a archivos separados.
- Block types de la librería (1 agente por block).
- Máximo 4-6 en paralelo para no saturar el contexto.

### Cuándo usar skills
- `security-review` → antes de cada deploy a producción.
- `review` → antes de merger un PR grande.
- `simplify` → cada vez que un archivo pasa 300 líneas o hay lógica duplicada.
- `ui-ux-pro-max` → toda decisión visual (paleta, tipografía, componentes).
- `claude-api` → cuando se integra/modifica código del SDK Anthropic.
- `nano-banana-2` → para generar OG images, mockups, placeholder assets.

### Reglas anti-agresión
- Nunca más de 6 agentes paralelos simultáneamente.
- Siempre finalizar una wave con `code-reviewer` antes de abrir la siguiente.
- Si un agente paralelo escribe a un archivo que otro también toca → serializar.

---

## Ejemplo concreto: Semana 5 Wave 1

```
USER: "Implementa stats_bar, benefits_grid, bento_projects como block types."

project-orchestrator:
1. Lanza 3 general-purpose agents en paralelo:

   agent-1:
     input: "Implementa block type 'stats_bar' en yadev-cms/api. Crea:
             - api/app/Blocks/StatsBar.php con schema completo
             - api/app/Http/Requests/Blocks/StatsBarRequest.php
             - admin/src/lib/blocks/stats_bar/Editor.svelte
             - runner/transformers/stats_bar.mjs
             - Test en api/tests/Feature/Blocks/StatsBarTest.php"

   agent-2:
     input: "Implementa block type 'benefits_grid' en yadev-cms/api. Crea: ..."

   agent-3:
     input: "Implementa block type 'bento_projects' en yadev-cms/api. Crea: ..."

2. Después de que los 3 terminan:
   - code-reviewer audita los 3 PRs.
   - Si hay issues → general-purpose específico para cada fix.
   - Si OK → merge.

3. Wave 2 lanza siguientes 3 block types.
```

Este patrón reduce tiempo de Fase 2 Semana 5 de ~5 días a ~2 días reales.
