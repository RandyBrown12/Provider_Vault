from django.shortcuts import render
from django.http import HttpResponse
from django.views.decorators.http import require_POST


# Create your views here.
def home(request):
    return render(request, "home.html")


def main_page(request):
    return render(request, "main_page.html")


def register(request):
    return render(request, "register.html")


@require_POST
def check_match(request):
    """
    View to check if two fields (e.g., password and confirm_password) match.
    Expects POST with 'password' and 'confirm_password'.
    """
    password = request.POST.get("password", "")
    confirm_password = request.POST.get("confirm_password", "")
    if not password or not confirm_password:
        return HttpResponse("Please enter a Password!", content_type="text/html")
    if password and confirm_password and password != confirm_password:
        return HttpResponse("Passwords do not match!", content_type="text/html")
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
