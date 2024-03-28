from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.views import View
from django.utils.decorators import method_decorator
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.core.files.storage import default_storage
from django.core.files.base import ContentFile

from django.http.response import JsonResponse
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from datetime import date, timezone, timedelta, datetime
from moduloPrincipal.models.__init__ import *

# Clase para inciar sesion de los distintos usuairos
class Login(View):
    def get(self, request):
        return render(request, 'login.html')

    def post(self, request):
        username = request.POST.get('username')
        password = request.POST.get('contra')
        # Valida que se encuentre el usuario
        user = authenticate(request, username=username, password=password)
        if user is not None:
            aux_user = User.objects.get(username=username)
            if aux_user.is_staff:
                # Si es admin, unicamente guarda la sesion y redirige a la ventana de inicio
                login(request, user)
                request.session['user_type'] = 'admin'
                return redirect('inicio_admin')
            else:

                aux_usuario = Usuario.objects.get(id_usuario_id=aux_user.id)
                if aux_usuario.tipo == 'E':
                    aux_especialista = Especialista.objects.get(id_usuario_id=aux_usuario.id)

                    if aux_especialista.estatus == '0':
                        datos = {'message': "Todavia no tienes acceso a la pagina"}
                        return render(request, 'login.html', {"datos": datos})
                    else:
                        login(request, user)
                        request.session['user_type'] = 'E'
                        return redirect('inicio_especialista')
                else:
                    aux_paciente = Paciente.objects.get(id_usuario_id=aux_usuario.id)
                    if aux_paciente.estatus == '0':
                        datos = {'message': "Todavia no tienes acceso a la pagina"}
                        return render(request, 'login.html', {"datos": datos})
                    else:
                        login(request, user)
                        request.session['user_type'] = 'P'
                        return redirect('inicio_paciente')
        else:
            datos = {'message': "Correo o contraseña incorrectos"}
            return render(request, 'login.html', {"datos": datos})
# class UserType(View):
#     def get(self, request):
#         user_type = request.session.get('user_type')
#         #return {'user_type': user_type}
#         return JsonResponse({'user_type': user_type})

# Clase para borrar la sesion del usuario
class CerrarSesion(View):
    @method_decorator(login_required(login_url='login'), name='dispatch')
    def post(self, request):
        logout(request)
        return redirect('login')
# Clase para redirigir a los distintos tipos de usaurio a su respectivo inicio
class Redirigir(View):
    @method_decorator(login_required(login_url='login'), name='dispatch')
    def get(self, request):
        if (request.user.is_staff == 0):
            aux_usuario = Usuario.objects.get(id_usuario_id=request.user.id)

            if (aux_usuario.tipo == 'P'):
                return render(request, 'inicio.html', {"user_type": 'P'})

            return render(request, 'inicio.html',{"user_type": 'E'})

        else:
            return render(request,'inicio.html',{"user_type": 'admin'})

# Clase para visualizar la ventana de "acerca de"
class Acerca(View):
    def get(self, request):
        return render(request, 'acerca_de.html')

# Clase para actualizar la imagen de perfil de los usuarios, sea paciente o especialista
class SubirImagenPerfil(View):

    @method_decorator(login_required, name='dispatch')
    def post(self, request):

        image = request.FILES['imagen_perfil'].read()
        if image:
            aux_usuario = Usuario.objects.get(id_usuario_id=request.user.id)
            if aux_usuario.foto:
                default_storage.delete(aux_usuario.foto.path)  # se borra la foto anterior

            aux_usuario.foto.save('imagen_usuario_' + str(aux_usuario.id) + '.jpg', ContentFile(image),
                                  save=False)  # se guarda la nueva foto
            aux_usuario.save()

        if (aux_usuario.tipo == "P"):
            return redirect('/configuracion/paciente/0')
        else:
            return redirect('/configuracion/especialista/0/0')

# CLase para visualizar la ventana de registro
class Registrarse(View):
    def get(self, request):
        # se obtienen las especialiades para mostrarlas en el formulario de registro de especialista
        aux_especialidades = list(Especialidades.objects.values())

        # Fecha para establecer que para el registro se deba ingresar una fecha de nacimiento de hace minimo 18 años
        fecha_actual = datetime.now()
        fecha_maxima = fecha_actual - timedelta(days=365 * 18)
        if len(aux_especialidades) > 0:
            datos = {"Especialidades": aux_especialidades, "Fecha_Maxima": fecha_maxima.strftime('%Y-%m-%d')}
        else:
            datos = {'message': "No se encontraron especialidades", "Fecha_Maxima": fecha_maxima.strftime('%Y-%m-%d')}
        return render(request, 'registro.html', {"datos": datos})

# Clase para cambiar la contraseña de los especialistas y pacientes
class Cambiar_Contra(View):
    @method_decorator(login_required(login_url='login'), name='dispatch')
    def get(self, request):
        if (request.user.is_staff == 0):
            aux_usuario = Usuario.objects.get(id_usuario=request.user.id)
            if aux_usuario.tipo == "E":
                return render(request, 'ventanas_especialista/cambiar_contra_especialista.html')
            else:
                return render(request, 'ventanas_paciente/cambiar_contra_paciente.html')
        else:
            return redirect('inicio_admin')

    def post(self, request):
        password = request.POST.get('contra_actual')
        new_password = request.POST.get('nueva_contra')
        user = authenticate(request, username=request.user.username, password=password)

        if user is not None:
            aux_user = User.objects.get(username=request.user.username)
            aux_user.set_password(new_password)
            aux_user.save()
            return redirect('login')
        else:
            return redirect('cambiar_contra')