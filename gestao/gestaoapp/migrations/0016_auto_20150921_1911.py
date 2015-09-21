# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('gestaoapp', '0015_auto_20150921_1836'),
    ]

    operations = [
        migrations.AlterField(
            model_name='usuario',
            name='periodo',
            field=models.CharField(max_length=255, null=True, blank=True),
        ),
    ]
