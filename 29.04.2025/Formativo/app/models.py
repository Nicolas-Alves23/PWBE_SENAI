from django.db import models
from django.core.validators import RegexValidator

# Utilizando o validator para validar se o usuário vai colocar o telefone corretamente 
telefone_validator = RegexValidator(
    regex=r'^\+?[\d\s\-\(\)]{10,20}$',
    message="Informe um número de telefone válido."
)

class Professor(models.Model):
    ni = models.PositiveIntegerField()
    nome = models.CharField(max_length=255)
    email = models.EmailField()
    telefone = models.CharField(
        max_length= 30,
        validators=[telefone_validator],
        help_text="O número deve ser passado neste modelo (xx)xxxxx-xxxx"
    )
    data_contratacao = models.DateField()
    data_nascimento = models.DateField()

class Disciplina(models.Model):
    nome = models.CharField(max_length=255)
    curso = models.CharField(max_length=255)
    carga_horario = models.PositiveIntegerField
    descricao = models.TextField()
    professor = models.ForeignKey(Professor, on_delete=models.CASCADE)

class Sala(models.Model):
    nome = models.CharField(max_length=90)
    tamanho = models.PositiveIntegerField()
    capacidade = models.PositiveIntegerField

class Reserva_ambiente(models.Model):
    data_inicio = models.DateField()
    data_termino = models.DateField()
    
    escolha_horario = (
        ('M', 'Manhã'),
        ('T', 'Tarde'),
        ('N', 'Noite')
    )

    periodo = models.CharField(max_length=1, choices=escolha_horario)
    
    sala = models.ForeignKey(Sala, on_delete=models.CASCADE)
    professor = models.ForeignKey(Professor, on_delete=models.CASCADE)
    disciplina = models.ForeignKey(Disciplina, on_delete=models.CASCADE)