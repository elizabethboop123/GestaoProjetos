# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('gestaoapp', '0004_auto_20150922_1752'),
    ]

    operations = [
        migrations.CreateModel(
            name='Nucleo',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('nome', models.CharField(max_length=255)),
                ('sigla', models.CharField(max_length=5)),
                ('descricao', models.CharField(max_length=255)),
            ],
        ),
    ]
