from django.db import models
from django.core.validators import RegexValidator
from django.utils.translation import gettext_lazy as _
from django.contrib.auth.models import AbstractUser # Utilizando o modelo pronto de usuário na onde os seguintes itens já são solicitados
"""
1 - Nome do usuário (username)
2 - Primeiro nome (first_name)
3 - Ultimo nome (last_name)
4 - Email (email)
5 - Organização (is_staff)
6 - Se a conta está ativada (is_active)
7 - A data que se juntou (date_joined)

(Para acessar todas as informações CRTL + CLICK🖱)
"""

# Utilizando o validator para validar se o usuário vai colocar o telefone corretamente 
telefone_validator = RegexValidator(
    regex=r'^\+?[\d\s\-\(\)]{10,20}$',
    message="Informe um número de telefone válido."
)

# Utilizando o AbstractUser para criar um usuário, o usuário professor que será manipulado somente pelo Gestor
class Usuario(AbstractUser):
    TIPO_CHOICES = [
        ('G', 'Gestor'),
        ('P', 'Professor')
    ]

    tipo = models.CharField(max_length=1, choices=TIPO_CHOICES, default='P')
    ni = models.PositiveIntegerField(_("Número de identificação"), unique=True)
    telefone = models.CharField(_("Número de telefone padrão '(xx)xxxxx-xxxx'"),
        max_length= 30,
        validators=[telefone_validator],
        help_text="O número deve ser passado neste modelo (xx)xxxxx-xxxx"
    )
    data_contratacao = models.DateField(_("Data de contratação"))
    data_nascimento = models.DateField(_("A data de nascimento do usuário"))

    REQUIRED_FIELDS = ['ni', 'data_contratacao', 'data_nascimento']

    def __str__(self):
        return f'{self.username} ({self.get_tipo_display()})'


# Uma disciplique tem como chave estrangeira professor
class Disciplina(models.Model):
    nome = models.CharField(_("Nome da discilplina, ex:'Fisíca' "),max_length=255)
    curso = models.CharField(_("Qual curso essa matéria está?"),max_length=255)
    carga_horario = models.PositiveIntegerField(_("Quantas horas da matéria"), default=100)
    descricao = models.TextField(_("Sobre a matéria"))
    professor = models.ForeignKey(Usuario, on_delete=models.SET_NULL, null= True, blank= True, limit_choices_to={'tipo':'P'},verbose_name=_("Professor que ministra essa disciplina"))
    
    def __str__(self):
        return self.nome

class Sala(models.Model):
    nome = models.CharField(_("Nome da sala, ex: 'sala verde'"),max_length=90)
    tamanho = models.PositiveIntegerField()
    capacidade = models.PositiveIntegerField(default=50)

    def __str__(self):
        return self.nome

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
    professor = models.ForeignKey(Usuario, on_delete=models.SET_NULL, null= True, blank= True, limit_choices_to={'tipo':'P'},verbose_name=_("Escolha qual professor"))
    disciplina = models.ForeignKey(Disciplina, on_delete=models.CASCADE,verbose_name=_("A disciplina"))