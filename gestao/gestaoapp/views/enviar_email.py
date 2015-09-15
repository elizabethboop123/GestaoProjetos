from django.shortcuts import render, redirect
from django.views.generic.base import View
from gestaoapp.models.usuario import Usuario
from django.core.mail import send_mail

def get(self, request , usuario_id = None):
	
	nome = Usuario.objects.get(id =usuario_id)
	mail= nome.email

	print(mail)


send_mail('Subject here', 'Here is the message.', 'from@example.com',
    ['to@example.com'], fail_silently=False)