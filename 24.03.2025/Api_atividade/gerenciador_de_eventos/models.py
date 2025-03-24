from django.db import models


class Eventos(models.Model):
    nome = models.CharField(max_length=255)
    descricao = models.TextField()
    data = models.DateField()
    local = models.CharField(max_length=300)
    escolhas_combustivel = (
          ('MÚSICA','Música'),
          ('PALESTRA', 'Palestra'),
          ('WORKSHOP','Workshop'),
     )
    categoria = models.CharField(max_length=8, choices=escolhas_combustivel)

    def __str__(self):
        return self.nome


