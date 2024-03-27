from django.db import models
from django.db import models
from django.contrib.auth.models import User
class Usuario(models.Model):
    id_usuario = models.ForeignKey(User, on_delete=models.DO_NOTHING, default=1)
    fecha_nacimiento = models.DateField()
    foto = models.ImageField(upload_to='imagenes_usuario')
    tipo = models.CharField(max_length=1, null=False, default="P")  # P= Paciente, E=Especialista

    class Meta:
        app_label = 'moduloPrincipal'