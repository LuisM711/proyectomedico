from django.db import models
from django.db import models
from django.contrib.auth.models import User
from .modelEspecialista import Especialista
from .modelPaciente import Paciente

class Solicitudes(models.Model):
    id_especialista = models.ForeignKey(Especialista, on_delete=models.DO_NOTHING)
    id_paciente = models.ForeignKey(Paciente, on_delete=models.DO_NOTHING)
    estatus = models.CharField(max_length=1)  # ACEPTADA (A), RECHAZADA(R), PENDIENTE(P), BAJA(B)

    class Meta:
        app_label = 'moduloPrincipal'