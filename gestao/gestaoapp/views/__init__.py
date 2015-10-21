from django.shortcuts import render
from django.template import RequestContext
from gestaoapp.views.usuario import CadastroUsuario, VerificarUsuario, ConsultaUsuario, LiberarUsuario, VisualizarUsuario, AdministrarUsuario
from gestaoapp.views.perfil import CadastroPerfil
from gestaoapp.views.horario import CadastroHorario
from gestaoapp.views.nucleo import CadastroNucleo, ConsultaNucleo, VisualizarNucleo
from gestaoapp.views.recurso import CadastroRecurso, ConsultaRecurso, VisualizarVisualizar
from gestaoapp.views.tiporecurso import CadastroTipoRecurso
from gestaoapp.views.artefato import CadastroArtefato, ConsultaArtefato, VisualizarArtefato
from gestaoapp.views.atividade import CadastroAtividade, ConsultaAtividade, VisualizarAtividade
from gestaoapp.views.edital import CadastroEdital, ConsultaEdital, VisualizarEdital
from gestaoapp.views.projeto import CadastroProjeto, ConsultaProjeto, VisualizarProjeto
from gestaoapp.views.tipoprojeto import CadastroTipoProjeto

def sucesso(request):
	return render(request, 'usuario/sucesso.html')

def cadastro_liberado(request):
	return render(request, 'usuario/cadastro_liberado.html')