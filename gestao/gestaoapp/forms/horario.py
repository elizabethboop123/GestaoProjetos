from django import forms
from gestaoapp.models import Horario


class FormHorario(forms.ModelForm):

	class Meta:
		model = Horario
		fields = "__all__" 