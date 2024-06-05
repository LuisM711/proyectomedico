from django.shortcuts import render, redirect
from django.views import View
import json
import sys
from django.http import JsonResponse
from moduloNutricion.models.modelAlimento import *

class Lista_Alimentos(View):
   def get(self, request):
    alimentos = Alimento.objects.all()
    return render(request, 'listaAlimentos.html',{'alimentos': alimentos})

def fetch_category_data(request):
   if request.method == 'GET':
      category = request.GET.get('category')
      print(category)
      if category:
         alimentos = Alimento.objects.filter(tipo__id=category)
         data = list(alimentos.values())
         return JsonResponse(data, safe=False)
   return JsonResponse({"error":"Category not found."}, status=400)
