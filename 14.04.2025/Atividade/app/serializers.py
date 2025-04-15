from rest_framework import serializers
from .models import UsuarioDS16

class UsuarioSerializar(serializers.ModelSerializer):
    class Meta:
        model = UsuarioDS16
        fields = "__all__"