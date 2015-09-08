from django.db import models
from gestaoapp.models import Coordenador
from gestaoapp.models import Bolsista
from gestaoapp.models import Nucleo

class Projeto(models.Model):
	nome_projeto = models.CharField(max_length=255)
	coordenador = models.ForeignKey(Coordenador)
	nucleo = models.ForeignKey(Nucleo)
	bolsista = models.ForeignKey(Bolsista)
	cliente = models.CharField(max_length=255)
	data_inicio = models.DateField()
	data_termino = models.DateField()

	def __unicode__(self):
		return self.nome_projeto