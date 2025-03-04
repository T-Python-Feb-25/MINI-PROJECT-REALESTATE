from . import views
from django.urls import path

app_name = 'main'

urlpatterns = [
  path("", views.home_view, name ="home"),
  path("properties/", views.properties_view, name ="properties"),
  path("contact/", views.contact_view, name ="contact"),
  path("mode/light", views.light_view, name ="light_view"),
  path("mode/dark", views.dark_view, name ="dark_view"),
]