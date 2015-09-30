# from django.db import models
# from gestaoapp.models.recurso import Recurso
# from gestaoapp.models.nucleo import Nucleo
# from gestaoapp.models.usuario import Usuario
# from gestaoapp.models.atividade import Atividade
# from gestaoapp.models.artefato import Artefato



# class Projeto(models.Model):
	
# 	codigo = models.CharField(max_length= 255)
# 	nome = models.CharField(max_length = 255)
# 	duração = models.CharField(max_length = 255)
# 	data_inicio = models.DateField()
# 	data_fim = models.DateField()
# 	situacao = models.BooleanField()
# 	qtd_bolsa = models.IntegerField()
# 	nucleo = models.ManyToManyField(Nucleo)
# 	atividade = models.ManyToManyField(Atividade)
# 	equipe = models.ManyToManyField(Usuario)
# 	recurso = models.ManyToManyField(Recurso)
# 	coordenador = models.ForeignKey(Usuario)
# 	endereco_git = models.URLField(max_length=200)
# 	data_cadastro = data_fim = models.DateField(auto_now= True)
# 	descricao = models.CharField(max_length = 255)
# 	tipo = models.ForeignKey(TipoProjeto)

# 	def __unicode__(self):
# 		return self.nome