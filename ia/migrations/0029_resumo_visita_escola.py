# Generated by Django 5.0.6 on 2024-09-09 12:59

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ia', '0028_visita_escola'),
    ]

    operations = [
        migrations.CreateModel(
            name='Resumo_Visita_Escola',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('resumo', models.TextField(blank=True, null=True, verbose_name='Resumo da Visita')),
                ('escola', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='resumos_visita_escola', to='ia.crm_fui', verbose_name='Nome da Escola Visita')),
                ('visita', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='resumos_visita', to='ia.visita_escola', verbose_name='Visita Escola')),
            ],
        ),
    ]
