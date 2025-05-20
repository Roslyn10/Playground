// Preloader functionality
window.addEventListener('load', () => {
    const preloader = document.getElementById('preloader');
    preloader.style.display = 'none';
});

// Animate on Scroll
AOS.init({
    duration: 1000,
    once: true,
});