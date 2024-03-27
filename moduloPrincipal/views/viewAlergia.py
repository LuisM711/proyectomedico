from django.views import View
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from django.shortcuts import render, redirect
import json
from django.http.response import JsonResponse
from moduloPrincipal.models.__init__ import *

class Registrar_Alergia(View):
    @method_decorator(login_required, name="dispatch")
    def post(self, request):
        # Si el metodo es put se va a otra funcion
        if "_put" in request.POST:
            return self.put(request)

        # Validacion del tipo de usuario para realizar el registro de una forma u otra
        aux_usuario = Usuario.objects.get(id_usuario_id=request.user.id)
        if (aux_usuario.tipo == 'P'):
            nombre = request.POST.get('nombre')
            aux_usuario = Usuario.objects.get(id_usuario=request.user.id)
            paciente = Paciente.objects.get(id_usuario=aux_usuario.id)

            aux_alergia = Alergias.objects.create(id_paciente_id=paciente.id, nombre=nombre)
            aux_alergia.save()
            return redirect('perfil_clinico')
        else:
            nombre = request.POST.get('nombre')
            aux_usuario = Usuario.objects.get(id_usuario=request.user.id)
            id_paciente = request.POST.get('id_paciente')

            aux_alergia = Alergias.objects.create(id_paciente_id=id_paciente, nombre=nombre)
            aux_alergia.save()
            return redirect('/informacion/paciente/full/' + id_paciente)

    @method_decorator(login_required, name="dispatch")
    def delete(self, request):
        jd = json.loads(request.body)
        try:
            Alergias.objects.filter(id=jd["id"]).delete()
            return JsonResponse({'success': True})
        except Alergias.DoesNotExist:
            return JsonResponse({'success': False, 'error': 'Alergia no encontrada'})

    @method_decorator(login_required, name="dispatch")
    def put(self, request):
        # Se leen los datos del formulario
        alergia = request.POST.get('nombre')
        clave = request.POST.get('id')

        # Se busca el elemento en la BD
        aux_alergia = Alergias.objects.get(id=clave)

        # Se actualiza
        aux_alergia.nombre = alergia
        aux_alergia.save()

        # Validacion del tipo de usuario para redirigir
        aux_usuario = Usuario.objects.get(id_usuario_id=request.user.id)
        if (aux_usuario.tipo == 'P'):
            aux_usuario = Usuario.objects.get(id_usuario=request.user.id)
            return redirect('perfil_clinico')
        else:
            id_paciente = request.POST.get('id_paciente')
            return redirect('/informacion/paciente/full/' + id_paciente)