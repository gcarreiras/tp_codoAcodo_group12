from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm

#class LoginForm(forms.Form):
#    username = forms.CharField(max_length=65)
#    password = forms.CharField(max_length=65, widget=forms.PasswordInput)

class RegisterForm(UserCreationForm):

    username = forms.CharField(widget=forms.TextInput(attrs={'class': 'inputs'}))
    email = forms.EmailField(widget=forms.EmailInput(attrs={'class': 'form-control'}))

    class Meta:
        model=User
        fields = ['username', 'email', 'password1', 'password2']

