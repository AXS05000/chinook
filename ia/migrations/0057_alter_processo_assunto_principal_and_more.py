# Generated by Django 5.0.6 on 2024-11-11 19:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ia', '0056_processo_protesto'),
    ]

    operations = [
        migrations.AlterField(
            model_name='processo',
            name='assunto_principal',
            field=models.CharField(blank=True, max_length=2550, null=True),
        ),
        migrations.AlterField(
            model_name='processo',
            name='documento_polo_ativo',
            field=models.CharField(blank=True, max_length=2550, null=True),
        ),
        migrations.AlterField(
            model_name='processo',
            name='documento_polo_passivo',
            field=models.CharField(blank=True, max_length=2550, null=True),
        ),
        migrations.AlterField(
            model_name='processo',
            name='nome_polo_ativo',
            field=models.CharField(blank=True, max_length=2550, null=True),
        ),
        migrations.AlterField(
            model_name='processo',
            name='nome_polo_passivo',
            field=models.CharField(blank=True, max_length=2550, null=True),
        ),
        migrations.AlterField(
            model_name='processo',
            name='numero_do_processo',
            field=models.CharField(blank=True, max_length=2550, null=True),
        ),
        migrations.AlterField(
            model_name='processo',
            name='status_do_processo',
            field=models.CharField(blank=True, max_length=2550, null=True),
        ),
        migrations.AlterField(
            model_name='processo',
            name='tipo_de_tribunal',
            field=models.CharField(blank=True, max_length=2550, null=True),
        ),
        migrations.AlterField(
            model_name='processo',
            name='tipo_do_processo',
            field=models.CharField(blank=True, max_length=2550, null=True),
        ),
        migrations.AlterField(
            model_name='protesto',
            name='cartorio',
            field=models.CharField(blank=True, max_length=2550, null=True),
        ),
        migrations.AlterField(
            model_name='protesto',
            name='documento',
            field=models.CharField(blank=True, max_length=2550, null=True),
        ),
        migrations.AlterField(
            model_name='protesto',
            name='resultado',
            field=models.CharField(blank=True, max_length=2550, null=True),
        ),
        migrations.AlterField(
            model_name='protesto',
            name='status',
            field=models.CharField(blank=True, max_length=2550, null=True),
        ),
    ]
