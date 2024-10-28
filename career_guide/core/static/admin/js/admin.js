document.addEventListener('DOMContentLoaded', function() {
    // Example function to handle feedback submission (if you implement a form submission)
    const feedbackForm = document.querySelector('#feedbackForm');
    if (feedbackForm) {
        feedbackForm.addEventListener('submit', function(event) {
            event.preventDefault(); // Prevent default form submission

            // Example of showing an alert
            alert('Thank you for your feedback!');

            // Clear the form (optional)
            feedbackForm.reset();
        });
    }
});
