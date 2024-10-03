# Generated by Django 5.0.6 on 2024-10-03 21:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ia', '0048_alter_reclamacao_escola_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='reclamacao',
            name='conclusao_final',
        ),
        migrations.AddField(
            model_name='reclamacao',
            name='parecer_final',
            field=models.TextField(blank=True, null=True, verbose_name='Parecer final da área'),
        ),
        migrations.AddField(
            model_name='reclamacao',
            name='resposta_enviada_reclamante',
            field=models.TextField(blank=True, null=True, verbose_name='Resposta enviada ao reclamante'),
        ),
        migrations.AddField(
            model_name='reclamacao',
            name='tem_evidencias',
            field=models.CharField(blank=True, choices=[('sim', 'Sim'), ('nao', 'Não'), ('nao_tem', 'Não tem')], default='nao', max_length=7, null=True, verbose_name='Tem evidências ou provas?'),
        ),
        migrations.AlterField(
            model_name='reclamacao',
            name='foi_feita_reuniao_pais',
            field=models.CharField(blank=True, choices=[('sim', 'Sim'), ('nao', 'Não'), ('nao_tem', 'Não tem')], default='nao', max_length=7, null=True, verbose_name='Foi Feita a Reunião com os Pais'),
        ),
        migrations.AlterField(
            model_name='reclamacao',
            name='prioridade',
            field=models.CharField(blank=True, choices=[('baixa', 'Verde'), ('media', 'Amarelo'), ('alta', 'Vermelho')], max_length=50, null=True, verbose_name='Prioridade'),
        ),
        migrations.AlterField(
            model_name='reclamacao',
            name='tem_ata',
            field=models.CharField(blank=True, choices=[('sim', 'Sim'), ('nao', 'Não'), ('nao_tem', 'Não tem')], default='nao', max_length=7, null=True, verbose_name='Tem ATA'),
        ),
        migrations.AlterField(
            model_name='reclamacao',
            name='tem_camera',
            field=models.CharField(blank=True, choices=[('sim', 'Sim'), ('nao', 'Não'), ('nao_tem', 'Não tem')], default='nao', max_length=7, null=True, verbose_name='Tem fotos, vídeos, prints ou imagens?'),
        ),
        migrations.AlterField(
            model_name='reclamacao',
            name='tem_testemunha',
            field=models.CharField(blank=True, choices=[('sim', 'Sim'), ('nao', 'Não'), ('nao_tem', 'Não tem')], default='nao', max_length=7, null=True, verbose_name='Tem Testemunha'),
        ),
    ]
