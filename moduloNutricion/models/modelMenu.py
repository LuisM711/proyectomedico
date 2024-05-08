from django.db import models
from moduloPrincipal.models.modelEspecialista import Especialista
from moduloPrincipal.models.modelPaciente import Paciente
from moduloPrincipal.models.modelCita import Cita

class Menu(models.Model):
    id = models.AutoField(primary_key=True)
    id_cita = models.id_cita = models.ForeignKey(Cita, on_delete=models.DO_NOTHING)
    idEsp = models.ForeignKey(Especialista, on_delete=models.DO_NOTHING)
    idPaciente = models.ForeignKey(Paciente, on_delete=models.DO_NOTHING)
    fecha = models.DateField
    menu = models.TextField(max_length=100, default="")

    class Meta:
        app_label = 'moduloNutricion'
