from django.shortcuts import render
from django.http import HttpRequest, HttpResponse

# Create your views here.
def home(request:HttpRequest):

    return render(request,'real_estate_app/home.html')

def properties(request:HttpRequest):
    
    return render(request,'real_estate_app/properties.html')

def contact(request:HttpRequest):
    
    return render(request,'real_estate_app/contact.html')