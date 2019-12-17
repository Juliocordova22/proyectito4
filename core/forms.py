from django import forms
from django.forms import ModelForm
from .models import Cliente ,Ordentrabajo,Tecnico
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

class ClienteForm(ModelForm):

    nombre = forms.CharField(min_length=6 , max_length=25)

    class Meta:
        model = Cliente
        fields =  ['nombre','direccion','ciudad','comuna','telefono','correo']


class OrdentrabajoForm(ModelForm):

    class Meta:
        model = Ordentrabajo
        fields =  ['ot' ,'cliente','fecha' ,'hora_inicio' ,'hora_termino' ,'id_ascensor' , 'modelo_ascensor' ,'fallas_detectadas' ,'reparacion_efectuada' ,'piezas_cambiadas' ,'tecnico' ]

        widgets = {
            'fecha': forms.SelectDateWidget(years=range(1990,2021)),
            
        }

class TecnicoForm(ModelForm):

    nombre = forms.CharField(min_length=6 , max_length=25)

    class Meta:
        model = Tecnico
        fields =  ['nombre','imagen']

class CustomUserForm(UserCreationForm):
    
    class Meta:
        model = User
        fields = ['first_name','last_name','email','username','password1','password2']