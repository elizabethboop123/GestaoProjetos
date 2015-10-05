from django.db import models
from gestaoapp.models.recurso import Recurso
from gestaoapp.models.nucleo import Nucleo
from gestaoapp.models.usuario import Usuario
from gestaoapp.models.atividade import Atividade
from gestaoapp.models.edital import Edital
from gestaoapp.models.tipoprojeto import TipoProjeto
from gestaoapp.models.situacaoprojeto import SituacaoProjeto

class Projeto(models.Model):
	
	codigo = models.CharField(max_length= 255)
	nome = models.CharField(max_length = 255)
	descricao = models.CharField(max_length = 255)
	tipo = models.ForeignKey(TipoProjeto)
	duracao = models.CharField(max_length = 255)
	data_inicio = models.DateField()
	data_fim = models.DateField()
	situacao = models.ForeignKey(SituacaoProjeto)
	edital = models.ManyToManyField(Edital)
	qtd_bolsa = models.IntegerField()
	nucleo = models.ManyToManyField(Nucleo)
	atividade = models.ManyToManyField(Atividade)
	equipe = models.ManyToManyField(Usuario, related_name = "bolsistas")
	recurso = models.ManyToManyField(Recurso)
	coordenador = models.ForeignKey(Usuario,related_name = "coordenador")
	data_cadastro =  models.DateField(auto_now= True)
	endereco_git = models.URLField(max_length=200)

	def __unicode__(self):
		return self.nome