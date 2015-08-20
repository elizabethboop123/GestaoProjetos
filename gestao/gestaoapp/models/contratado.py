from django.db import models
from gestaoapp.models.projeto import Projeto
from gestaoapp.models.aluno import Aluno

class Contratado (models.Model):

	projeto = models.ForeignKey(Projeto)
	aluno = models.ForeignKey(Aluno)
	bolsa = models.BooleanField()
	dt_inicio = models.DateField()
	dt_termino = models.DateField()

	def __unicode__(self):
		return self.aluno