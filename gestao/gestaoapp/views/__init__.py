from django.shortcuts import render
from django.template import RequestContext
from gestaoapp.views.usuario import CadastroUsuario, VerificarUsuario, ConsultaUsuario, LiberarUsuario, VisualizarUsuario, AdministrarUsuario
from gestaoapp.views.perfil import CadastroPerfil
from gestaoapp.views.horario import CadastroHorario
from gestaoapp.views.nucleo import CadastroNucleo, ConsultaNucleo
from gestaoapp.views.recurso import CadastroRecurso, ConsultaRecurso
from gestaoapp.views.tiporecurso import CadastroTipoRecurso
from gestaoapp.views.artefato import CadastroArtefato, ConsultaArtefato
from gestaoapp.views.atividade import CadastroAtividade, ConsultaAtividade
from gestaoapp.views.edital import CadastroEdital, ConsultaEdital
from gestaoapp.views.projeto import CadastroProjeto, ConsultaProjeto, VisualizarProjeto
from gestaoapp.views.tipoprojeto import CadastroTipoProjeto

def sucesso(request):
	return render(request, 'usuario/sucesso.html')

def cadastro_liberado(request):
	return render(request, 'usuario/cadastro_liberado.html')