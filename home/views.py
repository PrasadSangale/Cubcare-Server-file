import pyrebase
from typing import ContextManager
from django.shortcuts import redirect, render
from datetime import datetime
from home.models import Contact, Vet
from django.contrib import messages
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.forms import AuthenticationForm
from home.models import Trainer,Vet,Dog_info,Product,Places,Breed_info
from rest_framework import viewsets
from home.serializers import TrainerSerializer,VetSerializer,Dog_infoSerializer,PlacesSerializer,Breed_infoSerializer,ProductSerializer

# Create your views here.
firebaseConfig = {
  "apiKey": "AIzaSyC9mUrKG6wkhXJaguOjOYgIK8BqzoWGkxU",
  "authDomain": "phoneverification-e40da.firebaseapp.com",
  "projectId": "phoneverification-e40da",
  "storageBucket": "phoneverification-e40da.appspot.com",
  "messagingSenderId": "685807440974",
  "appId": "1:685807440974:web:e45c134d591d2886415f1f",
  "measurementId": "G-PZ5VJNB73F",
  "databaseURL": "https://phoneverification-e40da-default-rtdb.firebaseio.com/"
}
firebase=pyrebase.initialize_app(firebaseConfig)
auth=firebase.auth()
database=firebase.database()

class TrainerViewSet(viewsets.ModelViewSet):
    queryset = Trainer.objects.all().order_by('name')
    serializer_class = TrainerSerializer
    
class VetViewSet(viewsets.ModelViewSet):
    queryset = Vet.objects.all().order_by('name')
    serializer_class = VetSerializer
    
class Dog_infoViewSet(viewsets.ModelViewSet):
    queryset = Dog_info.objects.all().order_by('name')
    serializer_class = Dog_infoSerializer
    
class PlacesViewSet(viewsets.ModelViewSet):
    queryset = Places.objects.all().order_by('name')
    serializer_class = PlacesSerializer
    
class Breed_infoViewSet(viewsets.ModelViewSet):
    queryset = Breed_info.objects.all().order_by('name')
    serializer_class = Breed_infoSerializer
    
class ProductViewSet(viewsets.ModelViewSet):
    queryset = Product.objects.all().order_by('name')
    serializer_class = ProductSerializer

#from .models import Hero



def index(request):
    
    return render(request,'index.html')
  #  return HttpResponse("this is homepage")

def about(request): 
   return render(request,'about.html')

  #  return HttpResponse("this is about page")

def services(request):
    return render(request,'services.html')
    #return HttpResponse("this is about services page")

def contact(request):
    if request.method=="POST":
        name=request.POST.get("name")
        email=request.POST.get("email")
        phone=request.POST.get("phone")
        desc=request.POST.get("desc")
        contact= Contact(name=name, email=email, phone=phone, desc=desc, date=datetime.today())
        contact.save()
        messages.success(request, 'Your form has been submitted')

    return render(request,'contact.html')
   # return HttpResponse("this is about contact page")
   
def register(request):
    if request.method == "POST":
        form=UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')
    else:
           form=UserCreationForm
    return render(request, 'register.html',{'form':form})

def login(request):
    if request.method == "POST":
        form=AuthenticationForm(data=request.POST)
        if form.is_valid():
            return redirect('home')
    else:
        form=AuthenticationForm
    return render(request, 'login.html',{'form':form})
