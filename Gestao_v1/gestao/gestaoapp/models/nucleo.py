from django.db import models

class Nucleo (models.Model):
	nome_nucleo = models.CharField(max_length=255)
	descricao = models.CharField(max_length =255)


	def __unicode__(self):
		return self.nome_nucleo