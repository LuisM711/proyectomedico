from django.db import models
from django.db import models
from django.contrib.auth.models import User
from .modelPaciente import Paciente
class Toxicomania(models.Model):
    id_paciente = models.ForeignKey(Paciente, on_delete=models.DO_NOTHING)
    nombre = models.CharField(max_length=100)
    cantidad = models.CharField(max_length=20)
    frecuencia = models.CharField(max_length=20)
    tiempo = models.FloatField()

    class Meta:
        app_label = 'moduloPrincipal'