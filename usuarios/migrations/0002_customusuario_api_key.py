# Generated by Django 5.0.6 on 2024-08-01 19:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('usuarios', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='customusuario',
            name='api_key',
            field=models.CharField(blank=True, max_length=255, null=True, verbose_name='Chave API'),
        ),
    ]
