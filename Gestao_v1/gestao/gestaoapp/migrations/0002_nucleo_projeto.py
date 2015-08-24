# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('gestaoapp', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Nucleo',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('nome_nucleo', models.CharField(max_length=255)),
                ('descricao', models.CharField(max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='Projeto',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('nome_projeto', models.CharField(max_length=255)),
                ('cliente', models.CharField(max_length=255)),
                ('data_inicio', models.DateField()),
                ('data_termino', models.DateField()),
                ('bolsista', models.ForeignKey(to='gestaoapp.Bolsista')),
                ('coordenador', models.ForeignKey(to='gestaoapp.Coordenador')),
                ('nucleo', models.ForeignKey(to='gestaoapp.Nucleo')),
            ],
        ),
    ]
