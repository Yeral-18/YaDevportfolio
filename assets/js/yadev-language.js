/**
 * YaDev UI - Language System (i18n)
 * Sistema de cambio de idioma funcional
 */

(function() {
    'use strict';

    // Default translations
    const translations = {
        es: {
            // Navigation
            'nav.home': 'Inicio',
            'nav.services': 'Servicios',
            'nav.about': 'Nosotros',
            'nav.process': 'Proceso',
            'nav.contact': 'Contacto',
            'nav.quote': 'Cotizar Ahora',
            'nav.accreditations': 'Acreditaciones',

            // Common
            'common.readMore': 'Leer más',
            'common.viewAll': 'Ver todos',
            'common.submit': 'Enviar',
            'common.loading': 'Cargando...',
            'common.phone': 'Teléfono',
            'common.email': 'Correo',
            'common.address': 'Dirección',
            'common.schedule': 'Horario',

            // Hero
            'hero.title': 'Título Principal',
            'hero.subtitle': 'Subtítulo descriptivo',
            'hero.cta': 'Comenzar Ahora',

            // Services
            'services.title': 'Nuestros Servicios',
            'services.subtitle': 'Ofrecemos soluciones integrales',

            // About
            'about.title': 'Sobre Nosotros',
            'about.mission': 'Misión',
            'about.vision': 'Visión',
            'about.values': 'Valores',

            // Contact
            'contact.title': 'Contáctenos',
            'contact.name': 'Nombre',
            'contact.phone': 'Teléfono',
            'contact.email': 'Correo electrónico',
            'contact.message': 'Mensaje',
            'contact.send': 'Enviar Mensaje',

            // Footer
            'footer.rights': 'Todos los derechos reservados',
            'footer.privacy': 'Privacidad',
            'footer.terms': 'Términos',

            // Cookie consent
            'cookies.title': 'Usamos cookies',
            'cookies.message': 'Este sitio utiliza cookies para mejorar tu experiencia.',
            'cookies.accept': 'Aceptar',
            'cookies.configure': 'Configurar',

            // Electrico specific
            'electrico.certifications': 'Certificaciones',
            'electrico.retie': 'Certificación RETIE',
            'electrico.retilap': 'Certificación RETILAP',
            'electrico.ritel': 'Certificación RITEL',
            'electrico.quote': 'Solicitar Cotización',
            'electrico.process': '¿Cómo Funciona?',
        },
        en: {
            // Navigation
            'nav.home': 'Home',
            'nav.services': 'Services',
            'nav.about': 'About Us',
            'nav.process': 'Process',
            'nav.contact': 'Contact',
            'nav.quote': 'Get Quote',
            'nav.accreditations': 'Accreditations',

            // Common
            'common.readMore': 'Read more',
            'common.viewAll': 'View all',
            'common.submit': 'Submit',
            'common.loading': 'Loading...',
            'common.phone': 'Phone',
            'common.email': 'Email',
            'common.address': 'Address',
            'common.schedule': 'Schedule',

            // Hero
            'hero.title': 'Main Title',
            'hero.subtitle': 'Descriptive subtitle',
            'hero.cta': 'Get Started',

            // Services
            'services.title': 'Our Services',
            'services.subtitle': 'We offer comprehensive solutions',

            // About
            'about.title': 'About Us',
            'about.mission': 'Mission',
            'about.vision': 'Vision',
            'about.values': 'Values',

            // Contact
            'contact.title': 'Contact Us',
            'contact.name': 'Name',
            'contact.phone': 'Phone',
            'contact.email': 'Email',
            'contact.message': 'Message',
            'contact.send': 'Send Message',

            // Footer
            'footer.rights': 'All rights reserved',
            'footer.privacy': 'Privacy',
            'footer.terms': 'Terms',

            // Cookie consent
            'cookies.title': 'We use cookies',
            'cookies.message': 'This site uses cookies to improve your experience.',
            'cookies.accept': 'Accept',
            'cookies.configure': 'Configure',

            // Electrico specific
            'electrico.certifications': 'Certifications',
            'electrico.retie': 'RETIE Certification',
            'electrico.retilap': 'RETILAP Certification',
            'electrico.ritel': 'RITEL Certification',
            'electrico.quote': 'Request Quote',
            'electrico.process': 'How It Works?',
        }
    };

    // Current language
    let currentLang = localStorage.getItem('yadev-lang') || 'es';

    /**
     * Get translation for a key
     */
    function t(key, lang = currentLang) {
        const langData = translations[lang] || translations['es'];
        return langData[key] || key;
    }

    /**
     * Set the current language
     */
    function setLanguage(lang) {
        if (!translations[lang]) {
            console.warn(`Language "${lang}" not available`);
            return;
        }

        currentLang = lang;
        localStorage.setItem('yadev-lang', lang);
        document.documentElement.lang = lang;

        // Add translating class for animation
        document.body.classList.add('translating');

        // Translate all elements with data-i18n
        translatePage();

        // Remove translating class after animation
        setTimeout(() => {
            document.body.classList.remove('translating');
        }, 200);

        // Update language switcher UI
        updateLanguageSwitcher();

        // Dispatch event for custom handling
        document.dispatchEvent(new CustomEvent('languageChanged', {
            detail: { language: lang }
        }));

        console.log(`Language changed to: ${lang}`);
    }

    /**
     * Translate all elements with data-i18n attribute
     */
    function translatePage() {
        const elements = document.querySelectorAll('[data-i18n]');
        elements.forEach(el => {
            const key = el.dataset.i18n;
            const translation = t(key);

            if (el.tagName === 'INPUT' && el.placeholder) {
                el.placeholder = translation;
            } else {
                el.textContent = translation;
            }
        });

        // Translate elements with data-i18n-placeholder
        const placeholders = document.querySelectorAll('[data-i18n-placeholder]');
        placeholders.forEach(el => {
            const key = el.dataset.i18nPlaceholder;
            el.placeholder = t(key);
        });

        // Translate elements with data-i18n-title (for tooltips)
        const titles = document.querySelectorAll('[data-i18n-title]');
        titles.forEach(el => {
            const key = el.dataset.i18nTitle;
            el.title = t(key);
        });

        // Auto-translate common patterns without data-i18n
        autoTranslateCommonElements();
    }

    /**
     * Auto-translate common UI elements based on text matching
     */
    function autoTranslateCommonElements() {
        const autoTranslations = {
            es: {
                // Navigation
                'Home': 'Inicio',
                'Services': 'Servicios',
                'About': 'Nosotros',
                'About Us': 'Nosotros',
                'Contact': 'Contacto',
                'Contact Us': 'Contáctenos',
                'Get Quote': 'Cotizar',
                'Request Quote': 'Solicitar Cotización',
                'Our Team': 'Nuestro Equipo',
                'Testimonials': 'Testimonios',
                'Clients': 'Clientes',
                'Mission': 'Misión',
                'Vision': 'Visión',
                'Values': 'Valores',
                'Read More': 'Leer Más',
                'View All': 'Ver Todos',
                'Submit': 'Enviar',
                'Send': 'Enviar',
                'Send Message': 'Enviar Mensaje',
                'Name': 'Nombre',
                'Email': 'Correo',
                'Phone': 'Teléfono',
                'Message': 'Mensaje',
                'All rights reserved': 'Todos los derechos reservados',
                'Privacy Policy': 'Política de Privacidad',
                'Terms of Service': 'Términos de Servicio',
                'The Company': 'La Compañía',
            },
            en: {
                // Navigation
                'Inicio': 'Home',
                'Servicios': 'Services',
                'Nosotros': 'About Us',
                'Contacto': 'Contact',
                'Contáctenos': 'Contact Us',
                'Cotizar': 'Get Quote',
                'Cotizar Ahora': 'Get Quote Now',
                'Solicitar Cotización': 'Request Quote',
                'Solicite su Cotización Gratuita': 'Request Your Free Quote',
                'Nuestro Equipo': 'Our Team',
                'Testimonios': 'Testimonials',
                'Clientes': 'Clients',
                'Misión': 'Mission',
                'Visión': 'Vision',
                'Valores': 'Values',
                'Misión y Visión': 'Mission & Vision',
                'Leer Más': 'Read More',
                'Ver Todos': 'View All',
                'Ver más sectores': 'View more sectors',
                'Enviar': 'Submit',
                'Enviar Mensaje': 'Send Message',
                'Nombre': 'Name',
                'Nombre completo': 'Full Name',
                'Correo': 'Email',
                'Correo electrónico': 'Email address',
                'Teléfono': 'Phone',
                'Mensaje': 'Message',
                'Tu mensaje': 'Your message',
                'Escribe tu mensaje': 'Write your message',
                'Todos los derechos reservados': 'All rights reserved',
                'Política de Privacidad': 'Privacy Policy',
                'Términos de Servicio': 'Terms of Service',
                'La Compañía': 'The Company',
                'Confían en Nosotros': 'They Trust Us',
                'Nuestros Clientes': 'Our Clients',
                'Nuestros Aliados': 'Our Partners',
                'Profesionales': 'Professionals',
                'Expertos': 'Experts',
                'Certificados': 'Certified',
                'Acreditaciones': 'Accreditations',
                'Proceso': 'Process',
                'Proceso de Certificación': 'Certification Process',
                '¿Cómo Funciona?': 'How Does It Work?',
                'Respuesta Rápida': 'Fast Response',
                'Años de Experiencia': 'Years of Experience',
                'Clientes Satisfechos': 'Satisfied Clients',
                'Proyectos Completados': 'Completed Projects',
                'Certificaciones Emitidas': 'Certifications Issued',
                // Sections
                'Nuestros Servicios': 'Our Services',
                'Sobre Nosotros': 'About Us',
                'Director General': 'General Director',
                'Directora Técnica': 'Technical Director',
                'Ingeniero Senior': 'Senior Engineer',
                'Coordinador': 'Coordinator',
                'Coordinadora': 'Coordinator',
                // Footer
                'Enlaces Rápidos': 'Quick Links',
                'Servicios Destacados': 'Featured Services',
                'Contacto Directo': 'Direct Contact',
                'Horario de Atención': 'Business Hours',
                'Lunes a Viernes': 'Monday to Friday',
                'Sábados': 'Saturdays',
                // Common phrases
                'Volver a YaDev Portfolio': 'Back to YaDev Portfolio',
                'Este es un demo de diseño': 'This is a design demo',
                'Solicita tu cotización': 'Request your quote',
                'Contamos con': 'We have',
                'equipo de': 'team of',
                // Healthcare
                'Agendar Cita': 'Book Appointment',
                'Especialidades': 'Specialties',
                'Nuestros Doctores': 'Our Doctors',
                'Profesionales de la Salud': 'Healthcare Professionals',
                // Ecommerce
                'Comprar Ahora': 'Buy Now',
                'Agregar al Carrito': 'Add to Cart',
                'Ver Productos': 'View Products',
                'Ofertas': 'Offers',
                // Technology
                'Comenzar': 'Get Started',
                'Comenzar Gratis': 'Start Free',
                'Características': 'Features',
                'Precios': 'Pricing',
                'Documentación': 'Docs',
                // Construction
                'Nuestros Proyectos': 'Our Projects',
                'Proyectos Destacados': 'Featured Projects',
                // Transport
                'Rastreo': 'Tracking',
                'Rastrear Envío': 'Track Shipment',
                'Flota': 'Fleet',
                'Cobertura': 'Coverage',
                // Forestry
                'Sostenibilidad': 'Sustainability',
                'Certificación Forestal': 'Forest Certification',
                'Gestión Ambiental': 'Environmental Management',
                // Electrical sector
                'Certificaciones': 'Certifications',
                'Certificaciones Eléctricas': 'Electrical Certifications',
                'Eléctricas': 'Electrical',
                'Profesionales': 'Professionals',
                'Organismo de inspección acreditado por ONAC.': 'ONAC accredited inspection body.',
                'Garantizamos el cumplimiento normativo de sus instalaciones eléctricas con los más altos estándares de calidad.': 'We guarantee regulatory compliance of your electrical installations with the highest quality standards.',
                'Años de Experiencia': 'Years of Experience',
                'Departamentos': 'Departments',
                'Satisfacción': 'Satisfaction',
                'Llamar Ahora': 'Call Now',
                'Solicitar Cotización': 'Request Quote',
                '¿Por qué Elegirnos?': 'Why Choose Us?',
                'Nuestro Proceso': 'Our Process',
                'Acreditaciones': 'Accreditations',
                'Acreditaciones y': 'Accreditations and',
                'Proceso de Certificación': 'Certification Process',
                'Paso': 'Step',
                'Solicitud': 'Application',
                'Inspección': 'Inspection',
                'Evaluación': 'Evaluation',
                'Certificación': 'Certification',
                'Complete el formulario': 'Complete the form',
                'Cotización Gratuita': 'Free Quote',
                'Respuesta Rápida': 'Fast Response',
                'Cotización en menos de 24 horas hábiles': 'Quote in less than 24 business hours',
                'Asesoría Personalizada': 'Personalized Advice',
                'Expertos disponibles para resolver sus dudas': 'Experts available to answer your questions',
                'Precios Competitivos': 'Competitive Prices',
                'Las mejores tarifas del mercado': 'The best rates in the market',
                'Lo que dicen nuestros clientes': 'What our clients say',
                'Director General': 'General Director',
                'Directora Técnica': 'Technical Director',
                'Ingeniero Senior RETIE': 'Senior RETIE Engineer',
                'Ingeniera RETILAP': 'RETILAP Engineer',
                'Ingeniero RITEL': 'RITEL Engineer',
                'Jefe de Proyectos': 'Project Manager',
                'Nuestro Equipo': 'Our Team',
                'Profesionales Certificados': 'Certified Professionals',
                'Contamos con un equipo de ingenieros especializados con amplia experiencia en el sector eléctrico.': 'We have a team of specialized engineers with extensive experience in the electrical sector.',
                'Confían en Nosotros': 'They Trust Us',
                'Nuestros Clientes': 'Our Clients',
                'Todos los derechos reservados': 'All rights reserved',
                'Enlaces Rápidos': 'Quick Links',
                'Servicios': 'Services',
                'Lun - Vie': 'Mon - Fri',
            }
        };

        const currentTranslations = autoTranslations[currentLang] || {};

        // Translate text nodes in various elements
        const selectors = [
            'a', 'button', 'h1', 'h2', 'h3', 'h4', 'h5', 'h6',
            'p', 'span', 'label', 'li', 'th', 'td', 'dt', 'dd',
            '.text-sm', '.text-xs', '.font-semibold', '.font-bold'
        ];

        document.querySelectorAll(selectors.join(', ')).forEach(el => {
            // Skip elements with data-i18n or that contain child elements with significant text
            if (el.dataset.i18n) return;
            if (el.querySelector('svg, img')) return; // Skip elements with icons/images

            // Get direct text content (not from children)
            const childNodes = el.childNodes;
            childNodes.forEach(node => {
                if (node.nodeType === Node.TEXT_NODE) {
                    const text = node.textContent.trim();
                    if (text && currentTranslations[text]) {
                        node.textContent = node.textContent.replace(text, currentTranslations[text]);
                    }
                }
            });

            // Also check full text content for simple elements
            if (el.children.length === 0) {
                const text = el.textContent.trim();
                if (currentTranslations[text]) {
                    el.textContent = currentTranslations[text];
                }
            }
        });

        // Translate placeholders
        document.querySelectorAll('input[placeholder], textarea[placeholder]').forEach(el => {
            const placeholder = el.placeholder.trim();
            if (currentTranslations[placeholder]) {
                el.placeholder = currentTranslations[placeholder];
            }
        });

        // Translate title attributes
        document.querySelectorAll('[title]').forEach(el => {
            const title = el.title.trim();
            if (currentTranslations[title]) {
                el.title = currentTranslations[title];
            }
        });

        // Translate aria-labels
        document.querySelectorAll('[aria-label]').forEach(el => {
            const label = el.getAttribute('aria-label').trim();
            if (currentTranslations[label]) {
                el.setAttribute('aria-label', currentTranslations[label]);
            }
        });

        // Special handling for elements with mixed content (text + child elements)
        document.querySelectorAll('h1, h2, h3, h4, h5, h6, p, span, div, a, button').forEach(el => {
            if (el.dataset.i18n) return;

            // Check each child text node
            Array.from(el.childNodes).forEach(node => {
                if (node.nodeType === Node.TEXT_NODE) {
                    let text = node.textContent;
                    let changed = false;

                    // Try to translate parts of the text
                    Object.keys(currentTranslations).forEach(key => {
                        if (text.includes(key)) {
                            text = text.replace(key, currentTranslations[key]);
                            changed = true;
                        }
                    });

                    if (changed) {
                        node.textContent = text;
                    }
                }
            });
        });

        console.log('Auto-translation completed for:', currentLang);
    }

    /**
     * Update language switcher UI
     */
    function updateLanguageSwitcher() {
        // Update simple switchers
        const simpleLinks = document.querySelectorAll('.language-switcher--simple a');
        simpleLinks.forEach(link => {
            const lang = link.dataset.lang || link.textContent.toLowerCase().substring(0, 2);
            link.classList.toggle('active', lang === currentLang);
        });

        // Update dropdown switchers
        const dropdowns = document.querySelectorAll('.language-dropdown');
        dropdowns.forEach(dropdown => {
            const items = dropdown.querySelectorAll('.language-dropdown__item');
            items.forEach(item => {
                const lang = item.dataset.lang;
                item.classList.toggle('active', lang === currentLang);
            });

            // Update trigger text
            const trigger = dropdown.querySelector('.language-dropdown__trigger span');
            if (trigger) {
                trigger.textContent = currentLang.toUpperCase();
            }
        });
    }

    /**
     * Initialize language switcher interactions
     */
    function initLanguageSwitchers() {
        // Simple link switchers - support multiple selector patterns
        const langSelectors = [
            '.language-switcher--simple a',
            '.top-bar__lang a',
            '[data-lang]',
            '.lang-switch a',
            'a[href="#"][data-lang]'
        ];

        document.querySelectorAll(langSelectors.join(', ')).forEach(link => {
            // Remove any existing listeners
            const newLink = link.cloneNode(true);
            link.parentNode.replaceChild(newLink, link);

            newLink.addEventListener('click', (e) => {
                e.preventDefault();
                e.stopPropagation();

                let lang = newLink.dataset.lang;
                if (!lang) {
                    const text = newLink.textContent.toLowerCase();
                    lang = text.includes('esp') || text.includes('es') ? 'es' : 'en';
                }

                setLanguage(lang);

                // Visual feedback
                document.querySelectorAll('[data-lang]').forEach(l => {
                    l.classList.toggle('active', l.dataset.lang === lang);
                });
            });
        });

        // Dropdown switchers
        document.querySelectorAll('.language-dropdown').forEach(dropdown => {
            const trigger = dropdown.querySelector('.language-dropdown__trigger');
            const items = dropdown.querySelectorAll('.language-dropdown__item');

            // Toggle dropdown
            if (trigger) {
                trigger.addEventListener('click', (e) => {
                    e.stopPropagation();
                    dropdown.classList.toggle('open');
                });
            }

            // Select language
            items.forEach(item => {
                item.addEventListener('click', () => {
                    const lang = item.dataset.lang;
                    setLanguage(lang);
                    dropdown.classList.remove('open');
                });
            });
        });

        // Close dropdowns on outside click
        document.addEventListener('click', () => {
            document.querySelectorAll('.language-dropdown.open').forEach(d => {
                d.classList.remove('open');
            });
        });
    }

    /**
     * Add custom translations
     */
    function addTranslations(lang, data) {
        if (!translations[lang]) {
            translations[lang] = {};
        }
        Object.assign(translations[lang], data);
    }

    /**
     * Initialize the language system
     */
    function init() {
        // Set initial language from localStorage or default
        currentLang = localStorage.getItem('yadev-lang') || 'es';
        document.documentElement.lang = currentLang;

        // Initialize switcher interactions
        initLanguageSwitchers();

        // Initial translation
        translatePage();
        updateLanguageSwitcher();

        console.log('YaDev Language System initialized');
    }

    // Auto-init on DOM ready
    if (document.readyState === 'loading') {
        document.addEventListener('DOMContentLoaded', init);
    } else {
        init();
    }

    // Export API
    window.YaDevLanguage = {
        init,
        setLanguage,
        getLanguage: () => currentLang,
        t,
        addTranslations,
        translatePage,
    };
})();
