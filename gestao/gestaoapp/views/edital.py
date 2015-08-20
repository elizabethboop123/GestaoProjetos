from django.shortcuts import render, redirect
from django.views.generic.base import View
from gestaoapp.forms.edital import FormEdital
from gestaoapp.models.edital import Edital

class CadastroEdital(View):

	template = 'edital/cadastro.html'

	def get(self, request, edital_id=None):

		if edital_id:
			edital = Edital.objects.get(id=edital_id)
			form = FormEdital(instance= edital)
			editar=True
		else:
			form = FormEdital()
			editar=False
		
		return render(request, self.template, {'form': form,'editar':editar})

	def post(self, request, edital_id=None):
		
		if edital_id:
			edital = Edital.objects.get(id=edital_id)
			form = FormEdital(instance=edital, data=request.POST)
		else:

			form = FormEdital(request.POST)

		if form.is_valid():
			form.save(request)

			return redirect('/')

		else:
			return render(request, self.template, {'form': form})