from django.db import models
from gestaoapp.models.dia import Dia

class Horario(models.Model):
	
	dia = models.ForeignKey(Dia)
	hora_inicio = models.TimeField()
	hora_fim = models.TimeField()
	turno = models.CharField(max_length=255)
	
	def __unicode__(self):
		return self.dia