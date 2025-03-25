from django.db import models

class Postagem(models.Model):
    titulo = models.CharField(max_length=255) #titulo da postagem limitado a 255 caracteres
    conteudo = models.TextField()# o conteudo que não limitamos 
    data_criacao = models.DateTimeField(auto_now_add=True)#A data que o post foi criado 

    def __str__(self):
        return self.titulo
