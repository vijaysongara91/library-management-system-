from django.urls import path
from . import views
 
urlpatterns = [
    path("",views.index),
    path("contact",views.contact),
    path("login",views.login),
    path("catalog",views.catalog),
    path("My_Account",views.My_Account),
    path("about",views.about),
    path("Register",views.Register),
    path("browse",views.browse),
    path("home",views.home),
    path("book",views.book),
    path("help",views.help)


]

  
