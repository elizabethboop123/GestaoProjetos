from django.shortcuts import render, redirect
from django.views.generic.base import View
from gestaoapp.forms.nucleo import FormNucleo
from gestaoapp.models.nucleo import Nucleo
from gestaoapp.models.usuario import Usuario
from gestaoapp.views.loginrequired import LoginRequiredMixin

class CadastroNucleo(LoginRequiredMixin,View):

	template = 'nucleo/cadastro.html'

	def get(self, request, nucleo_id=None):

		if nucleo_id:
			nome = Horario.objects.get(id=nucleo_id)
			form = FormNucleo(instance= nome)
			editar=True
		else:
			form = FormNucleo()
			editar=False
		
		return render(request, self.template, {'form': form,'editar':editar})

	def post(self, request, nucleo_id=None):
		
		if nucleo_id:
			nome = Horario.objects.get(id=nucleo_id)
			form = FormNucleo(instance=nome, data=request.POST)
		else:

			form = FormNucleo(request.POST)
			
		if form.is_valid():
			dia = form.save(request)
			user = Usuario.objects.get(id=request.user.id)
			user.dia.add(dia)

			return redirect('/horario')

		else:
			return render(request, self.template, {'form': form})
