# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings
import django.contrib.auth.models


class Migration(migrations.Migration):

    dependencies = [
        ('auth', '0006_require_contenttypes_0002'),
    ]

    operations = [
        migrations.CreateModel(
            name='Dia',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('dia', models.CharField(max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='Horario',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('dia', models.CharField(max_length=255)),
                ('hora_inicio', models.TimeField()),
                ('hora_fim', models.TimeField()),
                ('turno', models.CharField(max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='Perfil',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('nome', models.CharField(max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='Usuario',
            fields=[
                ('user_ptr', models.OneToOneField(parent_link=True, auto_created=True, primary_key=True, serialize=False, to=settings.AUTH_USER_MODEL)),
                ('email_opcional', models.EmailField(max_length=254)),
                ('matricula', models.CharField(max_length=255)),
                ('foto', models.ImageField(upload_to=b'')),
                ('carga_horaria', models.IntegerField()),
                ('telefone1', models.CharField(max_length=11)),
                ('telefone2', models.CharField(max_length=11)),
                ('vinculo_institucional', models.CharField(max_length=255)),
                ('curso', models.CharField(max_length=255)),
                ('periodo', models.CharField(max_length=255)),
                ('dia', models.ManyToManyField(to='gestaoapp.Horario')),
                ('perfil', models.ForeignKey(to='gestaoapp.Perfil')),
            ],
            options={
                'abstract': False,
                'verbose_name': 'user',
                'verbose_name_plural': 'users',
            },
            bases=('auth.user',),
            managers=[
                ('objects', django.contrib.auth.models.UserManager()),
            ],
        ),
    ]
