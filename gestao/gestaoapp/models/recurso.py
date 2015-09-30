from django.db import models

class Recurso(models.Model):
	
	codigo = models.CharField(max_length=255, unique = True)
	nome = models.CharField(max_length=255)
	tipo = models.CharField(max_length=255)
	descricao = models.CharField(max_length = 255)

	def __unicode__(self):
		return self.nome