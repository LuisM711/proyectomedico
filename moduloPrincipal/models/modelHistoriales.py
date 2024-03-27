from django.db import models
from django.db import models
from django.contrib.auth.models import User
from .modelPaciente import Paciente
class Historiales(models.Model):
    id_paciente = models.ForeignKey(Paciente, on_delete=models.DO_NOTHING)
    ruta_doc = models.FileField(upload_to='Historiales', default='')

    class Meta:
        app_label = 'moduloPrincipal'