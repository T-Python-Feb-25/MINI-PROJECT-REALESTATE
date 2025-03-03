from django.shortcuts import render
from django.http import HttpRequest, HttpResponse

# Create your views here.


def index_view(request: HttpRequest):
    context = {
        'background_image': 'rul(/static/images/home-bg.jpg)'
    }

    return render(request, "main/index.html", context)


def light_mode(request: HttpRequest):
    context = {
        'background_image': 'rul(/static/images/skyscraper.jpg)'
    }

    return render(request, "main/light_mode.html", context)


def dark_mode(request: HttpRequest):
    context = {
        'background_image': 'rul(/static/images/skyscraper-dark.jpg)'
    }
    return render(request, "main/dark_mode.html", context)


def properties(request: HttpRequest):

    return render(request, "main/properties.html")


def contact(request: HttpRequest):
    context = {
        'background_image': 'rul(/static/images/email.jpg)'
    }

    return render(request, "main/contact.html", context)
