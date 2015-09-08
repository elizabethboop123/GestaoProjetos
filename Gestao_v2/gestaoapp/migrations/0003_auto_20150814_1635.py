# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings
import django.contrib.auth.models


class Migration(migrations.Migration):

    dependencies = [
        ('auth', '0006_require_contenttypes_0002'),
        ('admin', '0001_initial'),
        ('gestaoapp', '0002_nucleo_projeto'),
    ]

    operations = [
        migrations.CreateModel(
            name='Contratado',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('bolsa', models.BooleanField()),
                ('dt_inicio', models.DateField()),
                ('dt_termino', models.DateField()),
            ],
        ),
        migrations.CreateModel(
            name='Edital',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('numero', models.CharField(max_length=255)),
                ('orgao_concedente', models.CharField(max_length=255)),
                ('verba', models.FloatField()),
                ('qtd_bolsa', models.IntegerField()),
                ('dt_inicio', models.DateField()),
                ('dt_termino', models.DateField()),
            ],
        ),
        migrations.CreateModel(
            name='Graduacao',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('titulo', models.CharField(max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='Pessoa',
            fields=[
                ('user_ptr', models.OneToOneField(parent_link=True, auto_created=True, primary_key=True, serialize=False, to=settings.AUTH_USER_MODEL)),
                ('rg', models.CharField(max_length=255)),
                ('cpf', models.CharField(max_length=11)),
                ('endereco', models.CharField(max_length=255)),
                ('telefone', models.CharField(max_length=255)),
                ('dt_nascimento', models.DateField()),
                ('sexo', models.CharField(max_length=255)),
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
        migrations.RemoveField(
            model_name='bolsista',
            name='user_ptr',
        ),
        migrations.RemoveField(
            model_name='coordenador',
            name='user_ptr',
        ),
        migrations.RenameField(
            model_name='nucleo',
            old_name='nome_nucleo',
            new_name='nome',
        ),
        migrations.RenameField(
            model_name='projeto',
            old_name='nome_projeto',
            new_name='nome',
        ),
        migrations.RemoveField(
            model_name='projeto',
            name='nucleo',
        ),
        migrations.AddField(
            model_name='nucleo',
            name='projeto',
            field=models.ManyToManyField(to='gestaoapp.Projeto', null=True),
        ),
        migrations.AlterField(
            model_name='projeto',
            name='bolsista',
            field=models.ForeignKey(to='gestaoapp.Aluno'),
        ),
        migrations.AlterField(
            model_name='projeto',
            name='coordenador',
            field=models.ForeignKey(to='gestaoapp.Professor'),
        ),
        migrations.CreateModel(
            name='Aluno',
            fields=[
                ('pessoa_ptr', models.OneToOneField(parent_link=True, auto_created=True, primary_key=True, serialize=False, to='gestaoapp.Pessoa')),
                ('nome_responsavel', models.CharField(max_length=255)),
                ('tel_responsavel', models.CharField(max_length=20)),
                ('matricula', models.CharField(max_length=255)),
                ('filho', models.BooleanField()),
                ('nivel', models.CharField(max_length=255)),
                ('curso', models.CharField(max_length=255)),
            ],
            options={
                'abstract': False,
                'verbose_name': 'user',
                'verbose_name_plural': 'users',
            },
            bases=('gestaoapp.pessoa',),
            managers=[
                ('objects', django.contrib.auth.models.UserManager()),
            ],
        ),
        migrations.CreateModel(
            name='Professor',
            fields=[
                ('pessoa_ptr', models.OneToOneField(parent_link=True, auto_created=True, primary_key=True, serialize=False, to='gestaoapp.Pessoa')),
                ('siape', models.CharField(max_length=255)),
                ('graduacao', models.ForeignKey(to='gestaoapp.Graduacao')),
            ],
            options={
                'abstract': False,
                'verbose_name': 'user',
                'verbose_name_plural': 'users',
            },
            bases=('gestaoapp.pessoa',),
            managers=[
                ('objects', django.contrib.auth.models.UserManager()),
            ],
        ),
        migrations.DeleteModel(
            name='Bolsista',
        ),
        migrations.DeleteModel(
            name='Coordenador',
        ),
        migrations.AddField(
            model_name='contratado',
            name='projeto',
            field=models.ForeignKey(to='gestaoapp.Projeto'),
        ),
        migrations.AddField(
            model_name='projeto',
            name='edital',
            field=models.ForeignKey(default=1, to='gestaoapp.Edital'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='contratado',
            name='aluno',
            field=models.ForeignKey(to='gestaoapp.Aluno'),
        ),
    ]
