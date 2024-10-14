# Generated by Django 5.0.6 on 2024-10-14 18:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ia', '0054_remove_planificador_2024_acao_marketing_offline_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='planificador_2024',
            name='acoes_ativacao_alunos_sem_slm',
            field=models.CharField(blank=True, max_length=5000, null=True, verbose_name='Quais ativações foram realizadas/indicadas para os alunos rematriculados que não compraram o SLM 25?'),
        ),
        migrations.AddField(
            model_name='planificador_2024',
            name='acoes_reverter_nao_rematricula',
            field=models.CharField(blank=True, max_length=5000, null=True, verbose_name="Ações para reverter a 'Não rematrícula'"),
        ),
        migrations.AddField(
            model_name='planificador_2024',
            name='data_ativacao_alunos_rematriculados_sem_slm',
            field=models.DateField(blank=True, null=True, verbose_name='Caso não, quando será a data de ativação de alunos rematriculados que não compraram o SLM 25'),
        ),
        migrations.AddField(
            model_name='planificador_2024',
            name='data_contato_familias_pendentes_rematricula',
            field=models.DateField(blank=True, null=True, verbose_name='Caso não, uando será a data de realização do contato com as famílias de alunos pendentes de rematrícula'),
        ),
        migrations.AddField(
            model_name='planificador_2024',
            name='data_inicio_reunioes_rematricula',
            field=models.DateField(blank=True, null=True, verbose_name='Data de início das reuniões por série para rematrícula'),
        ),
        migrations.AddField(
            model_name='planificador_2024',
            name='fez_analise_nps',
            field=models.CharField(choices=[('SIM', 'Sim'), ('NAO', 'Não')], default='NAO', max_length=3, verbose_name='A escola fez análise de NPS?'),
        ),
        migrations.AddField(
            model_name='planificador_2024',
            name='fez_circular_rematricula_modelo_central',
            field=models.CharField(choices=[('SIM', 'Sim'), ('NAO', 'Não')], default='NAO', max_length=3, verbose_name='A escola criou a circular de rematrícula de acordo com o modelo da Central?'),
        ),
        migrations.AddField(
            model_name='planificador_2024',
            name='fez_contato_familias_pendentes_rematricula',
            field=models.CharField(choices=[('SIM', 'Sim'), ('NAO', 'Não')], default='NAO', max_length=3, verbose_name='A escola realizou contato individual com as famílias de alunos pendentes de rematrícula?'),
        ),
        migrations.AddField(
            model_name='planificador_2024',
            name='fez_plano_acoes_corretivas_nps',
            field=models.CharField(choices=[('SIM', 'Sim'), ('NAO', 'Não')], default='NAO', max_length=3, verbose_name='A escola fez o plano de ações corretivas baseado no resultado NPS?'),
        ),
        migrations.AddField(
            model_name='planificador_2024',
            name='fez_reuniao_rematricula_alinhamento',
            field=models.CharField(choices=[('SIM', 'Sim'), ('NAO', 'Não')], default='NAO', max_length=3, verbose_name='A escola fez reunião por série ou segmento de rematrícula para alinhamento da próxima série do ano letivo seguinte?'),
        ),
        migrations.AddField(
            model_name='planificador_2024',
            name='iniciou_ativacao_alunos_rematriculados_sem_slm',
            field=models.CharField(choices=[('SIM', 'Sim'), ('NAO', 'Não')], default='NAO', max_length=3, verbose_name='Já iniciou a ativação de alunos rematriculados que não compraram o SLM 25?'),
        ),
        migrations.AddField(
            model_name='planificador_2024',
            name='motivo_nao_fez_analise_nps',
            field=models.CharField(blank=True, max_length=5000, null=True, verbose_name='Se não, motivo por não fazer a análise de NPS'),
        ),
        migrations.AddField(
            model_name='planificador_2024',
            name='motivo_nao_fez_plano_acoes_nps',
            field=models.CharField(blank=True, max_length=5000, null=True, verbose_name='Se não, motivo por não fazer o plano de ações corretivas'),
        ),
        migrations.AddField(
            model_name='planificador_2024',
            name='motivo_nao_fez_reuniao_rematricula',
            field=models.CharField(blank=True, max_length=5000, null=True, verbose_name='Se não, motivo por não ter feito a reunião de rematrícula'),
        ),
        migrations.AddField(
            model_name='planificador_2024',
            name='motivos_nao_rematricula',
            field=models.CharField(blank=True, max_length=5000, null=True, verbose_name="Motivos de 'não rematrícula'"),
        ),
        migrations.AddField(
            model_name='planificador_2024',
            name='numero_alunos_nao_rematricula',
            field=models.IntegerField(blank=True, null=True, verbose_name="Número de alunos que sinalizaram 'Não rematrícula'"),
        ),
    ]