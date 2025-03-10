from django.db import models

class Biblioteca(models.Model):
    titulo = models.CharField(max_length=255)
    autor = models.CharField(max_length=255)
    ano_pubi = models.IntegerField()
    descricao = models.TextField()

    def __str__(self):
        return self.titulo
# Create your models here.
