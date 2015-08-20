from django.db import models
from gestaoapp.models.pessoa import Pessoa

class Aluno (Pessoa):
	nome_responsavel = models.CharField(max_length=255)
	tel_responsavel = models.CharField(max_length=20)
	matricula = models.CharField(max_length=255)
	filho = models.BooleanField()
	nivel = models.CharField(max_length=255)
	curso = models.CharField(max_length=255)

	def __unicode__(self):
		return self.first_name