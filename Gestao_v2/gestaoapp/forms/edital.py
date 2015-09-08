from django import forms
from gestaoapp.models import Edital


class FormEdital(forms.ModelForm):

	class Meta:
		model = Edital
		fields = "__all__" 