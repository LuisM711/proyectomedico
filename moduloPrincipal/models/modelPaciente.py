from django.db import models
from django.db import models
from django.contrib.auth.models import User
from .modelUsuario import Usuario
class Paciente(models.Model):
    id_usuario = models.ForeignKey(Usuario, on_delete=models.DO_NOTHING)
    peso = models.FloatField()
    talla = models.FloatField()
    creatinina = models.FloatField(default=0)
    genero = models.CharField(max_length=1, default="M")  # MASCULINO (M), FEMENINO(F)
    estado_civil = models.CharField(max_length=1)
    estilo_vida = models.CharField(max_length=1)
    estatus = models.CharField(max_length=1, default=1)

    class Meta:
        app_label = 'moduloPrincipal'