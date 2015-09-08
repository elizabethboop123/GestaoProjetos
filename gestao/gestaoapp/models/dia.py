from django.db import models

class Dia(models.Model):
	
	dia = models.CharField(max_length=255)
	
	def __unicode__(self):
		return self.dia