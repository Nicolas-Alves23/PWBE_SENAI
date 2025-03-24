from .models import Eventos
from rest_framework import serializers 

class EventSerializer(serializers.ModelSerializer):
    class Meta:
        model = Eventos
        fields = "__all__"