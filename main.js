// Mobile Menu Toggle
const menuBtn = document.getElementById('menu-btn');
const mobileMenu = document.getElementById('mobile-menu');
const menuIcon = document.getElementById('menu-icon');

let isMenuOpen = false;

menuBtn.addEventListener('click', () => {
    isMenuOpen = !isMenuOpen;
    mobileMenu.classList.toggle('hidden');

    // Change icon
    if (isMenuOpen) {
        menuIcon.setAttribute('d', 'M6 18L18 6M6 6l12 12');
    } else {
        menuIcon.setAttribute('d', 'M4 6h16M4 12h16M4 18h16');
    }
});

// Close mobile menu when clicking a link
const mobileLinks = mobileMenu.querySelectorAll('a');
mobileLinks.forEach(link => {
    link.addEventListener('click', () => {
        mobileMenu.classList.add('hidden');
        isMenuOpen = false;
        menuIcon.setAttribute('d', 'M4 6h16M4 12h16M4 18h16');
    });
});

// Navbar background on scroll
const navbar = document.querySelector('nav');

window.addEventListener('scroll', () => {
    if (window.scrollY > 50) {
        navbar.classList.add('bg-darker/95');
        navbar.classList.remove('bg-darker/80');
    } else {
        navbar.classList.add('bg-darker/80');
        navbar.classList.remove('bg-darker/95');
    }
});

// Smooth reveal animation on scroll
const observerOptions = {
    root: null,
    rootMargin: '0px',
    threshold: 0.1
};

const observer = new IntersectionObserver((entries) => {
    entries.forEach(entry => {
        if (entry.isIntersecting) {
            entry.target.classList.add('animate-in');
        }
    });
}, observerOptions);

// Observe all sections
document.querySelectorAll('section').forEach(section => {
    section.style.opacity = '0';
    section.style.transform = 'translateY(20px)';
    section.style.transition = 'opacity 0.6s ease, transform 0.6s ease';
    observer.observe(section);
});

// Add animate-in styles
const style = document.createElement('style');
style.textContent = `
    .animate-in {
        opacity: 1 !important;
        transform: translateY(0) !important;
    }
`;
document.head.appendChild(style);

// Set first section visible immediately
document.getElementById('inicio').style.opacity = '1';
document.getElementById('inicio').style.transform = 'translateY(0)';
