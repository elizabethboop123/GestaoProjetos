from django import forms
from gestaoapp.models import Projeto

class FormProjeto(forms.ModelForm):

	class Meta:
		model = Projeto
		fields = "__all__" 