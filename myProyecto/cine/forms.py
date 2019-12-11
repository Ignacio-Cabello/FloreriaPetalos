from django import forms
from django.forms import ModelForm
from .models import Pelicula
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User


class FlorForm(ModelForm):
    


    class Meta:
        model = Pelicula
        fields = ['name', 'valor', 'descripcion', 'stock', 'estado','imagen']

    
class CustomUserForm(UserCreationForm):
    


    class Meta:
        model = User
        fields = ['first_name', 'last_name', 'email', 'username', 'password1','password2']
