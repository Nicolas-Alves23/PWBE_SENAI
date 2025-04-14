from django.urls import path
from .import views

urlpatterns =[
    path('create/', view=views.create_user, name='create_usuario'),
    path('logar/', view=views.logar_usuario, name='logar_usuario'),
    path('output/', view=views.output_user, name='output_user')
    
]