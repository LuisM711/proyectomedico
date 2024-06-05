from django.db import models

class Unidad(models.Model):
    id = models.AutoField(primary_key=True)
    unidad = models.TextField()
    
    class Meta:
        app_label = 'moduloNutricion'

class Tipo(models.Model):
    id = models.AutoField(primary_key=True)
    tipo = models.TextField()

    class Meta:
        app_label = 'moduloNutricion'

class Alimento(models.Model):
    id = models.AutoField(primary_key=True)
    nombre = models.TextField()
    tipo = models.ForeignKey(Tipo, on_delete=models.DO_NOTHING)
    porcion = models.FloatField()
    uni = models.ForeignKey(Unidad, on_delete=models.DO_NOTHING)
    peso = models.TextField()
    peso_neto = models.TextField()
    energia = models.TextField()
    proteina = models.TextField()
    lipidos = models.TextField()
    carbos = models.TextField()
    ag_satur = models.TextField()
    ag_mono = models.TextField()
    ag_poli = models.TextField()
    colesterol = models.TextField()
    azucar = models.TextField()
    fibra = models.TextField()
    vita_A = models.TextField()
    aci_asc = models.TextField()
    aci_foli = models.TextField()
    calcio = models.TextField()
    hierro = models.TextField()
    potasio = models.TextField()
    sodio = models.TextField()
    fosforo = models.TextField()
    etanol = models.TextField()
    ig = models.TextField()
    carga_gli = models.TextField()

    class Meta:
        app_label = 'moduloNutricion'




