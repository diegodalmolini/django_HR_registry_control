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


