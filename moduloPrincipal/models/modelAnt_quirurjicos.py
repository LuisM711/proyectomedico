from django.db import models
from django.db import models
from django.contrib.auth.models import User
from .modelPaciente import Paciente
class Ant_quirurjicos(models.Model):
    id_paciente = models.ForeignKey(Paciente, on_delete=models.DO_NOTHING)
    tipo = models.CharField(max_length=100)
    tiempo = models.FloatField()

    class Meta:
        app_label = 'moduloPrincipal'