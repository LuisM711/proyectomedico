from django.shortcuts import render, redirect
from django.views import View
import json
from django.http import JsonResponse

class alimentos(View):
    def get(self, request, id):
        jsonFile = 'moduloNutricion/alimentos.json'

        try:
            with open(jsonFile, 'r') as file:
                alimentosData = json.load(file)
            return JsonResponse(alimentosData)
        except FileNotFoundError:
            return JsonResponse({'error': 'Archivo de Alimentos no encontrado'}, status=404)
        except Exception as e:
            return JsonResponse({'error': str(e)}, status=500)