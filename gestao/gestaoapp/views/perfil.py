from django.shortcuts import render, redirect
from django.views.generic.base import View
from gestaoapp.forms.perfil import FormPerfil
from gestaoapp.models.perfil import Perfil
from gestaoapp.views.loginrequired import LoginRequiredMixin

class CadastroPerfil(View):

	template = 'perfil/cadastro.html'

	def get(self, request, perfil_id=None):

		if perfil_id:
			nome = Perfil.objects.get(id=perfil_id)
			form = FormPerfil(instance= nome)
			editar=True
		else:
			form = FormPerfil()
			editar=False
		
		return render(request, self.template, {'form': form,'editar':editar})

	def post(self, request, perfil_id=None):
		
		if perfil_id:
			nome = Perfil.objects.get(id=perfil_id)
			form = FormPerfil(instance=nome, data=request.POST)
		else:

			form = FormPerfil(request.POST)
			
		if form.is_valid():
			form.save(request)

			return redirect('/')

		else:
			return render(request, self.template, {'form': form})
