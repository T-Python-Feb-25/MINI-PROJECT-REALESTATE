from django.urls import path
from .views import home, properties_list, contact

urlpatterns = [
    path('', home, name='home'),  
    path('properties/', properties_list, name='properties'),  
    path('contact/', contact, name='contact'),  
]