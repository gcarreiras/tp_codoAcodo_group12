from django.shortcuts import render
from django.contrib.auth.forms import UserCreationForm



def index(request):
    return render(request, 'index.html')

def createUser(request):
    return render(request, 'createUser.html',{
        'form': UserCreationForm
    })

def accesories(request):
    return render(request, 'accesories.html')

def cars(request):
    return render(request, 'cars.html')

def contact(request):
    return render(request, 'contact.html')

def login(request):
    return render(request, 'login.html')