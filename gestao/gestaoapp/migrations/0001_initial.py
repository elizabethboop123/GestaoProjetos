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
            name='Artefato',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('nome', models.CharField(max_length=255)),
                ('descricao', models.CharField(max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='Atividade',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('nome', models.CharField(max_length=255)),
                ('descricao', models.CharField(max_length=255)),
                ('artefato', models.ManyToManyField(to='gestaoapp.Artefato', blank=True)),
            ],
        ),
        migrations.CreateModel(
            name='Dia',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('dia', models.CharField(max_length=255)),
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
            name='Horario',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('hora_inicio', models.TimeField()),
                ('hora_fim', models.TimeField()),
                ('turno', models.CharField(max_length=255)),
                ('data', models.ForeignKey(to='gestaoapp.Dia')),
            ],
        ),
        migrations.CreateModel(
            name='Nucleo',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('nome', models.CharField(max_length=255)),
                ('sigla', models.CharField(max_length=5)),
                ('descricao', models.CharField(max_length=255)),
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
            name='Projeto',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('codigo', models.CharField(max_length=255)),
                ('nome', models.CharField(max_length=255)),
                ('descricao', models.CharField(max_length=255)),
                ('duracao', models.CharField(max_length=255)),
                ('data_inicio', models.DateField()),
                ('data_fim', models.DateField()),
                ('situacao', models.BooleanField()),
                ('qtd_bolsa', models.IntegerField()),
                ('data_cadastro', models.DateField(auto_now=True)),
                ('endereco_git', models.URLField()),
                ('atividade', models.ManyToManyField(to='gestaoapp.Atividade')),
            ],
        ),
        migrations.CreateModel(
            name='Recurso',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('codigo', models.CharField(unique=True, max_length=255)),
                ('nome', models.CharField(max_length=255)),
                ('descricao', models.CharField(max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='TipoProjeto',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('tipo', models.CharField(max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='TipoRecurso',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('tipo', models.CharField(max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='Usuario',
            fields=[
                ('user_ptr', models.OneToOneField(parent_link=True, auto_created=True, primary_key=True, serialize=False, to=settings.AUTH_USER_MODEL)),
                ('email_opcional', models.EmailField(max_length=254, null=True, blank=True)),
                ('matricula', models.CharField(unique=True, max_length=255)),
                ('foto', models.ImageField(upload_to=b'imagens', verbose_name=b'Imagem')),
                ('carga_horaria', models.IntegerField()),
                ('telefone1', models.CharField(max_length=11)),
                ('telefone2', models.CharField(max_length=11, null=True, blank=True)),
                ('vinculo_institucional', models.CharField(max_length=255, null=True, blank=True)),
                ('curso', models.CharField(max_length=255, null=True, blank=True)),
                ('periodo', models.CharField(max_length=255, null=True, blank=True)),
                ('verificacao', models.CharField(max_length=255, unique=True, null=True, blank=True)),
                ('verificado', models.BooleanField()),
                ('dia', models.ManyToManyField(to='gestaoapp.Horario', blank=True)),
                ('perfil', models.ForeignKey(blank=True, to='gestaoapp.Perfil', null=True)),
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
        migrations.CreateModel(
            name='Vinculo',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('vinculo', models.CharField(max_length=255)),
            ],
        ),
        migrations.AddField(
            model_name='recurso',
            name='tipo',
            field=models.ForeignKey(to='gestaoapp.TipoRecurso'),
        ),
        migrations.AddField(
            model_name='projeto',
            name='coordenador',
            field=models.ForeignKey(related_name='coordenador', to='gestaoapp.Usuario'),
        ),
        migrations.AddField(
            model_name='projeto',
            name='edital',
            field=models.ManyToManyField(to='gestaoapp.Edital'),
        ),
        migrations.AddField(
            model_name='projeto',
            name='equipe',
            field=models.ManyToManyField(related_name='bolsistas', to='gestaoapp.Usuario'),
        ),
        migrations.AddField(
            model_name='projeto',
            name='nucleo',
            field=models.ManyToManyField(to='gestaoapp.Nucleo'),
        ),
        migrations.AddField(
            model_name='projeto',
            name='recurso',
            field=models.ManyToManyField(to='gestaoapp.Recurso'),
        ),
        migrations.AddField(
            model_name='projeto',
            name='tipo',
            field=models.ForeignKey(to='gestaoapp.TipoProjeto'),
        ),
    ]
