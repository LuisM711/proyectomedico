from django.db import models
from django.db import models
from django.contrib.auth.models import User
from .modelPaciente import Paciente
class Alergias(models.Model):
    id_paciente = models.ForeignKey(Paciente, on_delete=models.DO_NOTHING)
    nombre = models.CharField(max_length=100)

    class Meta:
        app_label = 'moduloPrincipal'