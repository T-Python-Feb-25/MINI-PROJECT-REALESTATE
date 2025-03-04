from django.shortcuts import render, redirect
from django.http import HttpResponse

def home(request):
    return render(request, 'main/home.html')

def dark_mode(request):
    response = redirect('main:home')
    response.set_cookie('dark_mode', 'true', max_age=60*60*24*30)  
    return response

def light_mode(request):
    response = redirect('main:home')
    response.delete_cookie('dark_mode')
    return response

def properties(request):
    return render(request, 'main/properties.html')  # عرض صفحة الخصائص

def contact(request):
    return render(request, 'main/contact.html')  # عرض صفحة الاتصال