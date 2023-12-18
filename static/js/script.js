document.addEventListener("DOMContentLoaded", () => {
    let sections = document.querySelectorAll('section');
    let footer = document.querySelector('footer');

    let elements = [...sections, footer];

    const observer = new IntersectionObserver(entries => {
        entries.forEach(entry => {
            entry.target.classList.toggle("show-animation", entry.isIntersecting);
        });
    });

    elements.forEach( element => {
        observer.observe(element);
    });
});
