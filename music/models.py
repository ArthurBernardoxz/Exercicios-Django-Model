from django.db import models
from django.forms import CharField

# Create your models here.

class Musico(models.Model):
    musico = models.CharField(max_length=1000)
    email = models.CharField(max_length=1000)
    

    def _str_(self):
        return f"musico: {self.musico} email: {self.email}"

class EstiloMusical(models.Model):
    nome_estilo = models.CharField(max_length=1000)

    def _str_(self):
        return self.nome_estilo

class Banda(models.Model):
    nome_banda = models.CharField(max_length=1000)
    numero_integrantes = models.IntegerField(default = 0)
    numero_musicas = models.IntegerField(default = 0)
    estilo = models.ManyToManyField(EstiloMusical)
    musicos = models.ManyToManyField(Musico)



    def _str_(self):
        return f"Banda: {self.nome_banda}, numero de integrantes: {self.numero_integrantes}, numero de musicas: {self.numero_musicas}, estilo {self.estilo} e musicos: {self.musicos}"