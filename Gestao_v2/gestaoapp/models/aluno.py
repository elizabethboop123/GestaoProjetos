from django.db import models
from gestaoapp.models.pessoa import Pessoa
from gestaoapp.models.nivel import Nivel
from gestaoapp.models.curso import Curso

class Aluno (Pessoa):
	nome_responsavel = models.CharField(max_length=255)
	tel_responsavel = models.CharField(max_length=20)
	matricula = models.CharField(max_length=255)
	filho = models.BooleanField()
	nivel = models.ForeignKey(Nivel)
	curso = models.ForeignKey(Curso)

	def __unicode__(self):
		return self.first_name