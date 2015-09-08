from django import forms
from gestaoapp.models import Aluno

class FormAluno(forms.ModelForm):
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
		aluno = super(FormAluno, self).save(commit=False)
		aluno.set_password(self.cleaned_data['password'])
		if commit:
			aluno.save()
		return aluno

	class Meta:
		model = Aluno
		exclude = ('last_login',"last_name","groups","user_permissions","helptext","is_staff","date_joined","tipo",'is_active') 