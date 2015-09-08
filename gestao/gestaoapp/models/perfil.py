from django.db import models

class Perfil(models.Model):
	
	nome = models.CharField(max_length=255)
	
	def __unicode__(self):
		return self.nome