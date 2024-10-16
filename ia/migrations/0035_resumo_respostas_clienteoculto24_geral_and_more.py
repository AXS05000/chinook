# Generated by Django 5.0.6 on 2024-09-27 19:41

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ia', '0034_alter_planificador_2024_acao_1_elegivel_trade_marketing_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='Resumo_Respostas_ClienteOculto24_Geral',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('resumo', models.TextField(blank=True, null=True, verbose_name='Resumo Cliente Oculto Geral')),
                ('escola', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='nome_escola_resumo_co24_geral', to='ia.crm_fui', verbose_name='Nome da Escola do resumo do Cliente Oculto Geral 2024')),
            ],
        ),
        migrations.CreateModel(
            name='Resumo_Respostas_NPS_1_Onda_Geral',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('resumo', models.TextField(blank=True, null=True, verbose_name='Resumo Geral NPS 1° Onda')),
                ('escola', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='nome_escola_resumo_nps_1_onda_geral', to='ia.crm_fui', verbose_name='Nome da Escola do NPS 1° Onda Geral')),
            ],
        ),
    ]
