// register_placeholder.js

// Get the input elements
const usernameInput = document.getElementById('usernameInput');
const emailInput = document.getElementById('emailInput');
const firstNameInput = document.getElementById('firstNameInput');
const lastNameInput = document.getElementById('lastNameInput');
const password1Input = document.getElementById('password1Input');
const password2Input = document.getElementById('password2Input');

// Set the initial placeholder text with dots
usernameInput.setAttribute('placeholder', 'Username');
emailInput.setAttribute('placeholder', 'Email');
firstNameInput.setAttribute('placeholder', 'First name');
lastNameInput.setAttribute('placeholder', 'Last name');
password1Input.setAttribute('placeholder', 'Password');
password2Input.setAttribute('placeholder', 'Confirm password');

// Function to clear placeholder on focus
function clearPlaceholder(event) {
    const inputField = event.target;
    inputField.setAttribute('placeholder', '');
}

// Function to set placeholder if field is empty on blur
function setPlaceholder(event) {
    const inputField = event.target;
    if (!inputField.value) {
        switch (inputField.id) {
            case 'usernameInput':
                inputField.setAttribute('placeholder', 'Username');
                break;
            case 'emailInput':
                inputField.setAttribute('placeholder', 'Email');
                break;
            case 'firstNameInput':
                inputField.setAttribute('placeholder', 'First name');
                break;
            case 'lastNameInput':
                inputField.setAttribute('placeholder', 'Last name');
                break;
            case 'password1Input':
                inputField.setAttribute('placeholder', 'Password');
                break;
            case 'password2Input':
                inputField.setAttribute('placeholder', 'Confirm password');
                break;
            default:
                break;
        }
    }
}

// Attach event listeners to the input fields
usernameInput.addEventListener('focus', clearPlaceholder);
usernameInput.addEventListener('blur', setPlaceholder);

emailInput.addEventListener('focus', clearPlaceholder);
emailInput.addEventListener('blur', setPlaceholder);

firstNameInput.addEventListener('focus', clearPlaceholder);
firstNameInput.addEventListener('blur', setPlaceholder);

lastNameInput.addEventListener('focus', clearPlaceholder);
lastNameInput.addEventListener('blur', setPlaceholder);

password1Input.addEventListener('focus', clearPlaceholder);
password1Input.addEventListener('blur', setPlaceholder);

password2Input.addEventListener('focus', clearPlaceholder);
password2Input.addEventListener('blur', setPlaceholder);
