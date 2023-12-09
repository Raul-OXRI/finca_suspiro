from django.shortcuts import render
from django.http import HttpResponse


def registro(request):
    return render(request, "registro.html")