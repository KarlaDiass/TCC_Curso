# Generated by Django 3.1.5 on 2021-01-27 00:49

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Alergias',
            fields=[
                ('id_alergias', models.AutoField(primary_key=True, serialize=False)),
                ('tipo', models.TextField(verbose_name='Tipo de Alergia')),
                ('causador', models.TextField(verbose_name='Tipo de Causador')),
            ],
        ),
        migrations.CreateModel(
            name='Intolerancias',
            fields=[
                ('id_intolerancias', models.AutoField(primary_key=True, serialize=False)),
                ('tipo', models.TextField(verbose_name='Tipo de Alergia')),
                ('causador', models.TextField(verbose_name='Tipo de Causador')),
            ],
        ),
    ]
