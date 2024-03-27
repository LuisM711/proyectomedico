from django.utils.decorators import method_decorator
from django.contrib.auth.decorators import login_required
from django.views import View
from django.shortcuts import render, redirect
from django.http.response import JsonResponse
from moduloPrincipal.models.__init__ import *
# Clase para visualizar la ventana de horario y editarlo
class Horario(View):
    @method_decorator(login_required, name="dispatch")
    def get(self, request, id_paciente=0):
        # Validacion de tipos de usaurio
        if (request.user.is_staff == 0):
            aux_usuario = Usuario.objects.get(id_usuario_id=request.user.id)
            if (aux_usuario.tipo == 'E'):
                # Se realiza el proceso de obtencion del horario
                aux_usuario = Usuario.objects.get(id_usuario=request.user.id)
                aux_especialista = Especialista.objects.get(id_usuario=aux_usuario.id)

                # Se divide el horario en dias
                arreglo_horario = (aux_especialista.horario).split(";")

                # Se divide el horario hasta obtener los valores que se colocaran en los inputs para que el especialista solo edite y no tenga que escribir todo desde 0

                if arreglo_horario[0] == "":
                    Lunes = {"hora1_turno1": "", "min1_turno1": "", "hora2_turno1": "", "min2_turno1": "",
                             "hora1_turno2": "", "min1_turno2": "", "hora2_turno2": "", "min2_turno2": ""}
                else:
                    # Se valida si existe ese simbolo para dividir el horario en turnos en el lunes
                    if ", " in arreglo_horario[0]:
                        arreglo_dia = (arreglo_horario[0]).split(", ")
                        turno1 = arreglo_dia[0]
                        turno2 = arreglo_dia[1]

                        # Se dividen los turnos en horas
                        arreglo_turno = (turno1).split("-")
                        hora1_turno1 = arreglo_turno[0]
                        hora2_turno1 = arreglo_turno[1]

                        arreglo_turno = (turno2).split("-")
                        hora1_turno2 = arreglo_turno[0]
                        hora2_turno2 = arreglo_turno[1]

                        # Se dividen las horas en hora y minutos

                        arreglo_horas = (hora1_turno1).split(":")
                        aux_hora1_turno1 = arreglo_horas[0]
                        aux_min1_turno1 = arreglo_horas[1]

                        arreglo_horas = (hora2_turno1).split(":")
                        aux_hora2_turno1 = arreglo_horas[0]
                        aux_min2_turno1 = arreglo_horas[1]

                        arreglo_horas = (hora1_turno2).split(":")
                        aux_hora1_turno2 = arreglo_horas[0]
                        aux_min1_turno2 = arreglo_horas[1]

                        arreglo_horas = (hora2_turno2).split(":")
                        aux_hora2_turno2 = arreglo_horas[0]
                        aux_min2_turno2 = arreglo_horas[1]

                        Lunes = {"hora1_turno1": aux_hora1_turno1, "min1_turno1": aux_min1_turno1,
                                 "hora2_turno1": aux_hora2_turno1, "min2_turno1": aux_min2_turno1,
                                 "hora1_turno2": aux_hora1_turno2, "min1_turno2": aux_min1_turno2,
                                 "hora2_turno2": aux_hora2_turno2, "min2_turno2": aux_min2_turno2}
                    else:
                        # Se dividen el turno en horas
                        arreglo_turno = (arreglo_horario[0]).split("-")
                        hora1_turno1 = arreglo_turno[0]
                        hora2_turno1 = arreglo_turno[1]

                        arreglo_horas = (hora1_turno1).split(":")
                        aux_hora1_turno1 = arreglo_horas[0]
                        aux_min1_turno1 = arreglo_horas[1]

                        arreglo_horas = (hora2_turno1).split(":")
                        aux_hora2_turno1 = arreglo_horas[0]
                        aux_min2_turno1 = arreglo_horas[1]
                        Lunes = {"hora1_turno1": aux_hora1_turno1, "min1_turno1": aux_min1_turno1,
                                 "hora2_turno1": aux_hora2_turno1, "min2_turno1": aux_min2_turno1,
                                 "hora1_turno2": "", "min1_turno2": "", "hora2_turno2": "", "min2_turno2": ""}

                if arreglo_horario[1] == "":
                    Martes = {"hora1_turno1": "", "min1_turno1": "", "hora2_turno1": "", "min2_turno1": "",
                              "hora1_turno2": "", "min1_turno2": "", "hora2_turno2": "", "min2_turno2": ""}
                else:
                    # Se valida si existe ese simbolo para dividir el horario en turnos en el martes
                    if ", " in arreglo_horario[1]:
                        arreglo_dia = (arreglo_horario[1]).split(", ")
                        turno1 = arreglo_dia[0]
                        turno2 = arreglo_dia[1]

                        # Se dividen los turnos en horas
                        arreglo_turno = (turno1).split("-")
                        hora1_turno1 = arreglo_turno[0]
                        hora2_turno1 = arreglo_turno[1]

                        arreglo_turno = (turno2).split("-")
                        hora1_turno2 = arreglo_turno[0]
                        hora2_turno2 = arreglo_turno[1]

                        # Se dividen las horas en hora y minutos

                        arreglo_horas = (hora1_turno1).split(":")
                        aux_hora1_turno1 = arreglo_horas[0]
                        aux_min1_turno1 = arreglo_horas[1]

                        arreglo_horas = (hora2_turno1).split(":")
                        aux_hora2_turno1 = arreglo_horas[0]
                        aux_min2_turno1 = arreglo_horas[1]

                        arreglo_horas = (hora1_turno2).split(":")
                        aux_hora1_turno2 = arreglo_horas[0]
                        aux_min1_turno2 = arreglo_horas[1]

                        arreglo_horas = (hora2_turno2).split(":")
                        aux_hora2_turno2 = arreglo_horas[0]
                        aux_min2_turno2 = arreglo_horas[1]

                        Martes = {"hora1_turno1": aux_hora1_turno1, "min1_turno1": aux_min1_turno1,
                                  "hora2_turno1": aux_hora2_turno1, "min2_turno1": aux_min2_turno1,
                                  "hora1_turno2": aux_hora1_turno2, "min1_turno2": aux_min1_turno2,
                                  "hora2_turno2": aux_hora2_turno2, "min2_turno2": aux_min2_turno2}
                    else:
                        # Se dividen el turno en horas
                        arreglo_turno = (arreglo_horario[1]).split("-")
                        hora1_turno1 = arreglo_turno[0]
                        hora2_turno1 = arreglo_turno[1]

                        arreglo_horas = (hora1_turno1).split(":")
                        aux_hora1_turno1 = arreglo_horas[0]
                        aux_min1_turno1 = arreglo_horas[1]

                        arreglo_horas = (hora2_turno1).split(":")
                        aux_hora2_turno1 = arreglo_horas[0]
                        aux_min2_turno1 = arreglo_horas[1]
                        Martes = {"hora1_turno1": aux_hora1_turno1, "min1_turno1": aux_min1_turno1,
                                  "hora2_turno1": aux_hora2_turno1, "min2_turno1": aux_min2_turno1,
                                  "hora1_turno2": "", "min1_turno2": "", "hora2_turno2": "", "min2_turno2": ""}

                if arreglo_horario[2] == "":
                    Miercoles = {"hora1_turno1": "", "min1_turno1": "", "hora2_turno1": "", "min2_turno1": "",
                                 "hora1_turno2": "", "min1_turno2": "", "hora2_turno2": "", "min2_turno2": ""}
                else:
                    # Se valida si existe ese simbolo para dividir el horario en turnos en el miercoles
                    if ", " in arreglo_horario[2]:
                        arreglo_dia = (arreglo_horario[2]).split(", ")
                        turno1 = arreglo_dia[0]
                        turno2 = arreglo_dia[1]

                        # Se dividen los turnos en horas
                        arreglo_turno = (turno1).split("-")
                        hora1_turno1 = arreglo_turno[0]
                        hora2_turno1 = arreglo_turno[1]

                        arreglo_turno = (turno2).split("-")
                        hora1_turno2 = arreglo_turno[0]
                        hora2_turno2 = arreglo_turno[1]

                        # Se dividen las horas en hora y minutos

                        arreglo_horas = (hora1_turno1).split(":")
                        aux_hora1_turno1 = arreglo_horas[0]
                        aux_min1_turno1 = arreglo_horas[1]

                        arreglo_horas = (hora2_turno1).split(":")
                        aux_hora2_turno1 = arreglo_horas[0]
                        aux_min2_turno1 = arreglo_horas[1]

                        arreglo_horas = (hora1_turno2).split(":")
                        aux_hora1_turno2 = arreglo_horas[0]
                        aux_min1_turno2 = arreglo_horas[1]

                        arreglo_horas = (hora2_turno2).split(":")
                        aux_hora2_turno2 = arreglo_horas[0]
                        aux_min2_turno2 = arreglo_horas[1]

                        Miercoles = {"hora1_turno1": aux_hora1_turno1, "min1_turno1": aux_min1_turno1,
                                     "hora2_turno1": aux_hora2_turno1, "min2_turno1": aux_min2_turno1,
                                     "hora1_turno2": aux_hora1_turno2, "min1_turno2": aux_min1_turno2,
                                     "hora2_turno2": aux_hora2_turno2, "min2_turno2": aux_min2_turno2}
                    else:
                        # Se dividen el turno en horas
                        arreglo_turno = (arreglo_horario[2]).split("-")
                        hora1_turno1 = arreglo_turno[0]
                        hora2_turno1 = arreglo_turno[1]

                        arreglo_horas = (hora1_turno1).split(":")
                        aux_hora1_turno1 = arreglo_horas[0]
                        aux_min1_turno1 = arreglo_horas[1]

                        arreglo_horas = (hora2_turno1).split(":")
                        aux_hora2_turno1 = arreglo_horas[0]
                        aux_min2_turno1 = arreglo_horas[1]
                        Miercoles = {"hora1_turno1": aux_hora1_turno1, "min1_turno1": aux_min1_turno1,
                                     "hora2_turno1": aux_hora2_turno1, "min2_turno1": aux_min2_turno1,
                                     "hora1_turno2": "", "min1_turno2": "", "hora2_turno2": "", "min2_turno2": ""}

                if arreglo_horario[3] == "":
                    Jueves = {"hora1_turno1": "", "min1_turno1": "", "hora2_turno1": "", "min2_turno1": "",
                              "hora1_turno2": "", "min1_turno2": "", "hora2_turno2": "", "min2_turno2": ""}
                    # Se valida si existe ese simbolo para dividir el horario en turnos en el jueves
                else:
                    if ", " in arreglo_horario[3]:
                        arreglo_dia = (arreglo_horario[3]).split(", ")
                        turno1 = arreglo_dia[0]
                        turno2 = arreglo_dia[1]

                        # Se dividen los turnos en horas
                        arreglo_turno = (turno1).split("-")
                        hora1_turno1 = arreglo_turno[0]
                        hora2_turno1 = arreglo_turno[1]

                        arreglo_turno = (turno2).split("-")
                        hora1_turno2 = arreglo_turno[0]
                        hora2_turno2 = arreglo_turno[1]

                        # Se dividen las horas en hora y minutos

                        arreglo_horas = (hora1_turno1).split(":")
                        aux_hora1_turno1 = arreglo_horas[0]
                        aux_min1_turno1 = arreglo_horas[1]

                        arreglo_horas = (hora2_turno1).split(":")
                        aux_hora2_turno1 = arreglo_horas[0]
                        aux_min2_turno1 = arreglo_horas[1]

                        arreglo_horas = (hora1_turno2).split(":")
                        aux_hora1_turno2 = arreglo_horas[0]
                        aux_min1_turno2 = arreglo_horas[1]

                        arreglo_horas = (hora2_turno2).split(":")
                        aux_hora2_turno2 = arreglo_horas[0]
                        aux_min2_turno2 = arreglo_horas[1]

                        Jueves = {"hora1_turno1": aux_hora1_turno1, "min1_turno1": aux_min1_turno1,
                                  "hora2_turno1": aux_hora2_turno1, "min2_turno1": aux_min2_turno1,
                                  "hora1_turno2": aux_hora1_turno2, "min1_turno2": aux_min1_turno2,
                                  "hora2_turno2": aux_hora2_turno2, "min2_turno2": aux_min2_turno2}
                    else:
                        # Se dividen el turno en horas
                        arreglo_turno = (arreglo_horario[3]).split("-")
                        hora1_turno1 = arreglo_turno[0]
                        hora2_turno1 = arreglo_turno[1]

                        arreglo_horas = (hora1_turno1).split(":")
                        aux_hora1_turno1 = arreglo_horas[0]
                        aux_min1_turno1 = arreglo_horas[1]

                        arreglo_horas = (hora2_turno1).split(":")
                        aux_hora2_turno1 = arreglo_horas[0]
                        aux_min2_turno1 = arreglo_horas[1]
                        print(hora2_turno1)
                        Jueves = {"hora1_turno1": aux_hora1_turno1, "min1_turno1": aux_min1_turno1,
                                  "hora2_turno1": aux_hora2_turno1, "min2_turno1": aux_min2_turno1,
                                  "hora1_turno2": "", "min1_turno2": "", "hora2_turno2": "", "min2_turno2": ""}

                if arreglo_horario[4] == "":
                    Viernes = {"hora1_turno1": "", "min1_turno1": "", "hora2_turno1": "", "min2_turno1": "",
                               "hora1_turno2": "", "min1_turno2": "", "hora2_turno2": "", "min2_turno2": ""}
                    # Se valida si existe ese simbolo para dividir el horario en turnos en el viernes
                else:
                    if ", " in arreglo_horario[4]:
                        arreglo_dia = (arreglo_horario[4]).split(", ")
                        turno1 = arreglo_dia[0]
                        turno2 = arreglo_dia[1]

                        # Se dividen los turnos en horas
                        arreglo_turno = (turno1).split("-")
                        hora1_turno1 = arreglo_turno[0]
                        hora2_turno1 = arreglo_turno[1]

                        arreglo_turno = (turno2).split("-")
                        hora1_turno2 = arreglo_turno[0]
                        hora2_turno2 = arreglo_turno[1]

                        # Se dividen las horas en hora y minutos

                        arreglo_horas = (hora1_turno1).split(":")
                        aux_hora1_turno1 = arreglo_horas[0]
                        aux_min1_turno1 = arreglo_horas[1]

                        arreglo_horas = (hora2_turno1).split(":")
                        aux_hora2_turno1 = arreglo_horas[0]
                        aux_min2_turno1 = arreglo_horas[1]

                        arreglo_horas = (hora1_turno2).split(":")
                        aux_hora1_turno2 = arreglo_horas[0]
                        aux_min1_turno2 = arreglo_horas[1]

                        arreglo_horas = (hora2_turno2).split(":")
                        aux_hora2_turno2 = arreglo_horas[0]
                        aux_min2_turno2 = arreglo_horas[1]

                        Viernes = {"hora1_turno1": aux_hora1_turno1, "min1_turno1": aux_min1_turno1,
                                   "hora2_turno1": aux_hora2_turno1, "min2_turno1": aux_min2_turno1,
                                   "hora1_turno2": aux_hora1_turno2, "min1_turno2": aux_min1_turno2,
                                   "hora2_turno2": aux_hora2_turno2, "min2_turno2": aux_min2_turno2}
                    else:
                        # Se dividen el turno en horas
                        arreglo_turno = (arreglo_horario[4]).split("-")
                        hora1_turno1 = arreglo_turno[0]
                        hora2_turno1 = arreglo_turno[1]

                        arreglo_horas = (hora1_turno1).split(":")
                        aux_hora1_turno1 = arreglo_horas[0]
                        aux_min1_turno1 = arreglo_horas[1]

                        arreglo_horas = (hora2_turno1).split(":")
                        aux_hora2_turno1 = arreglo_horas[0]
                        aux_min2_turno1 = arreglo_horas[1]
                        Viernes = {"hora1_turno1": aux_hora1_turno1, "min1_turno1": aux_min1_turno1,
                                   "hora2_turno1": aux_hora2_turno1, "min2_turno1": aux_min2_turno1,
                                   "hora1_turno2": "", "min1_turno2": "", "hora2_turno2": "", "min2_turno2": ""}

                if arreglo_horario[5] == "":
                    Sabado = {"hora1_turno1": "", "min1_turno1": "", "hora2_turno1": "", "min2_turno1": "",
                              "hora1_turno2": "", "min1_turno2": "", "hora2_turno2": "", "min2_turno2": ""}
                else:
                    # Se valida si existe ese simbolo para dividir el horario en turnos en el sabado
                    if ", " in arreglo_horario[5]:
                        arreglo_dia = (arreglo_horario[5]).split(", ")
                        turno1 = arreglo_dia[0]
                        turno2 = arreglo_dia[1]

                        # Se dividen los turnos en horas
                        arreglo_turno = (turno1).split("-")
                        hora1_turno1 = arreglo_turno[0]
                        hora2_turno1 = arreglo_turno[1]

                        arreglo_turno = (turno2).split("-")
                        hora1_turno2 = arreglo_turno[0]
                        hora2_turno2 = arreglo_turno[1]

                        # Se dividen las horas en hora y minutos

                        arreglo_horas = (hora1_turno1).split(":")
                        aux_hora1_turno1 = arreglo_horas[0]
                        aux_min1_turno1 = arreglo_horas[1]

                        arreglo_horas = (hora2_turno1).split(":")
                        aux_hora2_turno1 = arreglo_horas[0]
                        aux_min2_turno1 = arreglo_horas[1]

                        arreglo_horas = (hora1_turno2).split(":")
                        aux_hora1_turno2 = arreglo_horas[0]
                        aux_min1_turno2 = arreglo_horas[1]

                        arreglo_horas = (hora2_turno2).split(":")
                        aux_hora2_turno2 = arreglo_horas[0]
                        aux_min2_turno2 = arreglo_horas[1]

                        Sabado = {"hora1_turno1": aux_hora1_turno1, "min1_turno1": aux_min1_turno1,
                                  "hora2_turno1": aux_hora2_turno1, "min2_turno1": aux_min2_turno1,
                                  "hora1_turno2": aux_hora1_turno2, "min1_turno2": aux_min1_turno2,
                                  "hora2_turno2": aux_hora2_turno2, "min2_turno2": aux_min2_turno2}
                    else:
                        # Se dividen el turno en horas
                        arreglo_turno = (arreglo_horario[5]).split("-")
                        hora1_turno1 = arreglo_turno[0]
                        hora2_turno1 = arreglo_turno[1]

                        arreglo_horas = (hora1_turno1).split(":")
                        aux_hora1_turno1 = arreglo_horas[0]
                        aux_min1_turno1 = arreglo_horas[1]

                        arreglo_horas = (hora2_turno1).split(":")
                        aux_hora2_turno1 = arreglo_horas[0]
                        aux_min2_turno1 = arreglo_horas[1]
                        Sabado = {"hora1_turno1": aux_hora1_turno1, "min1_turno1": aux_min1_turno1,
                                  "hora2_turno1": aux_hora2_turno1, "min2_turno1": aux_min2_turno1,
                                  "hora1_turno2": "", "min1_turno2": "", "hora2_turno2": "", "min2_turno2": ""}

                if arreglo_horario[6] == "":
                    Domingo = {"hora1_turno1": "", "min1_turno1": "", "hora2_turno1": "", "min2_turno1": "",
                               "hora1_turno2": "", "min1_turno2": "", "hora2_turno2": "", "min2_turno2": ""}
                else:
                    # Se valida si existe ese simbolo para dividir el horario en turnos en el domingo
                    if ", " in arreglo_horario[6]:
                        arreglo_dia = (arreglo_horario[6]).split(", ")
                        turno1 = arreglo_dia[0]
                        turno2 = arreglo_dia[1]

                        # Se dividen los turnos en horas
                        arreglo_turno = (turno1).split("-")
                        hora1_turno1 = arreglo_turno[0]
                        hora2_turno1 = arreglo_turno[1]

                        arreglo_turno = (turno2).split("-")
                        hora1_turno2 = arreglo_turno[0]
                        hora2_turno2 = arreglo_turno[1]

                        # Se dividen las horas en hora y minutos

                        arreglo_horas = (hora1_turno1).split(":")
                        aux_hora1_turno1 = arreglo_horas[0]
                        aux_min1_turno1 = arreglo_horas[1]

                        arreglo_horas = (hora2_turno1).split(":")
                        aux_hora2_turno1 = arreglo_horas[0]
                        aux_min2_turno1 = arreglo_horas[1]

                        arreglo_horas = (hora1_turno2).split(":")
                        aux_hora1_turno2 = arreglo_horas[0]
                        aux_min1_turno2 = arreglo_horas[1]

                        arreglo_horas = (hora2_turno2).split(":")
                        aux_hora2_turno2 = arreglo_horas[0]
                        aux_min2_turno2 = arreglo_horas[1]

                        Domingo = {"hora1_turno1": aux_hora1_turno1, "min1_turno1": aux_min1_turno1,
                                   "hora2_turno1": aux_hora2_turno1, "min2_turno1": aux_min2_turno1,
                                   "hora1_turno2": aux_hora1_turno2, "min1_turno2": aux_min1_turno2,
                                   "hora2_turno2": aux_hora2_turno2, "min2_turno2": aux_min2_turno2}
                    else:
                        # Se dividen el turno en horas
                        arreglo_turno = (arreglo_horario[6]).split("-")
                        hora1_turno1 = arreglo_turno[0]
                        hora2_turno1 = arreglo_turno[1]

                        arreglo_horas = (hora1_turno1).split(":")
                        aux_hora1_turno1 = arreglo_horas[0]
                        aux_min1_turno1 = arreglo_horas[1]

                        arreglo_horas = (hora2_turno1).split(":")
                        aux_hora2_turno1 = arreglo_horas[0]
                        aux_min2_turno1 = arreglo_horas[1]
                        Domingo = {"hora1_turno1": aux_hora1_turno1, "min1_turno1": aux_min1_turno1,
                                   "hora2_turno1": aux_hora2_turno1, "min2_turno1": aux_min2_turno1,
                                   "hora1_turno2": "", "min1_turno2": "", "hora2_turno2": "", "min2_turno2": ""}

                json_horario = {"Lunes": Lunes, "Martes": Martes, "Miercoles": Miercoles, "Jueves": Jueves,
                                "Viernes": Viernes, "Sabado": Sabado, "Domingo": Domingo}
                print(Jueves["min2_turno1"])
                datos = {"horario": json_horario}

                return render(request, "ventanas_especialista/horario.html", {"datos": datos})
            else:
                return redirect('inicio_paciente')
        else:
            return redirect('inicio_admin')

    # Funcion post unicamente porque html no no permitio el metodo put
    @method_decorator(login_required, name="dispatch")
    def post(self, request):
        # Si el metodo es put se va a otra funcion
        if "_put" in request.POST:
            return self.put(request)
        datos = {"Error": "No se encontro el campo put"}
        return JsonResponse(datos)

    # Metodo put para editar el horario
    @method_decorator(login_required, name='dispatch')
    def put(self, request):
        aux_usuario = Usuario.objects.get(id_usuario_id=request.user.id)
        aux_especialista = Especialista.objects.get(id_usuario_id=aux_usuario.id)
        # Se concatenan los horarios de todos los dias
        horario = ''

        # Primero se evalua que si haya registro de horas para un dia es especifico, si no lo hay, se le concatena solo un simbolo de ;
        if "lunes-hora1" in request.POST:
            # Se valida si se habilito el segundo turno
            if "lunes-hora2" in request.POST:
                lunes = request.POST.get('lunes-hora1') + ":" + request.POST.get('lunes-min1') + "-" + request.POST.get(
                    'lunes-hora1-2') + ":" + request.POST.get('lunes-min1-2') + ", " + request.POST.get(
                    'lunes-hora2') + ":" + request.POST.get('lunes-min2') + "-" + request.POST.get(
                    'lunes-hora2-2') + ":" + request.POST.get('lunes-min2-2')
            else:
                lunes = request.POST.get('lunes-hora1') + ":" + request.POST.get('lunes-min1') + "-" + request.POST.get(
                    'lunes-hora1-2') + ":" + request.POST.get('lunes-min1-2')
            horario = lunes
        else:
            horario = ";"

        if "martes-hora1" in request.POST:
            # Se valida si se habilito el segundo turno
            if "martes-hora2" in request.POST:
                martes = request.POST.get('martes-hora1') + ":" + request.POST.get(
                    'martes-min1') + "-" + request.POST.get('martes-hora1-2') + ":" + request.POST.get(
                    'martes-min1-2') + ", " + request.POST.get('martes-hora2') + ":" + request.POST.get(
                    'martes-min2') + "-" + request.POST.get('martes-hora2-2') + ":" + request.POST.get('martes-min2-2')
            else:
                martes = request.POST.get('martes-hora1') + ":" + request.POST.get(
                    'martes-min1') + "-" + request.POST.get('martes-hora1-2') + ":" + request.POST.get('martes-min1-2')
            horario += ";" + martes
        else:
            horario += ";"

        if "miercoles-hora1" in request.POST:
            # Se valida si se habilito el segundo turno
            if "miercoles-hora2" in request.POST:
                miercoles = request.POST.get('miercoles-hora1') + ":" + request.POST.get(
                    'miercoles-min1') + "-" + request.POST.get('miercoles-hora1-2') + ":" + request.POST.get(
                    'miercoles-min1-2') + ", " + request.POST.get('miercoles-hora2') + ":" + request.POST.get(
                    'miercoles-min2') + "-" + request.POST.get('miercoles-hora2-2') + ":" + request.POST.get(
                    'miercoles-min2-2')
            else:
                miercoles = request.POST.get('miercoles-hora1') + ":" + request.POST.get(
                    'miercoles-min1') + "-" + request.POST.get('miercoles-hora1-2') + ":" + request.POST.get(
                    'miercoles-min1-2')
            horario += ";" + miercoles
        else:
            horario += ";"

        if "jueves-hora1" in request.POST:
            # Se valida si se habilito el segundo turno
            if "jueves-hora2" in request.POST:
                jueves = request.POST.get('jueves-hora1') + ":" + request.POST.get(
                    'jueves-min1') + "-" + request.POST.get('jueves-hora1-2') + ":" + request.POST.get(
                    'jueves-min1-2') + ", " + request.POST.get('jueves-hora2') + ":" + request.POST.get(
                    'jueves-min2') + "-" + request.POST.get('jueves-hora2-2') + ":" + request.POST.get('jueves-min2-2')
            else:
                jueves = request.POST.get('jueves-hora1') + ":" + request.POST.get(
                    'jueves-min1') + "-" + request.POST.get('jueves-hora1-2') + ":" + request.POST.get('jueves-min1-2')
            horario += ";" + jueves
        else:
            horario += ";"

        if "viernes-hora1" in request.POST:
            # Se valida si se habilito el segundo turno
            if "viernes-hora2" in request.POST:
                viernes = request.POST.get('viernes-hora1') + ":" + request.POST.get(
                    'viernes-min1') + "-" + request.POST.get('viernes-hora1-2') + ":" + request.POST.get(
                    'viernes-min1-2') + ", " + request.POST.get('viernes-hora2') + ":" + request.POST.get(
                    'viernes-min2') + "-" + request.POST.get('viernes-hora2-2') + ":" + request.POST.get(
                    'viernes-min2-2')
            else:
                viernes = request.POST.get('viernes-hora1') + ":" + request.POST.get(
                    'viernes-min1') + "-" + request.POST.get('viernes-hora1-2') + ":" + request.POST.get(
                    'viernes-min1-2')
            horario += ";" + viernes
        else:
            horario += ";"

        if "sabado-hora1" in request.POST:
            # Se valida si se habilito el segundo turno
            if "sabado-hora2" in request.POST:
                sabado = request.POST.get('sabado-hora1') + ":" + request.POST.get(
                    'sabado-min1') + "-" + request.POST.get('sabado-hora1-2') + ":" + request.POST.get(
                    'sabado-min1-2') + ", " + request.POST.get('sabado-hora2') + ":" + request.POST.get(
                    'sabado-min2') + "-" + request.POST.get('sabado-hora2-2') + ":" + request.POST.get('sabado-min2-2')
            else:
                sabado = request.POST.get('sabado-hora1') + ":" + request.POST.get(
                    'sabado-min1') + "-" + request.POST.get('sabado-hora1-2') + ":" + request.POST.get('sabado-min1-2')
            horario += ";" + sabado
        else:
            horario += ";"

        if "domingo-hora1" in request.POST:
            # Se valida si se habilito el segundo turno
            if "domingo-hora2" in request.POST:
                domingo = request.POST.get('domingo-hora1') + ":" + request.POST.get(
                    'domingo-min1') + "-" + request.POST.get('domingo-hora1-2') + ":" + request.POST.get(
                    'domingo-min1-2') + ", " + request.POST.get('domingo-hora2') + ":" + request.POST.get(
                    'domingo-min2') + "-" + request.POST.get('domingo-hora2-2') + ":" + request.POST.get(
                    'domingo-min2-2')
            else:
                domingo = request.POST.get('domingo-hora1') + ":" + request.POST.get(
                    'domingo-min1') + "-" + request.POST.get('domingo-hora1-2') + ":" + request.POST.get(
                    'domingo-min1-2')
            horario += ";" + domingo
        else:
            horario += ";"

            # Se actualiza el horario en la BD
        aux_especialista.horario = horario
        aux_especialista.save()

        # arreglo_horario= horario.split(";")
        # datos={"Lunes": arreglo_horario[0], "Martes":arreglo_horario[1], "Miercoles":arreglo_horario[2], "Jueves":arreglo_horario[3], "Viernes":arreglo_horario[4], "Sabado":arreglo_horario[5], "Domingo":arreglo_horario[6]}
        return redirect('/configuracion/especialista/0/0')