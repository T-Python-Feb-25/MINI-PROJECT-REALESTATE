# home/views.py
from django.shortcuts import render

def home(request):
    return render(request, 'home/home.html')

def home_dark(request):
    return render(request, 'home/home_dark.html')
