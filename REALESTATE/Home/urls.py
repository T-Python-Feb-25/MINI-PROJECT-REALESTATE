from django.urls import path
from . import views

app_name="Home"

urlpatterns = [
    path('',views.home_view,name='home_view'),
    path('properties/realstate', views.properties_view, name='properties_view'),
    path('contact/realstate', views.contact_view, name='contact_view'),
    path('about/realstate', views.About_view, name='About_view'),
    path('services/realstate', views.Services_view, name='Services_view'),
    path('dark/realstate', views.dark_mode_view, name='dark_mode_view'),
    path('light/realstate', views.light_mode_view, name='light_mode_view'),

]