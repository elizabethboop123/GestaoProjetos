from django.shortcuts import render, redirect
from django.views.generic.base import View
from gestaoapp.forms.bolsista import FormBolsista
from gestaoapp.models.bolsista import Bolsista

class CadastroBolsista(View):

	template = 'bolsista/cadastro.html'

	def get(self, request, bolsista_id=None):

		if bolsista_id:
			nome = Bolsista.objects.get(id=bolsista_id)
			form = FormBolsista(instance= nome)
			editar=True
		else:
			form = FormBolsista()
			editar=False
		
		return render(request, self.template, {'form': form,'editar':editar})

	def post(self, request, bolsista_id=None):
		
		if bolsista_id:
			nome = Bolsista.objects.get(id=bolsista_id)
			form = FormBolsista(instance=nome, data=request.POST)
		else:

			form = FormBolsista(request.POST)

		if form.is_valid():
			form.save(request)

			return redirect('/')

		else:
			return render(request, self.template, {'form': form})
