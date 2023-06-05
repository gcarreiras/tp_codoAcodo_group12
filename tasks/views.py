from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login, authenticate, logout
from .forms import RegisterForm, ContactForm, LoginForm
from django.contrib import messages
from django.urls import reverse
from .models import User, Accessory
from django.contrib.auth.models import User


def index(request):
    contact_form = ContactForm()
    login_form = LoginForm()


    if request.method == "POST":
        contact_form = ContactForm(request.POST)
       
        if contact_form.is_valid():
            name = contact_form.cleaned_data['name'],
            email = contact_form.cleaned_data['email'],
            msg = contact_form.cleaned_data['msg']
            messages.add_message(request, messages.SUCCESS,'Mensaje enviado correctamente')
            return redirect(reverse('index') + '#contacto')
        else:
            messages.add_message(request, messages.ERROR, 'Ocurrió un error al enviar el mensaje')
   
    else:
        contact_form = ContactForm()
   
    return render(request, 'index.html',{'contact_form': contact_form, 'login_form':login_form})

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
    login_form = LoginForm()
    if request.method == "POST":
        form = RegisterForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password1']
            # Crear un nuevo usuario
            new_user = User.objects.create_user(username=username, password=password)
            new_user.email = form.cleaned_data['email']
            #new_user.first_name = form.cleaned_data['first_name']
            #new_user.last_name = form.cleaned_data['last_name']
            new_user.save()
            
            messages.success(request, "Registro exitoso!")
            return redirect('index')
    else:
        form = RegisterForm()
    return render(request, 'signup.html', {'form': form, 'login_form':login_form})

# def signup(request):
#     if request.method == "POST":
#         form = RegisterForm(request.POST)
#         if form.is_valid():
#             # form.save()
#             username = form.cleaned_data['username']
#             password = form.cleaned_data['password1']
#             new_user = User(username=username, password=password)
#             new_user.save()
#             user = authenticate(username=username, password=password)
#             # login(request,user)
#             messages.success(request, ("Registro exitoso!"))
#             return redirect('index')
#     else:
#         form = RegisterForm()
#     return render(request, 'signup.html',{
#         'form':form
#     })

#def signup(request):
#    return render(request, 'signup.html')

def accesories(request):
    accessory = Accessory.objects.all()
    return render(request, 'accesories.html', {'accessory': accessory})

def cars(request):
    return render(request, 'cars.html')

def contact(request):
    return render(request, '/index#contact.html')

def login(request):
    return render(request, 'login.html')