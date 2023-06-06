from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login, authenticate, logout
from .forms import RegisterForm, ContactForm, LoginForm
from django.contrib import messages
from django.urls import reverse
from .models import User, Accessory , Brand
from django.contrib.auth.models import User


def index(request):
    contact_form = ContactForm()
    login_form = LoginForm()
    is_accesories_page = False

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
    print('is_accesories_page', is_accesories_page)
    return render(request, 'index.html',{'contact_form': contact_form, 'login_form':login_form , 'is_accesories_page': is_accesories_page})

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


def accesories(request):

    accessory = Accessory.objects.all()
    is_accesories_page = True
    print('is_accesories_page', is_accesories_page) 
    return render(request, 'accesories.html', {'accessory': accessory , 'is_accesories_page': is_accesories_page})

def cars(request):
    return render(request, 'cars.html')

def contact(request):
    return render(request, '/index#contact.html')



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


#///////////// add accesory from modal //////////////////////////////////

def add_accessory(request):
   
    brand_name = request.POST.get('brand')
    brand = get_object_or_404(Brand, brand=brand_name)

    if request.method == 'POST':
        name = request.POST.get('name')
        color = request.POST.get('color')
       #brand = request.POST.get('brand')
        description = request.POST.get('description')
        image = request.FILES.get('image')
        price = request.POST.get('price')
        
        #username = 'gaston'
        # try:
        #     user = User.objects.get(username=username)
        # except User.DoesNotExist:
        #     # Manejo de error si el usuario no existe
        #     # Por ejemplo, puedes redirigir a una página de error o mostrar un mensaje al usuario.
        #     return HttpResponse('El usuario no existe')


        # # Verificar si el usuario está autenticado, esto es a modo de prueba ... despues solo usuario con permisos
        # if request.user.is_authenticated:
        #     user = request.user
        # else:
            
        #     user = User.objects.get(username='default_user')

        accessory = Accessory(
            name=name,
            color=color,
            brand=brand,
            description=description,
            image=image,
            price=price,
            #user=user
        )
        
        accessory.save()
    return redirect('accesories')


    #return render(request, 'accesories.html')

# //////////////// end add accesory //////////////////////////////////