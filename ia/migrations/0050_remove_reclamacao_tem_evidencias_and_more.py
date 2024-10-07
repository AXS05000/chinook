# Generated by Django 5.0.6 on 2024-10-07 12:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ia', '0049_remove_reclamacao_conclusao_final_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='reclamacao',
            name='tem_evidencias',
        ),
        migrations.AlterField(
            model_name='reclamacao',
            name='foi_feita_reuniao_pais',
            field=models.CharField(blank=True, choices=[('sim', 'Sim'), ('nao', 'Não'), ('nao_se_aplica', 'Não Se Aplica')], default='nao', max_length=13, null=True, verbose_name='Foi Feita a Reunião com os Pais'),
        ),
        migrations.AlterField(
            model_name='reclamacao',
            name='origem_reclamacao',
            field=models.CharField(blank=True, choices=[('reclame_aqui', 'Reclame Aqui'), ('fale_maple', 'Fale Maple'), ('ouvidoria_seb', 'Ouvidoria SEB'), ('ouvidoria_global', 'Ouvidoria Global'), ('redes_sociais', 'Redes Sociais'), ('outros', 'Outros')], max_length=50, null=True, verbose_name='Origem da Reclamacao'),
        ),
        migrations.AlterField(
            model_name='reclamacao',
            name='status',
            field=models.CharField(blank=True, choices=[('finalizado', 'Finalizado'), ('aguardando_escola', 'Aguardando retorno escola'), ('aguardando_escola_replica', 'Aguardando retorno escola replica'), ('escola_nao_retornou', 'Escola não retornou'), ('aguardando_responsavel', 'Aguardando retorno do responsável'), ('pendente', 'Pendente'), ('nivel_diretoria', 'Nível Diretoria')], max_length=50, null=True, verbose_name='Status'),
        ),
        migrations.AlterField(
            model_name='reclamacao',
            name='tem_ata',
            field=models.CharField(blank=True, choices=[('sim', 'Sim'), ('nao', 'Não'), ('nao_se_aplica', 'Não Se Aplica')], default='nao', max_length=13, null=True, verbose_name='Tem ATA ou outros documentos ?'),
        ),
        migrations.AlterField(
            model_name='reclamacao',
            name='tem_camera',
            field=models.CharField(blank=True, choices=[('sim', 'Sim'), ('nao', 'Não'), ('nao_se_aplica', 'Não Se Aplica')], default='nao', max_length=13, null=True, verbose_name='Tem fotos, vídeos, prints ou imagens?'),
        ),
        migrations.AlterField(
            model_name='reclamacao',
            name='tem_testemunha',
            field=models.CharField(blank=True, choices=[('sim', 'Sim'), ('nao', 'Não'), ('nao_se_aplica', 'Não Se Aplica')], default='nao', max_length=13, null=True, verbose_name='Tem Testemunha'),
        ),
    ]
