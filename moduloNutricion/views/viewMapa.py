from django.shortcuts import render, redirect
from django.views import View


def visualizarMapa(request):
    return render(request,'index.html')