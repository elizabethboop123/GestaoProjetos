# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('gestaoapp', '0006_auto_20150908_1715'),
    ]

    operations = [
        migrations.AlterField(
            model_name='horario',
            name='dia',
            field=models.ForeignKey(to='gestaoapp.Dia'),
        ),
    ]
