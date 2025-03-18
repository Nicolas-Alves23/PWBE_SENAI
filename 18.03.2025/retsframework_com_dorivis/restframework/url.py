# from django.contrib import admin
from django.urls import path, include
# from rest_framework.routers import DefaultRouter
from . import views

# router = DefaultRouter()
# router.register(r'carros', read_carros)

urlpatterns = [
    path('api/', views.read_carros ),
    path('api/buscar/<int:pk>', views.pegar_carro),
    path('carros/criar/', views.create_carro),
    path('carros/update/<int:pk>', views.update_carro),
    path('carros/delete/<int:pk>', views.delete_carro)
]
# /*[
#     {
#         "nome": "Adrian",
        
#         "marca": "Chevrolett",
        
#         "qtdRodas": 4,

#         "ano": 2005,

#         "cor": "Roxo",
        
#         "combustivel": "GASOLINA"
#     },
#     {
#         "nome": "Nicolas",
        
#         "marca": "Chevrolett",
        
#         "qtdRodas": 4,

#         "ano": 2006,

#         "cor": "Roxo",
        
#         "combustivel": "GASOLINA"
#     }
# ]*/