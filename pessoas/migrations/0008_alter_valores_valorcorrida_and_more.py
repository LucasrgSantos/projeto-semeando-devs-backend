# Generated by Django 4.2.2 on 2023-09-06 01:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pessoas', '0007_alter_valores_valorcorrida_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='valores',
            name='valorCorrida',
            field=models.CharField(max_length=5),
        ),
        migrations.AlterField(
            model_name='valores',
            name='valorCorridaComDesconto',
            field=models.CharField(max_length=5),
        ),
    ]
