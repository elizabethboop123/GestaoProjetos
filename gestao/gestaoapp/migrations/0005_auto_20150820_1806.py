# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('gestaoapp', '0004_auto_20150820_1759'),
    ]

    operations = [
        migrations.AddField(
            model_name='projeto',
            name='participante',
            field=models.ManyToManyField(related_name='oi', null=True, to='gestaoapp.Professor'),
        ),
        migrations.AlterField(
            model_name='projeto',
            name='coordenador',
            field=models.ForeignKey(related_name='tchau', to='gestaoapp.Professor'),
        ),
    ]
