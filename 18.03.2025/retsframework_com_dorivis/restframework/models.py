from django.db import models
# Meu modelo de banco de dados 
class Carros(models.Model):
     nome = models.CharField(max_length=255)#guardando o nome do carro
     marca = models.CharField(max_length=255)#a marca do carro
     qtdRodas = models.PositiveIntegerField()#quantidade de rodas no carro 
     ano = models.PositiveIntegerField()# o ano que o carro foi contruido 
     cor = models.CharField(max_length=255) # cor do carro 
     escolhas_combustivel = (# as escolhas possiveis de combustivel 
          ('GASOLINA','Gasolina'),
          ('ETANOL', 'Etanol'),
          ('GNV','GNV'),
          ('ELETRICO','Eletrico'),
          ('ALCOOL','Alcool'),
          ('DIESEL','Diesel'),
          ('FB','FeedBack'),
     )
     combustivel = models.CharField(max_length=9, choices=escolhas_combustivel)# chamando as possiveis escolhas

     def __str__(self):
          return self.nome    