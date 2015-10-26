# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('gestaoapp', '0004_auto_20151021_1544'),
    ]

    operations = [
        migrations.CreateModel(
            name='HoraProjeto',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('hora_atribuida', models.ManyToManyField(to='gestaoapp.Horario', blank=True)),
                ('projeto', models.ForeignKey(to='gestaoapp.Projeto')),
                ('usuario', models.ForeignKey(to='gestaoapp.Usuario')),
            ],
        ),
    ]
