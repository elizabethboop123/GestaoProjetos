from django.shortcuts import render
from django.template import RequestContext
from gestaoapp.views.usuario import CadastroUsuario, LiberarUsuario, ConsultaUsuario
from gestaoapp.views.perfil import CadastroPerfil
from gestaoapp.views.horario import CadastroHorario


def sucesso(request):
	return render(request, 'usuario/sucesso.html')

def cadastro_liberado(request):
	return render(request, 'usuario/cadastro_liberado.html')