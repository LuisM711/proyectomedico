from django.db import models
from moduloPrincipal.models.modelEspecialista import Especialista
from moduloPrincipal.models.modelPaciente import Paciente
from moduloPrincipal.models.modelCita import Cita

class Menu_Bien(models.Model):
    id_cita = models.ForeignKey(Cita, on_delete=models.DO_NOTHING)
    especialista = models.ForeignKey(Especialista, on_delete=models.DO_NOTHING)
    paciente = models.ForeignKey(Paciente, on_delete=models.DO_NOTHING)
    menu=models.TextField()

    class Meta:
        app_label='moduloNutricion'