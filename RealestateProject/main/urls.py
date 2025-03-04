from django.urls import path
from .views import home, dark_mode, light_mode, properties, contact  

app_name = 'main'

urlpatterns = [
    path('', home, name='home'),
    path('dark-mode/', dark_mode, name='dark_mode'),
    path('light-mode/', light_mode, name='light_mode'),
    path('properties/', properties, name='properties'),  
    path('contact/', contact, name='contact'),  
]