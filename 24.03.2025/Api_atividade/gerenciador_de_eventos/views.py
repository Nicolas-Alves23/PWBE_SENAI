from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.decorators import api_view
from .models import Eventos
from .serializers import EventSerializer
from rest_framework import status
from datetime import datetime, timedelta


# Método VISUALIZAR

@api_view(['GET']) # Método Get que é usado nessa função abaixo
def read_eventos(request):
    info = Eventos.objects.all()
    
    # utilizando o query_params para fazer o filtro 
    categoria = request.query_params.get('categoria')
    # caso na url exista o termo 'categoria' esse if será ativo 
    if categoria:
        # dentro de todo o banco de dados ('info') filtra essa categoria
        info = info.filter(categoria__icontains = categoria)

    # Funcionando da mesma forma do item 'categoria'
    data = request.query_params.get('data')
    if data:
        info = info.filter(data__icontains = data)

    # A principal diferença desse bloco de código é que a quantidade é um int e não um filter exatamente
    quantidade = request.query_params.get('quantidade')
    if quantidade:
        info = info[:int(quantidade)]# passamos no link a quantida que queremos e fazemos o return dessa informação

    ordenacao = request.query_params.get('ordenacao')
    if ordenacao:
        info = info.order_by('data').values()# Order_by é utilizado para ordenar, no caso ordenaremos por data 

    #-------------------------------------------------

    # Para verificarmos os proximos 7 dias 
    proximo = request.query_params.get('proximos')

    if proximo:
        data_atual = datetime.now()# Nossa data atual
        data_futura = data_atual + timedelta(days=7)# Referente aos próximos 7 dias
        info = info.filter(data__gte = data_atual, data__lte=data_futura) #filtrando os próximos 7 dias


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

