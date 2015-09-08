# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('gestaoapp', '0002_auto_20150908_1649'),
    ]

    operations = [
        migrations.AlterField(
            model_name='usuario',
            name='telefone2',
            field=models.CharField(default=1, max_length=11, blank=True),
            preserve_default=False,
        ),
    ]
