/**
 * YaDev UI - Template Switcher
 * Sistema para cambiar plantillas por sector
 */

(function() {
    'use strict';

    // Template configurations by industry
    const templates = {
        electrico: [
            {
                id: 'electrico-default',
                name: 'CertiPower Clásico',
                description: 'Diseño profesional con fondo blanco',
                colors: ['#ffcb36', '#1a1a1a', '#ffffff'],
                stylesheet: null,
            },
            {
                id: 'electrico-dark',
                name: 'Modo Oscuro',
                description: 'Dark mode corporativo completo',
                colors: ['#ffcb36', '#0d0d0d', '#1a1a1a'],
                stylesheet: 'electrico-dark.css',
            },
            {
                id: 'electrico-modern',
                name: 'ODIR Moderno',
                description: 'Bordes decorativos y cards con hover',
                colors: ['#ffcb36', '#ffffff', '#f5f5f5'],
                stylesheet: 'electrico-modern.css',
            },
            {
                id: 'electrico-corporate',
                name: 'Corporativo ENEL',
                description: 'Layout magazine, tipografía grande',
                colors: ['#ffcb36', '#0a0a0a', '#fafafa'],
                stylesheet: 'electrico-corporate.css',
            },
            {
                id: 'electrico-tech',
                name: 'Tech Futurista',
                description: 'Grid neón, efectos glitch',
                colors: ['#ffcb36', '#0a0a0f', '#1a1a25'],
                stylesheet: 'electrico-tech.css',
            },
            {
                id: 'electrico-dashboard',
                name: 'Dashboard Admin',
                description: 'Panel de control con métricas',
                colors: ['#fbbf24', '#1e293b', '#0f172a'],
                stylesheet: 'electrico-dashboard.css',
            },
        ],
        transporte: [
            {
                id: 'transporte-default',
                name: 'Logística Pro',
                description: 'Diseño azul cyan profesional',
                colors: ['#0284c7', '#06b6d4', '#ffffff'],
                stylesheet: null,
            },
                        {
                id: 'transporte-corporate',
                name: 'Corporativo',
                description: 'Estilo azul oscuro empresarial',
                colors: ['#1e40af', '#3b82f6', '#f8fafc'],
                stylesheet: 'transporte-corporate.css',
            },
            {
                id: 'transporte-modern',
                name: 'Moderno',
                description: 'Glassmorphism con ondas',
                colors: ['#06b6d4', '#0891b2', '#ffffff'],
                stylesheet: 'transporte-modern.css',
            },
            {
                id: 'transporte-split',
                name: 'Split Layout',
                description: 'Pantalla dividida 50/50 minimalista',
                colors: ['#0369a1', '#06b6d4', '#ffffff'],
                stylesheet: 'transporte-split.css',
            },
        ],
        construccion: [
            {
                id: 'construccion-default',
                name: 'Constructor',
                description: 'Diseño ámbar sólido',
                colors: ['#f59e0b', '#ea580c', '#ffffff'],
                stylesheet: null,
            },
            {
                id: 'construccion-industrial',
                name: 'Industrial',
                description: 'Estilo industrial oscuro',
                colors: ['#d97706', '#292524', '#fafaf9'],
                stylesheet: 'construccion-industrial.css',
            },
            {
                id: 'construccion-blueprint',
                name: 'Blueprint',
                description: 'Estilo planos arquitectónicos',
                colors: ['#1e40af', '#fbbf24', '#1e3a5f'],
                stylesheet: 'construccion-blueprint.css',
            },
            {
                id: 'construccion-brutalist',
                name: 'Brutalista',
                description: 'Tipografía gigante, bordes gruesos',
                colors: ['#fbbf24', '#000000', '#ffffff'],
                stylesheet: 'construccion-brutalist.css',
            },
        ],
        tecnologia: [
            {
                id: 'tecnologia-default',
                name: 'Tech Dark',
                description: 'Modo oscuro futurista',
                colors: ['#4f46e5', '#7c3aed', '#0f172a'],
                stylesheet: null,
            },
            {
                id: 'tecnologia-light',
                name: 'Tech Light',
                description: 'Modo claro minimalista',
                colors: ['#6366f1', '#818cf8', '#ffffff'],
                stylesheet: 'tecnologia-light.css',
            },
            {
                id: 'tecnologia-neon',
                name: 'Cyberpunk Neon',
                description: 'Efectos neón futuristas',
                colors: ['#00ff88', '#ff00ff', '#0a0a0a'],
                stylesheet: 'tecnologia-neon.css',
            },
            {
                id: 'tecnologia-neumorphic',
                name: 'Neumórfico',
                description: 'Soft UI con sombras suaves',
                colors: ['#5a67d8', '#e8eef4', '#d1d9e6'],
                stylesheet: 'tecnologia-neumorphic.css',
            },
        ],
        ecommerce: [
            {
                id: 'ecommerce-default',
                name: 'Shop Modern',
                description: 'Tienda moderna violeta',
                colors: ['#7c3aed', '#ec4899', '#ffffff'],
                stylesheet: null,
            },
            {
                id: 'ecommerce-dark',
                name: 'Shop Dark',
                description: 'Tienda premium oscura',
                colors: ['#7c3aed', '#ec4899', '#0f0f0f'],
                stylesheet: 'ecommerce-dark.css',
            },
            {
                id: 'ecommerce-minimal',
                name: 'Minimal',
                description: 'Diseño minimalista limpio',
                colors: ['#000000', '#ffffff', '#fafafa'],
                stylesheet: 'ecommerce-minimal.css',
            },
            {
                id: 'ecommerce-magazine',
                name: 'Magazine Editorial',
                description: 'Estilo revista con tipografía serif',
                colors: ['#e11d48', '#1a1a1a', '#f5f5f0'],
                stylesheet: 'ecommerce-magazine.css',
            },
        ],
        forestal: [
            {
                id: 'forestal-default',
                name: 'Eco Natural',
                description: 'Diseño verde orgánico',
                colors: ['#10b981', '#22c55e', '#ffffff'],
                stylesheet: null,
            },
            {
                id: 'forestal-organic',
                name: 'Orgánico',
                description: 'Estilo papel y tierra',
                colors: ['#065f46', '#92400e', '#faf7f2'],
                stylesheet: 'forestal-organic.css',
            },
            {
                id: 'forestal-dark',
                name: 'Bosque Nocturno',
                description: 'Modo oscuro natural',
                colors: ['#10b981', '#34d399', '#0c1810'],
                stylesheet: 'forestal-dark.css',
            },
            {
                id: 'forestal-immersive',
                name: 'Inmersivo',
                description: 'Full-screen parallax storytelling',
                colors: ['#059669', '#10b981', '#ecfdf5'],
                stylesheet: 'forestal-immersive.css',
            },
        ],
        salud: [
            {
                id: 'salud-default',
                name: 'Medical Pro',
                description: 'Limpio y profesional cyan',
                colors: ['#0891b2', '#2dd4bf', '#ffffff'],
                stylesheet: null,
            },
            {
                id: 'salud-clean',
                name: 'Ultra Limpio',
                description: 'Minimalista médico',
                colors: ['#0891b2', '#f0fdfa', '#ffffff'],
                stylesheet: 'salud-clean.css',
            },
            {
                id: 'salud-hospital',
                name: 'Hospital',
                description: 'Institucional azul/rojo',
                colors: ['#0369a1', '#dc2626', '#f0f9ff'],
                stylesheet: 'salud-hospital.css',
            },
            {
                id: 'salud-glass',
                name: 'Glassmorphism',
                description: 'Cristal difuminado y transparencias',
                colors: ['#06b6d4', '#14b8a6', '#f0fdfa'],
                stylesheet: 'salud-glass.css',
            },
        ],
    };

    let currentTemplate = null;
    let isOpen = false;

    /**
     * Get current industry from HTML data attribute
     */
    function getCurrentIndustry() {
        return document.documentElement.dataset.industry || 'default';
    }

    /**
     * Get templates for current industry
     */
    function getTemplates() {
        const industry = getCurrentIndustry();
        return templates[industry] || [];
    }

    /**
     * Create template switcher HTML
     */
    function createSwitcher() {
        const industry = getCurrentIndustry();
        const industryTemplates = getTemplates();

        if (industryTemplates.length <= 1) {
            return; // No need for switcher with only one template
        }

        // Get saved template or use first one
        currentTemplate = localStorage.getItem(`yadev-template-${industry}`) || industryTemplates[0]?.id;

        const switcher = document.createElement('div');
        switcher.className = 'template-switcher';
        switcher.innerHTML = `
            <button class="template-switcher__toggle" aria-label="Cambiar plantilla">
                <svg fill="none" stroke="currentColor" viewBox="0 0 24 24">
                    <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M7 21a4 4 0 01-4-4V5a2 2 0 012-2h4a2 2 0 012 2v12a4 4 0 01-4 4zm0 0h12a2 2 0 002-2v-4a2 2 0 00-2-2h-2.343M11 7.343l1.657-1.657a2 2 0 012.828 0l2.829 2.829a2 2 0 010 2.828l-8.486 8.485M7 17h.01"/>
                </svg>
            </button>
            <div class="template-switcher__panel">
                <div class="template-switcher__header">
                    <h3 class="template-switcher__title">
                        <svg fill="none" stroke="currentColor" viewBox="0 0 24 24">
                            <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M4 5a1 1 0 011-1h14a1 1 0 011 1v2a1 1 0 01-1 1H5a1 1 0 01-1-1V5zM4 13a1 1 0 011-1h6a1 1 0 011 1v6a1 1 0 01-1 1H5a1 1 0 01-1-1v-6zM16 13a1 1 0 011-1h2a1 1 0 011 1v6a1 1 0 01-1 1h-2a1 1 0 01-1-1v-6z"/>
                        </svg>
                        Plantillas
                    </h3>
                </div>
                <div class="template-switcher__industry">
                    Sector: ${industry.charAt(0).toUpperCase() + industry.slice(1)}
                </div>
                <div class="template-switcher__options">
                    ${industryTemplates.map(t => `
                        <div class="template-option ${t.id === currentTemplate ? 'active' : ''}" data-template="${t.id}">
                            <div class="template-option__colors">
                                ${t.colors.map(c => `<span style="background:${c}"></span>`).join('')}
                            </div>
                            <div class="template-option__info">
                                <div class="template-option__name">${t.name}</div>
                                <div class="template-option__desc">${t.description}</div>
                            </div>
                            <div class="template-option__check">
                                <svg fill="none" stroke="currentColor" viewBox="0 0 24 24">
                                    <path stroke-linecap="round" stroke-linejoin="round" stroke-width="3" d="M5 13l4 4L19 7"/>
                                </svg>
                            </div>
                        </div>
                    `).join('')}
                </div>
                <div class="template-switcher__footer">
                    <a href="../index.html">
                        <svg class="w-4 h-4" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                            <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M10 19l-7-7m0 0l7-7m-7 7h18"/>
                        </svg>
                        Ver más sectores
                    </a>
                </div>
            </div>
        `;

        document.body.appendChild(switcher);
        console.log('Template switcher button added to DOM');

        // Add transition overlay
        const overlay = document.createElement('div');
        overlay.className = 'template-transition';
        document.body.appendChild(overlay);

        // Setup event listeners
        setupEventListeners(switcher, overlay);

        // Apply saved template
        applyTemplate(currentTemplate, false);

        // Verify button is visible
        const btn = switcher.querySelector('.template-switcher__toggle');
        if (btn) {
            const rect = btn.getBoundingClientRect();
            console.log('Template button position:', rect);
        }
    }

    /**
     * Setup event listeners
     */
    function setupEventListeners(switcher, overlay) {
        const toggle = switcher.querySelector('.template-switcher__toggle');
        const options = switcher.querySelectorAll('.template-option');

        // Toggle panel
        toggle.addEventListener('click', () => {
            isOpen = !isOpen;
            switcher.classList.toggle('open', isOpen);
        });

        // Close on outside click
        document.addEventListener('click', (e) => {
            if (isOpen && !switcher.contains(e.target)) {
                isOpen = false;
                switcher.classList.remove('open');
            }
        });

        // Template selection
        options.forEach(option => {
            option.addEventListener('click', () => {
                const templateId = option.dataset.template;
                if (templateId !== currentTemplate) {
                    changeTemplate(templateId, overlay, switcher);
                }
            });
        });

        // Keyboard navigation
        document.addEventListener('keydown', (e) => {
            if (e.key === 'Escape' && isOpen) {
                isOpen = false;
                switcher.classList.remove('open');
            }
        });
    }

    /**
     * Change template with animation
     */
    function changeTemplate(templateId, overlay, switcher) {
        // Start transition
        overlay.classList.add('active');

        setTimeout(() => {
            // Apply new template
            applyTemplate(templateId, true);

            // Update UI
            const options = switcher.querySelectorAll('.template-option');
            options.forEach(opt => {
                opt.classList.toggle('active', opt.dataset.template === templateId);
            });

            currentTemplate = templateId;

            // Save preference
            const industry = getCurrentIndustry();
            localStorage.setItem(`yadev-template-${industry}`, templateId);

            // End transition
            setTimeout(() => {
                overlay.classList.remove('active');
                overlay.classList.add('exit');
                setTimeout(() => {
                    overlay.classList.remove('exit');
                }, 500);
            }, 300);
        }, 500);
    }

    /**
     * Apply template stylesheet
     */
    function applyTemplate(templateId, animate) {
        const industry = getCurrentIndustry();
        const industryTemplates = templates[industry] || [];
        const template = industryTemplates.find(t => t.id === templateId);

        if (!template) return;

        // Remove existing template stylesheet
        const existingLink = document.querySelector('link[data-template-style]');
        if (existingLink) {
            existingLink.remove();
        }

        // Add new stylesheet if needed
        if (template.stylesheet) {
            const link = document.createElement('link');
            link.rel = 'stylesheet';
            link.href = `../assets/css/templates/${template.stylesheet}`;
            link.dataset.templateStyle = templateId;
            document.head.appendChild(link);
        }

        // Update body class
        document.body.className = document.body.className.replace(/template-\S+/g, '');
        document.body.classList.add(`template-${templateId}`);

        // Dispatch event
        document.dispatchEvent(new CustomEvent('templateChanged', {
            detail: { template: templateId, industry }
        }));

        console.log(`Template changed to: ${templateId}`);
    }

    /**
     * Initialize
     */
    function init() {
        const html = document.documentElement;
        const industry = html.dataset.industry;

        // Check if on demo page (has data-industry attribute)
        if (!industry) {
            return;
        }

        // Get templates for this industry, default to empty array
        const industryTemplates = templates[industry] || [];

        // Only show switcher if there are multiple templates
        if (industryTemplates.length > 1) {
            createSwitcher();
        }
    }

    // Auto-init on DOM ready with retry
    function tryInit() {
        if (document.body) {
            init();
        } else {
            setTimeout(tryInit, 50);
        }
    }

    if (document.readyState === 'loading') {
        document.addEventListener('DOMContentLoaded', tryInit);
    } else {
        tryInit();
    }

    // Export API
    window.YaDevTemplateSwitcher = {
        init,
        getTemplates,
        getCurrentTemplate: () => currentTemplate,
        applyTemplate,
    };
})();
