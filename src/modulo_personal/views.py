from django.shortcuts import render, redirect
from django.http import HttpResponse
from .form import CreateUserForm
from django.contrib.auth.models import User

# Create your views here.

def personal(request):
    
    return render(request, "personal.html")



def create_user(request):
    if request.method == 'POST':
        form = CreateUserForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            first_name = form.cleaned_data['first_name']
            last_name = form.cleaned_data['last_name']
            group = form.cleaned_data['group']
            password = form.cleaned_data['password']

            user = User.objects.create_user(username=username, password=password, first_name=first_name, last_name=last_name)
            user.groups.add(group)

            return redirect('personal')  # Reemplaza 'página_de_inicio' con tu URL de redirección después de crear el usuario
    else:
        form = CreateUserForm()
    
    return render(request, 'create_user.html', {'form': form})