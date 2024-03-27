from django.db import models
from django.db import models
from django.contrib.auth.models import User
from .modelEspecialista import Especialista
from .modelPaciente import Paciente
class Cita(models.Model):
    id_especialista = models.ForeignKey(Especialista, on_delete=models.DO_NOTHING)
    id_paciente = models.ForeignKey(Paciente, on_delete=models.DO_NOTHING)
    fecha = models.DateField()
    hora = models.TimeField()
    motivo = models.TextField()
    estatus = models.CharField(max_length=1)  # P=pendiente, B=baja, C=confirmada, A=atendida
    imagen = models.ImageField(upload_to='imagenes_citas', default='')

    class Meta:
        app_label = 'moduloPrincipal'