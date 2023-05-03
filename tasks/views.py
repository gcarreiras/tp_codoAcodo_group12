from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login, authenticate, logout
from .forms import RegisterForm
from django.contrib import messages



def index(request):
    return render(request, 'index.html')

def login_user(request):
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username,password=password)
        if user is not None:
            login(request,user)
            return redirect('index')
        else:
            messages.success(request,("Error de login"))
            return redirect('login')

def logout_user(request):
    logout(request)
    messages.success(request, ("Deslogueado"))
    return redirect('index')

def signup(request):
    if request.method == "POST":
        form = RegisterForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data['username']
            password = form.cleaned_data['password1']
            user = authenticate(username=username, password=password)
            login(request,user)
            messages.success(request, ("Registro exitoso!"))
            return redirect('index')
    else:
        form = RegisterForm()
    return render(request, 'signup.html',{
        'form':form,
    })

#def signup(request):
#    return render(request, 'signup.html')

def accesories(request):
    #return render(request, acc)
    return render(request, '.accesories/accesories.html')

def cars(request):
    return render(request, 'cars.html')

def contact(request):
    return render(request, 'contact.html')

def login(request):
    return render(request, 'login.html')