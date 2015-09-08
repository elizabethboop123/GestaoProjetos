from django import forms
from gestaoapp.models import Nivel


class FormNivel(forms.ModelForm):

	class Meta:
		model = Nivel
		fields = "__all__" 