from . import views 
from django.urls import path


app_name='main'

urlpatterns=[
    path("", views.home_view,name="home_view"),
    path("darkmode/", views.dark_mode_view,name="dark_mode_view"),
    path("light/", views.light_mode_view,name="light_mode_view"),
    path("properties/", views.properties_view,name="properties_view"),
    path("contact/us/", views.contact_view,name="contact_view")

]