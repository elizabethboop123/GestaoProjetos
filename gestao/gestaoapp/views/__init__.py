from django.shortcuts import render_to_response
from django.template import RequestContext
from gestaoapp.views.aluno import CadastroAluno
from gestaoapp.views.professor import CadastroProfessor
from gestaoapp.views.nucleo import CadastroNucleo
from gestaoapp.views.projeto import CadastroProjeto
from gestaoapp.views.edital import CadastroEdital
from gestaoapp.views.contratado import CadastroContratado