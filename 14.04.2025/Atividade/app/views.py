from django.shortcuts import render
from rest_framework.decorators import api_view, permission_classes
from rest_framework.response import Response
from rest_framework import status
from .models import UsuarioDS16
from django.contrib.auth import authenticate
from rest_framework_simplejwt.tokens import RefreshToken
from rest_framework.permissions import IsAuthenticated

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
    
    if UsuarioDS16.objects.filter(idade=idade).exists():
        return Response ({'Erro':f'idade {idade} já existe'}, status=status.HTTP_400_BAD_REQUEST)
    
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
    return Response({'Mensagem':'Olá! DS16'}, status=status.HTTP_200_OK)