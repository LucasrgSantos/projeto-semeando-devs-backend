# Generated by Django 4.2.2 on 2023-09-06 00:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pessoas', '0004_alter_pessoas_cpf'),
    ]

    operations = [
        migrations.AlterField(
            model_name='valores',
            name='valorCorrida',
            field=models.DecimalField(decimal_places=2, max_digits=10),
        ),
        migrations.AlterField(
            model_name='valores',
            name='valorCorridaComDesconto',
            field=models.DecimalField(decimal_places=2, max_digits=10),
        ),
    ]