from django.db import models

class Graduacao (models.Model):
	titulo = models.CharField(max_length=255)
	
	def __unicode__(self):
		return self.titulo