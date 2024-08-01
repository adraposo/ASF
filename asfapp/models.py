from django.db import models
from django.utils import timezone
from django.contrib.auth.models import AbstractUser

# Create your models here.

LISTA_CATEGORIAS = (
    ( "digital", "Estratégias Digital"),
    ( "vendas", "Vendas" ),
    ( "imagem" , "Comunicação Visual"),
    ( "financas" , "Finanças" )
)


class Curso(models.Model):
    titulo = models.CharField(max_length=100)
    thumb = models.ImageField(upload_to='thumb_aulas')
    descricao = models.TextField(max_length=1000)
    categoria = models.CharField(max_length=30, choices=LISTA_CATEGORIAS)
    visualizacoes = models.IntegerField(default=0)
    data_criacao = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.titulo

class Aula(models.Model):
    curso = models.ForeignKey("Curso", related_name="aulas", on_delete=models.CASCADE)
    titulo = models.CharField(max_length=100)
    video = models.URLField()

    def __str__(self):
        return self.curso.titulo + " - " + self.titulo

class Usuario(AbstractUser):
    aulas_assistidas = models.ManyToManyField("Curso")