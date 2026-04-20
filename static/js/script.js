document.addEventListener('DOMContentLoaded', function () {

    // Navbar Scroll Effect
    const navbar = document.getElementById('mainNavbar');

    // Check initial scroll position
    if (window.scrollY > 50) {
        navbar.classList.add('scrolled');
    }

    // Add scroll event listener
    window.addEventListener('scroll', function () {
        if (window.scrollY > 50) {
            navbar.classList.add('scrolled');
        } else {
            navbar.classList.remove('scrolled');
        }
    });

    // Add search listener
    const searchForm = document.querySelector('.custom-search-form');
    if (searchForm) {
        searchForm.addEventListener('submit', handleSearch);
    }

});

// Handle simple client-side search (redirects to dances or alerts based on keyword)
function handleSearch(event) {
    event.preventDefault();
    const input = document.getElementById('searchInput');
    if (!input || !input.value.trim()) return;

    const query = input.value.toLowerCase().trim();

    // Simple routing based on key phrases logic for this educational project
    if (query.includes('mokhibo') || query.includes('women')) {
        window.location.href = '/dance/1';
    } else if (query.includes('famo') || query.includes('music') || query.includes('accordion')) {
        window.location.href = '/dance/2';
    } else if (query.includes('mohobelo') || query.includes('men') || query.includes('kick')) {
        window.location.href = '/dance/3';
    } else if (query.includes('interview') || query.includes('people')) {
        window.location.href = '/interviews';
    } else if (query.includes('gallery') || query.includes('photo') || query.includes('image')) {
        window.location.href = '/gallery';
    } else {
        alert("No specific matching pages found for '" + query + "'. Try 'Mokhibo', 'Famo', or 'Mohobelo'.");
    }
}

// Global function to handle lightbox state, defined globally so onclick handlers in HTML can hit it
window.openLightbox = function (index) {
    if (typeof galleryItems !== 'undefined') {
        const item = galleryItems[index];
        if (item) {
            const modalImg = document.getElementById('lightboxImage');
            const modalCaption = document.getElementById('lightboxCaption');

            modalImg.src = item.src;
            modalCaption.innerText = item.caption;

            const modalEl = document.getElementById('lightboxModal');
            const modal = bootstrap.Modal.getOrCreateInstance(modalEl);
            modal.show();
        }
    } else {
        console.error("Gallery items not loaded properly for Lightbox functionality.");
    }
};
