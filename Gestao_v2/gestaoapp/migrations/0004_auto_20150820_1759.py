# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('gestaoapp', '0003_auto_20150814_1635'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='projeto',
            name='bolsista',
        ),
        migrations.AddField(
            model_name='projeto',
            name='bolsista',
            field=models.ManyToManyField(to='gestaoapp.Aluno', null=True),
        ),
    ]
