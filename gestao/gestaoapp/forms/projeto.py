from django import forms
from gestaoapp.models import Projeto

class FormProjeto(forms.ModelForm):

	# def save(self, commit=True):
		
	# 	projeto = super(FormProjeto, self).save(commit=False)
		
	# 	if commit:
	# 		projeto.situacao = 'Pendente de Aprovacao'

	# 	return projeto
	
	class Meta:
		model = Projeto
		fields = "__all__"