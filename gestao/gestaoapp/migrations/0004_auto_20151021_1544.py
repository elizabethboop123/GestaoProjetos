# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('gestaoapp', '0003_auto_20151006_1801'),
    ]

    operations = [
        migrations.AlterField(
            model_name='projeto',
            name='edital',
            field=models.ManyToManyField(to='gestaoapp.Edital', blank=True),
        ),
    ]
