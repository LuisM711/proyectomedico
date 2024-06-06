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
   def post(self, request):
      #print(json.loads( request.body)[0].get('tipo'))
      objeto = json.loads(request.body)
      print(objeto.get('tipo'))
      #eliminar todos los alimentos de la categoria
      alimentos = Alimento.objects.filter(tipo__id=objeto.get('tipo'))
      alimentos.delete()
      #insertar los nuevos alimentos
      for alimento in objeto.get('datos'):
         alimento = Alimento(
            nombre = alimento.get('nombre'),
            tipo = Tipo.objects.get(id=objeto.get('tipo')),
            uni = Unidad.objects.get(id=alimento.get('unidad')),
            porcion = alimento.get('porcion'),
            peso = alimento.get('peso'),
            peso_neto = alimento.get('peso_neto'),
            energia = alimento.get('energia'),
            proteina = alimento.get('proteina'),
            lipidos = alimento.get('lipidos'),
            carbos = alimento.get('carbos'),
            ag_satur = alimento.get('ag_satur'),
            ag_mono = alimento.get('ag_mono'),
            ag_poli = alimento.get('ag_poli'),
            colesterol = alimento.get('colesterol'),
            azucar = alimento.get('azucar'),
            fibra = alimento.get('fibra'),
            vita_A = alimento.get('vita_A'),
            aci_asc = alimento.get('aci_asc'),
            aci_foli = alimento.get('aci_foli'),
            calcio = alimento.get('calcio'),
            hierro = alimento.get('hierro'),
            potasio = alimento.get('potasio'),
            sodio = alimento.get('sodio'),
            fosforo = alimento.get('fosforo'),
            etanol = alimento.get('etanol'),
            ig = alimento.get('ig'),
            carga_gli = alimento.get('carga_gli'),
         )
         alimento.save()
         




      return JsonResponse({'error':'skibidi toilet'} , status=200)



def fetch_category_data(request):
   if request.method == 'GET':
      category = request.GET.get('category')
      if category:
         alimentos = Alimento.objects.filter(tipo__id=category).select_related('tipo','uni')
         if(len(alimentos) == 0):
            return JsonResponse({"nombre":category, "error":"No hay datos"}, status=200)
         data = [
                {
                    'id': alimento.id,
                    'nombre': alimento.nombre,
                    'tipo': alimento.tipo.id,            
                    'tipo_nombre': alimento.tipo.tipo_nombre, 
                    'unidad': alimento.uni.id,
                     'unidad_nombre':alimento.uni.unidad,
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
