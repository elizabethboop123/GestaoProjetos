from django import forms
from gestaoapp.models import Usuario
from django.contrib.auth.models import User
from random import *
import string

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

	def clean_password(self):

		if 'password' in self.cleaned_data:

			password = self.cleaned_data['password']

			if len(password) < 8:
				raise forms.ValidationError("A senha deve ter no minino 8 caracteres")

			else:
				first_isalpha = password[0].isalpha()
				if all(c.isalpha() == first_isalpha for c in password):
					raise forms.ValidationError("A senha deve ter numeros e letras")
				else:
					return password

	def clean_email(self):
		email = self.cleaned_data.get('email')
		username = self.cleaned_data.get('username')
		if email and User.objects.filter(email=email).exclude(username=username).count():
			raise forms.ValidationError(u'Email ja cadastrado')
		return email

	def save(self, commit=True):
		print('oi')
		self.clean_confirma_senha()
		usuario = super(FormUsuario, self).save(commit=False)
		usuario.set_password(self.cleaned_data['password'])

		letras = list(string.ascii_lowercase)
		ver = []
		for i in range(10):
			ver.append(random.choice(letras))

		''.join(ver)
		print (''.join(ver))
		usuario.verificacao = (''.join(ver))
		
		if commit:
			usuario.is_active = False
			usuario.save()

		return usuario

	class Meta:
		model = Usuario
		exclude = ('last_login',"groups","user_permissions","helptext","is_staff","date_joined",'is_active','dia','mail','verificacao') 