from django.db import models
from gestaoapp.models.pessoa import Pessoa
from gestaoapp.models.graduacao import Graduacao

class Professor (Pessoa):
	siape = models.CharField(max_length=255)
	graduacao = models.ForeignKey(Graduacao)

	def __unicode__(self):
		return self.first_name