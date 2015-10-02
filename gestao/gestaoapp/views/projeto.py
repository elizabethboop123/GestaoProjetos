from django.shortcuts import render, redirect
from django.views.generic.base import View
from gestaoapp.forms.projeto import FormProjeto
from gestaoapp.models.projeto import Projeto
from gestaoapp.views.loginrequired import LoginRequiredMixin

class CadastroProjeto(LoginRequiredMixin,View):

	template = 'projeto/cadastro.html'

	def get(self, request, projeto_id=None):

		if projeto_id:
			nome = Projeto.objects.get(id=projeto_id)
			form = FormProjeto(instance= nome)
			editar=True
		else:
			form = FormProjeto()
			editar=False
		
		return render(request, self.template, {'form': form,'editar':editar})

	def post(self, request, projeto_id=None):
		
		if projeto_id:
			nome = Projeto.objects.get(id=projeto_id)
			form = FormProjeto(instance=nome, data=request.POST)
		else:
			form = FormProjeto(request.POST)
			
		if form.is_valid():
			form.save(request)
			return redirect('/projeto')
		else:
			return render(request, self.template, {'form': form})

