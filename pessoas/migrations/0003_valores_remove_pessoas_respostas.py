# Generated by Django 4.2.4 on 2023-08-31 23:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pessoas', '0002_respostas_pessoas_respostas'),
    ]

    operations = [
        migrations.CreateModel(
            name='Valores',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('valorCorrida', models.IntegerField()),
                ('valorCorridaComDesconto', models.IntegerField()),
            ],
        ),
        migrations.RemoveField(
            model_name='pessoas',
            name='respostas',
        ),
    ]