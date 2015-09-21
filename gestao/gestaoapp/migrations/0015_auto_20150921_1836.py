# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('gestaoapp', '0014_usuario_verificado'),
    ]

    operations = [
        migrations.CreateModel(
            name='Vinculo',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('vinculo', models.CharField(max_length=255)),
            ],
        ),
        migrations.AlterField(
            model_name='usuario',
            name='vinculo_institucional',
            field=models.ForeignKey(to='gestaoapp.Vinculo'),
        ),
    ]
