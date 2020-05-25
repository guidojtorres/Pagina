from django import forms
from django.contrib.auth import get_user_model
from django.contrib.auth.forms import UserCreationForm


class UserCreateForm(UserCreationForm):
    class Meta:
        model = get_user_model()
        fields = ('email', 'nombre', 'telefono')

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['email'].label = 'Correo Electronico'
        self.fields['telefono'].label = 'Numero de Telefono (Opcional)'
        self.fields['nombre'].label = 'Nombre Completo (Opcional)'
