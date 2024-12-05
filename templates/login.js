document.addEventListener('DOMContentLoaded', function() {
    const loginForm = document.querySelector('.login-form');
    const welcomeMessage = document.getElementById('welcomeMessage');

    loginForm.addEventListener('submit', function(e) {
        e.preventDefault();

        // Show welcome message
        welcomeMessage.classList.add('show');

        // After showing welcome message, submit the form
        setTimeout(() => {
            this.submit();
        }, 2000);
    });
});