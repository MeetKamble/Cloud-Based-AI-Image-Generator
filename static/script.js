// script.js
document.addEventListener('DOMContentLoaded', function () {
    const form = document.getElementById('generateForm');
    const loadingScreen = document.getElementById('loadingScreen');

    form.addEventListener('submit', function (event) {
        loadingScreen.style.display = 'block'; // Show the loading screen
    });
});
document.addEventListener('DOMContentLoaded', function () {
    const cards = document.querySelectorAll('.card');

    cards.forEach(card => {
        card.addEventListener('click', function () {
            const downloadUrl = this.getAttribute('data-download-url');
            if (downloadUrl) {
                window.location.href = downloadUrl;
            }
        });
    });
});
document.addEventListener('DOMContentLoaded', () => {
    // Get the buttons
    const downloadBtn = document.getElementById('downloadBtn');
    const backBtn = document.getElementById('backBtn');

    // Get the image path and homepage URL from button data attributes
    const imagePath = downloadBtn.getAttribute('data-image-path');
    const homepageUrl = backBtn.getAttribute('data-homepage-url');

    // Download button functionality
    downloadBtn.addEventListener('click', () => {
        // Create a temporary link element to trigger the download
        const link = document.createElement('a');
        link.href = imagePath;
        link.download = imagePath.split('/').pop(); // Set the filename for download
        document.body.appendChild(link);
        link.click();
        document.body.removeChild(link);
    });

    // Back to homepage button functionality
    backBtn.addEventListener('click', () => {
        window.location.href = homepageUrl;
    });
});

