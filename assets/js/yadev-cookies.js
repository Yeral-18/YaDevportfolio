/* ============================================
   YaDev UI - Cookie Consent Manager
   Premium cookie consent with preferences
   ============================================ */

(function() {
    'use strict';

    const COOKIE_NAME = 'yadev_cookie_consent';
    const COOKIE_EXPIRY_DAYS = 365;

    // Default configuration
    const defaultConfig = {
        privacyUrl: '#',
        termsUrl: '#',
        companyName: 'nuestra empresa',
        onAccept: null,
        onReject: null,
        onSave: null
    };

    let config = { ...defaultConfig };

    // Cookie utilities
    const CookieUtils = {
        set(name, value, days) {
            const expires = new Date();
            expires.setTime(expires.getTime() + days * 24 * 60 * 60 * 1000);
            document.cookie = `${name}=${JSON.stringify(value)};expires=${expires.toUTCString()};path=/;SameSite=Lax`;
        },

        get(name) {
            const match = document.cookie.match(new RegExp('(^| )' + name + '=([^;]+)'));
            if (match) {
                try {
                    return JSON.parse(match[2]);
                } catch (e) {
                    return null;
                }
            }
            return null;
        },

        remove(name) {
            document.cookie = `${name}=;expires=Thu, 01 Jan 1970 00:00:00 GMT;path=/`;
        }
    };

    // Create modal HTML
    function createModal() {
        const modalHTML = `
            <div class="cookie-overlay" id="cookieOverlay"></div>
            <div class="cookie-modal" id="cookieModal" role="dialog" aria-labelledby="cookieTitle" aria-modal="true">
                <h2 class="cookie-modal__title" id="cookieTitle">Gestionar Cookies</h2>
                <p class="cookie-modal__content">
                    Utilizamos cookies para mejorar la experiencia en nuestro sitio web. Al hacer clic en
                    'Aceptar', usted está otorgando su consentimiento para el uso de cookies de acuerdo
                    con nuestros <a href="${config.termsUrl}" target="_blank">Términos de Uso</a> y
                    <a href="${config.privacyUrl}" target="_blank">Política de Privacidad</a>.
                    Si desea ajustar sus preferencias de cookies puede hacer clic en 'Configurar Cookies'.
                </p>

                <div class="cookie-modal__buttons">
                    <button class="cookie-btn cookie-btn--primary" id="cookieAcceptAll">
                        Aceptar
                    </button>
                    <button class="cookie-btn cookie-btn--secondary" id="cookieConfigure">
                        Configurar Cookies
                    </button>
                </div>

                <div class="cookie-settings" id="cookieSettings">
                    <div class="cookie-option">
                        <div class="cookie-option__info">
                            <div class="cookie-option__label">Cookies Esenciales</div>
                            <div class="cookie-option__desc">Necesarias para el funcionamiento del sitio</div>
                        </div>
                        <label class="cookie-toggle">
                            <input type="checkbox" checked disabled data-cookie="essential">
                            <span class="cookie-toggle__slider"></span>
                        </label>
                    </div>

                    <div class="cookie-option">
                        <div class="cookie-option__info">
                            <div class="cookie-option__label">Cookies Analíticas</div>
                            <div class="cookie-option__desc">Nos ayudan a entender cómo usa el sitio</div>
                        </div>
                        <label class="cookie-toggle">
                            <input type="checkbox" data-cookie="analytics">
                            <span class="cookie-toggle__slider"></span>
                        </label>
                    </div>

                    <div class="cookie-option">
                        <div class="cookie-option__info">
                            <div class="cookie-option__label">Cookies de Marketing</div>
                            <div class="cookie-option__desc">Permiten mostrarte publicidad relevante</div>
                        </div>
                        <label class="cookie-toggle">
                            <input type="checkbox" data-cookie="marketing">
                            <span class="cookie-toggle__slider"></span>
                        </label>
                    </div>

                    <div class="cookie-option">
                        <div class="cookie-option__info">
                            <div class="cookie-option__label">Cookies Funcionales</div>
                            <div class="cookie-option__desc">Mejoran la funcionalidad y personalización</div>
                        </div>
                        <label class="cookie-toggle">
                            <input type="checkbox" data-cookie="functional">
                            <span class="cookie-toggle__slider"></span>
                        </label>
                    </div>

                    <button class="cookie-btn cookie-btn--primary cookie-btn--save" id="cookieSavePrefs">
                        Guardar Preferencias
                    </button>
                </div>
            </div>
        `;

        const container = document.createElement('div');
        container.id = 'yadevCookieConsent';
        container.innerHTML = modalHTML;
        document.body.appendChild(container);
    }

    // Show modal
    function showModal() {
        const overlay = document.getElementById('cookieOverlay');
        const modal = document.getElementById('cookieModal');

        if (overlay && modal) {
            overlay.classList.add('active');
            modal.classList.add('active');
            document.body.style.overflow = 'hidden';

            // Focus trap
            modal.querySelector('button').focus();
        }
    }

    // Hide modal
    function hideModal() {
        const overlay = document.getElementById('cookieOverlay');
        const modal = document.getElementById('cookieModal');

        if (overlay && modal) {
            overlay.classList.remove('active');
            modal.classList.remove('active');
            document.body.style.overflow = '';
        }
    }

    // Toggle settings panel
    function toggleSettings() {
        const settings = document.getElementById('cookieSettings');
        const configBtn = document.getElementById('cookieConfigure');

        if (settings) {
            settings.classList.toggle('active');
            configBtn.textContent = settings.classList.contains('active')
                ? 'Ocultar Opciones'
                : 'Configurar Cookies';
        }
    }

    // Accept all cookies
    function acceptAll() {
        const preferences = {
            essential: true,
            analytics: true,
            marketing: true,
            functional: true,
            timestamp: Date.now()
        };

        CookieUtils.set(COOKIE_NAME, preferences, COOKIE_EXPIRY_DAYS);
        hideModal();

        if (typeof config.onAccept === 'function') {
            config.onAccept(preferences);
        }

        // Enable Google Analytics if present
        enableAnalytics();
    }

    // Save preferences
    function savePreferences() {
        const preferences = {
            essential: true, // Always true
            analytics: document.querySelector('[data-cookie="analytics"]')?.checked || false,
            marketing: document.querySelector('[data-cookie="marketing"]')?.checked || false,
            functional: document.querySelector('[data-cookie="functional"]')?.checked || false,
            timestamp: Date.now()
        };

        CookieUtils.set(COOKIE_NAME, preferences, COOKIE_EXPIRY_DAYS);
        hideModal();

        if (typeof config.onSave === 'function') {
            config.onSave(preferences);
        }

        // Enable analytics if accepted
        if (preferences.analytics) {
            enableAnalytics();
        }
    }

    // Enable Google Analytics
    function enableAnalytics() {
        if (typeof gtag === 'function') {
            gtag('consent', 'update', {
                'ad_storage': 'granted',
                'analytics_storage': 'granted'
            });
        }
    }

    // Check if consent exists
    function hasConsent() {
        return CookieUtils.get(COOKIE_NAME) !== null;
    }

    // Get current preferences
    function getPreferences() {
        return CookieUtils.get(COOKIE_NAME);
    }

    // Initialize event listeners
    function initEvents() {
        document.getElementById('cookieAcceptAll')?.addEventListener('click', acceptAll);
        document.getElementById('cookieConfigure')?.addEventListener('click', toggleSettings);
        document.getElementById('cookieSavePrefs')?.addEventListener('click', savePreferences);
        document.getElementById('cookieOverlay')?.addEventListener('click', function(e) {
            if (e.target === this) {
                // Optional: close on overlay click
                // hideModal();
            }
        });

        // ESC key to close (optional)
        document.addEventListener('keydown', function(e) {
            if (e.key === 'Escape') {
                const modal = document.getElementById('cookieModal');
                if (modal?.classList.contains('active')) {
                    // hideModal(); // Uncomment if you want ESC to close
                }
            }
        });
    }

    // Initialize
    function init(userConfig = {}) {
        config = { ...defaultConfig, ...userConfig };

        // Only show if no consent given yet
        if (!hasConsent()) {
            createModal();
            initEvents();

            // Small delay for smooth animation
            setTimeout(showModal, 500);
        } else {
            // Apply saved preferences
            const prefs = getPreferences();
            if (prefs?.analytics) {
                enableAnalytics();
            }
        }
    }

    // Public API
    window.YaDevCookies = {
        init,
        show: showModal,
        hide: hideModal,
        hasConsent,
        getPreferences,
        reset: function() {
            CookieUtils.remove(COOKIE_NAME);
            location.reload();
        }
    };

    // Auto-init if data attribute present
    document.addEventListener('DOMContentLoaded', function() {
        const autoInit = document.querySelector('[data-yadev-cookies]');
        if (autoInit) {
            init({
                privacyUrl: autoInit.dataset.privacyUrl || '#',
                termsUrl: autoInit.dataset.termsUrl || '#'
            });
        }
    });

})();
