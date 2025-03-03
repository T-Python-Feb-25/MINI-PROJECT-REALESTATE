# home/views.py
from django.shortcuts import render

def home(request):
    return render(request, 'home/home.html')

def home_dark(request):
    return render(request, 'home/home_dark.html')

def contact(request):
    return render(request, 'home/contact.html')

def properties(request):
    properties = [
        {"title": "Villa Modern in Malqa", "image": "villa1.jpg"},
        {"title": "Great home for you in Rimal", "image": "villa2.jpg"},
        {"title": "Villa with 8 bedrooms in Swedey", "image": "villa3.jpg"},
        {"title": "Amazing Villa in Hitten", "image": "villa4.jpg"},
    ]
    return render(request, 'home/properties.html', {'properties': properties})
