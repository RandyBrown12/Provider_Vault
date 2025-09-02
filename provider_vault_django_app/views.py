from django.http import HttpResponse
from django.shortcuts import render


# Create your views here.
def home(request):
    return render(request, "home.html")


def application(request):
    return render(request, "application.html")


def get_element(request):
    value = request.GET.get("value", None)

    if value is None:
        return HttpResponse("Invalid value", status=400)

    value = int(value)
    if value is None:
        return HttpResponse("Value is not a number!", status=400)

    value += 1
    return HttpResponse(value)
