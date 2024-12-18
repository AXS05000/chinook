# Generated by Django 5.0.6 on 2024-11-11 19:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ia', '0057_alter_processo_assunto_principal_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='processo',
            name='assunto_principal',
            field=models.TextField(blank=True, max_length=2550, null=True),
        ),
        migrations.AlterField(
            model_name='processo',
            name='documento_polo_ativo',
            field=models.TextField(blank=True, max_length=2550, null=True),
        ),
        migrations.AlterField(
            model_name='processo',
            name='documento_polo_passivo',
            field=models.TextField(blank=True, max_length=2550, null=True),
        ),
        migrations.AlterField(
            model_name='processo',
            name='nome_polo_ativo',
            field=models.TextField(blank=True, max_length=2550, null=True),
        ),
        migrations.AlterField(
            model_name='processo',
            name='nome_polo_passivo',
            field=models.TextField(blank=True, max_length=2550, null=True),
        ),
        migrations.AlterField(
            model_name='processo',
            name='numero_do_processo',
            field=models.TextField(blank=True, max_length=2550, null=True),
        ),
        migrations.AlterField(
            model_name='processo',
            name='status_do_processo',
            field=models.TextField(blank=True, max_length=2550, null=True),
        ),
        migrations.AlterField(
            model_name='processo',
            name='tipo_de_tribunal',
            field=models.TextField(blank=True, max_length=2550, null=True),
        ),
        migrations.AlterField(
            model_name='processo',
            name='tipo_do_processo',
            field=models.TextField(blank=True, max_length=2550, null=True),
        ),
        migrations.AlterField(
            model_name='protesto',
            name='cartorio',
            field=models.TextField(blank=True, max_length=2550, null=True),
        ),
        migrations.AlterField(
            model_name='protesto',
            name='documento',
            field=models.TextField(blank=True, max_length=2550, null=True),
        ),
        migrations.AlterField(
            model_name='protesto',
            name='resultado',
            field=models.TextField(blank=True, max_length=2550, null=True),
        ),
        migrations.AlterField(
            model_name='protesto',
            name='status',
            field=models.TextField(blank=True, max_length=2550, null=True),
        ),
    ]
