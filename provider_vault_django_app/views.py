import json
from django.shortcuts import render
from django.http import HttpResponse
from django.views.decorators.http import require_POST
import psycopg2
import dotenv
import os
import bcrypt

dotenv.load_dotenv()


# Create your views here.
def home(request):
    return render(request, "home.html")


def main_page(request):
    return render(request, "main_page.html")


def register(request):
    return render(request, "register.html")


def login(request):
    return render(request, "login.html")


@require_POST
def login_to_database(request):
    """
    View to handle user login.

    Expects POST with 'email' and 'password'.
    """
    data = json.loads(request.body)
    email = data.get("email", "")
    password = data.get("password", "")

    if not email or not password:
        return HttpResponse(
            "Please enter both email and password!", content_type="text/html"
        )

    try:
        conn = psycopg2.connect(
            dbname=os.getenv("DB_NAME", ""),
            user=os.getenv("DB_USERNAME", ""),
            password=os.getenv("DB_PASSWORD", ""),
            host=os.getenv("DB_HOST", ""),
            port=os.getenv("DB_PORT", ""),
        )

        cursor = conn.cursor()

        query = "SELECT password_hash FROM users WHERE email = %s "
        cursor.execute(query, (email,))

        user_password_hash = cursor.fetchone()
        if not user_password_hash:
            return HttpResponse("Invalid email or password!", content_type="text/html")

        stored_password_hash = None
        if isinstance(user_password_hash[0], memoryview):
            stored_password_hash = user_password_hash[0].tobytes()
        else:
            stored_password_hash = user_password_hash[0]

        if bcrypt.checkpw(password.encode("utf-8"), stored_password_hash):
            cursor.close()
            conn.close()
            return HttpResponse("Passwords match!", content_type="text/html")
        else:
            cursor.close()
            conn.close()
            return HttpResponse("Incorrect password!", content_type="text/html")
    except Exception as e:
        cursor.close()
        conn.close()
        return HttpResponse(f"An error occurred: {str(e)}", content_type="text/html")


@require_POST
def register_to_database(request):
    """
    View to handle user registration.

    Expects POST with 'email' and 'password'.
    """
    data = json.loads(request.body)
    email = data.get("email", "")
    password = data.get("password", "")

    if not email or not password:
        return HttpResponse(
            "Please enter both email and password!", content_type="text/html"
        )

    try:
        conn = psycopg2.connect(
            dbname=os.getenv("DB_NAME", ""),
            user=os.getenv("DB_USERNAME", ""),
            password=os.getenv("DB_PASSWORD", ""),
            host=os.getenv("DB_HOST", ""),
            port=os.getenv("DB_PORT", ""),
        )

        cursor = conn.cursor()
        password_bytes = bytes(password, "utf-8")
        password_hash = bcrypt.hashpw(password_bytes, bcrypt.gensalt())

        query = (
            "INSERT INTO users (email, password_hash, user_type) VALUES (%s, %s, %s)"
        )
        cursor.execute(query, (email, password_hash, "user"))
        conn.commit()
        cursor.close()
        conn.close()
        return HttpResponse("Registration Successful!", content_type="text/html")
    except Exception as e:
        cursor.close()
        conn.close()
        return HttpResponse(f"An error occurred: {str(e)}", content_type="text/html")


@require_POST
def check_match(request):
    """
    View to check if two fields (e.g., password and confirm_password) match.
    Expects POST with 'password' and 'confirm_password'.
    """
    password = request.POST.get("password", "")
    confirm_password = request.POST.get("confirm_password", "")
    if password and confirm_password and password != confirm_password:
        return HttpResponse("Passwords do not match!", content_type="text/html")
    elif not password or not confirm_password:
        return HttpResponse("Please enter a Password!", content_type="text/html")
    return HttpResponse("", content_type="text/html")


@require_POST
def check_password(request):
    """
    View to validate password constraints.

    Constraints:
    - Minimum length of 8 characters
    - Must contain both uppercase and lowercase letters
    - Must include at least one number
    - Must include at least one special character (!@#$%^&*)

    Expects POST with 'password'.
    """
    password = request.POST.get("password", "")
    if not password:
        return HttpResponse("Please enter a Password!", content_type="text/html")
    elif len(password) < 8:
        return HttpResponse(
            "Password must be at least 8 characters long!", content_type="text/html"
        )
    elif not any(character.islower() for character in password) or not any(
        character.isupper() for character in password
    ):
        return HttpResponse(
            "Password must contain both uppercase and lowercase letters!",
            content_type="text/html",
        )
    elif not any(character.isdigit() for character in password):
        return HttpResponse(
            "Password must include at least one number!", content_type="text/html"
        )
    elif not any(character in "!@#$%^&*" for character in password):
        return HttpResponse(
            "Password must include at least one special character (!@#$%^&*)!",
            content_type="text/html",
        )
    return HttpResponse("", content_type="text/html")
