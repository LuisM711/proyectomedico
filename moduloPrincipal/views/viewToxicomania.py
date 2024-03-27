from django.views import View
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from django.shortcuts import render, redirect
from django.http.response import JsonResponse
import json
from moduloPrincipal.models.__init__ import *
# Clases para realizar el registro de los datos del perfil clinico
class Registrar_Toxicomania(View):
    @method_decorator(login_required, name="dispatch")
    def post(self, request):
        # Si el metodo es put se va a otra funcion
        if "_put" in request.POST:
            return self.put(request)

        # Validacion del tipo de usuario que hizo el registro para redirigir a una ventana u otra
        aux_usuario = Usuario.objects.get(id_usuario_id=request.user.id)
        if (aux_usuario.tipo == 'P'):  # El propio paciente hizo el registro
            nombre = request.POST.get('nombre')
            cantidad = request.POST.get('cantidad')
            frecuencia = request.POST.get('frecuencia')
            tiempo = request.POST.get('tiempo')
            # Se toma el id directamente desde el request
            aux_usuario = Usuario.objects.get(id_usuario=request.user.id)
            paciente = Paciente.objects.get(id_usuario=aux_usuario.id)
            aux_tox = Toxicomania.objects.create(id_paciente_id=paciente.id, nombre=nombre, cantidad=cantidad,
                                                 frecuencia=frecuencia, tiempo=tiempo)
            aux_tox.save()
            return redirect('perfil_clinico')
        else:  # El registro lo hace un especialista
            nombre = request.POST.get('nombre')
            cantidad = request.POST.get('cantidad')
            frecuencia = request.POST.get('frecuencia')
            tiempo = request.POST.get('tiempo')
            # Se toma el id de un input
            id_paciente = request.POST.get('id_paciente')
            aux_tox = Toxicomania.objects.create(id_paciente_id=id_paciente, nombre=nombre, cantidad=cantidad,
                                                 frecuencia=frecuencia, tiempo=tiempo)
            aux_tox.save()
            return redirect('/informacion/paciente/full/' + id_paciente)

    @method_decorator(login_required, name="dispatch")
    def delete(self, request):
        jd = json.loads(request.body)
        try:
            Toxicomania.objects.filter(id=jd["id"]).delete()
            return JsonResponse({'success': True})
        except Toxicomania.DoesNotExist:
            return JsonResponse({'success': False, 'error': 'Toxicomania no encontrada'})

    @method_decorator(login_required, name="dispatch")
    def put(self, request):
        # Se leen los datos del formulario
        nombre = request.POST.get('nombre')
        cantidad = request.POST.get('cantidad')
        frecuencia = request.POST.get('frecuencia')
        tiempo = request.POST.get('tiempo')
        clave = request.POST.get('id')

        # Se busca en el elemento en la BD
        aux_toxicomania = Toxicomania.objects.get(id=clave)

        # Se actualiza
        aux_toxicomania.nombre = nombre
        aux_toxicomania.cantidad = cantidad
        aux_toxicomania.frecuencia = frecuencia
        aux_toxicomania.tiempo = tiempo
        aux_toxicomania.save()

        # Validacion del tipo de usuario para redirigir
        aux_usuario = Usuario.objects.get(id_usuario_id=request.user.id)
        if (aux_usuario.tipo == 'P'):
            aux_usuario = Usuario.objects.get(id_usuario=request.user.id)
            return redirect('perfil_clinico')
        else:
            id_paciente = request.POST.get('id_paciente')
            return redirect('/informacion/paciente/full/' + id_paciente)