document.addEventListener('DOMContentLoaded', function() {
    const closeIcon = document.getElementById('close-icon');

    closeIcon.addEventListener('click', function() {
        const alertBox = document.getElementById('alert-box');
        alertBox.style.display = 'none';
    });
});