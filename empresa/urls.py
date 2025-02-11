from django.urls import path

from . import views
from avaliacao.views import avaliacao, relatorio

urlpatterns = [
    path('', views.empresa, name='empresa'),
    path('empresa_list', views.EmpresaList.as_view(), name='empresa_list'),
    path('atualizar/<int:id>/', views.empresa_update, name='empresa_update'),
    path('excluir/<int:id>/', views.empresa_delete, name='empresa_delete'),
    path('avaliar/<int:id>/', avaliacao, name='avaliacao'),
    path('relatorio/<int:id>/', relatorio, name='relatorio'),
]