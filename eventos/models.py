from django.db import models
from django.contrib.auth.models import User


# Create your models here.
# esse arquivo é para tudo que o usuário fizer upload so sistema
class Events(models.Model):
    creator = models.ForeignKey(User,on_delete=models.DO_NOTHING, null = True, blank=True)
    nome = models.CharField(max_length=200) # charFiled é um campo que pode ser preenchido com caracteres
    descricao = models.TextField() # textfilel pode ser preenchido com caracteres mas não tem limite de qunatidade
    data_inicio = models.DateField()
    data_termino = models.DateField()
    carga_horaria = models.IntegerField()
    logo = models.ImageField(upload_to= "logos")

    participantes = models.ManyToManyField(User, related_name= "evento_participante", null=True, blank=True)

    #paletas de cores
    #fffffff
    cor_principal = models.CharField(max_length=7)
    cor_secundaria = models.CharField(max_length=7)
    cor_fundo = models.CharField(max_length=7)

    def __str__(self) -> str:
        return self.nome
    
class Certificado(models.Model):
        certificado = models.ImageField(upload_to="certificados")
        participante = models.ForeignKey(User, on_delete=models.DO_NOTHING)
        evento = models.ForeignKey(Events, on_delete=models.DO_NOTHING)
