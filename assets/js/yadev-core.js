/**
 * YaDev Core JavaScript
 * Sistema de interactividad compartido para el portafolio
 */

(function() {
    'use strict';

    // ========================================
    // Reveal on Scroll (Intersection Observer)
    // ========================================
    function initReveal() {
        const reveals = document.querySelectorAll('.reveal, .reveal-left, .reveal-right, .reveal-scale, .stagger-children');

        if (reveals.length === 0) return;

        const observer = new IntersectionObserver((entries) => {
            entries.forEach(entry => {
                if (entry.isIntersecting) {
                    entry.target.classList.add('active');
                    // Unobserve after animation to improve performance
                    observer.unobserve(entry.target);
                }
            });
        }, {
            threshold: 0.15,
            rootMargin: '0px 0px -50px 0px'
        });

        reveals.forEach(el => observer.observe(el));
    }

    // ========================================
    // Counter Animation
    // ========================================
    function initCounters() {
        const counters = document.querySelectorAll('.counter');

        if (counters.length === 0) return;

        const animateCounter = (counter) => {
            const target = parseInt(counter.getAttribute('data-target'), 10);
            const duration = parseInt(counter.getAttribute('data-duration'), 10) || 2000;
            const start = 0;
            const startTime = performance.now();

            const updateCounter = (currentTime) => {
                const elapsed = currentTime - startTime;
                const progress = Math.min(elapsed / duration, 1);

                // Easing function (ease-out-cubic)
                const easeOut = 1 - Math.pow(1 - progress, 3);
                const current = Math.floor(easeOut * target);

                counter.textContent = current.toLocaleString();

                if (progress < 1) {
                    requestAnimationFrame(updateCounter);
                } else {
                    counter.textContent = target.toLocaleString();
                }
            };

            requestAnimationFrame(updateCounter);
        };

        const observer = new IntersectionObserver((entries) => {
            entries.forEach(entry => {
                if (entry.isIntersecting) {
                    animateCounter(entry.target);
                    observer.unobserve(entry.target);
                }
            });
        }, { threshold: 0.5 });

        counters.forEach(counter => observer.observe(counter));
    }

    // ========================================
    // Navbar Scroll Effect
    // ========================================
    function initNavbar() {
        const navbar = document.querySelector('.navbar-animated');

        if (!navbar) return;

        const threshold = parseInt(navbar.getAttribute('data-scroll-threshold'), 10) || 50;
        let ticking = false;

        const updateNavbar = () => {
            if (window.scrollY > threshold) {
                navbar.classList.add('scrolled');
            } else {
                navbar.classList.remove('scrolled');
            }
            ticking = false;
        };

        window.addEventListener('scroll', () => {
            if (!ticking) {
                requestAnimationFrame(updateNavbar);
                ticking = true;
            }
        }, { passive: true });

        // Check initial state
        updateNavbar();
    }

    // ========================================
    // Mobile Menu Toggle
    // ========================================
    function initMobileMenu() {
        const toggleBtn = document.querySelector('[data-mobile-toggle]');
        const mobileMenu = document.querySelector('[data-mobile-menu]');
        const closeBtn = document.querySelector('[data-mobile-close]');
        const menuLinks = document.querySelectorAll('[data-mobile-menu] a');

        if (!toggleBtn || !mobileMenu) return;

        const openMenu = () => {
            mobileMenu.classList.add('active');
            document.body.style.overflow = 'hidden';
            toggleBtn.setAttribute('aria-expanded', 'true');
            if (toggleBtn.querySelector('.hamburger')) {
                toggleBtn.querySelector('.hamburger').classList.add('active');
            }
        };

        const closeMenu = () => {
            mobileMenu.classList.remove('active');
            document.body.style.overflow = '';
            toggleBtn.setAttribute('aria-expanded', 'false');
            if (toggleBtn.querySelector('.hamburger')) {
                toggleBtn.querySelector('.hamburger').classList.remove('active');
            }
        };

        toggleBtn.addEventListener('click', () => {
            if (mobileMenu.classList.contains('active')) {
                closeMenu();
            } else {
                openMenu();
            }
        });

        if (closeBtn) {
            closeBtn.addEventListener('click', closeMenu);
        }

        // Close menu when clicking a link
        menuLinks.forEach(link => {
            link.addEventListener('click', closeMenu);
        });

        // Close menu on escape key
        document.addEventListener('keydown', (e) => {
            if (e.key === 'Escape' && mobileMenu.classList.contains('active')) {
                closeMenu();
            }
        });

        // Close menu when clicking outside
        mobileMenu.addEventListener('click', (e) => {
            if (e.target === mobileMenu) {
                closeMenu();
            }
        });
    }

    // ========================================
    // Smooth Scroll to Anchors
    // ========================================
    function initSmoothScroll() {
        const links = document.querySelectorAll('a[href^="#"]:not([href="#"])');

        links.forEach(link => {
            link.addEventListener('click', (e) => {
                const targetId = link.getAttribute('href');
                const targetElement = document.querySelector(targetId);

                if (targetElement) {
                    e.preventDefault();

                    const navbar = document.querySelector('.navbar-animated');
                    const offset = navbar ? navbar.offsetHeight : 0;

                    const targetPosition = targetElement.getBoundingClientRect().top + window.scrollY - offset;

                    window.scrollTo({
                        top: targetPosition,
                        behavior: 'smooth'
                    });

                    // Update URL without jumping
                    history.pushState(null, null, targetId);
                }
            });
        });
    }

    // ========================================
    // Active Navigation Indicator
    // ========================================
    function initActiveNav() {
        const sections = document.querySelectorAll('section[id]');
        const navLinks = document.querySelectorAll('[data-nav-link]');

        if (sections.length === 0 || navLinks.length === 0) return;

        const observer = new IntersectionObserver((entries) => {
            entries.forEach(entry => {
                if (entry.isIntersecting) {
                    const id = entry.target.getAttribute('id');

                    navLinks.forEach(link => {
                        link.classList.remove('active');
                        if (link.getAttribute('href') === `#${id}`) {
                            link.classList.add('active');
                        }
                    });
                }
            });
        }, {
            threshold: 0.3,
            rootMargin: '-20% 0px -60% 0px'
        });

        sections.forEach(section => observer.observe(section));
    }

    // ========================================
    // Image Lazy Loading Enhancement
    // ========================================
    function initLazyImages() {
        const images = document.querySelectorAll('img[data-src]');

        if (images.length === 0) return;

        const loadImage = (img) => {
            const src = img.getAttribute('data-src');
            if (src) {
                img.src = src;
                img.removeAttribute('data-src');
                img.classList.add('loaded');
            }
        };

        if ('IntersectionObserver' in window) {
            const observer = new IntersectionObserver((entries) => {
                entries.forEach(entry => {
                    if (entry.isIntersecting) {
                        loadImage(entry.target);
                        observer.unobserve(entry.target);
                    }
                });
            }, { rootMargin: '50px' });

            images.forEach(img => observer.observe(img));
        } else {
            // Fallback for older browsers
            images.forEach(loadImage);
        }
    }

    // ========================================
    // Form Validation Helper
    // ========================================
    function initFormValidation() {
        const forms = document.querySelectorAll('[data-validate]');

        forms.forEach(form => {
            form.addEventListener('submit', (e) => {
                let isValid = true;
                const inputs = form.querySelectorAll('[required]');

                inputs.forEach(input => {
                    if (!input.value.trim()) {
                        isValid = false;
                        input.classList.add('error');
                    } else {
                        input.classList.remove('error');
                    }
                });

                if (!isValid) {
                    e.preventDefault();
                }
            });
        });
    }

    // ========================================
    // Scroll to Top Button
    // ========================================
    function initScrollTop() {
        const scrollBtn = document.querySelector('[data-scroll-top]');

        if (!scrollBtn) return;

        const toggleVisibility = () => {
            if (window.scrollY > 500) {
                scrollBtn.classList.add('visible');
            } else {
                scrollBtn.classList.remove('visible');
            }
        };

        window.addEventListener('scroll', toggleVisibility, { passive: true });

        scrollBtn.addEventListener('click', () => {
            window.scrollTo({
                top: 0,
                behavior: 'smooth'
            });
        });
    }

    // ========================================
    // Parallax Effect (performance optimized)
    // ========================================
    function initParallax() {
        const parallaxElements = document.querySelectorAll('[data-parallax]');

        if (parallaxElements.length === 0) return;

        let ticking = false;

        const updateParallax = () => {
            parallaxElements.forEach(el => {
                const speed = parseFloat(el.getAttribute('data-parallax')) || 0.5;
                const rect = el.getBoundingClientRect();

                if (rect.bottom > 0 && rect.top < window.innerHeight) {
                    const yPos = (rect.top - window.innerHeight) * speed;
                    el.style.transform = `translateY(${yPos}px)`;
                }
            });
            ticking = false;
        };

        window.addEventListener('scroll', () => {
            if (!ticking) {
                requestAnimationFrame(updateParallax);
                ticking = true;
            }
        }, { passive: true });
    }

    // ========================================
    // Initialize All
    // ========================================
    function init() {
        initReveal();
        initCounters();
        initNavbar();
        initMobileMenu();
        initSmoothScroll();
        initActiveNav();
        initLazyImages();
        initFormValidation();
        initScrollTop();
        initParallax();
    }

    // Run when DOM is ready
    if (document.readyState === 'loading') {
        document.addEventListener('DOMContentLoaded', init);
    } else {
        init();
    }

    // Expose YaDev namespace for external use
    window.YaDev = {
        init,
        initReveal,
        initCounters,
        initNavbar,
        initMobileMenu,
        initSmoothScroll,
        initActiveNav,
        initLazyImages,
        initFormValidation,
        initScrollTop,
        initParallax
    };

})();
