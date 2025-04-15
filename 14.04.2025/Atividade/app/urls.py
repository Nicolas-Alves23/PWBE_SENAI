from django.urls import path
from .import views

urlpatterns =[
    path('create/', view=views.create_user, name='create_usuario'),
    path('logar/', view=views.logar_usuario, name='logar_usuario'),
    path('read/', view=views.output_user, name='output_user'),
    path('update/<int:pk>', view = views.update_usuario , name='update_usuario'),
    path('delete/<int:pk>', view = views.delete_usuario , name='delete_usuario'),
]
