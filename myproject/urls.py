from django.urls import path
from app import views

urlpatterns = [
    path('', views.listar_usuarios, name='listar_usuarios'),
    path('grupos/', views.listar_grupos, name='listar_grupos'),
    path('grupos/cadastrar/', views.cadastrar_grupo, name='cadastrar_grupo'),
    path('grupos/editar/<int:grupo_id>/', views.editar_grupo, name='editar_grupo'),
    path('grupos/excluir/<int:grupo_id>/', views.excluir_grupo, name='excluir_grupo'),
    path('usuarios/', views.listar_usuarios, name='listar_usuarios'),
    path('usuarios/cadastrar/', views.cadastrar_usuario, name='cadastrar_usuario'),
    path('usuarios/editar/<int:usuario_id>/', views.editar_usuario, name='editar_usuario'),
    path('usuarios/excluir/<int:usuario_id>/', views.excluir_usuario, name='excluir_usuario'),
]