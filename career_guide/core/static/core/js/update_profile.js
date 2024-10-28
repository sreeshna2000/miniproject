// static/js/scripts.js
document.addEventListener('DOMContentLoaded', function() {
    const form = document.querySelector('form');
    const username = document.querySelector('input[name="username"]');
    const email = document.querySelector('input[name="email"]');
    const qualification = document.querySelector('input[name="qualification"]');
    const age = document.querySelector('input[name="age"]');
    const location = document.querySelector('input[name="location"]');

    form.addEventListener('submit', function(event) {
        // Simple form validation
        if (username.value === "" || email.value === "" || qualification.value === "" || age.value === "" || location.value === "") {
            alert("Please fill in all fields.");
            event.preventDefault();  // Prevent form submission if validation fails
        }
    });
});
