# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('gestaoapp', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='usuario',
            name='dia',
            field=models.ManyToManyField(to='gestaoapp.Horario', blank=True),
        ),
        migrations.AlterField(
            model_name='usuario',
            name='perfil',
            field=models.ForeignKey(to='gestaoapp.Perfil', null=True),
        ),
        migrations.AlterField(
            model_name='usuario',
            name='telefone2',
            field=models.CharField(max_length=11, null=True),
        ),
    ]
