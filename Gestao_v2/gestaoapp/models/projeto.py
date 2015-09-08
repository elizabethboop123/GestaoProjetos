from django.db import models
from gestaoapp.models.professor import Professor
from gestaoapp.models.aluno import Aluno
from gestaoapp.models.edital import Edital

class Projeto(models.Model):
	nome = models.CharField(max_length=255)
	coordenador = models.ForeignKey(Professor,related_name = "tchau")
	bolsista = models.ManyToManyField(Aluno)
	cliente = models.CharField(max_length=255)
	data_inicio = models.DateField()
	data_termino = models.DateField()
	edital = models.ForeignKey(Edital)
	participante = models.ManyToManyField(Professor,related_name = "oi")


	def __unicode__(self):
		return self.nome
		