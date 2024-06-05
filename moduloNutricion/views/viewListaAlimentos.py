from django.shortcuts import render, redirect
from django.views import View
import json
from django.http import JsonResponse

class Lista_Alimentos(View):
   def get(self, request):
    return render(request, 'listaAlimentos.html')