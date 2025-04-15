from django.urls import path
from .views import *

urlpatterns = [
    path('piloto/', view=PilotoListCreateAPIView.as_view()),
    path('carro/', view=CarroListCreateAPIView.as_view()),
    path('piloto/tudo/<int:pk>', view=PilotoRetrieveUpdateDestroyAPIView.as_view()),

]
