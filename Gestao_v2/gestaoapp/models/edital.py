from django.db import models

class Edital (models.Model):
	numero = models.CharField(max_length=255)
	orgao_concedente = models.CharField(max_length =255)
	verba = models.FloatField()
	qtd_bolsa = models.IntegerField()
	dt_inicio = models.DateField()
	dt_termino = models.DateField()

	def __unicode__(self):
		return self.numero