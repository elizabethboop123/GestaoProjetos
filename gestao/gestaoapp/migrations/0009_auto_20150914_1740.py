# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('gestaoapp', '0008_auto_20150908_1842'),
    ]

    operations = [
        migrations.AddField(
            model_name='usuario',
            name='mail',
            field=models.EmailField(default=1, unique=True, max_length=254),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='usuario',
            name='matricula',
            field=models.CharField(unique=True, max_length=255),
        ),
        migrations.AlterField(
            model_name='usuario',
            name='telefone2',
            field=models.CharField(max_length=11, null=True, blank=True),
        ),
    ]
