# Generated by Django 3.1.5 on 2021-01-21 01:33

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='AvaliacaoDiaria',
            fields=[
                ('id_avaliacao_diaria', models.AutoField(primary_key=True, serialize=False)),
                ('sintomas', models.CharField(choices=[('dorDeCabeca', 'Dor de Cabeça'), ('dorNoCorpo', 'Dor no corpo'), ('cansaco', 'Cansaço'), ('dorNoEstomago', 'Dor no estômago'), ('inchaco', 'Inchaço'), ('nausea', 'Náusea'), ('enjoo', 'Enjôo'), ('faltaDeAr', 'Falta de ar'), ('ansiedade', 'Ansiedade'), ('outro', 'Outro')], max_length=15, verbose_name='Sintomas')),
                ('observacoes', models.TextField(verbose_name='Observações')),
            ],
        ),
    ]
