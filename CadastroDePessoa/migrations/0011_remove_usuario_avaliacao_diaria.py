# Generated by Django 3.1.5 on 2021-02-04 00:21

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('CadastroDePessoa', '0010_auto_20210203_2050'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='usuario',
            name='avaliacao_diaria',
        ),
    ]