function register_user() {
    const firstName = document.getElementById('first_name').value;
    const lastName = document.getElementById('last_name').value;
    const email = document.getElementById('email').value;
    const password = document.getElementById('password').value;
    const confirmPassword = document.getElementById('confirm_password').value;
    const password_error_message = document.getElementById('password_check_msg').innerText;
    const confirm_password_error_message = document.getElementById('password_match_msg').innerText;

    if(password_error_message || confirm_password_error_message) {
        window.alert('There are error messages displayed. Please fix these issues');
        return;
    }

    if (!firstName) {
        window.alert('There is no First Name Inputted!');
        return;
    } else if (!lastName) {
        window.alert('There is no Last Name Inputted!');
        return;
    } else if (!email) {
        window.alert('There is no Email Inputted!');
        return;
    } else if (!password) {
        window.alert('There is no Password Inputted!');
        return;
    } else if (!confirmPassword) {
        window.alert('There is no Confirm Password Inputted!');
        return;
    }

    // Check Passwords
    if(password !== confirmPassword) {
        window.alert('Password & Confirm Password does not match!');
        return;
    }

    window.alert('Registration Complete!');
}
