/**
 * YaDev UI - Preloader
 * Animación de carga elegante
 */

(function() {
    'use strict';

    const PRELOADER_TIMEOUT = 3000; // Max time to show preloader (ms)
    const MIN_DISPLAY_TIME = 800; // Minimum display time (ms)

    /**
     * Create and inject preloader HTML
     */
    function createPreloader() {
        // Check if preloader already exists
        if (document.querySelector('.yadev-preloader')) {
            return document.querySelector('.yadev-preloader');
        }

        // Get industry for custom styling
        const industry = document.documentElement.dataset.industry || 'default';

        // Get spinner style based on industry
        let spinnerHTML = '';
        switch (industry) {
            case 'electrico':
                spinnerHTML = `
                    <div class="preloader__spinner preloader__spinner--electric">
                        <svg fill="none" stroke="currentColor" viewBox="0 0 24 24">
                            <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M13 10V3L4 14h7v7l9-11h-7z"/>
                        </svg>
                    </div>
                `;
                break;
            case 'tecnologia':
                spinnerHTML = `
                    <div class="preloader__spinner preloader__spinner--dots">
                        <span></span><span></span><span></span>
                    </div>
                `;
                break;
            case 'construccion':
                spinnerHTML = `
                    <div class="preloader__spinner preloader__spinner--bars">
                        <span></span><span></span><span></span><span></span><span></span>
                    </div>
                `;
                break;
            default:
                spinnerHTML = `
                    <div class="preloader__spinner preloader__spinner--circle"></div>
                `;
        }

        // Create preloader element
        const preloader = document.createElement('div');
        preloader.className = 'yadev-preloader';
        preloader.innerHTML = `
            ${spinnerHTML}
            <div class="preloader__progress">
                <div class="preloader__progress-bar"></div>
            </div>
            <p class="preloader__text">Cargando...</p>
        `;

        // Insert at beginning of body
        document.body.insertBefore(preloader, document.body.firstChild);

        return preloader;
    }

    /**
     * Hide preloader with animation
     */
    function hidePreloader() {
        const preloader = document.querySelector('.yadev-preloader');
        if (!preloader) return;

        preloader.classList.add('hidden');

        // Remove from DOM after animation
        setTimeout(() => {
            preloader.remove();
        }, 500);
    }

    /**
     * Initialize preloader
     */
    function initPreloader() {
        // Check if preloader is disabled
        if (document.documentElement.dataset.preloader === 'false') {
            return;
        }

        // Only show preloader on demo pages (not index)
        const isDemo = document.documentElement.dataset.yadevCookies !== undefined;
        if (!isDemo) {
            return;
        }

        const preloader = createPreloader();
        const startTime = Date.now();

        // Function to check if page is loaded
        const checkLoaded = () => {
            const elapsed = Date.now() - startTime;
            const remaining = Math.max(0, MIN_DISPLAY_TIME - elapsed);

            setTimeout(hidePreloader, remaining);
        };

        // Hide on window load
        if (document.readyState === 'complete') {
            checkLoaded();
        } else {
            window.addEventListener('load', checkLoaded);
        }

        // Safety timeout
        setTimeout(hidePreloader, PRELOADER_TIMEOUT);
    }

    // Auto-init if not disabled
    if (document.documentElement.dataset.preloaderAuto !== 'false') {
        // Run immediately to create preloader before content renders
        if (document.readyState === 'loading') {
            document.addEventListener('DOMContentLoaded', initPreloader);
        } else {
            initPreloader();
        }
    }

    // Export for manual control
    window.YaDevPreloader = {
        create: createPreloader,
        hide: hidePreloader,
        init: initPreloader,
    };
})();
