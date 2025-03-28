from __future__ import unicode_literals
from django.urls import path
from django.contrib.auth import views as auth_views
from . import views

urlpatterns = [
     path("cadastros", views.UserAdminRegisterView.as_view(),name="cadastros"),
     path("", views.UserRegisterView.as_view(),name="cadastro"),
     path("home/", views.UserListView.as_view(),name="home"),
     path('logout/', views.logout_view, name='logout'),
     path('atualizar/<int:id>/', views.usuario_update, name='usuario_update'),
     path('excluir/<int:id>/', views.usuario_delete, name='usuario_delete'),
     path('reset_password/', auth_views.PasswordResetView.as_view(), name='password_reset'),
     path('reset_password_sent/', 
          auth_views.PasswordResetDoneView.as_view(), 
          name='password_reset_done'), 
     path('reset/<uidb64>/<token>/', 
         auth_views.PasswordResetConfirmView.as_view(), 
         name='password_reset_confirm'),
     path('reset_password_complete/', 
         auth_views.PasswordResetCompleteView.as_view(), 
         name='password_reset_complete'),
]