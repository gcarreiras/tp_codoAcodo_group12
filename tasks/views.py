from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login, authenticate
from .forms import RegisterForm



def index(request):
    return render(request, 'index.html')

def signup(request):
    if request.method == 'GET':
        form = RegisterForm()
        return render(request, 'signup.html', {'form': form})
    
    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.username = user.username.lower()
            user.save()
            messages.success(request, 'Registro con exito')
            login(request, user)
            return redirect('index')
        else:
            return render(request, 'signup.html', {'form': form})

#def signup(request):
#    return render(request, 'signup.html')

def accesories(request):
    #return render(request, acc)
    return render(request, './accesories/accesories.html')

def cars(request):
    return render(request, 'cars.html')

def contact(request):
    return render(request, 'contact.html')

def login(request):
    return render(request, 'login.html')