from django import forms
from gestaoapp.models import Graduacao


class FormGraduacao(forms.ModelForm):

	class Meta:
		model = Graduacao
		fields = "__all__" 