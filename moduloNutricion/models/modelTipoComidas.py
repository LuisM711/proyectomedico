from django.db import models
from django.contrib.auth.models import User
class tipoComida(models.Model):
    id = models.AutoField(primary_key=True)
    comida = models.CharField(max_length=20)
    
    class Meta:
        app_label = 'moduloNutricion'