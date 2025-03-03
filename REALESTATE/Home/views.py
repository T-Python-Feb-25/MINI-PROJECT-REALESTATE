from lib2to3.fixes.fix_input import context
from urllib import response

from django.shortcuts import render

# Create your views here.


from django.shortcuts import render,redirect
from django.http import HttpRequest, HttpResponse
# Create your views here.

def get_mode(request):
    return request.COOKIES.get("mode", "light")

def home_view(request: HttpRequest):
    return render(request, "Home/homepage.html", {"mode": get_mode(request)})

def properties_view(request: HttpRequest):

    properties = [
    {"title": "Villa Modern in Malqa", "image": "villa1.jpg"},
    {"title": "Great home for you in Rimal", "image": "villa2.jpg"},
    {"title": "Villa with 8 bedrooms in Swedey", "image": "villa3.jpg"},
    {"title": "Amazing Villa in Hitten", "image": "villa4.jpg"}
    ]

    return render(request, "Home/Properties.html",{"properties": properties, "mode": get_mode(request)})

def contact_view(request: HttpRequest):
    return render(request, "Home/Contact.html", {"mode": get_mode(request)})

def About_view(request: HttpRequest):
    return render(request, "Home/About.html", {"mode": get_mode(request)})

def Services_view(request: HttpRequest):
    return render(request, "Home/Services.html", {"mode": get_mode(request)})

def dark_mode_view(request: HttpRequest):
    response = redirect(request.META.get('HTTP_REFERER', '/'))
    response.set_cookie("mode", "dark", max_age=60*60*24*7)
    return response

def light_mode_view(request: HttpRequest):
    response = redirect(request.META.get('HTTP_REFERER', '/'))
    response.set_cookie("mode", "light", max_age=60*60*24*7)
    return response
