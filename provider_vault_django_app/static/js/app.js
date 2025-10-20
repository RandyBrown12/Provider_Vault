async function register_user() {
    const firstName = document.getElementById('first_name').value;
    const lastName = document.getElementById('last_name').value;
    const email = document.getElementById('email').value;
    const password = document.getElementById('register_password').value;
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

    if(password !== confirmPassword) {
        window.alert('Password & Confirm Password does not match!');
        return;
    }

    const response_json = await register_to_database(email, password);

    if(response_json.message === "Registration Successful!") {
        window.location.href = "/login"
    } else {
        window.alert(`${response_json.message}`);
    }
}

async function login_user() {
    const email = document.getElementById('email').value;
    const password = document.getElementById('login_password').value;

    if (!email) {
        window.alert('There is no Email Inputted!');
        return;
    } else if (!password) {
        window.alert('There is no Password Inputted!');
        return;
    }

    const response_json = await login_to_database(email, password);

    if(response_json.message === "Passwords match!") {
        window.location.href = `/auth/?token=${response_json.token}`;
    } else {
        const login_error_element = document.getElementById('login_form_error');
        login_error_element.innerText = response_json.message;
    }
}

async function register_to_database(email, password) {
    try
    {
        const response = await fetch("/register_to_database/", {
            method: "POST",
            headers: {
                "Content-Type": "application/json",
                "X-CSRFToken": getCookie("csrftoken")
            },
            body: JSON.stringify({
                email: email,
                password: password
            })
        });

        if(!response.ok) {
            throw new Error("4XX or 5XX error");
        }

        const data = await response.json();
        return data;
    } catch (error) {
        console.log("Fetch error:", error.message);
    }
}

async function login_to_database(email, password) {
    try
    {
        const response = await fetch("/login_to_database/", {
            method: "POST",
            headers: {
                "Content-Type": "application/json",
                "X-CSRFToken": getCookie("csrftoken")
            },
            body: JSON.stringify({
                email: email,
                password: password
            })
        });

        if(!response.ok) {
            throw new Error("4XX or 5XX error");
        }

        const data = await response.json();
        return data;
    } catch (error) {
        console.log("Fetch error:", error.message);
    }
}

function getCookie(name) {
  const value = `; ${document.cookie}`;
  const parts = value.split(`; ${name}=`);
  if (parts.length === 2) return parts.pop().split(";").shift();
}

const csrftoken = getCookie("csrftoken");

function show_password_toggle(password_input_id, password_icon_id) {
    const password_element = document.getElementById(password_input_id);
    const password_icon = document.getElementById(password_icon_id);

    if(!password_element) {
        window.alert(`Password input id: ${password_input_id} not found!`)
        return
    } else if (!password_icon) {
        window.alert(`Password icon id: ${password_icon_id} not found!`)
        return
    }

    if(password_element.type === "password") {
        password_element.type = "text";
        password_icon.src = "/static/img/eye-off.svg";
    } else {
        password_element.type = "password";
        password_icon.src = "/static/img/eye.svg";
    }

}
