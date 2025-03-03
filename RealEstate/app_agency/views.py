from django.shortcuts import render , redirect
from django.http import HttpResponse
 # Create your views here.

def home(request):
    

    return render(request, 'app_agency/home.html')

def dark(request):
    response=redirect('app_agency:home')
    response.set_cookie('dark', 'true', max_age=60*60*24*30)
    return response

def light(request):
    response = redirect('app_agency:home')
    response.delete_cookie('dark')
    return response

def properties(request):
    
    return render(request, 'app_agency/properties.html')

def contact(request):

    return render(request, 'app_agency/contact.html')