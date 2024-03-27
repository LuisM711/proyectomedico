from django.db import models
from django.db import models
from django.contrib.auth.models import User


class Especialidades(models.Model):
    nombre = models.CharField(max_length=100)
    descripcion = models.TextField()
    # Los siguientes 2 campos son para validar si el especialista tiene acceso a registrar exploracion_fisica y tratamiento
    exploracion_fisica = models.CharField(max_length=2, default="si")
    diagnostico_tratamiento = models.CharField(max_length=2, default="si")

    class Meta:
        app_label = 'moduloPrincipal'