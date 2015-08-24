from django.shortcuts import render, redirect
from django.views.generic.base import View
from gestaoapp.forms.coordenador import FormCoordenador
from gestaoapp.models.coordenador import Coordenador

class CadastroCoordenador(View):

	template = 'coordenador/cadastro.html'

	def get(self, request, coordenador_id=None):

		if coordenador_id:
			nome = Coordenador.objects.get(id=coordenador_id)
			form = FormCoordenador(instance= nome)
			editar=True
		else:
			form = FormCoordenador()
			editar=False
		
		return render(request, self.template, {'form': form,'editar':editar})

	def post(self, request, coordenador_id=None):
		
		if coordenador_id:
			nome = Coordenador.objects.get(id=coordenador_id)
			form = FormCoordenador(instance=nome, data=request.POST)
		else:

			form = FormCoordenador(request.POST)

		if form.is_valid():
			form.save(request)

			return redirect('/')

		else:
			return render(request, self.template, {'form': form})