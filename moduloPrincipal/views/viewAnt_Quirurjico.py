from django.views import View
from django.utils.decorators import method_decorator
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from django.http.response import JsonResponse
import json
from moduloPrincipal.models.__init__ import *

class Registrar_Ant_Quirurjico(View):
    @method_decorator(login_required, name="dispatch")
    def post(self, request):
        # Si el metodo es put se va a otra funcion
        if "_put" in request.POST:
            return self.put(request)

        # Validacion del tipo de usuario para realizar el registro de una forma u otra
        aux_usuario = Usuario.objects.get(id_usuario_id=request.user.id)
        if (aux_usuario.tipo == 'P'):
            tipo = request.POST.get('tipo')
            tiempo = request.POST.get('tiempo')
            aux_usuario = Usuario.objects.get(id_usuario=request.user.id)
            paciente = Paciente.objects.get(id_usuario=aux_usuario.id)

            aux_quirurjico = Ant_quirurjicos.objects.create(id_paciente_id=paciente.id, tipo=tipo, tiempo=tiempo)
            aux_quirurjico.save()
            return redirect('perfil_clinico')
        else:
            tipo = request.POST.get('tipo')
            tiempo = request.POST.get('tiempo')
            aux_usuario = Usuario.objects.get(id_usuario=request.user.id)
            id_paciente = request.POST.get('id_paciente')

            aux_quirurjico = Ant_quirurjicos.objects.create(id_paciente_id=id_paciente, tipo=tipo, tiempo=tiempo)
            aux_quirurjico.save()
            return redirect('/informacion/paciente/full/' + id_paciente)

    @method_decorator(login_required, name="dispatch")
    def delete(self, request):
        jd = json.loads(request.body)
        try:
            Ant_quirurjicos.objects.filter(id=jd["id"]).delete()
            return JsonResponse({'success': True})
        except Ant_quirurjicos.DoesNotExist:
            return JsonResponse({'success': False, 'error': 'Antecedente quirurjico no encontrado'})

    @method_decorator(login_required, name="dispatch")
    def put(self, request):
        # Se leen los datos del formulario
        tipo = request.POST.get('tipo')
        tiempo = request.POST.get('tiempo')
        clave = request.POST.get('id')

        # Se busca en el elemento en la BD
        aux_quirurjico = Ant_quirurjicos.objects.get(id=clave)

        # Se actualiza
        aux_quirurjico.tipo = tipo
        aux_quirurjico.tiempo = tiempo
        aux_quirurjico.save()

        # Validacion del tipo de usuario para redirigir
        aux_usuario = Usuario.objects.get(id_usuario_id=request.user.id)
        if (aux_usuario.tipo == 'P'):
            aux_usuario = Usuario.objects.get(id_usuario=request.user.id)
            return redirect('perfil_clinico')
        else:
            id_paciente = request.POST.get('id_paciente')
            return redirect('/informacion/paciente/full/' + id_paciente)