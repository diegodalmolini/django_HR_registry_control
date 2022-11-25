from django.db import models

class Feedbacks(models.Model):
    
    TYPES_CHOICES = (
        ('positivo', 'Positivo'),
        ('corretivo', 'Corretivo'),
        ('redirecionador', 'Redirecionador'),
        ('outros', 'Outros')
    )

    type = models.CharField('Tipo', max_length=14, choices=TYPES_CHOICES, help_text='Escolha o tipo do feedback.')
    description = models.CharField('Descrição', max_length=200, help_text='Descreva a situação da ocorrência.')
    action = models.CharField('Ação', max_length=200, help_text='Descreva a ação tomada.')


class Epis(models.Model):
    
    EPI_CHOICES = (
        ('oculos', 'Óculos de segurança'),
        ('luva', 'Luva de proteção'),
        ('creme', 'Creme de proteção'),
        ('sapato', 'Sapato de segurança')
    )

    epi = models.CharField('EPI', max_length=6, choices=EPI_CHOICES, help_text='Escolha o tipo de EPI.')
    last_give = models.DateField('Data de entrega', max_length=9, help_text='Data da ultima entrega de EPI')
    next_change = models.DateField('Data de troca', max_length=9, help_text='Data da próxima troca de EPI')


class Advantage(models.Model):

    ADVANTAGE_CHOICES = (
        ('saude', 'Plano de saúde'),
        ('odontologico', 'Plano odontológico')
    )

    advantage = models.CharField('Benificio', max_length=12, help_text='Escolha o tipo de plano:')
    user = models.CharField('Usuário', max_length=50, help_text='Escolha o usuário que irá utilizar o plano.')
    value = models.DecimalField('Valor', help_text='Informe o valor do plano.')


class Scholarity(models.Models):

    DEGREE_CHOICES = (
        ('en_fundamental', 'Ensino Fundamental'),
        ('en_medio', 'Ensino Médio'),
        ('en_superior', 'Ensino Superior'),
        ('pos', 'Pós Graduação/Especialização'),
        ('mestrado', 'Mestrado'),
        ('Doutorado', 'Doutorado')
    )

    SITUATION_CHOICES = (
        ('incompleto', 'Incompleto'),
        ('completo', 'Completo'),
        ('cursando', 'Cursando')
    )
    degree = models.CharField('Nível de Formação', max_length=14, choices=DEGREE_CHOICES , help_text='Escolha entre os tipos de niveis de formação.')
    start_date = models.DateField('Data de ínicio', max_length=6, help_text='MM/AA')
    conclusion_date = models.DateField('Data de conclusão', max_length=6, help_text='MM/AA')
    situation = models.CharField('Situação', max_length=10, choices=SITUATION_CHOICES)