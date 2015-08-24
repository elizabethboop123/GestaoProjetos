from django.db import models
from django.contrib.auth.models import User

class Coordenador (User):
	rg = models.CharField(max_length=255)
	cpf = models.CharField(max_length=11)
	siape = models.CharField(max_length=255)
	graduacao = models.CharField(max_length=255)

	def __unicode__(self):
		return self.first_name