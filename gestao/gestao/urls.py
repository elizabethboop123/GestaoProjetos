from django.conf.urls import include, url
from django.contrib import admin
from django.conf.urls.static import static
from django.conf import settings
from gestaoapp.views import CadastroAluno, CadastroNucleo, CadastroProjeto, CadastroProfessor

urlpatterns = [
    url(r'^admin/', include(admin.site.urls)),

    url(r'^aluno/', CadastroAluno.as_view()),
    url(r'^editaraluno/(?P<aluno_id>\d+)/$', CadastroAluno.as_view()),

    url(r'^professor/', CadastroProfessor.as_view()),
    url(r'^editarprofessor/(?P<professor_id>\d+)/$', CadastroProfessor.as_view()),

    url(r'^nucleo/', CadastroNucleo.as_view()),
    url(r'^editarnucleo/(?P<nucleo_id>\d+)/$', CadastroNucleo.as_view()),

    url(r'^projeto/', CadastroProjeto.as_view()),
    url(r'^editarprojeto/(?P<projeto_id>\d+)/$', CadastroProjeto.as_view()),

]+ static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
