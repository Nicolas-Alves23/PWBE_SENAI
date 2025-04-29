from rest_framework import serializers
from .models import Usuario, Empresa
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer

class UsuarioSerializer(serializers.ModelSerializer):
    class Meta:
        model = Usuario
        fields = '__all__'

class EmpresaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Empresa
        fields = '__all__'

class LoginSerializer(TokenObtainPairSerializer):
    def validate(self, attrs):
        # super herda do TokenObtainPairSerializer
        data = super().validate(attrs)
        data ['usuario'] = {
            'id': self.user.id,
            'username': self.user.username,
        }
        return data
