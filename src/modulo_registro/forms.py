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
        self.fields['propietario'].queryset = usuarios_grupo

    def clean(self):
        cleaned_data = super().clean()
        genero = cleaned_data.get('genero')
        partos = cleaned_data.get('partos')

        if genero == 'toro':
            cleaned_data['partos'] = 0

        return cleaned_data