from django.shortcuts import render, redirect
from django.views.generic.base import View
from gestaoapp.forms.curso import FormCurso
from gestaoapp.models.curso import Curso
from gestaoapp.views.loginrequired import LoginRequiredMixin

class CadastroCurso(LoginRequiredMixin, View):

	template = 'curso/cadastro.html'

	def get(self, request, curso_id=None):

		if curso_id:
			curso = Curso.objects.get(id=curso_id)
			form = FormCurso(instance= curso)
			editar=True
		else:
			form = FormCurso()
			editar=False
		
		return render(request, self.template, {'form': form,'editar':editar})

	def post(self, request, curso_id=None):
		
		if curso_id:
			curso = Curso.objects.get(id=curso_id)
			form = FormCurso(instance=curso, data=request.POST)
		else:

			form = FormCurso(request.POST)

		if form.is_valid():
			form.save(request)

			return redirect('/')

		else:
			return render(request, self.template, {'form': form})