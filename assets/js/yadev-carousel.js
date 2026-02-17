/**
 * YaDev UI - Premium Carousels
 * Inicialización y configuración de Swiper.js
 */

(function() {
    'use strict';

    // Wait for Swiper to be available
    function initCarousels() {
        if (typeof Swiper === 'undefined') {
            console.warn('Swiper.js not loaded');
            return;
        }

        // Testimonials Carousel
        const testimonialCarousels = document.querySelectorAll('.testimonials-carousel');
        testimonialCarousels.forEach(el => {
            new Swiper(el, {
                slidesPerView: 1,
                spaceBetween: 30,
                loop: true,
                autoplay: {
                    delay: 5000,
                    disableOnInteraction: false,
                },
                pagination: {
                    el: '.swiper-pagination',
                    clickable: true,
                },
                navigation: {
                    nextEl: '.swiper-button-next',
                    prevEl: '.swiper-button-prev',
                },
                breakpoints: {
                    640: {
                        slidesPerView: 2,
                    },
                    1024: {
                        slidesPerView: 3,
                    },
                },
            });
        });

        // Clients/Logos Carousel
        const clientsCarousels = document.querySelectorAll('.clients-carousel');
        clientsCarousels.forEach(el => {
            new Swiper(el, {
                slidesPerView: 2,
                spaceBetween: 20,
                loop: true,
                autoplay: {
                    delay: 3000,
                    disableOnInteraction: false,
                },
                breakpoints: {
                    480: {
                        slidesPerView: 3,
                    },
                    768: {
                        slidesPerView: 4,
                    },
                    1024: {
                        slidesPerView: 5,
                    },
                    1280: {
                        slidesPerView: 6,
                    },
                },
            });
        });

        // Projects/Gallery Carousel
        const projectCarousels = document.querySelectorAll('.projects-carousel');
        projectCarousels.forEach(el => {
            new Swiper(el, {
                slidesPerView: 1,
                spaceBetween: 30,
                loop: true,
                effect: 'coverflow',
                centeredSlides: true,
                coverflowEffect: {
                    rotate: 0,
                    stretch: 0,
                    depth: 100,
                    modifier: 2,
                    slideShadows: false,
                },
                pagination: {
                    el: '.swiper-pagination',
                    clickable: true,
                },
                navigation: {
                    nextEl: '.swiper-button-next',
                    prevEl: '.swiper-button-prev',
                },
                breakpoints: {
                    768: {
                        slidesPerView: 2,
                    },
                    1024: {
                        slidesPerView: 3,
                    },
                },
            });
        });

        // Team Carousel
        const teamCarousels = document.querySelectorAll('.team-carousel');
        teamCarousels.forEach(el => {
            new Swiper(el, {
                slidesPerView: 1,
                spaceBetween: 30,
                loop: true,
                pagination: {
                    el: '.swiper-pagination',
                    clickable: true,
                },
                navigation: {
                    nextEl: '.swiper-button-next',
                    prevEl: '.swiper-button-prev',
                },
                breakpoints: {
                    640: {
                        slidesPerView: 2,
                    },
                    768: {
                        slidesPerView: 3,
                    },
                    1024: {
                        slidesPerView: 4,
                    },
                },
            });
        });

        // Hero Carousel (Full Width)
        const heroCarousels = document.querySelectorAll('.hero-carousel');
        heroCarousels.forEach(el => {
            new Swiper(el, {
                slidesPerView: 1,
                loop: true,
                effect: 'fade',
                fadeEffect: {
                    crossFade: true,
                },
                autoplay: {
                    delay: 6000,
                    disableOnInteraction: false,
                },
                pagination: {
                    el: '.swiper-pagination',
                    clickable: true,
                },
                on: {
                    slideChangeTransitionStart: function() {
                        // Animate content on slide change
                        const activeSlide = this.slides[this.activeIndex];
                        const content = activeSlide.querySelector('.hero-content');
                        if (content) {
                            content.style.opacity = '0';
                            content.style.transform = 'translateY(30px)';
                        }
                    },
                    slideChangeTransitionEnd: function() {
                        const activeSlide = this.slides[this.activeIndex];
                        const content = activeSlide.querySelector('.hero-content');
                        if (content) {
                            content.style.transition = 'all 0.6s ease';
                            content.style.opacity = '1';
                            content.style.transform = 'translateY(0)';
                        }
                    },
                },
            });
        });

        // Generic Auto-init for [data-carousel]
        const genericCarousels = document.querySelectorAll('[data-carousel]');
        genericCarousels.forEach(el => {
            const config = el.dataset.carousel;
            let options = {
                slidesPerView: 1,
                spaceBetween: 20,
                pagination: {
                    el: '.swiper-pagination',
                    clickable: true,
                },
            };

            // Parse custom options from data attribute
            if (config && config !== 'true') {
                try {
                    options = { ...options, ...JSON.parse(config) };
                } catch (e) {
                    console.warn('Invalid carousel config:', config);
                }
            }

            new Swiper(el, options);
        });

        console.log('YaDev Carousels initialized');
    }

    // Initialize on DOM ready
    if (document.readyState === 'loading') {
        document.addEventListener('DOMContentLoaded', initCarousels);
    } else {
        initCarousels();
    }

    // Export for manual initialization
    window.YaDevCarousel = {
        init: initCarousels,
    };
})();
