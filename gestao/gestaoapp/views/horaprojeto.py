from django.shortcuts import render, redirect
from django.views.generic.base import View
from gestaoapp.forms.horaprojeto import FormHoraProjeto
from gestaoapp.models.horaprojeto import HoraProjeto
from gestaoapp.forms.busca import Busca
from gestaoapp.views.loginrequired import LoginRequiredMixin

class CadastroHoraProjeto(LoginRequiredMixin,View):

	template = 'horaprojeto/cadastro.html'

	def get(self, request, horaprojeto_id=None):

		if horaprojeto_id:
			nome = HoraProjeto.objects.get(id=horaprojeto_id)
			form = FormHoraProjeto(instance= nome)
			editar=True
		else:
			form = FormHoraProjeto()
			editar=False
		
		return render(request, self.template, {'form': form,'editar':editar})

	def post(self, request, horaprojeto_id=None):
		
		if horaprojeto_id:
			nome = HoraProjeto.objects.get(id=horaprojeto_id)
			form = FormHoraProjeto(instance=nome, data=request.POST)
		else:
			form = FormHoraProjeto(request.POST)
			
		if form.is_valid():
			form.save(request)
			return redirect('/sucesso')
		else:
			return render(request, self.template, {'form': form})
