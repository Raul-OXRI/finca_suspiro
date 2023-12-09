from django.shortcuts import render
from django.http import HttpResponse


def registro(request):
    return render(request, "registro.html")


def create_registred(request):
    return render(request, "create_registred.html")