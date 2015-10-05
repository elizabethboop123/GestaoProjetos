from django.shortcuts import render, redirect
from django.views.generic.base import View
from gestaoapp.forms.atividade import FormAtividade
from gestaoapp.models.atividade import Atividade
from gestaoapp.views.loginrequired import LoginRequiredMixin

class CadastroAtividade(View):

	template = 'atividade/cadastro.html'

	def get(self, request, atividade_id=None):

		if atividade_id:
			nome = Atividade.objects.get(id=atividade_id)
			form = FormAtividade(instance= nome)
			editar=True
		else:
			form = FormAtividade()
			editar=False
		
		return render(request, self.template, {'form': form,'editar':editar})

	def post(self, request, atividade_id=None):
		
		if atividade_id:
			nome = Atividade.objects.get(id=atividade_id)
			form = FormAtividade(instance=nome, data=request.POST)
		else:

			form = FormAtividade(request.POST)
			
		if form.is_valid():
			form.save(request)
			return redirect('/atividade')

		else:
			return render(request, self.template, {'form': form})
