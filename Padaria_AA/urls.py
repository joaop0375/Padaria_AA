from django.urls import path, include
from app_padaria_aa import views
from django.views.generic import TemplateView
from django.conf.urls.static import static
from django.conf import settings


urlpatterns = [
    
    path('', TemplateView.as_view(template_name='index.html'), name='home'),
    
    path('cadastrar_cliente/', views.cadastrar_cliente, name='cadastrar_cliente'),
    path('lista_clientes/', views.lista_clientes, name='lista_clientes'),

    # Administração de Estoque
    path('listar_estoque/', views.listar_estoque, name='listar_estoque'),

    # Cadastro de Reclamações
    path('cadastrar_reclamacao/', views.cadastrar_reclamacao, name='cadastrar_reclamacao'),
    path('lista_reclamacoes/', views.lista_reclamacoes, name='lista_reclamacoes'),

    # Agenda de Encomendas
    path('agendar_encomenda/', views.agendar_encomenda, name='agendar_encomenda'),
    path('lista_encomendas/', views.lista_encomendas, name='lista_encomendas'),

    # Cadastro de Pedidos
    path('cadastrar_pedido/', views.cadastrar_pedido, name='cadastrar_pedido'),
    path('lista_pedidos/', views.lista_pedidos, name='lista_pedidos'),

]

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)