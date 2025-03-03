from django.urls import path
from . import views
app_name = "main"
urlpatterns = [path("",views.home_view,name="home_view"),
               path("properties/",views.properties_view,name="properties_view"),
               path("contact/",views.contact_view,name="contact_view"),
               path("dark/",views.drak_mode,name="drak_mode"),
               path("light/",views.light_mode,name="light_mode")
               ]
