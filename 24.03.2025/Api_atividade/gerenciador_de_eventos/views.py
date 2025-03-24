from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.decorators import api_view
from .models import Eventos
from .serializers import EventSerializer
from rest_framework import status



# Método VISUALIZAR

@api_view(['GET']) # Método Get que é usado nessa função abaixo
def read_eventos(request):
    info = Eventos.objects.all()

    bomba = request.query_params.get('categoria')
    if bomba:
        info = Eventos.filter(categoria__icontains = bomba)

    serializer = EventSerializer(info, many=True)
    return Response(serializer.data)



# Método BUSCAR POR PRIMARY KEY

@api_view(['GET']) # Método Get que é usado nessa função pois eu faço um requisição
def pegar_evento(request,pk):
    try:
        evento = Eventos.objects.get (pk=pk)
    except Eventos.DoesNotExist:
        return Response({'erro': 'Evento inexistente'}, status= status.HTTP_404_NOT_FOUND)
    
    serializer =  EventSerializer(evento)
    return Response(serializer.data)



# Método CRIAR

@api_view(['POST']) # Iremos colocar informações no banco de dados então o Método POST é utilizado
def create_evento(resquest):
    if resquest.method == 'POST':
        serializer = EventSerializer(data=resquest.data, many=isinstance(resquest.data, list))
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)



# Método UPDATE

@api_view(['PUT']) 
def update_evento(resquest, pk): # O pk é utilizado para pegar a primary key

    try:
        evento = Eventos.objects.get (pk=pk)
    except Eventos.DoesNotExist:
        return Response({'erro': 'evento inexistente'}, status= status.HTTP_404_NOT_FOUND)
    
    serializer = EventSerializer(evento, data=resquest.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_200_OK)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)



# Método DELETAR informações 

@api_view(['DELETE'])
def delete_evento(request, pk):
    # Pegamos a pk e apagamos ela em sequencia
    try:
        evento = Eventos.objects.get (pk=pk)
    except Eventos.DoesNotExist():
        return Response({'erro': 'evento inexistente'}, status= status.HTTP_404_NOT_FOUND)

    evento.delete()
    return Response({'Mensagem':f'O seu {evento.nome} foi apagado'}, status=status.HTTP_200_OK)

# Método FILTRAR 

