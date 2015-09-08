from django.conf.urls import include, url
from django.contrib import admin
from django.conf.urls.static import static
from django.conf import settings
from gestaoapp.views import CadastroUsuario,CadastroPerfil

urlpatterns = [
    url(r'^admin/', include(admin.site.urls)),
    url(r'^login/$', 'django.contrib.auth.views.login', {'template_name': 'login.html'}, name='login'),
    url(r'^logout/$', 'django.contrib.auth.views.logout', {'template_name': 'logout.html'}, name='logout'),
    
    url(r'^usuario/', CadastroUsuario.as_view()),
    url(r'^editarusuario/(?P<usuario_id>\d+)/$', CadastroUsuario.as_view()),

    url(r'^perfil/', CadastroPerfil.as_view()),
    url(r'^editarperfil/(?P<perfil_id>\d+)/$', CadastroPerfil.as_view()),

]+ static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
