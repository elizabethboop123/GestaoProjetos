from django.shortcuts import render, redirect
from django.views.generic.base import View
from gestaoapp.forms.contratado import FormContratado
from gestaoapp.models.contratado import Contratado

class CadastroContratado(View):

	template = 'contratado/cadastro.html'

	def get(self, request, contratado_id=None):

		if contratado_id:
			contratado = Contratado.objects.get(id=contratado_id)
			form = FormContratado(instance= contratado)
			editar=True
		else:
			form = FormContratado()
			editar=False
		
		return render(request, self.template, {'form': form,'editar':editar})

	def post(self, request, contratado_id=None):
		
		if contratado_id:
			contratado = Contratado.objects.get(id=contratado_id)
			form = FormContratado(instance=contratado, data=request.POST)
		else:

			form = FormContratado(request.POST)

		if form.is_valid():
			form.save(request)

			return redirect('/')

		else:
			return render(request, self.template, {'form': form})