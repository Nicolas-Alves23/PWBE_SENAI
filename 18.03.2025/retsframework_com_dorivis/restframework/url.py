from django.urls import path, include
from . import views

# As urls do projeto

urlpatterns = [
    path('api/', views.read_carros ),
    path('api/buscar/<int:pk>', views.pegar_carro),
    path('carros/criar/', views.create_carro),
    path('carros/update/<int:pk>', views.update_carro),
    path('carros/delete/<int:pk>', views.delete_carro)
]
