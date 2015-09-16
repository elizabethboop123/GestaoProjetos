from django.shortcuts import render, redirect
from django.views.generic.base import View
from gestaoapp.forms.usuario import FormUsuario
from gestaoapp.models.usuario import Usuario

class CadastroUsuario(View):

	template = 'usuario/cadastro.html'

	def get(self, request , usuario_id = None):

		if usuario_id:
			nome = Usuario.objects.get(id =usuario_id)
			form = FormUsuario(instance= nome)
			editar=True
		else:
			form = FormUsuario()
			editar=False

		return render(request, self.template, {'form': form,'editar':editar})

	def post(self, request, usuario_id=None):
		
		if usuario_id:
			nome = Usuario.objects.get(id=usuario_id)
			form = FormUsuario(instance=nome, data=request.POST)
		else:
			form = FormUsuario(request.POST, request.FILES)
		if form.is_valid():
			form.save(request)
			return redirect('/sucesso')

		else:
			return render(request, self.template, {'form': form})

class LiberarUsuario(View):

	template = 'usuario/conta_desbloqueada.html'

	def get(self, request, usuario_verificacao = None):

		if usuario_verificacao:
			nome = Usuario.objects.get(verificacao =usuario_verificacao)
			nome.is_active = True
			nome.save()
			
		return render(request, self.template)
