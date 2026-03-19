# Catalogo de Modelos y Templates - YaDev Portfolio

> Ultima actualizacion: 2026-03-18
> Total: 11 HTML templates, 20 modelos de referencia, 29 CSS themes

---

## 1. Templates HTML (proyectos/)

Templates propios creados por YaDev con el sistema YaDev UI (Tailwind CDN + yadev-tokens + yadev-animations + Swiper.js + template-switcher).

| Archivo | Industria | Nombre Demo | Tipografia | Layout Hero | Estilo Visual | Calidad |
|---|---|---|---|---|---|---|
| construccion.html | Construccion | Constructora Edificar | Space Grotesk | Full-width dark con angulos fuertes | Brutalist Industrial (BIG/Foster inspired) | Premium |
| ecommerce.html | E-commerce | ShopStyle Store | Inter | Promo banner + producto grid | Product cards con hover lift + wishlist | Good |
| electrico.html | Electrico/RETIE | CertiPower | Inter | Corporate split con Schema.org | Clean corporate, amarillo RETIE | Premium |
| forestal.html | Forestal/Ambiental | EcoForest Solutions | Playfair Display + Inter | Editorial storytelling full-bleed | Editorial orgánico (Patagonia/NatGeo inspired) | Premium |
| salud.html | Salud/Clinica | VitalCare Clinica | DM Sans + Inter | Calm gradient con breathing animation | Clean clinical (One Medical/Calm inspired) | Premium |
| tecnologia.html | Tecnologia/SaaS | NexaTech Solutions | Satoshi + JetBrains Mono | Dark immersive con ambient glow | Glassmorphism + Bento grid (Linear/Vercel inspired) | Premium |
| transporte.html | Transporte/Logistica | TransLogix | Inter | Map dots + gradient split | Corporate dinamico con process-line | Good |
| restaurante.html | Restaurante/Gastronomia | Casa Raices | Playfair Display + Lato | Full-width food hero calido | Editorial calido, terracotta, fotografia comida (Noma/Eleven Madison inspired) | Premium |
| inmobiliaria.html | Inmobiliaria/Bienes Raices | Elite Propiedades | Cormorant Garamond + Nunito Sans | Buscador hero + propiedades grid | Luxury navy + gold, serif elegant (Sotheby's/Christie's inspired) | Premium |
| educacion.html | Educacion/Academia | Universidad Academica Nacional | Merriweather + Open Sans | Hero institucional con CTA inscripcion | Academico formal, azul + verde, scholarly (MIT/Stanford inspired) | Premium |
| legal.html | Legal/Abogados | Valcarcel & Asociados | Libre Baskerville + Source Sans Pro | Split hero con foto equipo | Conservador elegante, slate + burgundy, serif authority (Cravath inspired) | Premium |

### Resumen de Calidad Templates HTML
- **Premium (9):** construccion, electrico, forestal, salud, tecnologia, restaurante, inmobiliaria, educacion, legal
- **Good (2):** ecommerce, transporte
- **Basic (0):** ninguno

### Notas de Mejora
- **ecommerce.html:** Falta Schema.org, tipografia generica (solo Inter), podria beneficiarse de tipografia display unica
- **transporte.html:** Buen contenido pero el estilo visual es mas generico comparado con los otros, falta yadev-animations-advanced.css

---

## 2. CSS Theme Files (assets/css/templates/)

Cada template HTML soporta multiples themes via el template-switcher. Agrupados por industria:

### Construccion (3 themes)
| Archivo | Estilo | Colores | Bordes | Sombras | Calidad |
|---|---|---|---|---|---|
| construccion-blueprint.css | Blueprint tecnico | Azul plano + blanco | Sharp | Flat | Good |
| construccion-brutalist.css | Brutalista crudo | Negro + amarillo + blanco | Sharp 0px | Box-shadow solido 8px | Premium |
| construccion-industrial.css | Industrial pesado | Grises oscuros + naranja | Mixed | Material | Good |

### E-commerce (3 themes)
| Archivo | Estilo | Colores | Bordes | Sombras | Calidad |
|---|---|---|---|---|---|
| ecommerce-dark.css | Dark mode elegante | Negro + dorado | Rounded | Glow sutil | Good |
| ecommerce-magazine.css | Editorial magazine | Blanco + tipografia bold | Mixed | Soft | Good |
| ecommerce-minimal.css | Minimalista limpio | Blanco + negro | Pill | None/minimal | Good |

### Electrico (5 themes)
| Archivo | Estilo | Colores | Bordes | Sombras | Calidad |
|---|---|---|---|---|---|
| electrico-corporate.css | Corporativo formal | Azul oscuro + gris | Rounded md | Material | Good |
| electrico-dark.css | Dark tech | Negro + amarillo RETIE | Rounded | Glow amarillo | Good |
| electrico-dashboard.css | Dashboard/panel | Gris + indicadores color | Rounded lg | Card shadow | Premium |
| electrico-modern.css | Moderno limpio | Blanco + azul + amarillo | Rounded xl | Soft | Good |
| electrico-tech.css | Tech futurista | Oscuro + cyan + amarillo | Sharp | Neon glow | Good |

### Forestal (3 themes)
| Archivo | Estilo | Colores | Bordes | Sombras | Calidad |
|---|---|---|---|---|---|
| forestal-dark.css | Dark nature | Verde oscuro + negro | Rounded | Subtle | Good |
| forestal-immersive.css | Inmersivo full-screen | Verdes profundos + fotos | Rounded xl | Overlay | Premium |
| forestal-organic.css | Organico artesanal | Crema + verde + papel textura | Pill 50px + dashed | None (handcraft) | Premium |

### Salud (3 themes)
| Archivo | Estilo | Colores | Bordes | Sombras | Calidad |
|---|---|---|---|---|---|
| salud-clean.css | Limpio clinico | Blanco + cyan + teal | Rounded xl | Soft pastel | Good |
| salud-glass.css | Glassmorphism medico | Translucido + teal | Rounded 2xl | Glass blur | Premium |
| salud-hospital.css | Hospital institucional | Blanco + azul formal | Rounded md | Material | Good |

### Tecnologia (5 themes)
| Archivo | Estilo | Colores | Bordes | Sombras | Calidad |
|---|---|---|---|---|---|
| tecnologia-light.css | Light mode SaaS | Blanco + indigo | Rounded xl | Soft | Good |
| tecnologia-neon.css | Cyberpunk/Neon | Negro + verde neon + magenta + cyan | Sharp | Neon glow pulsante | Premium |
| tecnologia-neumorphic.css | Neumorfismo | Gris claro + indigo | Rounded 2xl | Neumorphic inner/outer | Premium |
| tecnologia-dashboard.css | Data dashboard | Navy profundo + grid lines + monospace | Rounded | Card shadow | Premium |
| tecnologia-gradient.css | Bold gradient (Linear-inspired) | Purple-to-blue gradientes + glass | Rounded xl | Glow luminoso | Premium |

### Transporte (3 themes)
| Archivo | Estilo | Colores | Bordes | Sombras | Calidad |
|---|---|---|---|---|---|
| transporte-corporate.css | Corporativo azul | Azul + gris | Rounded | Material | Good |
| transporte-modern.css | Moderno dinamico | Azul + cyan gradiente | Rounded xl | Soft | Good |
| transporte-split.css | Split layout | Azul oscuro + blanco mitades | Mixed | Shadow deep | Good |

### Restaurante (1 theme)
| Archivo | Estilo | Colores | Bordes | Sombras | Calidad |
|---|---|---|---|---|---|
| restaurante-warm.css | Warm editorial | Terracotta + texturas ricas | Rounded lg | Soft warm | Premium |

### Inmobiliaria (1 theme)
| Archivo | Estilo | Colores | Bordes | Sombras | Calidad |
|---|---|---|---|---|---|
| inmobiliaria-elegant.css | Luxury elegante | Navy + dorado | Rounded | Material elegante | Premium |

### Educacion (1 theme)
| Archivo | Estilo | Colores | Bordes | Sombras | Calidad |
|---|---|---|---|---|---|
| educacion-academic.css | Academico institucional | Azul + verde institucional | Rounded md | Soft | Good |

### Legal (1 theme)
| Archivo | Estilo | Colores | Bordes | Sombras | Calidad |
|---|---|---|---|---|---|
| legal-classic.css | Clasico conservador | Slate oscuro + burgundy | Rounded md | Material | Premium |

### Resumen CSS Themes
- **Premium (12):** construccion-brutalist, electrico-dashboard, forestal-immersive, forestal-organic, salud-glass, tecnologia-neon, tecnologia-neumorphic, tecnologia-dashboard, tecnologia-gradient, restaurante-warm, inmobiliaria-elegant, legal-classic
- **Good (17):** el resto
- **Industria con mas themes:** Electrico y Tecnologia (5 cada una)
- **Industria con menos themes:** Restaurante, Inmobiliaria, Educacion, Legal (1 cada una)

---

## 3. Modelos de Referencia (Modelos/)

Archivos HTML guardados de sitios web reales como referencia de diseno e investigacion de competencia. NO son templates propios.

| Archivo | Sitio Real | Industria | Stack Original | Proposito |
|---|---|---|---|---|
| Modelo1.txt | ODIR Certificaciones (odircertificaciones.com) | Electrico/RETIE | Bootstrap + jQuery + Owl Carousel | Referencia competencia RETIE |
| Modelo2.txt | Ingenio Electrocivil (ingenioelectrocivil.com) | Electrico/Civil | Bootstrap + custom CMS | Referencia electrico+civil |
| Modelo 3/ | Proyecto PHP completo (directorio) | Transporte | PHP + Bootstrap + custom | Sitio completo de referencia |
| Modelo 5.txt | GeoPark (geo-park.com) | Petroleo/Gas | WordPress + custom theme | Referencia corporativa premium |
| Modelo 6.txt | Wix site (electrico) | Electrico | Wix Builder | Referencia layout Wix |
| Modelo 7.txt | Neuralink (neuralink.com) | Tecnologia | Static + custom CSS | Referencia diseno tech premium |
| Modelo 8.txt | SpaceX (spacex.com) | Tecnologia/Aerospace | Angular + custom fonts | Referencia dark immersive premium |
| Modelo 9.txt | (archivo muy grande) | Varios | Desconocido | Referencia general |
| Modelo10 cmp-carousel__content LIKE.txt | Intel (intel.la) | Tecnologia | AEM + custom framework | Referencia carousel/componente |
| Modelo11 TRANSPORTE.txt | Kuehne+Nagel | Transporte/Logistica | Nuxt.js + Storyblok | Referencia transporte global |
| Modelo12 TRANSPORTE.txt | (archivo muy grande) | Transporte | Desconocido | Referencia transporte |
| Modelo13 TRANSPORTE.txt | Dispetrocom | Transporte/Petroleo | WordPress + Yoast | Referencia transporte petroleo CO |
| Modelo14 TRANSPORTE.txt | OPL Carga (oplcarga.com) | Transporte Sostenible | HubSpot CMS | Referencia transporte verde CO |
| Modelo15 ELECTRICO.txt | Enel X Colombia | Electrico/RETIE | AEM + custom | Referencia corporativa grande RETIE |
| Modelo16 ELECTRICO.txt | RETIE Ingenieria y Gestion | Electrico/RETIE | WordPress + Yoast | Referencia competencia RETIE CO |
| Modelo17 ELECTRICO.txt | Certiretie S.A.S. | Electrico/RETIE | WordPress + Yoast | Referencia competencia RETIE CO |
| Modelo18 ELECTRICO.txt | Wix site (electrico) | Electrico | Wix Builder | Referencia layout electrico |
| Modelo19 TRANSPORTE.txt | Grupo FRIMAC | Transporte/Logistica | Bootstrap 3 + jQuery | Referencia transporte CO |
| Editor Modelo1.txt | CMS Damos Soluciones (editor) | Herramienta | Custom PHP CMS | Panel admin de referencia |
| Editor Modelo2.txt | Ingenio Electrocivil (editor) | Herramienta | Metronic template + Laravel | Panel admin de referencia |

### Distribucion por Industria (Modelos de Referencia)
- **Electrico/RETIE:** 7 archivos (Modelo 1, 2, 6, 15, 16, 17, 18)
- **Transporte/Logistica:** 7 archivos (Modelo 3, 11, 12, 13, 14, 19)
- **Tecnologia:** 3 archivos (Modelo 7, 8, 10)
- **Petroleo/Gas:** 1 archivo (Modelo 5)
- **Herramientas/CMS:** 2 archivos (Editor Modelo 1, 2)

---

## 4. Mapeo Templates ←→ CSS Themes

| Template HTML | CSS Themes Disponibles | Theme por Defecto |
|---|---|---|
| construccion.html | blueprint, brutalist, industrial | brutalist (inline) |
| ecommerce.html | dark, magazine, minimal | minimal (inline) |
| electrico.html | corporate, dark, dashboard, modern, tech | modern (inline) |
| forestal.html | dark, immersive, organic | organic (inline) |
| salud.html | clean, glass, hospital | clean (inline) |
| tecnologia.html | light, neon, neumorphic, dashboard, gradient | neon (inline SaaS dark) |
| transporte.html | corporate, modern, split | modern (inline) |
| restaurante.html | warm | warm (inline) |
| inmobiliaria.html | elegant | elegant (inline) |
| educacion.html | academic | academic (inline) |
| legal.html | classic | classic (inline) |

---

## 5. Industrias/Nichos que Faltan (Sugerencias)

De las 5 industrias sugeridas originalmente, 4 ya fueron construidas (restaurante, inmobiliaria, educacion, legal). Queda pendiente:

### 5.1 Agro / Agricultura
- **Por que:** Colombia es pais agricola, muchas cooperativas y empresas agro necesitan web
- **Estilo sugerido:** Natural pero robusto, verdes-tierra-dorados, fotos de campo
- **Layout:** Hero panoramico con campo, productos/cultivos en bento grid, proceso de produccion timeline, certificaciones
- **CSS Themes sugeridos:** agro-rustic, agro-corporate, agro-organic

### Otras industrias potenciales
- **Fitness / Gym** — Dinamico, energetico, colores fuertes
- **Belleza / Spa** — Elegante, pastel, tipografia fina
- **Veterinaria** — Amigable, colores calidos, iconografia de mascotas
- **Contabilidad / Finanzas** — Profesional, numeros, graficos, confianza

---

## 6. Checklist de Diferenciacion Visual

Para asegurar que ningun template se parezca a otro (regla critica del proyecto):

| Aspecto | CON | ECO | ELE | FOR | SAL | TEC | TRA | RES | INM | EDU | LEG |
|---|---|---|---|---|---|---|---|---|---|---|---|
| Tipografia | Space Grotesk | Inter | Inter | Playfair Display | DM Sans | Satoshi | Inter | Playfair+Lato | Cormorant+Nunito | Merriweather+Open Sans | Libre Baskerville+Source Sans |
| Hero tipo | Full dark | Promo grid | Split corp | Editorial bleed | Calm gradient | Dark glow | Map dots | Full-width calido | Buscador hero | Institucional CTA | Split equipo |
| Fondo | Dark stone | Blanco | Blanco | Green gradient | Teal gradient | Negro #030712 | Gris claro | Crema calido | Blanco elegante | Blanco institucional | Slate oscuro |
| Estilo cards | Sharp brutal | Product hover | Border-left | Photo essay | Breathing badge | Glass blur | Process step | Menu card warm | Property listing | Program tabs | Practice area |
| Nav estilo | Dark + yellow bar | Standard | Standard + acred | Editorial serif | Calm clean | Dark glassmorphism | White shadow | Warm serif | Luxury minimal | Academic bar | Conservative dark |
| Animacion | Industrial reveal | Product zoom | Fade standard | Horizontal scroll | Breathing pulse | Ambient glow float | Pulse ring | Warm fade | Elegant slide | Structured reveal | Subtle fade |

**Alerta:** ecommerce y transporte ambos usan Inter sin tipografia secundaria diferenciadora. Considerar cambiar uno de ellos.
**Nota:** Todos los 4 nuevos templates (RES, INM, EDU, LEG) usan tipografias serif unicas, garantizando diferenciacion visual total.

---

## 7. Sistema de Archivos YaDev UI

Archivos CSS compartidos que usan todos los templates:
- `yadev-tokens.css` - Design tokens globales
- `yadev-animations.css` - Animaciones base
- `yadev-animations-advanced.css` - Animaciones avanzadas
- `yadev-topbar.css` - Barra superior con contacto y redes
- `yadev-cookies.css` - Banner de cookies/GDPR
- `yadev-carousel.css` - Estilos Swiper.js
- `yadev-preloader.css` - Animacion de carga
- `yadev-language.css` - Selector de idioma
- `yadev-template-switcher.css` - Switcher de themes en demo
- `assets/css/industries/{industria}.css` - Estilos base por industria (11 archivos: construccion, ecommerce, educacion, electrico, forestal, inmobiliaria, legal, restaurante, salud, tecnologia, transporte)
