from django.shortcuts import render
from rest_framework.decorators import api_view, permission_classes
from rest_framework.response import Response
from .models import UsuarioDS16
from rest_framework_simplejwt.tokens import RefreshToken
from rest_framework import status
