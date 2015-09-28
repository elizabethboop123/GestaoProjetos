from django.db import models
from django.contrib.auth.models import User
from gestaoapp.models.perfil import Perfil
from gestaoapp.models.horario import Horario
from PIL import Image

class Usuario(User):
	
	email_opcional = models.EmailField(max_length=254, null=True, blank=True)
	matricula = models.CharField(max_length=255, unique = True)
	foto = models.ImageField('Imagem', upload_to='imagens')
	carga_horaria = models.IntegerField()
	telefone1 = models.CharField(max_length=11)
	telefone2 = models.CharField(max_length=11, blank=True, null=True)
	vinculo_institucional = models.CharField(max_length=255,null=True, blank=True)
	curso = models.CharField(max_length=255,null=True, blank=True)
	periodo =models.CharField(max_length=255,null=True, blank=True)
	perfil = models.ForeignKey(Perfil, null=True, blank=True)
	dia = models.ManyToManyField(Horario, blank=True)
	verificacao=models.CharField(max_length=255,null=True, blank=True, unique = True)
	verificado = models.BooleanField()

	def __unicode__(self):
		return self.first_name