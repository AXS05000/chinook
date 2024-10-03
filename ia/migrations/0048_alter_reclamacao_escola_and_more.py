# Generated by Django 5.0.6 on 2024-10-03 21:07

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ia', '0047_alter_reclamacao_nome_responsavel'),
    ]

    operations = [
        migrations.AlterField(
            model_name='reclamacao',
            name='escola',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='nome_escola_reclamacao', to='ia.crm_fui', verbose_name='Nome da Escola Reclamação'),
        ),
        migrations.AlterField(
            model_name='reclamacao',
            name='nome_responsavel',
            field=models.CharField(blank=True, max_length=255, null=True, verbose_name='Nome Responsavel'),
        ),
    ]
