from django.urls import path, include
from . import views

app_name = "main"

urlpatterns = [
    path("", views.index_view, name="index_view"),
    path("light/mode/", views.light_mode, name="light_mode"),
    path("dark/mode/", views.dark_mode, name="dark_mode"),
    path("properties/", views.properties, name="properties"),
    path("contact/", views.contact, name="contact"),


]
