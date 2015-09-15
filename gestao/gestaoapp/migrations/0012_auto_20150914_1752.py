# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('gestaoapp', '0011_auto_20150914_1752'),
    ]

    operations = [
        migrations.AlterField(
            model_name='usuario',
            name='email_opcional',
            field=models.EmailField(max_length=254, null=True, blank=True),
        ),
    ]
