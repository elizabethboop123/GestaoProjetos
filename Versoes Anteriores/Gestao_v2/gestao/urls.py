from django.conf.urls import include, url
from django.contrib import admin
from django.conf.urls.static import static
from django.conf import settings
from gestaoapp.views import CadastroAluno, CadastroNucleo, CadastroProjeto, CadastroProfessor, CadastroEdital, CadastroContratado, CadastroGraduacao, CadastroCurso, CadastroNivel

urlpatterns = [
    url(r'^admin/', include(admin.site.urls)),
    url(r'^login/$', 'django.contrib.auth.views.login', {'template_name': 'login.html'}, name='login'),
    url(r'^logout/$', 'django.contrib.auth.views.logout', {'template_name': 'logout.html'}, name='logout'),
    
    url(r'^aluno/', CadastroAluno.as_view()),
    url(r'^editaraluno/(?P<aluno_id>\d+)/$', CadastroAluno.as_view()),

    url(r'^professor/', CadastroProfessor.as_view()),
    url(r'^editarprofessor/(?P<professor_id>\d+)/$', CadastroProfessor.as_view()),

    url(r'^nucleo/', CadastroNucleo.as_view()),
    url(r'^editarnucleo/(?P<nucleo_id>\d+)/$', CadastroNucleo.as_view()),

    url(r'^projeto/', CadastroProjeto.as_view()),
    url(r'^editarprojeto/(?P<projeto_id>\d+)/$', CadastroProjeto.as_view()),

    url(r'^edital/', CadastroEdital.as_view()),
    url(r'^editaredital/(?P<edital_id>\d+)/$', CadastroEdital.as_view()),

    url(r'^contratado/', CadastroContratado.as_view()),
    url(r'^editarcontratado/(?P<contratado_id>\d+)/$', CadastroContratado.as_view()),

    url(r'^graduacao/', CadastroGraduacao.as_view()),
    url(r'^editargraduacao/(?P<graduacao_id>\d+)/$', CadastroGraduacao.as_view()),

    url(r'^curso/', CadastroCurso.as_view()),
    url(r'^editarcurso/(?P<curso_id>\d+)/$', CadastroCurso.as_view()),

    url(r'^nivel/', CadastroNivel.as_view()),
    url(r'^editarnivel/(?P<nivel_id>\d+)/$', CadastroNivel.as_view()),

]+ static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
