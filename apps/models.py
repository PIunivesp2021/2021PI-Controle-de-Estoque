from django.db import models



# Create your models here.
class Controle(models.Model):
    Empenho = models.IntegerField()
    Nota_Fiscal = models.IntegerField()
    Material = models.CharField(max_length=100)
    Data_Envio = models.DateField('data', null=True, blank=True)
    Obs = models.CharField(max_length=150)
