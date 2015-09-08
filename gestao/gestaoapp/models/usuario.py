from django.db import models
from django.contrib.auth.models import User
from gestaoapp.models.perfil import Perfil
from gestaoapp.models.horario import Horario

class Usuario(User):
	
	email_opcional = models.EmailField(max_length=254)
	matricula = models.CharField(max_length=255)
	foto = models.FileField(null = True, blank=True, upload_to='')
	carga_horaria = models.IntegerField()
	telefone1 = models.CharField(max_length=11)
	telefone2 = models.CharField(max_length=11, blank=True)
	vinculo_institucional = models.CharField(max_length=255)
	curso = models.CharField(max_length=255)
	periodo =models.CharField(max_length=255)
	perfil = models.ForeignKey(Perfil, null=True, blank=True)
	dia = models.ManyToManyField(Horario, blank=True)

	def __unicode__(self):
		return self.first_name