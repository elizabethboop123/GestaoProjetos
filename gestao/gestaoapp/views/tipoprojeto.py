from django.shortcuts import render, redirect
from django.views.generic.base import View
from gestaoapp.forms.tipoprojeto import FormTipoProjeto
from gestaoapp.models.tipoprojeto import TipoProjeto
from gestaoapp.views.loginrequired import LoginRequiredMixin

class CadastroTipoProjeto(LoginRequiredMixin,View):

	template = 'projeto/tipo/cadastro.html'

	def get(self, request, tipoprojeto_id=None):

		if tipoprojeto_id:
			nome = TipoProjeto.objects.get(id=tipoprojeto_id)
			form = FormTipoProjeto(instance= nome)
			editar=True
		else:
			form = FormTipoProjeto()
			editar=False
		
		return render(request, self.template, {'form': form,'editar':editar})

	def post(self, request, tipoprojeto_id=None):
		
		if tipoprojeto_id:
			nome = TipoProjeto.objects.get(id=tipoprojeto_id)
			form = FormTipoProjeto(instance=nome, data=request.POST)
		else:
			form = FormTipoProjeto(request.POST)
			
		if form.is_valid():
			form.save(request)
			return redirect('/sucesso')
		else:
			return render(request, self.template, {'form': form})