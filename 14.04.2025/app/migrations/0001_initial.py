# Generated by Django 5.2 on 2025-04-14 12:00

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Piloto',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=255)),
                ('equipe', models.CharField(max_length=255)),
                ('idade', models.PositiveIntegerField()),
                ('classificacao', models.PositiveIntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Carro',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=255)),
                ('marca', models.CharField(max_length=255)),
                ('velocidade_maxima', models.PositiveIntegerField()),
                ('cor', models.CharField(choices=[('VERMELHO', 'Vermelho'), ('ROSA', 'Rosa'), ('PRETO', 'Preto'), ('ROXO', 'Roxo'), ('CINZA', 'Cinza')], max_length=50)),
                ('piloto', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.piloto')),
            ],
        ),
    ]
