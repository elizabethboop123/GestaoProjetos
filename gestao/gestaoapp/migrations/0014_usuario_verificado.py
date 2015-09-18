# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('gestaoapp', '0013_usuario_verificacao'),
    ]

    operations = [
        migrations.AddField(
            model_name='usuario',
            name='verificado',
            field=models.BooleanField(default=1),
            preserve_default=False,
        ),
    ]
