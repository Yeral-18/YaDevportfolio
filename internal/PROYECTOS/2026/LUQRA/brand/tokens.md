# LUQRA — Brand tokens

Razón social: **Luqra Ingeniería y Soluciones S.A.S.**
Sector: Transporte + logística + construcción + energías renovables + ambiental
Predecesor: Multiservicios P&J (rebrand 2026-05-03 — mismo equipo, scope ampliado)

## Paleta

### Azul corporativo (80% — seriedad / ingeniería)
| Token | Hex | Uso |
|---|---|---|
| `--brand-blue-base` | `#0A2A66` | Texto LUQRA principal, headings, fondos corporativos |
| `--brand-blue-mid` | `#123C8C` | Transición / gradientes |
| `--brand-blue-light` | `#1F5FBF` | Detalle / brillos / acentos azul |

### Naranja (20% — impacto / recordación)
| Token | Hex | Uso |
|---|---|---|
| `--brand-orange-base` | `#FF6A00` | Letra Q (identidad fuerte), CTAs principales |
| `--brand-orange-mid` | `#FF8C1A` | Transición / gradientes |
| `--brand-orange-light` | `#FFA533` | Brillos / hover states |

### Complementarios
| Token | Hex | Uso |
|---|---|---|
| `--surface` | `#FFFFFF` | Fondos principales |
| `--text-secondary` | `#1A1A1A` | Texto secundario / muted |

## Regla 80/20

**80% azul → seriedad.** **20% naranja → recordación.**
El naranja NO debe dominar. Es el acento que hace memorable la marca.

## Tipografía propuesta (a confirmar próxima sesión)

3 combos candidatos según el "tono ingenieril + dinamismo":

1. **Plus Jakarta Sans + Inter** (recomendado) — heredado de Multiservicios, mantiene continuidad operativa, mod
ern + legible en mobile.
2. **Sora + Inter** — más geométrica, vibe tech. Buen match con la identidad ingenieril.
3. **Manrope + Inter** — humanista, calida. Suaviza el azul institucional sin perder seriedad.

Display weights: 700/800 para LUQRA-style headings.
Body: Inter 400/500/600.
Mono: JetBrains Mono (para códigos de proyecto, números técnicos, IDs de seguimiento de carga).

## Logo files

- `logo.jpeg` — original recibido del cliente (84 KB, fondo blanco).
- `logo.png` — versión transparente (1600x800, 256 KB, flood-fill bg removido).
- `logo_b64.txt` — data URI para email signatures / brandbook embed.

## TODO próxima sesión

1. Confirmar tipografía con cliente (1, 2 o 3).
2. Decidir cutover: ¿`luqra.com.co` nuevo dominio o seguir en `multiserviciospj.com` redirigido?
3. Decidir scope del sitio nuevo — ¿splash de relanzamiento o sitio completo de una?
4. Crear `LuqraSeeder.php` en yadev-cms reemplazando `MultiserviciosSeeder`.
5. Diseñar hero/servicios reflejando los 5 ejes operativos: transporte+logística, construcción, energía, ambiental, comercio internacional.
6. Generar OG image 1200x630 con logo centrado.
7. Generar firma de correo HTML con `logo_b64.txt`.
