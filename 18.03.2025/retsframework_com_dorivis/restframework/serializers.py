from .models import Carros
from rest_framework import serializers 

class CarSerializer(serializers.ModelSerializer):
    class Meta:
        # pegando dos itens do models e transformando em json 
        model = Carros
        fields = "__all__"