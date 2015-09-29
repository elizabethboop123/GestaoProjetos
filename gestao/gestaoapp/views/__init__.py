from django.shortcuts import render
from django.template import RequestContext
from gestaoapp.views.usuario import CadastroUsuario, VerificarUsuario, ConsultaUsuario, LiberarUsuario, VisualizarUsuario, AdministrarUsuario
from gestaoapp.views.perfil import CadastroPerfil
from gestaoapp.views.horario import CadastroHorario
from gestaoapp.views.nucleo import CadastroNucleo
from gestaoapp.views.recurso import CadastroRecurso


def sucesso(request):
	return render(request, 'usuario/sucesso.html')

def cadastro_liberado(request):
	return render(request, 'usuario/cadastro_liberado.html')