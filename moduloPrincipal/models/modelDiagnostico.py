from django.db import models
from django.db import models
from django.contrib.auth.models import User
from .modelCita import Cita
class Diagnostico(models.Model):
    id_cita = models.ForeignKey(Cita, on_delete=models.DO_NOTHING)
    descripcion = models.TextField()
    ruta_doc = models.FileField(upload_to='Historiales', default='')

    class Meta:
        app_label = 'moduloPrincipal'