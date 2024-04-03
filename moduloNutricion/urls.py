from django.urls import path, re_path
from django.contrib import admin
from django.urls import path, re_path
from django.contrib.auth.views import LoginView, PasswordResetView, PasswordResetDoneView, PasswordResetConfirmView, PasswordResetCompleteView
from moduloNutricion.views.exampleView import *
urlpatterns = [
    path('nutricion', nutriologo.as_view(), name='nutriologo')
]