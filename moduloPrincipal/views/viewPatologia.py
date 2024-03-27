import json
from django.http.response import JsonResponse
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from django.shortcuts import render, redirect
from django.views import View
from moduloPrincipal.models.__init__ import *
class Registrar_Patologia(View):

    @method_decorator(login_required, name="dispatch")
    def post(self, request):
        # Si el metodo es put se va a otra funcion
        if "_put" in request.POST:
            return self.put(request)

        # Validacion del tipo de usuario para realizar el registro de una forma u otra
        aux_usuario = Usuario.objects.get(id_usuario_id=request.user.id)
        if (aux_usuario.tipo == 'P'):
            patologia = request.POST.get('patologia')
            aux_usuario = Usuario.objects.get(id_usuario=request.user.id)  # Se toma directamente del request
            paciente = Paciente.objects.get(id_usuario=aux_usuario.id)
            aux_pat = Ant_Patologicos.objects.create(id_paciente_id=paciente.id, patologia=patologia)
            aux_pat.save()
            return redirect('perfil_clinico')
        else:
            patologia = request.POST.get('patologia')
            aux_usuario = Usuario.objects.get(id_usuario=request.user.id)
            id_paciente = request.POST.get('id_paciente')  # Se toma de un input
            aux_pat = Ant_Patologicos.objects.create(id_paciente_id=id_paciente, patologia=patologia)
            aux_pat.save()
            return redirect('/informacion/paciente/full/' + id_paciente)

    @method_decorator(login_required, name="dispatch")
    def delete(self, request):
        jd = json.loads(request.body)
        try:
            Ant_Patologicos.objects.filter(id=jd["id"]).delete()
            return JsonResponse({'success': True})
        except Ant_Patologicos.DoesNotExist:
            return JsonResponse({'success': False, 'error': 'Patologia no encontrada'})

    @method_decorator(login_required, name="dispatch")
    def put(self, request):
        # Se leen los datos del formulario
        patologia = request.POST.get('patologia')
        clave = request.POST.get('id')

        # Se busca el elemento en la BD
        aux_patologia = Ant_Patologicos.objects.get(id=clave)

        # Se actualiza
        aux_patologia.patologia = patologia
        aux_patologia.save()

        # Validacion del tipo de usuario para redirigir
        aux_usuario = Usuario.objects.get(id_usuario_id=request.user.id)
        if (aux_usuario.tipo == 'P'):
            aux_usuario = Usuario.objects.get(id_usuario=request.user.id)
            return redirect('perfil_clinico')
        else:
            id_paciente = request.POST.get('id_paciente')
            return redirect('/informacion/paciente/full/' + id_paciente)