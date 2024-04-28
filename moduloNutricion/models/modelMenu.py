from django.db import models
from moduloPrincipal.models.modelEspecialista import Especialista
from moduloPrincipal.models.modelPaciente import Paciente

class menu(models.Model):
    id = models.AutoField(primary_key=True)
    idEsp = models.ForeignKey(Especialista, on_delete=models.DO_NOTHING)
    idPaciente = models.ForeignKey(Paciente, on_delete=models.DO_NOTHING)
    fecha = models.DateField

    class Meta:
        app_label = 'moduloNutricion'
