# Generated by Django 5.0.6 on 2024-10-01 18:12

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ia', '0036_delete_resumo_respostas_clienteoculto24_geral'),
    ]

    operations = [
        migrations.CreateModel(
            name='Resumo_SAC',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('resumo', models.TextField(blank=True, null=True, verbose_name='Resumo Geral NPS 1° Onda')),
                ('escola', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='nome_escola_resumo_sac', to='ia.crm_fui', verbose_name='Nome da Escola do SAC')),
            ],
        ),
    ]