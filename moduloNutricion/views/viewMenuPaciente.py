from django.shortcuts import render, redirect
from django.views import View
from django.http import JsonResponse
import json
class Menu_paciente(View):
    def get(self, request):
        return render(request,'menuPaciente.html')