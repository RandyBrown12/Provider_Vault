"""
URL configuration for provider_vault_django project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""

from django.urls import path
from .views import check_match, check_password, home, login, main_page, register

urlpatterns = [
    path("", home, name="home"),
    path("main_page/", main_page, name="main_page"),
    path("register/", register, name="register"),
    path("login/", login, name="login"),
    path(
        "check_match/", check_match, name="check_match"
    ),  # HTMX endpoint for element text matching
    path(
        "check_password/", check_password, name="check_password"
    ),  # HTMX endpoint for password validation
]
