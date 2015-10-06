# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('gestaoapp', '0002_auto_20151005_1810'),
    ]

    operations = [
        migrations.CreateModel(
            name='FaseProjeto',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('fase', models.CharField(max_length=255)),
            ],
        ),
        migrations.AlterField(
            model_name='projeto',
            name='edital',
            field=models.ManyToManyField(to='gestaoapp.Edital', null=True, blank=True),
        ),
        migrations.AddField(
            model_name='projeto',
            name='fase',
            field=models.ForeignKey(default=1, to='gestaoapp.FaseProjeto'),
            preserve_default=False,
        ),
    ]
