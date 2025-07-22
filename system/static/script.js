document.addEventListener('DOMContentLoaded', function() {
    // Auto-focus search input
    const searchInput = document.querySelector('input[name="query"]');
    if (searchInput) {
        searchInput.focus();
    }
    
    // Animate stats cards
    const stats = document.querySelectorAll('.stat-card');
    stats.forEach((stat, index) => {
        setTimeout(() => {
            stat.style.opacity = 1;
            stat.style.transform = 'translateY(0)';
        }, index * 200);
    });
});