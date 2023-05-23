from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
import re

#FORMULARIO LOGIN
class LoginForm(forms.Form):
    usuario = forms.CharField(max_length=65)
    password = forms.CharField(max_length=65, widget=forms.PasswordInput)

#FORMULARIO CONTACTO
class ContactForm (forms.Form):
    name = forms.CharField (label = 'Nombre: ', max_length = 50,required = True)
    email = forms.EmailField (label = 'Email: ', required = True)
    msg = forms.CharField (label = 'Mensaje: ', widget = forms.Textarea(attrs={'resize': 'none'}), max_length = 100, required=True)
   
    #Validacion para que el nombre no pueda contener numeros
    def clean_name(self):
        name = self.cleaned_data['name']
        if not re.match(r'^[a-zA-Z]+$', name):
            raise forms.ValidationError('Nombre invalido')
        return name

    #Validacion para que el email sea correcto
    def clean_email(self):
        email = self.cleaned_data['email']
        if not re.match(r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$', email):
            raise forms.ValidationError("Ingrese una dirección de correo electrónico válida.")
        return email
    
#FORMULARIO PARA REGISTRO
class RegisterForm(UserCreationForm):

    #username = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control'}))
    email = forms.EmailField(widget=forms.EmailInput(attrs={'class': 'form-control'}))


    class Meta:
        model=User
        fields = ['username', 'email', 'password1', 'password2']

    def __init__(self, *args, **kwargs):
        super(RegisterForm, self).__init__(*args, **kwargs)

        self.fields['username'].widget.attrs['class'] = 'form-control'
        self.fields['password1'].widget.attrs['class'] = 'form-control'
        self.fields['password2'].widget.attrs['class'] = 'form-control'