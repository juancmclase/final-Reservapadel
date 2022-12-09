

from dataclasses import fields
from django import forms
from django.db.models.fields import DateTimeField
from django.forms.fields import ChoiceField
from .models import Contacto, Pistas, Reservas,Hora
from django.contrib.auth.forms import UserCreationForm,UserChangeForm
from django.contrib.auth.models import User
class ContactoForm(forms.ModelForm):

    class Meta:
        model= Contacto
        #fields=["nombre", "correo","tipo_consulta", "mensaje","avisos"]
        fields = '__all__'

class HoraForm(forms.ModelForm):
    class Meta:
        model= Hora
        fields = '__all__'

class CustomUserCreationForm(UserCreationForm):
    class Meta:
        model= User
        fields=['username',"first_name","last_name","email","password1","password2"]

class PistasForm(forms.ModelForm):
    class Meta:
        model= Pistas
        fields='__all__'

class DateInput(forms.DateInput):
    input_type= 'date'

class DisponibleForm(forms.ModelForm):
    class Meta:
        model=Reservas
        fields=['nombre','club','pista','fecha','hora']
        widgets = {'fecha':DateInput(),}
   

            
            
        
class UserProfile(UserChangeForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['first_name'].widget.attrs['autofocus']= True

    class Meta:
        model = User
        fields ='first_name','last_name','email','username'
        exclude = ['user_permissions', 'last_login','date_joined','is_superuser','is_active','is_staff','groups','password1','password2']
