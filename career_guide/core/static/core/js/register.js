// Simple client-side form validation
document.addEventListener("DOMContentLoaded", function() {
    const form = document.querySelector("form");
    form.addEventListener("submit", function(event) {
        const username = document.querySelector("#id_username");
        const email = document.querySelector("#id_email");
        const password1 = document.querySelector("#id_password1");
        const password2 = document.querySelector("#id_password2");

        if (username.value === "") {
            alert("Please enter your username.");
            event.preventDefault();  // Prevent form submission
        }

        if (email.value === "") {
            alert("Please enter your email.");
            event.preventDefault();
        }

        if (password1.value !== password2.value) {
            alert("Passwords do not match!");
            event.preventDefault();
        }
    });
});
