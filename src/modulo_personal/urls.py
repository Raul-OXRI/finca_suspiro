from django.contrib import admin
from django.urls import path
from django import views
from . import views

urlpatterns = [
    path('', views.personal, name="personal"),
    path('create_user/', views.create_user, name='create_user')
]
