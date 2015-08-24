from django.conf.urls import include, url
from django.contrib import admin
from django.conf.urls.static import static
from django.conf import settings
from gestaoapp.views import CadastroBolsista, CadastroNucleo, CadastroProjeto, CadastroCoordenador

urlpatterns = [
    url(r'^admin/', include(admin.site.urls)),

    url(r'^bolsista/', CadastroBolsista.as_view()),
    url(r'^editarbolsista/(?P<bolsista_id>\d+)/$', CadastroBolsista.as_view()),

    url(r'^coordenador/', CadastroCoordenador.as_view()),
    url(r'^editarcoordenador/(?P<coordenador_id>\d+)/$', CadastroCoordenador.as_view()),

    url(r'^nucleo/', CadastroNucleo.as_view()),
    url(r'^editarnucleo/(?P<nucleo_id>\d+)/$', CadastroNucleo.as_view()),

    url(r'^projeto/', CadastroProjeto.as_view()),
    url(r'^editarprojeto/(?P<projeto_id>\d+)/$', CadastroProjeto.as_view()),

]+ static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
