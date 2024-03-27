import matplotlib.pyplot as plt
import io
import base64
from matplotlib.backends.backend_agg import FigureCanvasAgg
from django.http import Http404, HttpResponse
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from django.views import View
from django.utils.decorators import method_decorator

from moduloPrincipal.models.__init__ import *
# Clases y funciones para las graficas
# Funcion para las graficas especificas de cada usuario
def grafica(request, id, tipo):
    exploraciones_fisicas = Exploracion_fisica.objects.filter(id_cita__id_paciente=id)

    fechas = [exploracion_fisica.id_cita.fecha for exploracion_fisica in exploraciones_fisicas]

    if (tipo == 1):
        # GRAFICA PARA EL PESO DEL PACIENTE
        x = [exploracion_fisica.peso for exploracion_fisica in exploraciones_fisicas]
        nx = 'Peso'
    elif (tipo == 2):
        # GRAFICA PARA LA TALLA DEL PACIENTE
        x = [exploracion_fisica.talla for exploracion_fisica in exploraciones_fisicas]
        nx = 'Talla'
    elif (tipo == 3):
        # GRAFICA PARA IMC
        x = [exploracion_fisica.imc for exploracion_fisica in exploraciones_fisicas]
        nx = 'IMC'
    elif (tipo == 4):
        # GRAFICA PARA LA GLUCOSA
        x = [exploracion_fisica.glucosa for exploracion_fisica in exploraciones_fisicas]
        nx = 'Glucosa'
    elif (tipo == 5):
        # GRAFICA PARA LA CREATININA
        x = [float(exploracion_fisica.creatinina) for exploracion_fisica in exploraciones_fisicas]
        nx = 'Creatinina'
    elif (tipo == 6):
        # GRAFICA PARA LA FILTRACION GLOMERURAL
        x = [float(exploracion_fisica.filtracion_glomerular) for exploracion_fisica in exploraciones_fisicas]
        nx = 'Filtracion glomerural'
    elif (tipo == 7):
        # GRAFICA PARA LA TA SISTOLICA
        x = [float(exploracion_fisica.TA_sistolica) for exploracion_fisica in exploraciones_fisicas]
        nx = 'TA sistolica'
    elif (tipo == 8):
        # GRAFICA PARA LA TA DIASTOLICA
        x = [float(exploracion_fisica.TA_diastolica) for exploracion_fisica in exploraciones_fisicas]
        nx = 'TA diastolica'
    elif (tipo == 9):
        # GRAFICA PARA LA FRECUENCIA CARDIACA
        x = [exploracion_fisica.frecuencia_cardiaca for exploracion_fisica in exploraciones_fisicas]
        nx = 'Frecuencia cardiaca'
    elif (tipo == 10):
        # GRAFICA PARA LA FRECUENCIA RESPIRATORIA
        x = [exploracion_fisica.frecuencia_respiratoria for exploracion_fisica in exploraciones_fisicas]
        nx = 'Frecuencia respiratoria'
    elif (tipo == 11):
        # GRAFICA PARA LA FRECUENCIA TEMPERATURA
        x = [exploracion_fisica.temperatura for exploracion_fisica in exploraciones_fisicas]
        nx = 'Temperatura'

    fig, ax = plt.subplots()
    ax.plot(fechas, x, marker='o', linestyle='-', color='blue')

    for fecha, valor in zip(fechas, x):
        ax.annotate(f'{valor}', (fecha, valor), textcoords="offset points", xytext=(0, 10), ha='center')

    ax.set_xlabel('Fecha')
    ax.set_ylabel(nx)

    ax.set_title('Datos da lo largo del tiempo')
    ax.tick_params(axis='x', rotation=45)
    fig.tight_layout()

    # GUARDAR GRAFICO COMO  BYTESIO
    buffer = io.BytesIO()
    canvas = FigureCanvasAgg(fig)
    canvas.print_png(buffer)
    buffer.seek(0)
    plt.close(fig)
    # CONVERTIR EL GRAFICO A BASE64
    image_png = buffer.getvalue()
    buffer.close()
    graphic = base64.b64encode(image_png).decode('utf-8')
    return HttpResponse('<img src="data:image/png;base64,{}" alt="Gráfica">'.format(graphic))

# Clase para acceder a la interfaz de visualizacion de graficas generales de todos los pacientes
class Graficas(View):

    @method_decorator(login_required(login_url='login'), name='dispatch')
    def get(self, request):
        usuario_id = Usuario.objects.get(id_usuario=request.user)
        esp = Especialista.objects.get(id_usuario=usuario_id.id)
        return render(request, "ventanas_especialista/graficas_especialista.html", {'esp': esp})

# Funcion para obtener las graficas de los usuarios
def grafica_EXP(request, id, tipo):
    pacientes = Solicitudes.objects.filter(id_especialista_id=id, estatus='A')
    if (tipo == 1):
        # PARA DETERMINAR EL GENERO DE LOS PACIENTES
        x = pacientes.filter(id_paciente__genero='M').count()
        y = pacientes.count() - x
        z = [x, y]
        n = ['Hombres', 'Mujeres']
        t = 'Porcentaje de pacientes por genero'
        myexplode = [0.1, 0]
    elif (tipo == 2):
        # PARA SELECCIONAR LOS PACIENTES QUE TIENEN LA PATOLOGIA DE DIABETES REGISTRADA
        x = pacientes.filter(id_paciente__ant_patologicos__patologia='Diabetes').count()
        x2 = pacientes.filter(id_paciente__ant_patologicos__patologia='Prediabetes').count()
        y = pacientes.count() - (x + x2)
        z = [x, y, x2]
        n = ['Diabeticos', 'No diabeticos', 'Prediabeticos']
        t = 'Porcentaje de pacientes Diabeticos'
        myexplode = [0.2, 0, 0]
    elif (tipo == 3):
        # PARA SELECCIONAR LOS PACIENTES CON INSUFICIENCIA RENAL
        x = pacientes.filter(id_paciente__ant_patologicos__patologia='Insuficiencia renal').count()
        x2 = pacientes.filter(id_paciente__ant_patologicos__patologia='Enfermedad renal').count()
        x3 = pacientes.filter(id_paciente__ant_patologicos__patologia='Enfermedad renal temprana').count()
        y = pacientes.count() - (x + x2 + x3)
        z = [x, x2, x3, y]
        n = ['Insuficiencia renal', 'Enfermedad renal', 'Enfermedad renal temprana', 'Normal']
        t = 'Porcentaje de pacientes con enfermedades renales'
        myexplode = [0.2, 0, 0, 0]
    elif (tipo == 4):
        # PARA SELECCIONAR LOS PACIENTES CON PROBLEMAS DE PRESION
        x = pacientes.filter(id_paciente__ant_patologicos__patologia='Elevada').count()
        x2 = pacientes.filter(id_paciente__ant_patologicos__patologia='Hipertensión nivel 1').count()
        x3 = pacientes.filter(id_paciente__ant_patologicos__patologia='Hipertensión nivel 2').count()
        x4 = pacientes.filter(id_paciente__ant_patologicos__patologia='Crisis de hipertensión').count()
        y = pacientes.count() - (x + x2 + x3 + x4)
        z = [x, x2, x3, x4, y]

        n = ['Elevada', 'Hipertensión nivel 1', 'Hipertensión nivel 2', 'Crisis de hipertensión', 'Normal']
        t = 'Porcentaje de pacientes con problemas de la presión'
        myexplode = [0, 0, 0, 0.2, 0]

    # Se filtran los labels y valores para no mostrar 0
    n_filtrados = [categoria for categoria, valor in zip(n, z) if valor != 0]
    z_filtrados = [valor for valor in z if valor != 0]
    myexplode_filtrado = [aux for aux, valor in zip(myexplode, z) if valor != 0]

    fig, ax = plt.subplots(figsize=(8, 8))
    ax.pie(z_filtrados, labels=n_filtrados, autopct='%1.1f%%', explode=myexplode_filtrado, )
    ax.legend(n_filtrados, loc='upper right', bbox_to_anchor=(1, 1))
    ax.set_title(t, pad=40)

    buffer = io.BytesIO()
    canvas = FigureCanvasAgg(fig)
    canvas.print_png(buffer)
    buffer.seek(0)
    plt.close(fig)
    # CONVERTIR EL GRAFICO A BASE64
    image_png = buffer.getvalue()
    buffer.close()
    graphic = base64.b64encode(image_png).decode('utf-8')
    return HttpResponse('<img src="data:image/png;base64,{}" alt="Gráfica">'.format(graphic))