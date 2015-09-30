from django.shortcuts import render, redirect
from django.views.generic.base import View
from gestaoapp.forms.artefato import FormArtefato
from gestaoapp.models.artefato import Artefato
from gestaoapp.views.loginrequired import LoginRequiredMixin

class CadastroArtefato(LoginRequiredMixin,View):

	template = 'artefato/cadastro.html'

	def get(self, request, artefato_id=None):

		if artefato_id:
			nome = Artefato.objects.get(id=artefato_id)
			form = FormArtefato(instance= nome)
			editar=True
		else:
			form = FormArtefato()
			editar=False
		
		return render(request, self.template, {'form': form,'editar':editar})

	def post(self, request, artefato_id=None):
		
		if artefato_id:
			nome = Artefato.objects.get(id=artefato_id)
			form = FormArtefato(instance=nome, data=request.POST)
		else:
			form = FormArtefato(request.POST)
			
		if form.is_valid():
			form.save(request)
			return redirect('/artefato')
		else:
			return render(request, self.template, {'form': form})

