from django.db import models
from django.db import models
from django.contrib.auth.models import User
from .modelCita import Cita
class Tratamiento(models.Model):
    id_cita = models.ForeignKey(Cita, on_delete=models.DO_NOTHING)
    tipo = models.BooleanField()
    descripcion = models.TextField()

    class Meta:
        app_label = 'moduloPrincipal'