# myapp/urls.py
from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('home_dark/', views.home_dark, name='home_dark'),
    path('contact/', views.contact, name='contact'),
    path('properties/', views.properties, name='properties'),
]
