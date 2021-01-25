# Generated by Django 3.1.5 on 2021-01-21 01:33

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='DoencasExistentes',
            fields=[
                ('id_doencas_existentes', models.AutoField(primary_key=True, serialize=False)),
                ('doenca', models.CharField(max_length=200, verbose_name='Doença')),
                ('ano_diagnostico', models.DateField(verbose_name='Ano do diagnóstico')),
                ('exame', models.FileField(blank=True, upload_to='midias/exames')),
            ],
        ),
    ]