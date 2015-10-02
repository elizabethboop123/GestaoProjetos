from django.conf.urls import include, url
from django.contrib import admin
from django.conf.urls.static import static
from django.conf import settings
from django.contrib.auth.views import password_reset
from gestaoapp.views import *

urlpatterns = [
    url(r'^admin/', include(admin.site.urls)),
    url(r'^login/$', 'django.contrib.auth.views.login', {'template_name': 'login.html'}, name='login'),
    url(r'^logout/$', 'django.contrib.auth.views.logout', {'template_name': 'logout.html'}, name='logout'),
    
    url(r'^usuario/', CadastroUsuario.as_view()),
    url(r'^editar_usuario/(?P<usuario_id>\d+)/$', CadastroUsuario.as_view()),
    url(r'^verificar_usuario/(?P<usuario_verificacao>\w+)/$', VerificarUsuario.as_view()),
    url(r'^desbloquear_usuario/', AdministrarUsuario.as_view()),
    url(r'^liberar_usuario/(?P<usuario_verificacao>\w+)/$', LiberarUsuario.as_view()),
    url(r'^consulta_usuario/', ConsultaUsuario.as_view()),
    url(r'^visualizar_usuario/(?P<usuario_id>\d+)/$', VisualizarUsuario.as_view()),

    url(r'^perfil/', CadastroPerfil.as_view()),
    url(r'^editar_perfil/(?P<perfil_id>\d+)/$', CadastroPerfil.as_view()),

    url(r'^horario/', CadastroHorario.as_view()),    

    url(r'^sucesso/', sucesso),
    url(r'^editar_horario/(?P<horario_id>\d+)/$', CadastroHorario.as_view()),

    url(r'^cadastro_liberado/', cadastro_liberado),

    url(r'^troca_senha/$', 'django.contrib.auth.views.password_change',{'template_name': 'troca.html'}),
    url(r'^sucesso_senha/$', CadastroUsuario.as_view(), name='password_change_done'),

    url(r'^nucleo/', CadastroNucleo.as_view()),
    url(r'^editar_nucleo/', CadastroNucleo.as_view()),

    url(r'^recurso/', CadastroRecurso.as_view()),
    url(r'^editar_recurso/', CadastroRecurso.as_view()),
    url(r'^tipo_recurso/', CadastroTipoRecurso.as_view()),
    url(r'^editar_tipo_recurso/', CadastroTipoRecurso.as_view()),

    url(r'^artefato/', CadastroArtefato.as_view()),
    url(r'^editar_artefato/', CadastroArtefato.as_view()),
    
    url(r'^atividade/', CadastroAtividade.as_view()),
    url(r'^editar_atividade/', CadastroAtividade.as_view()),

    url(r'^edital/', CadastroEdital.as_view()),

    url(r'^projeto/', CadastroProjeto.as_view()),

]+ static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)