# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('gestaoapp', '0005_auto_20150820_1806'),
    ]

    operations = [
        migrations.AlterField(
            model_name='nucleo',
            name='projeto',
            field=models.ManyToManyField(to='gestaoapp.Projeto'),
        ),
        migrations.AlterField(
            model_name='projeto',
            name='bolsista',
            field=models.ManyToManyField(to='gestaoapp.Aluno'),
        ),
        migrations.AlterField(
            model_name='projeto',
            name='participante',
            field=models.ManyToManyField(related_name='oi', to='gestaoapp.Professor'),
        ),
    ]
