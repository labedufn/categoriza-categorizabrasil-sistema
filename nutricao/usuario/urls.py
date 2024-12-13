from __future__ import unicode_literals
from django.urls import path
from . import views

urlpatterns = [
   path("cadastros", views.UserAdminRegisterView.as_view(),name="cadastros"),
   path("", views.UserRegisterView.as_view(),name="cadastro"),
   path("home/", views.UserListView.as_view(),name="home"),
   path('logout/', views.logout_view, name='logout'),
   path('atualizar/<int:id>/', views.usuario_update, name='usuario_update'),
   path('excluir/<int:id>/', views.usuario_delete, name='usuario_delete'),
]