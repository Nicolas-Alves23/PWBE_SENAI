from django.db import models
from django.contrib.auth.models import AbstractUser

class UsuarioDS16(AbstractUser):
    idade = models.PositiveIntegerField
    telefone = models.CharField(max_length=30)
    endereco = models.TextField()
    escolaridade = models.CharField(max_length=255)
    biografia = models.TextField()
    animais = models.PositiveIntegerField 

    REQUIRED_FIELDS = ['idade', 'telefone', 'animais' ]

    def __str__(self):
        return self.username