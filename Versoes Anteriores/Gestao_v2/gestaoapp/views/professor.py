from django.shortcuts import render, redirect
from django.views.generic.base import View
from gestaoapp.forms.professor import FormProfessor
from gestaoapp.models.professor import Professor
from gestaoapp.views.loginrequired import LoginRequiredMixin

class CadastroProfessor(LoginRequiredMixin, View):

	template = 'professor/cadastro.html'

	def get(self, request, professor_id=None):

		if professor_id:
			nome = Professor.objects.get(id=professor_id)
			form = FormProfessor(instance= nome)
			editar=True
		else:
			form = FormProfessor()
			editar=False
		
		return render(request, self.template, {'form': form,'editar':editar})

	def post(self, request, professor_id=None):
		
		if professor_id:
			nome = Professor.objects.get(id=professor_id)
			form = FormProfessor(instance=nome, data=request.POST)
		else:

			form = FormProfessor(request.POST)

		if form.is_valid():
			form.save(request)

			return redirect('/')

		else:
			return render(request, self.template, {'form': form})