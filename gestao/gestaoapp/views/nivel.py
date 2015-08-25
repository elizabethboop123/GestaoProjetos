from django.shortcuts import render, redirect
from django.views.generic.base import View
from gestaoapp.forms.nivel import FormNivel
from gestaoapp.models.nivel import Nivel
from gestaoapp.views.loginrequired import LoginRequiredMixin

class CadastroNivel(LoginRequiredMixin, View):

	template = 'nivel/cadastro.html'

	def get(self, request, nivel_id=None):

		if nivel_id:
			nivel = Nivel.objects.get(id=nivel_id)
			form = FormNivel(instance= nivel)
			editar=True
		else:
			form = FormNivel()
			editar=False
		
		return render(request, self.template, {'form': form,'editar':editar})

	def post(self, request, nivel_id=None):
		
		if nivel_id:
			nivel = Nivel.objects.get(id=nivel_id)
			form = FormNivel(instance=nivel, data=request.POST)
		else:

			form = FormNivel(request.POST)

		if form.is_valid():
			form.save(request)

			return redirect('/')

		else:
			return render(request, self.template, {'form': form})