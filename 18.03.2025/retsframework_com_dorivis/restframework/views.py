from django.shortcuts import render
from rest_framework.response import Response
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.filters import OrderingFilter
from rest_framework.decorators import api_view
from rest_framework import viewsets
from .models import Carros
from .serializers import CarSerializer
from rest_framework import status

@api_view(['GET'])
def read_carros(request):
    info = Carros.objects.all()
    serializer = CarSerializer(info, many=True)
    return Response(serializer.data)

@api_view(['GET'])
def pegar_carro(request,pk):
    try:
        carro = Carros.objects.get (pk=pk)
    except Carros.DoesNotExist:
        return Response({'erro': 'Carro inexistente'}, status= status.HTTP_404_NOT_FOUND)
    
    serializer =  CarSerializer(carro)
    return Response(serializer.data)

@api_view(['POST'])
def create_carro(resquest):
    if resquest.method == 'POST':
        serializer = CarSerializer(data=resquest.data, many=isinstance(resquest.data, list))
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)

@api_view(['PUT'])
def update_carro(resquest, pk):
    try:
        carro = Carros.objects.get (pk=pk)
    except Carros.DoesNotExist:
        return Response({'erro': 'Carro inexistente'}, status= status.HTTP_404_NOT_FOUND)
    
    serializer = CarSerializer(carro, data=resquest.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_200_OK)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['DELETE'])
def delete_carro(request, pk):
    try:
        carro = Carros.objects.get (pk=pk)
    except Carros.DoesNotExist():
        return Response({'erro': 'Carro inexistente'}, status= status.HTTP_404_NOT_FOUND)

    carro.delete()
    return Response({'Mensagem':f'O seu {carro.nome} foi apagado'}, status=status.HTTP_200_OK)

# class Carrosview(viewsets.ModelViewSet):
#     queryset = Carros.objects.all()

#     serializer_class = CarSerializer()
#     OrderingFilter = '__all__'