from django.db import models

class Feedbacks(models.Model):
    
    TYPES_CHOICES = (
        ('positivo', 'Positivo'),
        ('corretivo', 'Corretivo'),
        ('redirecionador', 'Redirecionador'),
        ('outros', 'Outros')
    )

    type = models.CharField('Tipo', max_length=14, choices=TYPES_CHOICES, help_text='Escolha o tipo do feedback.')
    description = models.TextField('Descrição', max_length=200, help_text='Descreva a situação da ocorrência.')
    action = models.TextField('Ação', max_length=200, help_text='Descreva a ação tomada.')

    
    class Meta:
        verbose_name = 'Feedback'
        verbose_name_plural = 'Feedbacks'

    def __str__(self):
        return self.type

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

    
    class Meta:
        verbose_name = 'EPI'
        verbose_name_plural = 'EPIs'

    def __str__(self):
        return f'{self.epi} - {self.last_give} > {self.next_change}'


class Benefits(models.Model):

    BENEFITS_CHOICES = (
        ('saude/personal', 'Plano de saúde/Personal'),
        ('saude/nacional', 'Plano de saúde/Nacional'),
        ('odontologico/c/protese', 'Plano odontológico com prótese'),
        ('odontologico/s/protese', 'Plano odontológico sem prótese'),
    )


    benefit = models.CharField('Benificio', max_length=22, choices=BENEFITS_CHOICES , help_text='Escolha o tipo de plano:')
    user = models.CharField('Usuário', max_length=50, help_text='Escolha o usuário que irá utilizar o plano.')
    value = models.FloatField('Valor', help_text='Informe o valor do plano.')

    
    class Meta:
        verbose_name = 'Benefício'
        verbose_name_plural = 'Benefícios'

    def __str__(self):
        return f'{self.user} - {self.benefit} - R${self.value}'

class Scholarity(models.Model):

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
    degree = models.CharField('Nível de Formação', max_length=14, choices=DEGREE_CHOICES, help_text='Escolha entre os tipos de niveis de formação.')
    start_date = models.DateField('Data de ínicio', max_length=6, help_text='MM/AA')
    conclusion_date = models.DateField('Data de conclusão', max_length=6, help_text='MM/AA')
    situation = models.CharField('Situação', max_length=10, choices=SITUATION_CHOICES)

    class Meta:
        verbose_name = 'Escolaridade'
        verbose_name_plural = 'Escolaridades'


    def __str__(self):
        return f'{self.degree} - {self.situation}'


class Dependents(models.Model):

    first_name = models.CharField('Nome', max_length=50, help_text='Primeiro nome do dependente.')
    last_name = models.CharField('Sobrenome', max_length=50, help_text='Sobrenome do dependente.')
    age = models.IntegerField('Idade', help_text='Idade do dependente.')
    relationship = models.CharField('Parentesco', max_length=50, help_text='O parentesco em relação ao colaborador.')

    class Meta:
        verbose_name = 'Dependente'
        verbose_name_plural = 'Dependentes'


    def __str__(self):
        return f'{self.first_name} {self.last_name} - {self.relationship}'


class Roles(models.Model):

    name = models.CharField('Cargo', max_length=50)

    class Meta:
        verbose_name = 'Cargo'
        verbose_name_plural = 'Cargos'


    def __str__(self):
        return f'{self.name}'


class Departments(models.Model):

    name = models.CharField('Setor', max_length=50)

    class Meta:
        verbose_name = 'Setor'
        verbose_name_plural = 'Setores'


    def __str__(self):
        return f'{self.name}'



class Trainings(models.Model):

    name = models.CharField('Nome', max_length=50, help_text='Informe o nome do treinamento.')
    instructor = models.CharField('Instrutor', max_length=50, help_text='Informe o nome do instrutor.')
    duration = models.IntegerField('Carga horária', help_text='Carga horario do treinamento.')
    description = models.TextField('Descrição', max_length=200, help_text='Descreva sobre os assuntos abordados.') 
    start_date = models.CharField('Data do inicio', max_length=9)
    finish_date = models.CharField('Data de conclução', max_length=9)

    class Meta:
        verbose_name = 'Treinamento'
        verbose_name_plural = 'Treinamentos'


    def __str__(self):
        return self.name


class Personal_data(models.Model):
    first_name = models.CharField('Nome', max_length=50)
    last_name = models.CharField('Sobrenome', max_length=50)
    rg = models.IntegerField('RG')
    cpf = models.CharField('CPF', max_length=14)
    birthday = models.DateField('Data de nascimento', max_length=9)
    adress = models.CharField('Endereço', max_length=100)
    phone = models.CharField('Telefone', max_length=15)
    father_name = models.CharField('Nome do pai', max_length=50)
    mother_name = models.CharField('Nome da mãe', max_length=50)

    class Meta:
        verbose_name = 'Dado pessoal'
        verbose_name_plural = 'Dados pessoais'

    def __str__(self):
        return f'{self.first_name} {self.last_name}'


class Employee(models.Model):

    SHIFT_CHOICES = (
        ('primeiro','Primeiro Turno'),
        ('segundo','Segundo Turno'),
        ('terceiro','Terceiro Turno'),
        ('normal','Normal'),
    )
    admission = models.DateField('Admissâo', max_length=9, help_text='Data de admissão do colaborador.')
    role = models.ForeignKey(Roles, verbose_name='Cargo', on_delete=models.CASCADE)
    cbo = models.CharField('CBO', max_length=7, help_text='Informe o número do CBO.')
    department = models.ForeignKey(Departments, verbose_name='Setor', on_delete=models.CASCADE)
    salary = models.FloatField('Salário')
    superior = models.CharField('Superior imediato', max_length=50)
    shift = models.CharField('Turno', max_length=8, choices=SHIFT_CHOICES)
    last_exam = models.DateField('Ultimo exame', max_length=9, help_text='Data do ultimo exame.')
    next_exam = models.DateField('Próximo exame', max_length=9, help_text='Data do próximo exame.')
    pis = models.CharField('PIS', max_length=14)
    ct_number = models.IntegerField('Número da carteira de trabalho')
    ct_series = models.IntegerField('Série da carteira de trabalho')
    internal_code = models.IntegerField('Código interno')
    dependents = models.ForeignKey(Dependents, verbose_name='Dependentes', on_delete=models.CASCADE)
    personal_data = models.OneToOneField(Personal_data, verbose_name='Pessoas', on_delete=models.CASCADE)
    trainings = models.ForeignKey(Trainings, verbose_name='Treinamentos', on_delete=models.CASCADE)
    feedbacks = models.ForeignKey(Feedbacks, verbose_name='Feedbacks', on_delete=models.CASCADE)
    epis = models.ForeignKey(Epis, verbose_name='EPIs', on_delete=models.CASCADE)
    benefits = models.ForeignKey(Benefits, verbose_name='Benifícios', on_delete=models.CASCADE)
    scholarity = models.ForeignKey(Scholarity, verbose_name='Escolaridade', on_delete=models.CASCADE)

    class Meta:
        verbose_name = 'Funcionario'
        verbose_name_plural = 'Funcionarios'

    def __str__(self):
        return f'{self.people.first_name} {self.people.last_name} - Cargo: {self.role}'
