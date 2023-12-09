from django.contrib import admin
from django.urls import path
from django import views
from . import views

urlpatterns = [
    path('', views.registro, name="registro"),
    path('create_registred/', views.create_registred, name='create_registred')
]
