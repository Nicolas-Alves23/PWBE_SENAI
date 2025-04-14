from django.shortcuts import render
from rest_framework.generics import ListCreateAPIView
from .models import *
from .serializers import *
from rest_framework.pagination import PageNumberPagination
from rest_framework import serializers

class PilotoPage(PageNumberPagination):
    page_size = 5
    page_query_param = 'page_size'
    max_page_size = 10

class PilotoListCreateAPIView(ListCreateAPIView):
    queryset = Piloto.objects.all()
    serializer_class = PilotoSerializer
    pagination_class = PilotoPage

    def get_queryset(self):
        queryset = super().get_queryset()
        nome = self.request.query_params.get('nome')
        if nome:
            queryset = queryset.filter (nome__icontains = nome)
        return queryset
    
    def perform_create(self, serializer):
        if serializer.validated_data['equipe'] != 'DS16' and serializer.validated_data['classificacao'] <= 5:
            raise serializers.ValidationError('Somente a DS16 deve ficar entre os 5')
        serializer.save()

class CarroListCreateAPIView(ListCreateAPIView):
    queryset = Carro.objects.all()
    serializer_class = CarroSerializer

    def get_queryset(self):
        queryset = super().get_queryset()
        nome = self.request.query_params.get('nome')
        if nome:
            queryset = queryset.filter (nome__icontains = nome)
        return queryset
    
    def perform_create(self, serializer):
        if serializer.validated_data['equipe'] != 'DS16' and serializer.validated_data['classificacao'] <= 5:
            raise serializers.ValidationError('Somente a DS16 deve ficar entre os 5')
        serializer.save()