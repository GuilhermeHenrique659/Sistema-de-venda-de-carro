from django.conf.urls import url
from .views import *

urlpatterns = [
    url(r'^veiculo/listar/(?P<categoria>[\w\-]+)/$', listar_veiculo, name='listar_veiculo'),
    url(r'^veiculo/perfil/(?P<pk>[0-9]+)', perfil_veiculo, name='perfil_veiculo'),
]