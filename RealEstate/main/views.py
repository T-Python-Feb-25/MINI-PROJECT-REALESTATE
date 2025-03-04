from django.shortcuts import render, redirect
from django.http import HttpRequest, HttpResponse



def home_view(request:HttpRequest):
  return render(request, "main/index.html")


def properties_view(request:HttpRequest):
  properties = [
    {"title" : "Villa Modern in Malqa", "image" : "villa1.jpg"},
    {"title" : "Great home for you in Rimal", "image" : "villa2.jpg"},
    {"title" : "Villa with 8 bedrooms in Swedey", "image" : "villa3.jpg"},
    {"title" : "Amazing Villa in Hitten", "image" : "villa4.jpg"},
]
  return render(request, "main/properties.html", context={"properties":properties})


def contact_view(request:HttpRequest):
  return render(request, "main/contact.html")

def light_view(request:HttpRequest):
  response = redirect("main:home")
  response.set_cookie("mode","light",max_age= -6000)
  return response


def dark_view(request:HttpRequest):
  response = redirect("main:home")
  response.set_cookie("mode","dark")
  return response


