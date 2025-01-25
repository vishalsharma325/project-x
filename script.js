// Smooth Scroll on Navigation
document.querySelectorAll('nav a').forEach(anchor => {
    anchor.addEventListener('click', function (e) {
        e.preventDefault();

        document.querySelector(this.getAttribute('href')).scrollIntoView({
            behavior: 'smooth',
            block: 'start'
        });
    });
});

// Button Animation on Hover
const ctaBtn = document.querySelector('.cta-btn');
ctaBtn.addEventListener('mouseover', () => {
    ctaBtn.style.transform = 'scale(1.1)';
});

ctaBtn.addEventListener('mouseout', () => {
    ctaBtn.style.transform = 'scale(1)';
});
