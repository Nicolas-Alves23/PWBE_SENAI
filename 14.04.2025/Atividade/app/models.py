from django.db import models
from django.contrib.auth.models import AbstractUser

class UsuarioDS16(AbstractUser):
    biografia = models.TextField()
    data_nascimento = models.DateField()
    idade = models.PositiveIntegerField()
    pets = models.PositiveIntegerField()
    telefone = models.CharField(max_length=255, null= True , blank=True)
    endereco = models.CharField(max_length=255, null= True , blank=True)
    escolaridade = models.CharField(max_length=255, null= True , blank=True)
    
    REQUIRED_FIELDS = ['data_nascimento', 'idade' ]

    def __str__(self):
        return self.username