from django import forms
from gestaoapp.models import Perfil


class FormPerfil(forms.ModelForm):

	class Meta:
		model = Perfil
		fields = "__all__" 