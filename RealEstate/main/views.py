from django.shortcuts import render,redirect
from django.http import HttpRequest,HttpResponse   
from django.shortcuts import redirect

def home_view(request):

    return render(request, 'home.html')

def properties_view(request):
    context = {

        "title1" : "Villa Modern in Malqa", "image1" : "villa1.jpg",
        "title2" : "Great home for you in Rimal", "image2" : "villa2.jpg",
        "title3" : "Villa with 8 bedrooms in Swedey", "image3" : "villa3.jpg",
        "title4" : "Amazing Villa in Hitten", "image4" : "villa4.jpg",
    }
    return render(request, 'properties.html',context=context)

def contact_view(request):

    return render(request, 'contact.html')

def theme_mode_view(request):

    referer = request.META.get('HTTP_REFERER', '/')
    response = redirect(referer)

    current_mode = request.COOKIES.get('dark_mode')
    
    if current_mode == 'true':
        response.set_cookie('dark_mode', 'false')
    else:
        response.set_cookie('dark_mode', 'true')
    
    return response