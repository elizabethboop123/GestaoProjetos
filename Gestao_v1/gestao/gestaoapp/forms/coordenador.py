from django import forms
from gestaoapp.models import Coordenador

class FormCoordenador(forms.ModelForm):
	password = forms.CharField(widget=forms.PasswordInput(attrs={'id': 'password'}))
	confirma_senha = forms.CharField(widget=forms.PasswordInput(attrs={'id': 'confirma_senha'}))
	

	def clean_confirma_senha(self):

		if 'password' in self.cleaned_data:

			password = self.cleaned_data['password']
			confirma_senha = self.cleaned_data['confirma_senha']

			if password == confirma_senha:
				return confirma_senha
			else:
				raise forms.ValidationError('Senha nao confere')
		else:
			raise forms.ValidationError('Senha nao confere')
		
	def save(self, commit=True):
		self.clean_confirma_senha()
		coordenador = super(FormCoordenador, self).save(commit=False)
		coordenador.set_password(self.cleaned_data['password'])
		if commit:
			coordenador.save()
		return coordenador

	class Meta:
		model = Coordenador
		exclude = ('last_login',"last_name","groups","user_permissions","helptext","is_staff","date_joined","tipo",'is_active') 