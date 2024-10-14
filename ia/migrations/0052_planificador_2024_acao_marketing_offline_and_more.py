# Generated by Django 5.0.6 on 2024-10-10 20:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ia', '0051_alter_reclamacao_telefones'),
    ]

    operations = [
        migrations.AddField(
            model_name='planificador_2024',
            name='acao_marketing_offline',
            field=models.CharField(choices=[('SIM', 'Sim'), ('NAO', 'Não')], default='NAO', max_length=3, verbose_name='A escola realiza ações de marketing offline?'),
        ),
        migrations.AddField(
            model_name='planificador_2024',
            name='campanhas_mkt_digital_local',
            field=models.CharField(choices=[('SIM', 'Sim'), ('NAO', 'Não')], default='NAO', max_length=3, verbose_name='A escola roda campanhas de marketing digital local?'),
        ),
        migrations.AddField(
            model_name='planificador_2024',
            name='consultor_campo_guia_mbear_experience',
            field=models.CharField(choices=[('SIM', 'Sim'), ('NAO', 'Não')], default='NAO', max_length=3, verbose_name='Consultor de campo compartilhou o guia Maple Bear Experience?'),
        ),
        migrations.AddField(
            model_name='planificador_2024',
            name='equipe_comercial_dedicada_novas_matriculas',
            field=models.CharField(choices=[('SIM', 'Sim'), ('NAO', 'Não')], default='NAO', max_length=3, verbose_name='A escola possui equipe comercial dedicada a venda de novas matrículas?'),
        ),
        migrations.AddField(
            model_name='planificador_2024',
            name='equipe_comercial_treinamento_central',
            field=models.CharField(choices=[('SIM', 'Sim'), ('NAO', 'Não')], default='NAO', max_length=3, verbose_name='A equipe comercial recebeu treinamento da central?'),
        ),
        migrations.AddField(
            model_name='planificador_2024',
            name='equipe_inscrita_mentoria_vendas',
            field=models.CharField(choices=[('SIM', 'Sim'), ('NAO', 'Não')], default='NAO', max_length=3, verbose_name='Equipe da escola está inscrita na Mentoria de Vendas?'),
        ),
        migrations.AddField(
            model_name='planificador_2024',
            name='escola_possui_equipe_ou_agencia_marketing',
            field=models.CharField(choices=[('SIM', 'Sim'), ('NAO', 'Não')], default='NAO', max_length=3, verbose_name='A escola possui equipe ou agência de marketing?'),
        ),
        migrations.AddField(
            model_name='planificador_2024',
            name='escola_possui_orcamento_marketing_local',
            field=models.CharField(choices=[('SIM', 'Sim'), ('NAO', 'Não')], default='NAO', max_length=3, verbose_name='A escola possui orçamento para investimentos em marketing local?'),
        ),
        migrations.AddField(
            model_name='planificador_2024',
            name='investimento_medio_mensal_campanhas_online',
            field=models.FloatField(blank=True, null=True, verbose_name='Investimento médio mensal em campanhas online'),
        ),
        migrations.AddField(
            model_name='planificador_2024',
            name='media_investimentos_marketing_offline',
            field=models.FloatField(blank=True, null=True, verbose_name='Média de investimentos em marketing offline'),
        ),
        migrations.AddField(
            model_name='planificador_2024',
            name='motivo_sem_equipe_comercial_novas_matriculas',
            field=models.CharField(blank=True, max_length=5000, null=True, verbose_name='Motivo sem equipe comercial dedicada a venda de novas matrículas'),
        ),
        migrations.AddField(
            model_name='planificador_2024',
            name='nro_consultores_equipe_comercial',
            field=models.IntegerField(blank=True, null=True, verbose_name='Nro de Consultores na equipe comercial'),
        ),
        migrations.AddField(
            model_name='planificador_2024',
            name='observacoes_equipe_comercial',
            field=models.TextField(blank=True, null=True, verbose_name='Observações sobre a equipe comercial'),
        ),
        migrations.AddField(
            model_name='planificador_2024',
            name='orcamento_marketing_anual_medio',
            field=models.FloatField(blank=True, null=True, verbose_name='Orçamento de marketing anual médio'),
        ),
        migrations.AddField(
            model_name='planificador_2024',
            name='pesquisa_concorrencia_realizada',
            field=models.CharField(choices=[('SIM', 'Sim'), ('NAO', 'Não')], default='NAO', max_length=3, verbose_name='Pesquisa de concorrência realizada?'),
        ),
        migrations.AddField(
            model_name='planificador_2024',
            name='planejamento_ativacoes_marketing_local',
            field=models.CharField(choices=[('SIM', 'Sim'), ('NAO', 'Não')], default='NAO', max_length=3, verbose_name='A escola possui planejamento de ativações de marketing local?'),
        ),
        migrations.AddField(
            model_name='planificador_2024',
            name='preco_material_didatico_ensino_medio_concorrente',
            field=models.FloatField(blank=True, null=True, verbose_name='Preço material didático ensino médio concorrente'),
        ),
        migrations.AddField(
            model_name='planificador_2024',
            name='preco_material_didatico_fundamental_concorrente',
            field=models.FloatField(blank=True, null=True, verbose_name='Preço material didático fundamental concorrente'),
        ),
        migrations.AddField(
            model_name='planificador_2024',
            name='preco_material_didatico_infantil_concorrente',
            field=models.FloatField(blank=True, null=True, verbose_name='Preço Material Didático Infantil Concorrente'),
        ),
        migrations.AddField(
            model_name='planificador_2024',
            name='ticket_ensino_medio_concorrente',
            field=models.FloatField(blank=True, null=True, verbose_name='Ticket Ensino Médio principal concorrente'),
        ),
        migrations.AddField(
            model_name='planificador_2024',
            name='ticket_fundamental_concorrente',
            field=models.FloatField(blank=True, null=True, verbose_name='Ticket fundamental principal concorrente'),
        ),
        migrations.AddField(
            model_name='planificador_2024',
            name='ticket_infantil_concorrente',
            field=models.FloatField(blank=True, null=True, verbose_name='Ticket infantil principal concorrente'),
        ),
    ]