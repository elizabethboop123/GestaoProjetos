from django.shortcuts import render, redirect
from django.views.generic.base import View
from gestaoapp.forms.horario import FormHorario
from gestaoapp.models.horario import Horario
from gestaoapp.models.usuario import Usuario

class CadastroHorario(View):

	template = 'horario/cadastro.html'

	def get(self, request, horario_id=None):

		if horario_id:
			nome = Horario.objects.get(id=horario_id)
			form = FormHorario(instance= nome)
			editar=True
		else:
			form = FormHorario()
			editar=False
		
		return render(request, self.template, {'form': form,'editar':editar})

	def post(self, request, horario_id=None):
		
		if horario_id:
			nome = Horario.objects.get(id=horario_id)
			form = FormHorario(instance=nome, data=request.POST)
		else:

			form = FormHorario(request.POST)
			
		if form.is_valid():
			dia = form.save(request)
			user = Usuario.objects.get(id=request.user.id)
			user.dia.add(dia)

			return redirect('/')

		else:
			return render(request, self.template, {'form': form})
