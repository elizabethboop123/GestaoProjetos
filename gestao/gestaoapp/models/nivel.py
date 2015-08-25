from django.db import models

class Nivel (models.Model):
	nivel = models.CharField(max_length=255)
	
	def __unicode__(self):
		return self.nivel