from django.shortcuts import render
from django.http import HttpRequest, HttpResponse
# Create your views here.

def Base_view(request: HttpRequest):
    return render(request, "main/base.html")


def Home_view(request: HttpRequest):
    return render(request, "main/home.html")