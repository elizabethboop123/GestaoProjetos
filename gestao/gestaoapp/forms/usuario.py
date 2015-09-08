from django import forms
from gestaoapp.models import Usuario

class FormUsuario(forms.ModelForm):
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
		usuario = super(FormUsuario, self).save(commit=False)
		usuario.set_password(self.cleaned_data['password'])
		if commit:
			usuario.save()
		return usuario

	class Meta:
		model = Usuario
		exclude = ('last_login',"groups","user_permissions","helptext","is_staff","date_joined",'is_active','dia') 