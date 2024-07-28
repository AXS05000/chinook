# Generated by Django 5.0.6 on 2024-07-28 04:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ia', '0005_rename_resposta_respostas_nps'),
    ]

    operations = [
        migrations.AddField(
            model_name='respostas_nps',
            name='nome',
            field=models.CharField(default='', verbose_name='Nome'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='crm_fui',
            name='estado_da_escola',
            field=models.CharField(blank=True, max_length=20, null=True, verbose_name='Estado da Escola'),
        ),
    ]
