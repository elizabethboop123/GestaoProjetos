from django.shortcuts import render, redirect
from django.views.generic.base import View
from gestaoapp.forms.graduacao import FormGraduacao
from gestaoapp.models.graduacao import Graduacao
from gestaoapp.views.loginrequired import LoginRequiredMixin

class CadastroGraduacao(LoginRequiredMixin, View):

	template = 'graduacao/cadastro.html'

	def get(self, request, graduacao_id=None):

		if graduacao_id:
			graduacao = Graduacao.objects.get(id=graduacao_id)
			form = FormGraduacao(instance= graduacao)
			editar=True
		else:
			form = FormGraduacao()
			editar=False
		
		return render(request, self.template, {'form': form,'editar':editar})

	def post(self, request, graduacao_id=None):
		
		if graduacao_id:
			graduacao = Graduacao.objects.get(id=graduacao_id)
			form = FormGraduacao(instance=graduacao, data=request.POST)
		else:

			form = FormGraduacao(request.POST)

		if form.is_valid():
			form.save(request)

			return redirect('/')

		else:
			return render(request, self.template, {'form': form})