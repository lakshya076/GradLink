function validateForm() {
    const form = document.getElementById('registrationForm');
    const password = document.getElementById('password');
    const repeatPassword = document.getElementById('repeatPassword');
    let isValid = true;

    form.querySelectorAll('input[required], select[required]').forEach((input) => {
        if (!input.value) {
            input.classList.add('error'); // Add red outline if empty
            console.log(`Field ${input.name} is empty.`); // Debugging output
            isValid = false;
        } else {
            input.classList.remove('error'); // Remove red outline if filled
        }
    });

    // Check if passwords match
    if ((password.value && repeatPassword.value && (password.value !== repeatPassword.value)) ||
        (password.value === "" && repeatPassword.value === "") ||
        (password.value === "" & repeatPassword.value !== "") ||
        (password.value !== "" && repeatPassword.value === "")) {
        password.classList.add('error');
        repeatPassword.classList.add('error');
        console.log("Passwords do not match."); // Debugging output
        isValid = false;
    } else {
        password.classList.remove('error');
        repeatPassword.classList.remove('error');
    }

    if (isValid) {
        console.log("Form OK");
        form.submit();
    }
}

function togglePasswordVisibility() {
    const passwordInput = document.getElementById("password");
    const icon = document.querySelector(".password-toggle-text");

    // Toggle password visibility
    if (passwordInput.type === "password") {
        passwordInput.type = "text";
        icon.textContent = "Hide Password";
    } else {
        passwordInput.type = "password";
        icon.textContent = "See Password";
    }
}

function toggleRepeatPasswordVisibility() {
    const repeatPasswordInput = document.getElementById("repeatPassword");
    const icon = document.querySelector(".repeat-password-toggle-text");

    // Toggle password visibility
    if (repeatPasswordInput.type === "password") {
        repeatPasswordInput.type = "text";
        icon.textContent = "Hide Password";
    } else {
        repeatPasswordInput.type = "password";
        icon.textContent = "See Password";
    }
}


const startYear = 1980;
const endYear = 2040;
const yearDropdown = document.getElementById("grad_year");

for (let year = startYear; year <= endYear; year++) {
    let option = document.createElement("option");
    option.value = year;
    option.textContent = year;
    yearDropdown.appendChild(option);
}