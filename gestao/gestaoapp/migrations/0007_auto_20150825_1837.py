# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('gestaoapp', '0006_auto_20150821_1734'),
    ]

    operations = [
        migrations.CreateModel(
            name='Curso',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('curso', models.CharField(max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='Nivel',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('nivel', models.CharField(max_length=255)),
            ],
        ),
        migrations.AlterField(
            model_name='aluno',
            name='curso',
            field=models.ForeignKey(to='gestaoapp.Curso'),
        ),
        migrations.AlterField(
            model_name='aluno',
            name='nivel',
            field=models.ForeignKey(to='gestaoapp.Nivel'),
        ),
    ]
