# Generated by Django 5.0.6 on 2024-10-03 20:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ia', '0045_alter_reclamacao_foi_feita_reuniao_pais_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='reclamacao',
            name='aluno',
            field=models.CharField(blank=True, max_length=255, null=True, verbose_name='Aluno'),
        ),
        migrations.AlterField(
            model_name='reclamacao',
            name='conclusao_final',
            field=models.TextField(blank=True, null=True, verbose_name='Conclusao Final'),
        ),
        migrations.AlterField(
            model_name='reclamacao',
            name='data_conclusao',
            field=models.DateField(blank=True, null=True, verbose_name='Data da Conclusao'),
        ),
        migrations.AlterField(
            model_name='reclamacao',
            name='data_reclamacao',
            field=models.DateField(blank=True, null=True, verbose_name='Data Reclamacao'),
        ),
        migrations.AlterField(
            model_name='reclamacao',
            name='descricao_reclamacao',
            field=models.TextField(blank=True, null=True, verbose_name='Descricao da Reclamacao'),
        ),
        migrations.AlterField(
            model_name='reclamacao',
            name='email',
            field=models.EmailField(blank=True, max_length=255, null=True, verbose_name='Email'),
        ),
        migrations.AlterField(
            model_name='reclamacao',
            name='foi_feita_reuniao_pais',
            field=models.CharField(blank=True, choices=[('sim', 'Sim'), ('nao', 'Não')], default='nao', max_length=3, null=True, verbose_name='Foi Feita a Reunião com os Pais'),
        ),
        migrations.AlterField(
            model_name='reclamacao',
            name='investigacao',
            field=models.TextField(blank=True, null=True, verbose_name='Investigacao'),
        ),
        migrations.AlterField(
            model_name='reclamacao',
            name='nome_responsavel',
            field=models.CharField(blank=True, max_length=255, null=True, verbose_name='Nome Responsavel'),
        ),
        migrations.AlterField(
            model_name='reclamacao',
            name='origem_reclamacao',
            field=models.CharField(blank=True, choices=[('reclame_aqui', 'Reclame Aqui'), ('fale_maple', 'Fale Maple'), ('social_media', 'Social Media'), ('ouvidoria_seb', 'Ouvidoria SEB'), ('redes_sociais', 'Redes Sociais'), ('outros', 'Outros')], max_length=50, null=True, verbose_name='Origem da Reclamacao'),
        ),
        migrations.AlterField(
            model_name='reclamacao',
            name='prioridade',
            field=models.CharField(blank=True, choices=[('baixa', 'Baixa'), ('media', 'Média'), ('alta', 'Alta')], max_length=50, null=True, verbose_name='Prioridade'),
        ),
        migrations.AlterField(
            model_name='reclamacao',
            name='status',
            field=models.CharField(blank=True, choices=[('aguardando_usuario', 'Aguardando retorno usuário'), ('finalizado', 'Finalizado'), ('aguardando_escola', 'Aguardando retorno escola'), ('sem_retorno_escola', 'Sem retorno da escola'), ('escola_nao_retornou', 'Escola não retornou'), ('pendente', 'Pendente'), ('aguardando_responsavel', 'Aguardando retorno do responsável')], max_length=50, null=True, verbose_name='Status'),
        ),
        migrations.AlterField(
            model_name='reclamacao',
            name='telefones',
            field=models.IntegerField(blank=True, null=True, verbose_name='Telefones'),
        ),
        migrations.AlterField(
            model_name='reclamacao',
            name='tem_ata',
            field=models.CharField(blank=True, choices=[('sim', 'Sim'), ('nao', 'Não')], default='nao', max_length=3, null=True, verbose_name='Tem ATA'),
        ),
        migrations.AlterField(
            model_name='reclamacao',
            name='tem_camera',
            field=models.CharField(blank=True, choices=[('sim', 'Sim'), ('nao', 'Não')], default='nao', max_length=3, null=True, verbose_name='Tem Câmera'),
        ),
        migrations.AlterField(
            model_name='reclamacao',
            name='tem_testemunha',
            field=models.CharField(blank=True, choices=[('sim', 'Sim'), ('nao', 'Não')], default='nao', max_length=3, null=True, verbose_name='Tem Testemunha'),
        ),
        migrations.AlterField(
            model_name='reclamacao',
            name='titulo',
            field=models.CharField(blank=True, max_length=255, null=True, verbose_name='Titulo'),
        ),
    ]
