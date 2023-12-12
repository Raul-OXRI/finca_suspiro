from django.shortcuts import render, redirect
from django.http import HttpResponse
from .forms import RegistroForm
from .models import Registro


def registro(request):
    registros = Registro.objects.all()
    return render(request, "registro.html", {'registros': registros})


#def create_registred(request):
    
#    return render(request, "create_registred.html")


def create_registred(request):
    if request.method == 'POST':
        form = RegistroForm(request.POST)
        if form.is_valid():
            form.save()  # Guarda los datos en la base de datos si el formulario es válido
            # Puedes redirigir a una página de éxito o realizar otras acciones después de guardar
            #form = RegistroForm()  # Limpiar el formulario después de guardar
            return redirect('registro')  # Redireccionar al template inicial
    else:
        form = RegistroForm()

    return render(request, 'create_registred.html', {'form': form})