# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('gestaoapp', '0007_auto_20150908_1726'),
    ]

    operations = [
        migrations.RenameField(
            model_name='horario',
            old_name='dia',
            new_name='data',
        ),
    ]
