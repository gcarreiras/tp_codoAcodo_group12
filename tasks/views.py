from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login, authenticate, logout
from .forms import RegisterForm, ContactForm, LoginForm
from django.contrib import messages
from django.urls import reverse
from .models import User, Accessory , Brand , Category
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from django.views.decorators.http import require_POST


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
    contact_form = ContactForm()
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username,password=password)
        if user is not None:
            print('usuario correcto')
            login(request, user)
            return render(request, 'index.html',  {'contact_form': contact_form})
            # return render(request, 'index.html',{'user': user, 'contact_form': contact_form})
        else:
            print('usuario incorrecto')
            messages.error(request, "Error de inicio de sesión")
        return redirect('index')


def logout_user(request):
    print('estoy en el logout')
    logout(request)
    messages.success(request, ("Deslogueado"))
    return redirect('index')


@login_required
def accesories(request):
    brands = Brand.objects.all()
    categories = Category.objects.all()
    print('CATEGORIES:' , categories )
    login_form= LoginForm()
    accessory = Accessory.objects.all()
    is_accesories_page = True

    return render(request, 'accesories.html', {'accessory': accessory , 'login_form': login_form, 'is_accesories_page': is_accesories_page, 'brands': brands , 'categories' : categories})

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
   

    if request.method == 'POST':
       
        category = request.POST.getlist('categories')
        print('Category in the post ' , category)
        brand_name = request.POST.get('brand')
        name = request.POST.get('name')
        color = request.POST.get('color')
        brand_name = request.POST.get('brand')
        brand = get_object_or_404(Brand, name=brand_name)
        description = request.POST.get('description')
        image = request.FILES.get('image')
        price = request.POST.get('price')
        
        accessory = Accessory(
            name=name,
            color=color,
            brands=brand,
            description=description,
            image=image,
            price=price,
        )
        
        accessory.save()
    return redirect('accesories')


    #return render(request, 'accesories.html')

# //////////////// end add accesory //////////////////////////////////

@require_POST
def eliminar_accesorio(request):
    accesorio_id = request.POST.get('accesorio_id')
    eliminar = get_object_or_404(Accessory, id=accesorio_id)
    eliminar.delete()
    return redirect('accesories')


def buscar_accesorios(request):
    
    
    nombre = request.GET.get('nombre')

    accesorios = Accessory.objects.filter(name__icontains=nombre)
    
    return render(request, 'accesories.html', {'accessory': accesorios})