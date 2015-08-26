from django.db import models
from django.contrib.auth.models import User

class Pessoa (User):
	rg = models.CharField(max_length=255)
	cpf = models.CharField(max_length=11)
	rua = models.CharField(max_length=255)
	numero = models.CharField(max_length=255)
	complemento = models.CharField(max_length=255)
	bairro = models.CharField(max_length=255)
	cidade = models.CharField(max_length=255)
	estado = models.CharField(max_length=255)
	cep = models.CharField(max_length=255)
	telefone = models.CharField(max_length=255)
	dt_nascimento = models.DateField()
	sexo = models.CharField(max_length=255)

	def __unicode__(self):
		return self.first_name