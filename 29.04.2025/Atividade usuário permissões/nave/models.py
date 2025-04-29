from django.db import models
from django.contrib.auth.models import AbstractUser

class Empresa(models.Model):
    nome = models.CharField(max_length=100)
    cnpj = models.CharField(max_length=100)

class Usuario(AbstractUser):
    apelido = models.CharField(max_length=100, null=True, blank=True)    
    telefone = models.CharField(max_length=100, null=True, blank=True)  

    genero = models.CharField(max_length=100, choices=(('M','Masculino'),('F','Feminino'), ('N','Prefiro nao dizer')), null=True, blank=True)    

    escolha_funcao = (
        ('G','Gestor'),
        ('E','Estagiario'),
        ('A','Aprendiz'),
        ('M','Meio oficial')
    )

    colaborador = models.CharField(max_length=1,choices=escolha_funcao,default='M')

    REQUIRED_FIELDS = ['colaborador']

    empresa = models.ForeignKey(Empresa, on_delete=models.CASCADE, null=True, blank=True)