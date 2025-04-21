from django.shortcuts import render
from rest_framework.decorators import api_view, permission_classes
from rest_framework.response import Response
from rest_framework import status
from .models import UsuarioDS16
from django.contrib.auth import authenticate
from rest_framework_simplejwt.tokens import RefreshToken
from rest_framework.permissions import IsAuthenticated
from .serializers import UsuarioSerializar

@api_view(['POST'])
def create_user(request):
    username = request.data.get('username')
    password = request.data.get('password')
    idade = request.data.get('idade')
    data_nascimento = request.data.get('data_nascimento')
    telefone = request.data.get('telefone')
    endereco = request.data.get('endereco')

    if not username or not password or not idade or not data_nascimento:
        return Response({'Erro':'Campos obrigatorios incompletos'}, status=status.HTTP_400_BAD_REQUEST)
    
    if UsuarioDS16.objects.filter(username=username).exists():
        return Response ({'Erro':f'Username {username} já existe'}, status=status.HTTP_400_BAD_REQUEST)
    

    usuario = UsuarioDS16.objects.create_user(
            username=username,
            password=password,
            idade=idade,
            data_nascimento = data_nascimento,
            telefone = telefone,
            endereco = endereco,
            email= "Nicolas.Vilela@bosch.com"
    )
    return Response({'Mensagem': f'Usuário {username} criado com sucesso'}, status=status.HTTP_201_CREATED)


@api_view(['POST'])
def logar_usuario(request):
    username = request.data.get('username')
    password = request.data.get('password')

    usuario  =  authenticate(username = username , password = password)

    if usuario:
        refresh = RefreshToken.for_user(usuario)
        return Response({
            'acesso': str(refresh.access_token),
            'refresh': str(refresh)
        }, status=status.HTTP_200_OK)
    else:
        return Response ({'Erro':'Usuario ou/e senha incorreto(s)'}, status=status.HTTP_401_UNAUTHORIZED)

@api_view(['GET'])
@permission_classes([IsAuthenticated])
def output_user(request):
    usuario = UsuarioDS16.objects.all()
    serializer = UsuarioSerializar(usuario, many = True)
    return Response(serializer.data, status=status.HTTP_200_OK)


@api_view(['PUT']) 
@permission_classes([IsAuthenticated])
def update_usuario(resquest, pk): # O pk é utilizado para pegar a primary key
    try:
        usuario = UsuarioDS16.objects.get (pk=pk)
    except UsuarioDS16.DoesNotExist:
        return Response({'erro': 'usuario inexistente'}, status= status.HTTP_404_NOT_FOUND)
    
    serializer = UsuarioSerializar(usuario, data=resquest.data, partial=True)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_200_OK)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['DELETE'])
@permission_classes([IsAuthenticated])
def delete_usuario(request, pk):
    # Pegamos a pk e apagamos ela em sequencia
    try:
        usuario = UsuarioDS16.objects.get(pk=pk)
    except UsuarioDS16.DoesNotExist():
        return Response({'erro': 'usuario inexistente'}, status= status.HTTP_404_NOT_FOUND)


    usuario.delete()
    return Response({'Mensagem':'foi apagado'}, status=status.HTTP_200_OK)
