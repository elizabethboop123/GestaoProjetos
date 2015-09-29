from django.shortcuts import render, redirect
from django.views.generic.base import View
from gestaoapp.forms.recurso import FormRecurso
from gestaoapp.models.recurso import Recurso
from gestaoapp.models.usuario import Usuario
from gestaoapp.views.loginrequired import LoginRequiredMixin

class CadastroRecurso(LoginRequiredMixin,View):

	template = 'recurso/cadastro.html'

	def get(self, request, recurso_id=None):

		if recurso_id:
			nome = Recurso.objects.get(id=recurso_id)
			form = FormRecurso(instance= nome)
			editar=True
		else:
			form = FormRecurso()
			editar=False
		
		return render(request, self.template, {'form': form,'editar':editar})

	def post(self, request, recurso_id=None):
		
		if recurso_id:
			nome = Recurso.objects.get(id=recurso_id)
			form = FormRecurso(instance=nome, data=request.POST)
		else:

			form = FormRecurso(request.POST)
			
		if form.is_valid():
			dia = form.save(request)
			return redirect('/')

		else:
			return render(request, self.template, {'form': form})
