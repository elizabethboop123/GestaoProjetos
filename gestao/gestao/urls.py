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
    url(r'^liberar_usuario/(?P<usuario_verificacao>\w+)/$', LiberarUsuario.as_view()),

    url(r'^perfil/', CadastroPerfil.as_view()),
    url(r'^editarperfil/(?P<perfil_id>\d+)/$', CadastroPerfil.as_view()),

    url(r'^horario/', CadastroHorario.as_view()),

    url(r'^sucesso/', sucesso),
    url(r'^editarhorario/(?P<horario_id>\d+)/$', CadastroHorario.as_view()),

    url(r'^cadastro_liberado/', cadastro_liberado),

    url(r'^troca_senha/$', 'django.contrib.auth.views.password_change',{'template_name': 'usuario/troca.html'}),
    url(r'^sucesso_senha/$', CadastroUsuario.as_view(), name='password_change_done')

]+ static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)