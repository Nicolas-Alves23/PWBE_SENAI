from django.urls import path, include
from . import views


urlpatterns = [
    path('api/', views.read_eventos ), #Para vizualizarmos /  ou filtramos 
    path('api/buscar/<int:pk>', views.pegar_evento), # Buscar com id 
    path('eventos/criar/', views.create_evento), # Criar um evento
    path('eventos/update/<int:pk>', views.update_evento), # Modificar um evento existente
    path('eventos/delete/<int:pk>', views.delete_evento) # Deletar um item 
]