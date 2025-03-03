from django.shortcuts import render,redirect
from django.urls import reverse
from django.http import HttpRequest,HttpResponse
# Create your views here.
def home_view(request:HttpRequest):
    response=render(request,"main/home.html")
    response.set_cookie("key","name",max_age=60*60*24)
    return response
def properties_view(request:HttpRequest):
    properties = [
        {"title" : "Villa Modern in Malqa", "image" : "villa1.jpg"},
        {"title" : "Great home for you in Rimal", "image" : "villa2.jpg"},
        {"title" : "Villa with 8 bedrooms in Swedey", "image" : "villa3.jpg"},
        {"title" : "Amazing Villa in Hitten", "image" : "villa4.jpg"},
    ]
    return render(request,"main/properties.html",context={"properties":properties})
def contact_view(request:HttpRequest):
    return render(request,"main/contact.html")
def drak_mode(request:HttpRequest):
    new_url = request.META.get('HTTP_REFERER', reverse("main:home_view"))
    response=redirect(new_url)
    response.set_cookie("screen","dark",max_age=60*60*24)
    return response
def light_mode(request:HttpRequest):
    new_url = request.META.get('HTTP_REFERER', reverse("main:home_view"))

    response=redirect(new_url)
    response.set_cookie("screen","light",max_age=-1)
    return response