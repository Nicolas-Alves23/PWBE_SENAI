from django.urls import path, include
from . import views


urlpatterns = [
    path('api/', views.read_eventos ),
    path('api/buscar/<int:pk>', views.pegar_evento),
    path('eventos/criar/', views.create_evento),
    path('eventos/update/<int:pk>', views.update_evento),
    path('eventos/delete/<int:pk>', views.delete_evento)
]