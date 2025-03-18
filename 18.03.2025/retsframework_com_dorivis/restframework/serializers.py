from .models import Carros
from rest_framework import serializers 

class CarSerializer(serializers.ModelSerializer):
    class Meta:
        model = Carros
        fields = "__all__"