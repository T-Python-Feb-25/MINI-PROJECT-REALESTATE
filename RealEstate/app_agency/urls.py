#from django.contrib import admin
from django.urls import path
from . import views

app_name = 'app_agency' 

urlpatterns = [
    #path('admin/', admin.site.urls),
    path('', views.home, name='home'),
    path('properties/', views.properties, name='properties'),
    path('contact/', views.contact, name='contact'),
    path('dark/', views.dark, name='dark'),
    path('light/', views.light, name='light'),
]

