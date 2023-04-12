from django.db import models

# Create your models here.
class Events(models.Model):
    nome = models.CharField(max_length=200)
    descricao = models.TextField()
    dataInicio = models.DateField()
    dataTermino = models.DateField()
    carga = models.IntegerField()
    logo = models.ImageField(upload_to="logos")

    #paletas de cores
    #fffffff
    corprincipal = models.CharField(max_length=7)
    corsecundaria = models.CharField(max_length=7)
    corfundo = models.CharField(max_length=7)
