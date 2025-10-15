import json
from django.shortcuts import render
from django.http import HttpResponse
from django.views.decorators.http import require_POST
import dotenv
from .models import Users

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


def auth(request):
    return render(request, "auth_page.html")


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

    check_password_requirements_message = check_password_requirements(password)
    if check_password_requirements_message != "":
        return HttpResponse(
            check_password_requirements_message, content_type="text/html"
        )

    try:
        user = Users.objects.filter(email=email).first()

        if user is None:
            return HttpResponse("Invalid email or password!", content_type="text/html")

        if user.check_password(password):
            return HttpResponse("Passwords match!", content_type="text/html")
        else:
            return HttpResponse("Incorrect password!", content_type="text/html")
    except Exception as e:
        print(str(e))
        return HttpResponse("An error occurred", content_type="text/html")


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
        user = Users.objects.create_user(email=email, user_type="User")
        user.set_password(password)
        user.save()
        return HttpResponse("Registration Successful!", content_type="text/html")
    except Exception as e:
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

    Expects POST with 'password'.
    """

    password = request.POST.get("password", "")
    check_password_requirements_message = check_password_requirements(password)
    return HttpResponse(check_password_requirements_message, content_type="text/html")


def check_password_requirements(password) -> str:
    """
    Helper function to validate password constraints.

    Returns a string with the error message if any constraint is violated,
    otherwise returns an empty string.
    """
    if len(password) < 8:
        return "Password must be at least 8 characters long!"
    elif not any(character.islower() for character in password) or not any(
        character.isupper() for character in password
    ):
        return "Password must contain both uppercase and lowercase letters!"
    elif not any(character.isdigit() for character in password):
        return "Password must include at least one number!"
    elif not any(character in "!@#$%^&*" for character in password):
        return "Password must include at least one special character (!@#$%^&*)!"

    return ""
