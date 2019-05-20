from django.urls import path,re_path
from . import views
from django.urls import reverse
app_name = 'fornecedor'

urlpatterns = [
    
    path(r'', views.IndexView.as_view(), name='index'),
    path(r'add/', views.FornecedorCreate.as_view(), name='fornecedor-add'),
    re_path(r'^(?P<pk>[0-9]+)/update/$', views.FornecedorUpdate.as_view(), name='fornecedor-update'),
    re_path(r'^(?P<pk>[0-9]+)/delete/$', views.FornecedorDelete.as_view(), name='fornecedor-delete'),   
    re_path(r'^(?P<pk>[0-9]+)/$', views.DetailView.as_view(), name='detail'),
     
]