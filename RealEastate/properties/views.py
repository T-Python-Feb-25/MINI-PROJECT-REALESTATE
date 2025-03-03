from django.shortcuts import render

def home(request):
    return render(request, 'properties/home.html')

def properties_list(request):
    properties = [
        {"title": "Villa Modern in Malqa", "image": "villa1.jpg"},
        {"title": "Great home for you in Rimal", "image": "villa2.jpg"},
        {"title": "Villa with 8 bedrooms in Swedey", "image": "villa3.jpg"},
        {"title": "Amazing Villa in Hitten", "image": "villa4.jpg"},
    ]
    return render(request, 'properties/properties.html', {'properties': properties})

def contact(request):
    return render(request, 'properties/contact.html')
