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