# Generated by Django 5.0.6 on 2024-10-01 18:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ia', '0037_resumo_sac'),
    ]

    operations = [
        migrations.AlterField(
            model_name='resumo_sac',
            name='resumo',
            field=models.TextField(blank=True, null=True, verbose_name='Resumo Geral SAC'),
        ),
    ]
