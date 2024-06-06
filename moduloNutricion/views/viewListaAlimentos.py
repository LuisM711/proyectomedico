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
         alimentos = Alimento.objects.filter(tipo__id=category).select_related('tipo','uni')
         data = [
                {
                    'nombre': alimento.nombre,
                    'tipo_nombre': alimento.tipo.tipo_nombre,  # Access the tipo_nombre field through the related tipo object
                    'unidad': alimento.uni.unidad,      # Access the unidad field through the related uni object
                    'porcion': alimento.porcion,
                    'peso': alimento.peso,
                    'peso_neto': alimento.peso_neto,
                    'energia': alimento.energia,
                    'proteina': alimento.proteina,
                    'lipidos': alimento.lipidos,
                    'carbos': alimento.carbos,
                    'ag_satur': alimento.ag_satur,
                    'ag_mono': alimento.ag_mono,
                    'ag_poli': alimento.ag_poli,
                    'colesterol': alimento.colesterol,
                    'azucar': alimento.azucar,
                    'fibra': alimento.fibra,
                    'vita_A': alimento.vita_A,
                    'aci_asc': alimento.aci_asc,
                    'aci_foli': alimento.aci_foli,
                    'calcio': alimento.calcio,
                    'hierro': alimento.hierro,
                    'potasio': alimento.potasio,
                    'sodio': alimento.sodio,
                    'fosforo': alimento.fosforo,
                    'etanol': alimento.etanol,
                    'ig': alimento.ig,
                    'carga_gli': alimento.carga_gli,
                } for alimento in alimentos
            ]
         return JsonResponse(data, safe=False)
   return JsonResponse({"error":"Category not found."}, status=400)
