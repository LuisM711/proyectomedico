from django.db import models
from django.db import models
from django.contrib.auth.models import User

from .modelCita import Cita


class Exploracion_fisica(models.Model):
    id_cita = models.ForeignKey(Cita, on_delete=models.DO_NOTHING)
    peso = models.FloatField()
    talla = models.FloatField()
    glucosa = models.IntegerField()
    TA_sistolica = models.CharField(max_length=20)
    TA_diastolica = models.CharField(max_length=20)
    frecuencia_cardiaca = models.IntegerField()
    frecuencia_respiratoria = models.IntegerField()
    temperatura = models.FloatField()
    descripcion = models.TextField()
    imc = models.FloatField(default=0.0)
    creatinina = models.FloatField(default=0.0)
    filtracion_glomerular = models.FloatField(default=0.0)

    class Meta:
        app_label = 'moduloPrincipal'