/**
 * YADEV THEME SWITCHER PRO
 * Sistema avanzado de cambio de arquitectura + paleta
 */

(function() {
    'use strict';

    // Configuración de themes por sector
    const THEMES_CONFIG = {
        tecnologia: {
            name: 'Tecnología',
            themes: [
                { id: 'dark-tech', name: 'Dark Tech', colors: ['#0a0a0f', '#6366f1', '#22d3ee'] },
                { id: 'light-saas', name: 'Light SaaS', colors: ['#ffffff', '#2563eb', '#7c3aed'] },
                { id: 'cyberpunk-neon', name: 'Cyberpunk', colors: ['#0d0d0d', '#ff00ff', '#00ffff'] },
                { id: 'minimal-white', name: 'Minimal', colors: ['#ffffff', '#000000', '#525252'] }
            ]
        },
        salud: {
            name: 'Salud',
            themes: [
                { id: 'clinical-light', name: 'Clinical', colors: ['#ffffff', '#0891b2', '#14b8a6'] },
                { id: 'medical-blue', name: 'Medical Blue', colors: ['#f8fafc', '#1e40af', '#0284c7'] },
                { id: 'soft-pastel', name: 'Soft Pastel', colors: ['#fef7f7', '#ec4899', '#f472b6'] },
                { id: 'premium-hospital', name: 'Premium', colors: ['#fafaf9', '#b45309', '#d97706'] }
            ]
        },
        construccion: {
            name: 'Construcción',
            themes: [
                { id: 'industrial-dark', name: 'Industrial', colors: ['#18181b', '#f97316', '#fbbf24'] },
                { id: 'concrete-light', name: 'Concrete', colors: ['#f5f5f5', '#525252', '#f97316'] },
                { id: 'brutal-yellow', name: 'Brutal', colors: ['#000000', '#fbbf24', '#ffffff'] },
                { id: 'blueprint-blue', name: 'Blueprint', colors: ['#1e3a5f', '#ffffff', '#67e8f9'] }
            ]
        },
        transporte: {
            name: 'Transporte',
            themes: [
                { id: 'midnight-fleet', name: 'Midnight', colors: ['#0c1929', '#0ea5e9', '#06b6d4'] },
                { id: 'motion-red', name: 'Motion Red', colors: ['#ffffff', '#dc2626', '#f97316'] },
                { id: 'urban-gray', name: 'Urban Gray', colors: ['#f3f4f6', '#374151', '#6366f1'] },
                { id: 'neon-mobility', name: 'Neon', colors: ['#0a0a0a', '#00ff88', '#00d4ff'] }
            ]
        },
        electrico: {
            name: 'Eléctrico',
            themes: [
                { id: 'energy-yellow', name: 'Energy', colors: ['#ffffff', '#eab308', '#f59e0b'] },
                { id: 'neon-voltage', name: 'Neon Voltage', colors: ['#0a0a0a', '#ffee00', '#00ffff'] },
                { id: 'clean-tech', name: 'Clean Tech', colors: ['#f8fafc', '#059669', '#0891b2'] },
                { id: 'electrico-industrial', name: 'Industrial', colors: ['#1a1a1a', '#f59e0b', '#fbbf24'] }
            ]
        },
        forestal: {
            name: 'Forestal',
            themes: [
                { id: 'editorial-nature', name: 'Editorial', colors: ['#fafaf9', '#166534', '#65a30d'] },
                { id: 'forest-dark', name: 'Forest Dark', colors: ['#0a1510', '#22c55e', '#a3e635'] },
                { id: 'earth-minimal', name: 'Earth', colors: ['#faf7f5', '#78350f', '#a16207'] },
                { id: 'eco-vibrant', name: 'Eco Vibrant', colors: ['#f0fdf4', '#65a30d', '#22c55e'] }
            ]
        },
        ecommerce: {
            name: 'E-commerce',
            themes: [
                { id: 'conversion-purple', name: 'Conversion', colors: ['#faf5ff', '#7c3aed', '#ec4899'] },
                { id: 'minimal-luxury', name: 'Luxury', colors: ['#ffffff', '#0a0a0a', '#a3a3a3'] },
                { id: 'neon-shop', name: 'Neon Shop', colors: ['#0a0a0a', '#f43f5e', '#818cf8'] },
                { id: 'warm-commerce', name: 'Warm', colors: ['#fffbeb', '#ea580c', '#dc2626'] }
            ]
        }
    };

    // Arquitecturas disponibles
    const ARCHITECTURES = [
        { id: 'base', name: 'Base', icon: 'grid' },
        { id: 'editorial', name: 'Editorial', icon: 'newspaper' },
        { id: 'experimental', name: 'Experimental', icon: 'sparkles' },
        { id: 'structural', name: 'Structural', icon: 'building' }
    ];

    class YaDevThemeSwitcherPro {
        constructor() {
            this.sector = document.documentElement.dataset.industry || 'tecnologia';
            this.currentTheme = localStorage.getItem('yadev-theme') || null;
            this.currentArch = localStorage.getItem('yadev-arch') || 'base';
            this.isOpen = false;

            this.init();
        }

        init() {
            this.createSwitcher();
            this.bindEvents();
            this.applyStoredSettings();
        }

        createSwitcher() {
            const themes = THEMES_CONFIG[this.sector]?.themes || THEMES_CONFIG.tecnologia.themes;
            const sectorName = THEMES_CONFIG[this.sector]?.name || 'Tecnología';

            const switcher = document.createElement('div');
            switcher.className = 'theme-switcher-pro';
            switcher.innerHTML = `
                <button class="theme-switcher-pro__toggle" aria-label="Cambiar tema">
                    <svg fill="none" stroke="currentColor" viewBox="0 0 24 24">
                        <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M7 21a4 4 0 01-4-4V5a2 2 0 012-2h4a2 2 0 012 2v12a4 4 0 01-4 4zm0 0h12a2 2 0 002-2v-4a2 2 0 00-2-2h-2.343M11 7.343l1.657-1.657a2 2 0 012.828 0l2.829 2.829a2 2 0 010 2.828l-8.486 8.485M7 17h.01"/>
                    </svg>
                </button>
                <div class="theme-switcher-pro__panel">
                    <div class="theme-switcher-pro__header">
                        <div class="theme-switcher-pro__title">Design System</div>
                        <div class="theme-switcher-pro__subtitle">${sectorName}</div>
                    </div>
                    <div class="theme-switcher-pro__content">
                        <div class="theme-switcher-pro__section">
                            <div class="theme-switcher-pro__section-title">Paleta de Colores</div>
                            <div class="theme-switcher-pro__options" id="themeOptions">
                                ${themes.map(theme => `
                                    <button class="theme-switcher-pro__option" data-theme="${theme.id}">
                                        <div class="theme-switcher-pro__color-preview" style="background: linear-gradient(135deg, ${theme.colors[0]} 0%, ${theme.colors[1]} 50%, ${theme.colors[2]} 100%);"></div>
                                        <div class="theme-switcher-pro__option-name">${theme.name}</div>
                                    </button>
                                `).join('')}
                            </div>
                        </div>
                        <div class="theme-switcher-pro__section">
                            <div class="theme-switcher-pro__section-title">Arquitectura</div>
                            <div class="theme-switcher-pro__options" id="archOptions">
                                ${ARCHITECTURES.map(arch => `
                                    <button class="theme-switcher-pro__option" data-arch="${arch.id}">
                                        <div class="theme-switcher-pro__arch-icon">
                                            ${this.getArchIcon(arch.icon)}
                                        </div>
                                        <div class="theme-switcher-pro__option-name">${arch.name}</div>
                                    </button>
                                `).join('')}
                            </div>
                        </div>
                    </div>
                    <div class="theme-switcher-pro__footer">
                        <button class="theme-switcher-pro__btn theme-switcher-pro__btn--secondary" id="resetTheme">
                            Reset
                        </button>
                        <button class="theme-switcher-pro__btn theme-switcher-pro__btn--primary" id="applyTheme">
                            Aplicar
                        </button>
                    </div>
                </div>
            `;

            document.body.appendChild(switcher);
            this.element = switcher;
        }

        getArchIcon(type) {
            const icons = {
                grid: '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><rect x="3" y="3" width="7" height="7"/><rect x="14" y="3" width="7" height="7"/><rect x="3" y="14" width="7" height="7"/><rect x="14" y="14" width="7" height="7"/></svg>',
                newspaper: '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M19 20H5a2 2 0 01-2-2V6a2 2 0 012-2h10a2 2 0 012 2v1m2 13a2 2 0 01-2-2V7m2 13a2 2 0 002-2V9a2 2 0 00-2-2h-2m-4-3H9M7 16h6M7 8h6v4H7V8z"/></svg>',
                sparkles: '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M5 3v4M3 5h4M6 17v4m-2-2h4m5-16l2.286 6.857L21 12l-5.714 2.143L13 21l-2.286-6.857L5 12l5.714-2.143L13 3z"/></svg>',
                building: '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M19 21V5a2 2 0 00-2-2H7a2 2 0 00-2 2v16m14 0h2m-2 0h-5m-9 0H3m2 0h5M9 7h1m-1 4h1m4-4h1m-1 4h1m-5 10v-5a1 1 0 011-1h2a1 1 0 011 1v5m-4 0h4"/></svg>'
            };
            return icons[type] || icons.grid;
        }

        bindEvents() {
            // Toggle panel
            const toggle = this.element.querySelector('.theme-switcher-pro__toggle');
            toggle.addEventListener('click', () => this.togglePanel());

            // Theme options
            const themeOptions = this.element.querySelectorAll('[data-theme]');
            themeOptions.forEach(option => {
                option.addEventListener('click', () => {
                    this.selectTheme(option.dataset.theme);
                });
            });

            // Architecture options
            const archOptions = this.element.querySelectorAll('[data-arch]');
            archOptions.forEach(option => {
                option.addEventListener('click', () => {
                    this.selectArchitecture(option.dataset.arch);
                });
            });

            // Reset button
            const resetBtn = this.element.querySelector('#resetTheme');
            resetBtn.addEventListener('click', () => this.reset());

            // Apply button
            const applyBtn = this.element.querySelector('#applyTheme');
            applyBtn.addEventListener('click', () => this.apply());

            // Close on outside click
            document.addEventListener('click', (e) => {
                if (this.isOpen && !this.element.contains(e.target)) {
                    this.togglePanel();
                }
            });
        }

        togglePanel() {
            this.isOpen = !this.isOpen;
            this.element.classList.toggle('open', this.isOpen);
        }

        selectTheme(themeId) {
            this.currentTheme = themeId;

            // Update UI
            const options = this.element.querySelectorAll('[data-theme]');
            options.forEach(opt => {
                opt.classList.toggle('active', opt.dataset.theme === themeId);
            });

            // Preview immediately
            this.previewTheme(themeId);
        }

        selectArchitecture(archId) {
            this.currentArch = archId;

            // Update UI
            const options = this.element.querySelectorAll('[data-arch]');
            options.forEach(opt => {
                opt.classList.toggle('active', opt.dataset.arch === archId);
            });

            // Preview immediately
            this.previewArchitecture(archId);
        }

        previewArchitecture(archId) {
            // Remove previous architecture
            if (archId === 'base') {
                document.documentElement.removeAttribute('data-architecture');
            } else {
                document.documentElement.dataset.architecture = archId;
            }
        }

        previewTheme(themeId) {
            document.documentElement.dataset.theme = themeId;
        }

        apply() {
            // Save theme
            if (this.currentTheme) {
                localStorage.setItem('yadev-theme', this.currentTheme);
                document.documentElement.dataset.theme = this.currentTheme;
            }

            // Save architecture
            localStorage.setItem('yadev-arch', this.currentArch);
            if (this.currentArch === 'base') {
                document.documentElement.removeAttribute('data-architecture');
            } else {
                document.documentElement.dataset.architecture = this.currentArch;
            }

            this.togglePanel();

            // Show confirmation
            this.showToast('Tema aplicado correctamente');

            // Trigger custom event for other scripts
            window.dispatchEvent(new CustomEvent('yadev-theme-change', {
                detail: { theme: this.currentTheme, architecture: this.currentArch }
            }));
        }

        showToast(message) {
            const toast = document.createElement('div');
            toast.className = 'yadev-toast';
            toast.textContent = message;
            toast.style.cssText = `
                position: fixed;
                bottom: 24px;
                left: 50%;
                transform: translateX(-50%);
                background: var(--accent, #6366f1);
                color: white;
                padding: 12px 24px;
                border-radius: 8px;
                font-size: 14px;
                font-weight: 500;
                z-index: 10000;
                animation: toast-in 0.3s ease;
            `;
            document.body.appendChild(toast);

            setTimeout(() => {
                toast.style.animation = 'toast-out 0.3s ease forwards';
                setTimeout(() => toast.remove(), 300);
            }, 2000);
        }

        reset() {
            localStorage.removeItem('yadev-theme');
            localStorage.removeItem('yadev-arch');

            document.documentElement.removeAttribute('data-theme');
            document.documentElement.removeAttribute('data-architecture');

            this.currentTheme = null;
            this.currentArch = 'base';

            // Clear active states
            this.element.querySelectorAll('.active').forEach(el => {
                el.classList.remove('active');
            });

            // Set base arch as active
            const baseArch = this.element.querySelector('[data-arch="base"]');
            if (baseArch) baseArch.classList.add('active');
        }

        applyStoredSettings() {
            if (this.currentTheme) {
                document.documentElement.dataset.theme = this.currentTheme;
                const themeOption = this.element.querySelector(`[data-theme="${this.currentTheme}"]`);
                if (themeOption) themeOption.classList.add('active');
            }

            if (this.currentArch) {
                document.documentElement.dataset.architecture = this.currentArch;
                const archOption = this.element.querySelector(`[data-arch="${this.currentArch}"]`);
                if (archOption) archOption.classList.add('active');
            }
        }
    }

    // Auto-init when DOM is ready
    if (document.readyState === 'loading') {
        document.addEventListener('DOMContentLoaded', () => new YaDevThemeSwitcherPro());
    } else {
        new YaDevThemeSwitcherPro();
    }

    // Export for manual use
    window.YaDevThemeSwitcherPro = YaDevThemeSwitcherPro;

})();
