from django import forms
from gestaoapp.models import HoraProjeto


class FormHoraProjeto(forms.ModelForm):

	class Meta:
		model = HoraProjeto
		fields = "__all__" 