from django.views import View
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from django.shortcuts import render, redirect
from django.http.response import JsonResponse
import json
from moduloPrincipal.models.__init__ import *
class Registrar_Vacuna(View):
    @method_decorator(login_required, name="dispatch")
    def post(self, request):
        # Si el metodo es put se va a otra funcion
        if "_put" in request.POST:
            return self.put(request)

        # Validacion del tipo de usuario para realizar el registro de una forma u otra
        aux_usuario = Usuario.objects.get(id_usuario_id=request.user.id)
        if (aux_usuario.tipo == 'P'):
            nombre = request.POST.get('nombre')
            dosis = request.POST.get('dosis')
            year = request.POST.get('year')
            aux_usuario = Usuario.objects.get(id_usuario=request.user.id)
            paciente = Paciente.objects.get(id_usuario=aux_usuario.id)

            aux_vacuna = Vacunacion.objects.create(id_paciente_id=paciente.id, nombre=nombre, dosis=dosis, año=year)
            aux_vacuna.save()
            return redirect('perfil_clinico')
        else:
            nombre = request.POST.get('nombre')
            dosis = request.POST.get('dosis')
            year = request.POST.get('year')
            aux_usuario = Usuario.objects.get(id_usuario=request.user.id)
            id_paciente = request.POST.get('id_paciente')

            aux_vacuna = Vacunacion.objects.create(id_paciente_id=id_paciente, nombre=nombre, dosis=dosis, año=year)
            aux_vacuna.save()

            return redirect('/informacion/paciente/full/' + id_paciente)

    @method_decorator(login_required, name="dispatch")
    def delete(self, request):
        jd = json.loads(request.body)
        try:
            Vacunacion.objects.filter(id=jd["id"]).delete()
            return JsonResponse({'success': True})
        except Vacunacion.DoesNotExist:
            return JsonResponse({'success': False, 'error': 'Vacuna no encontrada'})

    @method_decorator(login_required, name="dispatch")
    def put(self, request):
        # Se leen los datos del formulario
        nombre = request.POST.get('nombre')
        dosis = request.POST.get('dosis')
        year = request.POST.get('year')
        clave = request.POST.get('id')

        # Se busca el elemento en la BD
        aux_vacuna = Vacunacion.objects.get(id=clave)

        # Se actualiza
        aux_vacuna.nombre = nombre
        aux_vacuna.dosis = dosis
        aux_vacuna.año = year
        aux_vacuna.save()

        # Validacion del tipo de usuario para redirigir
        aux_usuario = Usuario.objects.get(id_usuario_id=request.user.id)
        if (aux_usuario.tipo == 'P'):
            aux_usuario = Usuario.objects.get(id_usuario=request.user.id)
            return redirect('perfil_clinico')
        else:
            id_paciente = request.POST.get('id_paciente')
            return redirect('/informacion/paciente/full/' + id_paciente)