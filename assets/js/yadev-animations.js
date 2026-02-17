/**
 * YaDev UI - Sistema de Animaciones Avanzadas
 * Scroll reveal, parallax, contadores, carruseles
 */

(function() {
    'use strict';

    // ===== SCROLL REVEAL SYSTEM =====
    class ScrollReveal {
        constructor() {
            this.elements = document.querySelectorAll('[data-reveal], .reveal');
            this.options = {
                threshold: 0.15,
                rootMargin: '0px 0px -50px 0px'
            };
            this.init();
        }

        init() {
            if (!this.elements.length) return;

            if ('IntersectionObserver' in window) {
                this.observer = new IntersectionObserver((entries) => {
                    entries.forEach(entry => {
                        if (entry.isIntersecting) {
                            entry.target.classList.add('revealed', 'visible');
                            // Unobserve after revealing
                            this.observer.unobserve(entry.target);
                        }
                    });
                }, this.options);

                this.elements.forEach(el => this.observer.observe(el));
            } else {
                // Fallback for older browsers
                this.elements.forEach(el => el.classList.add('revealed', 'visible'));
            }
        }
    }

    // ===== PARALLAX EFFECT =====
    class ParallaxEffect {
        constructor() {
            this.elements = document.querySelectorAll('[data-parallax]');
            this.ticking = false;
            this.init();
        }

        init() {
            if (!this.elements.length) return;
            window.addEventListener('scroll', () => this.onScroll(), { passive: true });
        }

        onScroll() {
            if (!this.ticking) {
                requestAnimationFrame(() => {
                    this.updatePositions();
                    this.ticking = false;
                });
                this.ticking = true;
            }
        }

        updatePositions() {
            const scrollY = window.pageYOffset;

            this.elements.forEach(el => {
                const speed = parseFloat(el.dataset.parallax) || 0.5;
                const rect = el.getBoundingClientRect();
                const elementTop = rect.top + scrollY;
                const offset = (scrollY - elementTop) * speed;

                el.style.transform = `translateY(${offset}px)`;
            });
        }
    }

    // ===== COUNTER ANIMATION =====
    class CounterAnimation {
        constructor() {
            this.counters = document.querySelectorAll('[data-counter], .counter');
            this.options = {
                threshold: 0.5
            };
            this.init();
        }

        init() {
            if (!this.counters.length) return;

            if ('IntersectionObserver' in window) {
                this.observer = new IntersectionObserver((entries) => {
                    entries.forEach(entry => {
                        if (entry.isIntersecting) {
                            this.animateCounter(entry.target);
                            this.observer.unobserve(entry.target);
                        }
                    });
                }, this.options);

                this.counters.forEach(counter => this.observer.observe(counter));
            } else {
                this.counters.forEach(counter => this.animateCounter(counter));
            }
        }

        animateCounter(element) {
            const target = parseInt(element.dataset.counter || element.textContent.replace(/\D/g, ''));
            const duration = parseInt(element.dataset.duration) || 2000;
            const suffix = element.dataset.suffix || '';
            const prefix = element.dataset.prefix || '';
            const start = 0;
            const startTime = performance.now();

            const updateCounter = (currentTime) => {
                const elapsed = currentTime - startTime;
                const progress = Math.min(elapsed / duration, 1);

                // Easing function (easeOutExpo)
                const easeProgress = progress === 1 ? 1 : 1 - Math.pow(2, -10 * progress);
                const current = Math.round(start + (target - start) * easeProgress);

                element.textContent = prefix + current.toLocaleString() + suffix;

                if (progress < 1) {
                    requestAnimationFrame(updateCounter);
                }
            };

            requestAnimationFrame(updateCounter);
        }
    }

    // ===== NAVBAR SCROLL EFFECT =====
    class NavbarScroll {
        constructor() {
            this.navbar = document.querySelector('.navbar-animated, .navbar');
            this.scrollThreshold = 50;
            this.init();
        }

        init() {
            if (!this.navbar) return;
            window.addEventListener('scroll', () => this.onScroll(), { passive: true });
            this.onScroll(); // Initial check
        }

        onScroll() {
            if (window.pageYOffset > this.scrollThreshold) {
                this.navbar.classList.add('scrolled', 'top-nav-collapse');
            } else {
                this.navbar.classList.remove('scrolled', 'top-nav-collapse');
            }
        }
    }

    // ===== SMOOTH SCROLL =====
    class SmoothScroll {
        constructor() {
            this.links = document.querySelectorAll('a[href^="#"]');
            this.init();
        }

        init() {
            this.links.forEach(link => {
                link.addEventListener('click', (e) => this.scrollTo(e));
            });
        }

        scrollTo(e) {
            const href = e.currentTarget.getAttribute('href');
            if (href === '#' || href === '#!') return;

            const target = document.querySelector(href);
            if (target) {
                e.preventDefault();
                const navbar = document.querySelector('.navbar-animated, .navbar');
                const offset = navbar ? navbar.offsetHeight : 0;
                const top = target.getBoundingClientRect().top + window.pageYOffset - offset;

                window.scrollTo({
                    top: top,
                    behavior: 'smooth'
                });
            }
        }
    }

    // ===== ACTIVE SECTION INDICATOR =====
    class ActiveSection {
        constructor() {
            this.sections = document.querySelectorAll('section[id]');
            this.navLinks = document.querySelectorAll('.navbar-animated a[href^="#"], .navbar a[href^="#"]');
            this.init();
        }

        init() {
            if (!this.sections.length || !this.navLinks.length) return;
            window.addEventListener('scroll', () => this.updateActive(), { passive: true });
        }

        updateActive() {
            const scrollY = window.pageYOffset;
            const navbar = document.querySelector('.navbar-animated, .navbar');
            const offset = navbar ? navbar.offsetHeight + 100 : 100;

            this.sections.forEach(section => {
                const top = section.offsetTop - offset;
                const bottom = top + section.offsetHeight;
                const id = section.getAttribute('id');

                if (scrollY >= top && scrollY < bottom) {
                    this.navLinks.forEach(link => {
                        link.classList.remove('active');
                        if (link.getAttribute('href') === `#${id}`) {
                            link.classList.add('active');
                        }
                    });
                }
            });
        }
    }

    // ===== PRELOADER =====
    class Preloader {
        constructor() {
            this.preloader = document.querySelector('.preloader, #preloader');
            this.init();
        }

        init() {
            if (!this.preloader) return;

            window.addEventListener('load', () => {
                setTimeout(() => {
                    this.preloader.classList.add('hidden');
                    document.body.style.overflow = 'visible';
                }, 500);
            });
        }
    }

    // ===== SCROLL PROGRESS BAR =====
    class ScrollProgress {
        constructor() {
            this.createProgressBar();
            this.init();
        }

        createProgressBar() {
            const existing = document.querySelector('.scroll-progress');
            if (existing) {
                this.progressBar = existing;
                return;
            }

            this.progressBar = document.createElement('div');
            this.progressBar.className = 'scroll-progress';
            this.progressBar.style.cssText = `
                position: fixed;
                top: 0;
                left: 0;
                height: 4px;
                background: var(--color-primary, #ffcb36);
                z-index: 10000;
                width: 0%;
                transition: width 0.1s ease;
            `;
            document.body.appendChild(this.progressBar);
        }

        init() {
            window.addEventListener('scroll', () => this.updateProgress(), { passive: true });
        }

        updateProgress() {
            const scrollTop = window.pageYOffset;
            const docHeight = document.documentElement.scrollHeight - window.innerHeight;
            const progress = (scrollTop / docHeight) * 100;
            this.progressBar.style.width = `${progress}%`;
        }
    }

    // ===== TILT EFFECT (3D Card) =====
    class TiltEffect {
        constructor() {
            this.cards = document.querySelectorAll('.card-tilt, [data-tilt]');
            this.init();
        }

        init() {
            this.cards.forEach(card => {
                card.addEventListener('mousemove', (e) => this.onMove(e, card));
                card.addEventListener('mouseleave', (e) => this.onLeave(e, card));
            });
        }

        onMove(e, card) {
            const rect = card.getBoundingClientRect();
            const x = e.clientX - rect.left;
            const y = e.clientY - rect.top;
            const centerX = rect.width / 2;
            const centerY = rect.height / 2;
            const rotateX = (y - centerY) / 10;
            const rotateY = (centerX - x) / 10;

            card.style.transform = `perspective(1000px) rotateX(${rotateX}deg) rotateY(${rotateY}deg)`;
        }

        onLeave(e, card) {
            card.style.transform = 'perspective(1000px) rotateX(0) rotateY(0)';
        }
    }

    // ===== TYPED TEXT EFFECT =====
    class TypedText {
        constructor() {
            this.elements = document.querySelectorAll('[data-typed]');
            this.init();
        }

        init() {
            this.elements.forEach(el => {
                const text = el.dataset.typed;
                const speed = parseInt(el.dataset.typedSpeed) || 100;
                this.typeText(el, text, speed);
            });
        }

        typeText(element, text, speed) {
            let i = 0;
            element.textContent = '';

            const type = () => {
                if (i < text.length) {
                    element.textContent += text.charAt(i);
                    i++;
                    setTimeout(type, speed);
                }
            };

            // Start typing when element is visible
            const observer = new IntersectionObserver((entries) => {
                entries.forEach(entry => {
                    if (entry.isIntersecting) {
                        type();
                        observer.unobserve(entry.target);
                    }
                });
            });
            observer.observe(element);
        }
    }

    // ===== MOBILE MENU TOGGLE =====
    class MobileMenu {
        constructor() {
            this.toggle = document.querySelector('.mobile-menu-toggle, [data-menu-toggle]');
            this.menu = document.querySelector('.mobile-menu, .navbar-collapse, [data-menu]');
            this.init();
        }

        init() {
            if (!this.toggle || !this.menu) return;

            this.toggle.addEventListener('click', () => {
                this.toggle.classList.toggle('active');
                this.menu.classList.toggle('active');
                this.menu.classList.toggle('show');
                document.body.classList.toggle('menu-open');
            });
        }
    }

    // ===== BACK TO TOP BUTTON =====
    class BackToTop {
        constructor() {
            this.createButton();
            this.init();
        }

        createButton() {
            const existing = document.querySelector('.back-to-top, #nekoToTop');
            if (existing) {
                this.button = existing;
                return;
            }

            this.button = document.createElement('button');
            this.button.className = 'back-to-top';
            this.button.innerHTML = `
                <svg width="24" height="24" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2">
                    <path d="M18 15l-6-6-6 6"/>
                </svg>
            `;
            this.button.style.cssText = `
                position: fixed;
                bottom: 100px;
                right: 20px;
                width: 50px;
                height: 50px;
                border-radius: 50%;
                background: var(--color-primary, #ffcb36);
                color: #000;
                border: none;
                cursor: pointer;
                display: none;
                align-items: center;
                justify-content: center;
                z-index: 999;
                transition: all 0.3s ease;
                box-shadow: 0 4px 15px rgba(0,0,0,0.2);
            `;
            document.body.appendChild(this.button);
        }

        init() {
            window.addEventListener('scroll', () => {
                if (window.pageYOffset > 300) {
                    this.button.style.display = 'flex';
                } else {
                    this.button.style.display = 'none';
                }
            }, { passive: true });

            this.button.addEventListener('click', () => {
                window.scrollTo({ top: 0, behavior: 'smooth' });
            });
        }
    }

    // ===== STAGGER ANIMATION =====
    class StaggerAnimation {
        constructor() {
            this.containers = document.querySelectorAll('[data-stagger-container]');
            this.init();
        }

        init() {
            this.containers.forEach(container => {
                const items = container.querySelectorAll('[data-stagger-item]');
                items.forEach((item, index) => {
                    item.style.transitionDelay = `${index * 0.1}s`;
                });
            });
        }
    }

    // ===== INITIALIZE ALL =====
    function init() {
        // Wait for DOM
        if (document.readyState === 'loading') {
            document.addEventListener('DOMContentLoaded', initAll);
        } else {
            initAll();
        }
    }

    function initAll() {
        new ScrollReveal();
        new ParallaxEffect();
        new CounterAnimation();
        new NavbarScroll();
        new SmoothScroll();
        new ActiveSection();
        new Preloader();
        new ScrollProgress();
        new TiltEffect();
        new TypedText();
        new MobileMenu();
        new BackToTop();
        new StaggerAnimation();

        console.log('YaDev Animations initialized');
    }

    init();

    // Export for external use
    window.YaDevAnimations = {
        ScrollReveal,
        ParallaxEffect,
        CounterAnimation,
        NavbarScroll,
        SmoothScroll,
        reinit: initAll
    };
})();
