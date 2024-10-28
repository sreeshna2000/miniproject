// Show a confirmation alert after profile update
document.addEventListener('DOMContentLoaded', function() {
    const form = document.querySelector('form');

    form.addEventListener('submit', function(event) {
        event.preventDefault();  // Prevent the default form submission behavior

        // Simulate form submission (you should handle this with AJAX or server response)
        alert('Profile successfully updated!');

        // After showing the alert, submit the form
        form.submit();
    });
});
