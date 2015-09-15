from django import forms
from gestaoapp.models import Usuario

class FormLiberar(forms.ModelForm):

	def save(self, commit=True):
			
		if commit:
			usuario.is_active = True
			return usuario
			
	class Meta:
		model = Usuario
		exclude = ('__all__') 