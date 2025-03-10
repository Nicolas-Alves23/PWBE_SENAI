from django.urls import path
from . import views 

urlpatterns = [
    path('', views.listar_livros, name='listar_livros'),
    path('cadastrar/', views.cadastrar_livro, name='cadastrar_livro'),
    path('atualizar/<int:pk>', views.atualizar_livros, name='atualizar_livros'),
    path('excluir/<int:pk>', views.excluir_livro, name='excluir_livro'),
]