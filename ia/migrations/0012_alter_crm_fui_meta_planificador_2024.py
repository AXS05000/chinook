# Generated by Django 5.0.6 on 2024-08-08 13:08

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ia', '0011_remove_crm_fui_alunos_crm_fui_complemento_escola_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='crm_fui',
            name='meta',
            field=models.IntegerField(blank=True, null=True, verbose_name='Meta 2024'),
        ),
        migrations.CreateModel(
            name='Planificador_2024',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ultima_data_atualizacao_bloc_drivers_comerciais_estrategicos', models.DateField(blank=True, null=True)),
                ('crm_b2c', models.CharField(choices=[('SIM', 'Sim'), ('NAO', 'Não')], default='NAO', max_length=3)),
                ('data_abertura_matricula_2025', models.DateField(blank=True, null=True)),
                ('circular_oferta_2025_publicado', models.CharField(choices=[('SIM', 'Sim'), ('NAO', 'Não')], default='NAO', max_length=3)),
                ('toddle', models.CharField(choices=[('SIM', 'Sim'), ('NAO', 'Não')], default='NAO', max_length=3)),
                ('toddle_planejamento', models.CharField(blank=True, max_length=255, null=True)),
                ('toddle_portfolio', models.CharField(blank=True, max_length=255, null=True)),
                ('arvore', models.CharField(choices=[('SIM', 'Sim'), ('NAO', 'Não')], default='NAO', max_length=3)),
                ('data_implementacao_arvore', models.DateField(blank=True, null=True)),
                ('ultima_data_atualizacao_bloc_funil_comercial', models.DateField(blank=True, null=True)),
                ('leads_central_ago_24', models.IntegerField(blank=True, null=True)),
                ('leads_escolas_ago_24', models.IntegerField(blank=True, null=True)),
                ('visitas_ago_24', models.IntegerField(blank=True, null=True)),
                ('taxa_conversao_atual_leads_visitas', models.FloatField(blank=True, null=True)),
                ('matriculas_ago_24', models.IntegerField(blank=True, null=True)),
                ('taxa_conversao_atual_visitas_matriculas', models.FloatField(blank=True, null=True)),
                ('taxa_conversao_leads_matriculas', models.FloatField(blank=True, null=True)),
                ('taxa_conversao_acumulada', models.FloatField(blank=True, null=True)),
                ('ultima_data_atualizacao_bloc_drivers_comerciais_meio', models.DateField(blank=True, null=True)),
                ('meta_alunos_5k_2024', models.IntegerField(blank=True, null=True)),
                ('real_alunos_5k_2024', models.IntegerField(blank=True, null=True)),
                ('gap_alunos_5k_2024', models.IntegerField(blank=True, null=True)),
                ('setup_plano_comercial_segundo_semestre', models.CharField(choices=[('SIM', 'Sim'), ('NAO', 'Não')], default='NAO', max_length=3)),
                ('acao_1_elegivel_trade_marketing', models.CharField(choices=[('SIM', 'Sim'), ('NAO', 'Não')], default='NAO', max_length=3)),
                ('acao_1_trade_valor', models.FloatField(blank=True, null=True)),
                ('acao_1_trade_marketing_acoes_alinhadas', models.CharField(blank=True, max_length=255, null=True)),
                ('acao_2_experience_day_10_08_24', models.CharField(choices=[('SIM', 'Sim'), ('NAO', 'Não')], default='NAO', max_length=3)),
                ('acao_2_experience_day_24_08_24', models.CharField(choices=[('SIM', 'Sim'), ('NAO', 'Não')], default='NAO', max_length=3)),
                ('acao_2_experience_day_21_09_24', models.CharField(choices=[('SIM', 'Sim'), ('NAO', 'Não')], default='NAO', max_length=3)),
                ('acao_2_experience_day_26_10_24', models.CharField(choices=[('SIM', 'Sim'), ('NAO', 'Não')], default='NAO', max_length=3)),
                ('acao_2_experience_day_09_11_24', models.CharField(choices=[('SIM', 'Sim'), ('NAO', 'Não')], default='NAO', max_length=3)),
                ('acao_3_friend_get_friend', models.CharField(choices=[('SIM', 'Sim'), ('NAO', 'Não')], default='NAO', max_length=3)),
                ('acao_4_webinars_com_autoridades_pre', models.CharField(choices=[('SIM', 'Sim'), ('NAO', 'Não')], default='NAO', max_length=3)),
                ('acao_4_webinars_com_autoridades_pos', models.CharField(choices=[('SIM', 'Sim'), ('NAO', 'Não')], default='NAO', max_length=3)),
                ('piloto_welcome_baby_bear', models.CharField(choices=[('SIM', 'Sim'), ('NAO', 'Não')], default='NAO', max_length=3)),
                ('acao_5_sdr_taxa_conversao_validacao_lead', models.FloatField(blank=True, null=True)),
                ('acao_5_sdr_taxa_conversao_visitas', models.FloatField(blank=True, null=True)),
                ('acao_6_alinhado_resgate_leads', models.CharField(choices=[('SIM', 'Sim'), ('NAO', 'Não')], default='NAO', max_length=3)),
                ('acao_6_quantidade_leads_resgatados', models.IntegerField(blank=True, null=True)),
                ('acao_6_todos_leads_resgatados_contatados', models.CharField(choices=[('SIM', 'Sim'), ('NAO', 'Não')], default='NAO', max_length=3)),
                ('data_atualizacao_resultados', models.DateField(blank=True, null=True)),
                ('slm_2022', models.FloatField(blank=True, null=True)),
                ('slm_2023', models.FloatField(blank=True, null=True)),
                ('slm_2024_posicao_atual', models.FloatField(blank=True, null=True)),
                ('meta_orcamentaria_2024', models.FloatField(blank=True, null=True)),
                ('meta_5k_2024', models.FloatField(blank=True, null=True)),
                ('gap_meta_orcamentaria_2024', models.FloatField(blank=True, null=True)),
                ('gap_meta_5k_2024', models.FloatField(blank=True, null=True)),
                ('slm_2025', models.FloatField(blank=True, null=True)),
                ('base_rematriculaveis_2025', models.IntegerField(blank=True, null=True)),
                ('meta_rematricula_2025', models.IntegerField(blank=True, null=True)),
                ('real_rematriculas_2025', models.IntegerField(blank=True, null=True)),
                ('atingimento_rematriculas_2025', models.FloatField(blank=True, null=True)),
                ('meta_matricula_2025', models.IntegerField(blank=True, null=True)),
                ('real_matricula_2025', models.IntegerField(blank=True, null=True)),
                ('atingimento_matriculas_2025', models.FloatField(blank=True, null=True)),
                ('total_meta_alunos_2025', models.IntegerField(blank=True, null=True)),
                ('total_real_alunos_2025', models.IntegerField(blank=True, null=True)),
                ('atingimento_real_alunos_2025', models.FloatField(blank=True, null=True)),
                ('correlacao_alunos_slms_2025', models.FloatField(blank=True, null=True)),
                ('mc_2025', models.FloatField(blank=True, null=True)),
                ('slms_2025_m', models.FloatField(blank=True, null=True)),
                ('pedidos_represados_logistica_2025', models.IntegerField(blank=True, null=True)),
                ('pedidos_faturados', models.IntegerField(blank=True, null=True)),
                ('pedidos_entregues', models.IntegerField(blank=True, null=True)),
                ('porcentagem_planificador', models.FloatField(blank=True, null=True)),
                ('escola', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='nome_escola_planificador', to='ia.crm_fui', verbose_name='Nome da Escola Planificador')),
            ],
        ),
    ]