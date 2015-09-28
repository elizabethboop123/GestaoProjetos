# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('gestaoapp', '0002_auto_20150922_1739'),
    ]

    operations = [
        migrations.AlterField(
            model_name='usuario',
            name='foto',
            field=models.ImageField(default=1, upload_to=b'imagens', verbose_name=b'Imagem', blank=True),
            preserve_default=False,
        ),
    ]
