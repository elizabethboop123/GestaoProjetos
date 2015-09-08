from django.db import models
from gestaoapp.models.projeto import Projeto

class Nucleo (models.Model):
	nome = models.CharField(max_length=255)
	descricao = models.CharField(max_length =255)
	projeto = models.ManyToManyField(Projeto)

	def __unicode__(self):
		return self.nome