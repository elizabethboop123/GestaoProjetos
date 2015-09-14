# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('gestaoapp', '0012_auto_20150914_1752'),
    ]

    operations = [
        migrations.AddField(
            model_name='usuario',
            name='verificacao',
            field=models.CharField(max_length=255, unique=True, null=True, blank=True),
        ),
    ]
