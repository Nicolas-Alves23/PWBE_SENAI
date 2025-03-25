from django.shortcuts import render
from rest_framework.response import Response
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.filters import OrderingFilter
from rest_framework.decorators import api_view
from rest_framework import viewsets
from .models import Carros
from .serializers import CarSerializer
from rest_framework import status

# Um projeto rest_framework necessita referenciar o método HTTP (@api_view)
@api_view(['GET'])
def read_carros(request):
    info = Carros.objects.all()
    serializer = CarSerializer(info, many=True) #O serializer para transformar o JSON 
    return Response(serializer.data)


@api_view(['GET'])
def pegar_carro(request,pk):
    # utilizando try para possíveis erros do usuário
    try:
        carro = Carros.objects.get (pk=pk)
    # caso o 'Carro' não exista este erro irá aparecer   
    except Carros.DoesNotExist:
        return Response({'erro': 'Carro inexistente'}, status= status.HTTP_404_NOT_FOUND)
    
    serializer =  CarSerializer(carro)
    return Response(serializer.data)

# Para cria um novo carro o método HTTP é o POST
@api_view(['POST'])
def create_carro(resquest):
    if resquest.method == 'POST':
        serializer = CarSerializer(data=resquest.data, many=isinstance(resquest.data, list))
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)

# Para fazer uma mudança em um dado já existente no banco, o método utilizado é o PUT 
@api_view(['PUT'])
def update_carro(resquest, pk):
    try:
        carro = Carros.objects.get (pk=pk)
        # Caso o carro não exista 
    except Carros.DoesNotExist:
        return Response({'erro': 'Carro inexistente'}, status= status.HTTP_404_NOT_FOUND)
    
    serializer = CarSerializer(carro, data=resquest.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_200_OK)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


# Método DELETE para deletar um valor do banco de dados 
@api_view(['DELETE'])
def delete_carro(request, pk):
    # Se a pk exister ela será excluida
    try:
        carro = Carros.objects.get (pk=pk)
    except Carros.DoesNotExist():
        return Response({'erro': 'Carro inexistente'}, status= status.HTTP_404_NOT_FOUND)

    carro.delete()
    # Print para dizer que a exclusão ocorreu da maneira correta 
    return Response({'Mensagem':f'O seu {carro.nome} foi apagado'}, status=status.HTTP_200_OK)

