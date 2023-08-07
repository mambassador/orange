// login_placeholder.js

// Get the username and password input elements
const usernameInput = document.getElementById('usernameInput');
const passwordInput = document.getElementById('passwordInput');

// Set the initial placeholder text with dots
usernameInput.setAttribute('placeholder', 'Username');
passwordInput.setAttribute('placeholder', '••••••••');

// Show actual input when the user starts typing (Username field)
usernameInput.addEventListener('focus', function() {
    usernameInput.setAttribute('placeholder', '');
});

// Show dots again when the input loses focus and is empty (Username field)
usernameInput.addEventListener('blur', function() {
    if (!usernameInput.value) {
        usernameInput.setAttribute('placeholder', 'Username');
    }
});

// Show actual input when the user starts typing (Password field)
passwordInput.addEventListener('focus', function() {
    passwordInput.setAttribute('placeholder', '');
});

// Show dots again when the input loses focus and is empty (Password field)
passwordInput.addEventListener('blur', function() {
    if (!passwordInput.value) {
        passwordInput.setAttribute('placeholder', '••••••••');
    }
});
