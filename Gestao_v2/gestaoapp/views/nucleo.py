from django.shortcuts import render, redirect
from django.views.generic.base import View
from gestaoapp.forms.nucleo import FormNucleo
from gestaoapp.models.nucleo import Nucleo
from gestaoapp.views.loginrequired import LoginRequiredMixin

class CadastroNucleo(LoginRequiredMixin, View):

	template = 'nucleo/cadastro.html'

	def get(self, request, nucleo_id=None):

		if nucleo_id:
			nucleo = Nucleo.objects.get(id=nucleo_id)
			form = FormNucleo(instance= nucleo)
			editar=True
		else:
			form = FormNucleo()
			editar=False
		
		return render(request, self.template, {'form': form,'editar':editar})

	def post(self, request, nucleo_id=None):
		
		if nucleo_id:
			nucleo = Nucleo.objects.get(id=nucleo_id)
			form = FormNucleo(instance=nucleo, data=request.POST)
		else:

			form = FormNucleo(request.POST)

		if form.is_valid():
			form.save(request)

			return redirect('/')

		else:
			return render(request, self.template, {'form': form})