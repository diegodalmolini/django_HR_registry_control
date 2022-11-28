# Generated by Django 4.1.3 on 2022-11-28 21:32

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Benefits',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('benefit', models.CharField(help_text='Escolha o tipo de plano:', max_length=12, verbose_name='Benificio')),
                ('user', models.CharField(help_text='Escolha o usuário que irá utilizar o plano.', max_length=50, verbose_name='Usuário')),
                ('value', models.FloatField(help_text='Informe o valor do plano.', verbose_name='Valor')),
            ],
        ),
        migrations.CreateModel(
            name='Departments',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50, verbose_name='Setor')),
            ],
            options={
                'verbose_name': 'Setor',
                'verbose_name_plural': 'Setores',
            },
        ),
        migrations.CreateModel(
            name='Dependents',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(help_text='Primeiro nome do dependente.', max_length=50, verbose_name='Nome')),
                ('last_name', models.CharField(help_text='Sobrenome do dependente.', max_length=50, verbose_name='Sobrenome')),
                ('age', models.IntegerField(help_text='Idade do dependente.', verbose_name='Idade')),
                ('relationship', models.CharField(help_text='O parentesco em relação ao colaborador.', max_length=50, verbose_name='Parentesco')),
            ],
        ),
        migrations.CreateModel(
            name='Epis',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('epi', models.CharField(choices=[('oculos', 'Óculos de segurança'), ('luva', 'Luva de proteção'), ('creme', 'Creme de proteção'), ('sapato', 'Sapato de segurança')], help_text='Escolha o tipo de EPI.', max_length=6, verbose_name='EPI')),
                ('last_give', models.DateField(help_text='Data da ultima entrega de EPI', max_length=9, verbose_name='Data de entrega')),
                ('next_change', models.DateField(help_text='Data da próxima troca de EPI', max_length=9, verbose_name='Data de troca')),
            ],
        ),
        migrations.CreateModel(
            name='Feedbacks',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('type', models.CharField(choices=[('positivo', 'Positivo'), ('corretivo', 'Corretivo'), ('redirecionador', 'Redirecionador'), ('outros', 'Outros')], help_text='Escolha o tipo do feedback.', max_length=14, verbose_name='Tipo')),
                ('description', models.TextField(help_text='Descreva a situação da ocorrência.', max_length=200, verbose_name='Descrição')),
                ('action', models.TextField(help_text='Descreva a ação tomada.', max_length=200, verbose_name='Ação')),
            ],
        ),
        migrations.CreateModel(
            name='Roles',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50, verbose_name='Cargo')),
            ],
            options={
                'verbose_name': 'Cargo',
                'verbose_name_plural': 'Cargos',
            },
        ),
        migrations.CreateModel(
            name='Scholarity',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('degree', models.CharField(choices=[('en_fundamental', 'Ensino Fundamental'), ('en_medio', 'Ensino Médio'), ('en_superior', 'Ensino Superior'), ('pos', 'Pós Graduação/Especialização'), ('mestrado', 'Mestrado'), ('Doutorado', 'Doutorado')], help_text='Escolha entre os tipos de niveis de formação.', max_length=14, verbose_name='Nível de Formação')),
                ('start_date', models.DateField(help_text='MM/AA', max_length=6, verbose_name='Data de ínicio')),
                ('conclusion_date', models.DateField(help_text='MM/AA', max_length=6, verbose_name='Data de conclusão')),
                ('situation', models.CharField(choices=[('incompleto', 'Incompleto'), ('completo', 'Completo'), ('cursando', 'Cursando')], max_length=10, verbose_name='Situação')),
            ],
        ),
        migrations.CreateModel(
            name='Trainings',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(help_text='Informe o nome do treinamento.', max_length=50, verbose_name='Nome')),
                ('instructor', models.CharField(help_text='Informe o nome do instrutor.', max_length=50, verbose_name='Instrutor')),
                ('duration', models.IntegerField(help_text='Carga horario do treinamento.', verbose_name='Carga horária')),
                ('description', models.TextField(help_text='Descreva sobre os assuntos abordados.', max_length=200, verbose_name='Descrição')),
                ('start_date', models.CharField(max_length=9, verbose_name='Data do inicio')),
                ('finish_date', models.CharField(max_length=9, verbose_name='Data de conclução')),
            ],
        ),
        migrations.CreateModel(
            name='Labor_data',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('admission', models.DateField(help_text='Data de admissão do colaborador.', max_length=9, verbose_name='Admissâo')),
                ('cbo', models.CharField(help_text='Informe o número do CBO.', max_length=7, verbose_name='CBO')),
                ('salary', models.FloatField(verbose_name='Salário')),
                ('superior', models.CharField(max_length=50, verbose_name='Superior imediato')),
                ('shift', models.CharField(choices=[('primeiro', 'Primeiro Turno'), ('segundo', 'Segundo Turno'), ('terceiro', 'Terceiro Turno'), ('normal', 'Normal')], max_length=8, verbose_name='Turno')),
                ('last_exam', models.DateField(help_text='Data do ultimo exame.', max_length=9, verbose_name='Ultimo exame')),
                ('next_exam', models.DateField(help_text='Data do próximo exame.', max_length=9, verbose_name='Próximo exame')),
                ('department', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='core.departments', verbose_name='Setor')),
                ('role', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='core.roles', verbose_name='Cargo')),
            ],
        ),
        migrations.CreateModel(
            name='Employee',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=50, verbose_name='Nome')),
                ('last_name', models.CharField(max_length=50, verbose_name='Sobrenome')),
                ('rg', models.IntegerField(verbose_name='RG')),
                ('cpf', models.CharField(max_length=14, verbose_name='CPF')),
                ('pis', models.CharField(max_length=14, verbose_name='PIS')),
                ('ct_number', models.IntegerField(verbose_name='Número da carteira de trabalho')),
                ('ct_series', models.IntegerField(verbose_name='Série da carteira de trabalho')),
                ('birthday', models.DateField(max_length=9, verbose_name='Data de nascimento')),
                ('internal_code', models.IntegerField(verbose_name='Código interno')),
                ('adress', models.CharField(max_length=100, verbose_name='Endereço')),
                ('phone', models.CharField(max_length=15, verbose_name='Telefone')),
                ('father_name', models.CharField(max_length=50, verbose_name='Nome do pai')),
                ('mother_name', models.CharField(max_length=50, verbose_name='Nome da mãe')),
                ('benefits', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='core.benefits', verbose_name='Benifícios')),
                ('dependents', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='core.dependents', verbose_name='Dependentes')),
                ('epis', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='core.epis', verbose_name='EPIs')),
                ('feedbacks', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='core.feedbacks', verbose_name='Feedbacks')),
                ('labor_data', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='core.labor_data', verbose_name='Dados laborais')),
                ('scholarity', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='core.scholarity', verbose_name='Escolaridade')),
                ('trainings', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='core.trainings', verbose_name='Treinamentos')),
            ],
        ),
    ]
