from django.shortcuts import render, redirect
from django.views.generic.base import View
from gestaoapp.forms.aluno import FormAluno
from gestaoapp.models.aluno import Aluno

class CadastroAluno(View):

	template = 'aluno/cadastro.html'

	def get(self, request, aluno_id=None):

		if aluno_id:
			nome = Aluno.objects.get(id=aluno_id)
			form = FormAluno(instance= nome)
			editar=True
		else:
			form = FormAluno()
			editar=False
		
		return render(request, self.template, {'form': form,'editar':editar})

	def post(self, request, aluno_id=None):
		
		if aluno_id:
			nome = Aluno.objects.get(id=aluno_id)
			form = FormAluno(instance=nome, data=request.POST)
		else:

			form = FormAluno(request.POST)
			print(type(form['filho'].value()))
		if form.is_valid():
			form.save(request)

			return redirect('/')

		else:
			return render(request, self.template, {'form': form})
