from django.db import models
from .modelTipoComidas import tipoComida
from .modelMenu import menu
class comida(models.Model):
    id = models.AutoField(primary_key=True)
    tipoComida = models.ForeignKey(tipoComida, on_delete=models.DO_NOTHING, related_name='comidas')
    verduras = models.IntegerField()
    frutas = models.IntegerField()
    cereales = models.IntegerField()
    leguminosas = models.IntegerField()
    origenAni = models.IntegerField()
    leche = models.IntegerField()
    grasas = models.IntegerField()
    azucares = models.IntegerField()
    idMenu = models.ForeignKey(menu, on_delete=models.DO_NOTHING)

    class Meta:
        app_label = 'moduloNutricion'