from django.shortcuts import render, redirect
from django.views import View
from django.http import JsonResponse
from moduloNutricion.models.modelMenuBien import Menu_Bien
from moduloPrincipal.models.modelUsuario import Usuario
from moduloPrincipal.models.modelPaciente import *
import json
class Menu_paciente(View):
    def get(self, request):
        auxUsuario = Usuario.objects.get(id_usuario=request.user)
        pacienteBien = Paciente.objects.get(id_usuario=auxUsuario)
        auxMenu = Menu_Bien.objects.filter(paciente=pacienteBien).order_by('fecha').first()
        auxMenu2 = auxMenu.menu
       # print(auxMenu2)
        menuPaciente = json.loads(auxMenu2)
        data={
            'paciente': pacienteBien,
            'menu': menuPaciente
        }
        return render(request,'menuPaciente.html', data)