from django.shortcuts import render, redirect
from django.views.generic.base import View
from gestaoapp.forms.usuario import FormNucleo
from gestaoapp.models.nucleo import Nucleo
from gestaoapp.views.loginrequired import LoginRequiredMixin

class CadastroNucleo(View):

	template = 'usuario/cadastro.html'

	def get(self, request , nucleo_id = None):

		if nucleo_id:
			nome = Usuario.objects.get(id =nucleo_id)
			form = FormNucleo(instance= nome)
			editar=True
		else:
			form = FormNucleo()
			editar=False

		return render(request, self.template, {'form': form,'editar':editar})

	def post(self, request, nucleo_id=None):
		
		if nucleo_id:
			nome = Usuario.objects.get(id=nucleo_id)
			form = FormNucleo(instance=nome, data=request.POST)
		else:
			print(request.FILES)
			form = FormNucleo(request.POST, request.FILES)

		if form.is_valid():
			form.save(request)
			return redirect('/sucesso')

		else:
			return render(request, self.template, {'form': form})
