from django.db import models
from django.contrib.auth.models import User

class Bolsista (User):
	nome_responsavel = models.CharField(max_length=255)
	matricula = models.CharField(max_length=255)
	cpf = models.CharField(max_length=11)
	rg = models.CharField(max_length=255)

	def __unicode__(self):
		return self.first_name