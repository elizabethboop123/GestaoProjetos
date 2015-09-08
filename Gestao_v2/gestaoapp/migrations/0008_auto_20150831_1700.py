# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('gestaoapp', '0007_auto_20150825_1837'),
    ]

    operations = [
        migrations.RenameField(
            model_name='pessoa',
            old_name='endereco',
            new_name='bairro',
        ),
        migrations.AddField(
            model_name='pessoa',
            name='cep',
            field=models.CharField(default=1, max_length=255),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='pessoa',
            name='cidade',
            field=models.CharField(default=1, max_length=255),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='pessoa',
            name='complemento',
            field=models.CharField(default=1, max_length=255),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='pessoa',
            name='estado',
            field=models.CharField(default=1, max_length=255),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='pessoa',
            name='numero',
            field=models.CharField(default=1, max_length=255),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='pessoa',
            name='rua',
            field=models.CharField(default=1, max_length=255),
            preserve_default=False,
        ),
    ]
