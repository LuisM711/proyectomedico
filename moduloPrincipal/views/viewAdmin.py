import json
from datetime import date, timezone, timedelta, datetime
from datetime import date, timezone, timedelta, datetime
from django.contrib.auth import authenticate, login, logout
from django.utils.decorators import method_decorator
from django.shortcuts import render, redirect
from django.views import View
from django.contrib.admin.views.decorators import staff_member_required
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from django.http.response import JsonResponse
from moduloPrincipal.models.__init__ import *

# Clase para enviar al administrador a su ventana de inicio
class InicioAdmin(View):
    @method_decorator(staff_member_required(login_url='login'),
                      name='dispatch')  # Decorador para que solo las cuentas de superusuario puedan accedera esta api
    def get(self, request):
        if (request.user.is_staff == 1):
            return render(request, 'inicio.html',{"user_type": 'admin'})
        else:
            return redirect('login')

# Clase para listar todos los pacientes para el administrador
class Pacientes_Admin(View):

    @method_decorator(staff_member_required(login_url='login'),
                      name='dispatch')  # Decorador para que solo las cuentas de superusuario puedan accedera esta api
    def get(self, request, id=0):
        # Se obtienen todos los pacientes
        pacientes = Paciente.objects.all()
        # Se les agrega la edad
        pacientes_con_edad = []
        for paciente in pacientes:
            fecha_act = date.today()
            fecha_na = paciente.id_usuario.fecha_nacimiento
            edad = fecha_act.year - fecha_na.year - ((fecha_act.month, fecha_act.day) < (fecha_na.month, fecha_na.day))
            pacientes_con_edad.append({'paciente': paciente, 'edad': edad})
        data = {'pacientes': pacientes_con_edad, 'user_type': 'admin'}

        return render(request, 'ventanas_admin/listar_pacientes.html', {'pacientes': pacientes_con_edad})

    # Metodo put para actualizar el estatus de un paciente
    @method_decorator(staff_member_required(login_url='login'),
                      name='dispatch')  # Decorador para que solo las cuentas de superusuario puedan accedera esta api
    def put(self, request, id):
        jd = json.loads(request.body)
        try:
            aux_paciente = Paciente.objects.get(id=id)
            aux_paciente.estatus = jd['estatus']
            aux_paciente.save()
            return JsonResponse({'success': True})
        except aux_paciente.DoesNotExist:
            return JsonResponse({'success': False, 'error': 'Paciente no encontrado'})

# Clase para listar todos los especialistas para el administrador
class Especialistas_Admin(View):

    @method_decorator(staff_member_required(login_url='login'),
                      name='dispatch')  # Decorador para que solo las cuentas de superusuario puedan accedera esta api
    def get(self, request, id=0):
        especialistas = Especialista.objects.all()
        return render(request, 'ventanas_admin/listar_especialistas.html', {'especialistas': especialistas})

    # Funcion put para actualizar el estatus de un usuario
    @method_decorator(staff_member_required(login_url='login'),
                      name='dispatch')  # Decorador para que solo las cuentas de superusuario puedan accedera esta api
    def put(self, request, id):
        jd = json.loads(request.body)
        try:
            aux_especialista = Especialista.objects.get(id=id)
            aux_especialista.estatus = jd['estatus']
            aux_especialista.save()
            return JsonResponse({'success': True})
        except Solicitudes.DoesNotExist:
            return JsonResponse({'success': False, 'error': 'Especialista no encontrado'})

# Clase para visualizar la informacion de especialista por parte del administrador
class Informacion_especialista_admin(View):

    @method_decorator(staff_member_required(login_url='login'),
                      name='dispatch')  # Decorador para que solo las cuentas de superusuario puedan accedera esta api
    def get(self, request, id_user, id_usuario, id_especialista):
        aux_user = User.objects.get(id=id_user)
        aux_usuario = Usuario.objects.get(id=id_usuario)
        aux_especialista = Especialista.objects.get(id=id_especialista)
        # Se divide el horario por dias
        arreglo_horario = (aux_especialista.horario).split(";")
        json_horario = {"Lunes": arreglo_horario[0], "Martes": arreglo_horario[1], "Miercoles": arreglo_horario[2],
                        "Jueves": arreglo_horario[3], "Viernes": arreglo_horario[4], "Sabado": arreglo_horario[5],
                        "Domingo": arreglo_horario[6]}
        datos = {'usuario': aux_usuario, 'nombre': aux_user.first_name + " " + aux_user.last_name,
                 'correo': aux_user.email, 'info_ad': aux_especialista.info_ad, 'cedula': aux_especialista.cedula,
                 'especialidad': aux_especialista.id_especialidad.nombre, 'horario': json_horario}
        return render(request, 'ventanas_admin/informacion_especialista.html', {"datos": datos})

# Clase para que el administrador visualice la informacion de un paciente
class Informacion_paciente_admin(View):
    @method_decorator(staff_member_required(login_url='login'),
                      name='dispatch')  # Decorador para que solo las cuentas de superusuario puedan accedera esta api
    def get(self, request, id):
        aux_usuario = Usuario.objects.get(id_usuario_id=id)
        datos = {'usuario': aux_usuario, 'nombre': aux_usuario.id_usuario.username,
                 'correo': aux_usuario.id_usuario.email}
        return render(request, 'ventanas_admin/informacion_paciente.html', {"datos": datos})

# Clase para que el administrador visualice, registre y edite las especialidades
class Listar_especialidades_admin(View):
    @method_decorator(staff_member_required(login_url='login'),
                      name='dispatch')  # Decorador para que solo las cuentas de superusuario puedan acceder a esta api
    def get(self, request):
        especialidades = Especialidades.objects.all()
        return render(request, 'ventanas_admin/especialidades.html', {"especialidades": especialidades})

    @method_decorator(staff_member_required(login_url='login'),
                      name='dispatch')  # Decorador para que solo las cuentas de superusuario puedan acceder a esta api
    def post(self, request):
        # Si el metodo es put se va a otra funcion
        if "_put" in request.POST:
            return self.put(request)

        print(request.POST)

        diag_trat = "si" if request.POST.get('diag_trat') == "on" else "no"
        exp_fisica = "si" if request.POST.get('exp_fisica') == "on" else "no"
        asignacion_menu = "si" if request.POST.get('asignar_menu') == "on" else "no"
        nombre = request.POST.get('nombre')
        descripcion = request.POST.get('descripcion')
        especialidad_data = {
            'nombre': nombre,
            'descripcion': descripcion,
            'exploracion_fisica': exp_fisica,
            'diagnostico_tratamiento': diag_trat,
            'asignacion_menu': asignacion_menu
        }

        especialidad = Especialidades.objects.create(**especialidad_data)

        #especialidad = Especialidades.objects.create(nombre=nombre, descripcion=descripcion, exploracion_fisica=exp_fisica, diagnostico_tratamiento=diag_trat, asignacion_menu= asignacion_menu)
        especialidad.save()
        return redirect('especialidades_admin')

    @method_decorator(login_required, name="dispatch")
    def put(self, request):
        #print(request.POST)
        aux_especialidad = Especialidades.objects.get(id=request.POST.get("id"))
        aux_especialidad.nombre = request.POST.get("nombre")
        aux_especialidad.descripcion = request.POST.get("descripcion")
        aux_especialidad.diagnostico_tratamiento = "si" if request.POST.get("diag_trat_put") == "on" else "no"
        aux_especialidad.exploracion_fisica = "si" if request.POST.get("exp_fisica_put") == "on" else "no"
        aux_especialidad.asignacion_menu = "si" if request.POST.get('asignacion_menu_put') == "on" else "no"
        aux_especialidad.save()
        return redirect('especialidades_admin')