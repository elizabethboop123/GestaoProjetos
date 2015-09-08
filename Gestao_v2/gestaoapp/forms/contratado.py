from django import forms
from gestaoapp.models import Contratado


class FormContratado(forms.ModelForm):

	class Meta:
		model = Contratado
		fields = "__all__" 