from django.db import models
from django.db import models
from django.contrib.auth.models import User
from .modelUsuario import Usuario
from .modelEspecialidades import Especialidades
class Especialista(models.Model):
    id_usuario = models.ForeignKey(Usuario, on_delete=models.DO_NOTHING)
    id_especialidad = models.ForeignKey(Especialidades, on_delete=models.DO_NOTHING)
    cedula = models.CharField(max_length=8)
    info_ad = models.TextField()
    horario = models.TextField()
    """ 10:00-13:00, 14:00-18:00;
        10:00-13:00, 14:00-18:00;
        10:00-13:00, 14:00-18:00;
        10:00-13:00, 14:00-18:00;
        10:00-13:00, 14:00-18:00;
        10:00-14:00;
        """
    estatus = models.CharField(max_length=1)  # 0 = dado de baja, 1=Activo

    class Meta:
        app_label = 'moduloPrincipal'