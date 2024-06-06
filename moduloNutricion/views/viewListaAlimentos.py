from django.shortcuts import render, redirect
from django.views import View
import json
import sys
from django.http import JsonResponse
from moduloNutricion.models.modelAlimento import *

class Lista_Alimentos(View):
   def get(self, request):
      alimentos = Alimento.objects.all()
      #return render(request, 'listaAlimentos.html',{'alimentos': alimentos})
      return render(request, 'listaAlimentos.html')

def fetch_category_data(request):
   if request.method == 'GET':
      category = request.GET.get('category')
      print(category)
      if category:
         alimentos = Alimento.objects.filter(tipo__tipo_nombre=category).select_related('tipo','uni')
         if(len(alimentos) == 0):
            return JsonResponse({"nombre":category, "error":"No hay datos"}, status=200)
         data = [
                {
                    'id': alimento.id,
                    'nombre': alimento.nombre,
                    'tipo': alimento.tipo.id,            
                    'tipo_nombre': alimento.tipo.tipo_nombre, 
                    'unidad': alimento.uni.id,

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
   return JsonResponse({"error":"Error, no hay categoria a buscar."}, status=200)
#fetch tipos
def fetch_tipo_data(request):
   if request.method == 'GET':
      tipos = Tipo.objects.all()
      if(len(tipos) == 0):
         return JsonResponse({"error":"No hay datos"}, status=200)
      data = [
             {
                 'id': tipo.id,
                 'tipo_nombre': tipo.tipo_nombre,
             } for tipo in tipos
         ]
      return JsonResponse(data, safe=False)
   return JsonResponse({"error":"Error, no hay categoria a buscar."}, status=200)
#fetch unidades
def fetch_unidades_data(request):
   if request.method == 'GET':
      unidades = Unidad.objects.all()
      if(len(unidades) == 0):
         return JsonResponse({"error":"No hay datos"}, status=200)
      data = [
             {
                 'id': unidad.id,
                 'unidad': unidad.unidad,
             } for unidad in unidades
         ]
      return JsonResponse(data, safe=False)
   return JsonResponse({"error":"Error, no hay categoria a buscar."}, status=200)
