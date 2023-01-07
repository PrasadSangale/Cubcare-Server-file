from django.contrib import admin
from django.urls import path 
from home import views


urlpatterns = [
    path("",views.index, name="home"),
    path("about",views.about, name="about"),
    path("services",views.services, name="services"),
    path("contact",views.contact, name="contact"),
    path("register",views.register,name="register"),
    path("login",views.login,name="login"),
    path("TrainerViewSet",views.TrainerViewSet.as_view({'get':'list'}),name="TrainerViewSet"),
    path("VetViewSet",views.VetViewSet.as_view({'get':'list'}),name="VetViewSet"),
    path("Dog_infoViewSet",views.Dog_infoViewSet.as_view({'get':'list'}),name="Dog_infoViewSet"),
    path("PlacesViewSet",views.PlacesViewSet.as_view({'get':'list'}),name="PlacesViewSet"),
    path("Breed_infoViewSet",views.Breed_infoViewSet.as_view({'get':'list'}),name="Breed_infoViewSet"),
    path("ProductViewSet",views.ProductViewSet.as_view({'get':'list'}),name="ProductViewSet"),
    
]
