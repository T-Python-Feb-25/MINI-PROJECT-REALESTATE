from . import views
from django.urls import path

app_name = "main"

urlpatterns = [
    path("",views.main,name="main"),
    path("properties/",views.properties_views,name="properties"),
    path("contact/",views.contact_view,name="contact"),
    path("mode/dark",views.dark_view,name="dark_view"),
    path("mode/light",views.light_view,name="light_view")
]