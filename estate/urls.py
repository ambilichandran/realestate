from django.urls import path
from .import views
urlpatterns=[
    path("",views.index,name="index"),
    path("about",views.about,name="about"),
    path("service",views.service,name="sevice"),
     path("more",views.more,name="more"),
     path("registration",views.registration,name="registration"),
     path("logout",views.logout,name="logout"),
]