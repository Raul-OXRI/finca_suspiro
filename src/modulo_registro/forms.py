from django import forms
from .models import Registro
from django.contrib.auth.models import Group, User

class RegistroForm(forms.ModelForm):
    class Meta:
        model = Registro
        fields = '__all__'  # O puedes especificar los campos individualmente si prefieres

    def __init__(self, *args, **kwargs):
        super(RegistroForm, self).__init__(*args, **kwargs)
        # Puedes personalizar el formulario aquí si necesitas hacer cambios específicos
        self.fields['fecha_nacimiento'].label = 'Fecha de nacimiento'
        
        grupo = Group.objects.get(name='Propietario')  # Reemplaza 'Propietario' con el nombre real de tu grupo
        usuarios_grupo = User.objects.filter(groups=grupo)
        self.fields['usuario'].queryset = usuarios_grupo