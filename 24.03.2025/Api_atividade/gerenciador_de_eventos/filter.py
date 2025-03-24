import django_filters
from .models import Eventos

class EventFilter(django_filters.FilterSet):
    # Usando 'lookup_expr' em vez de 'Lookup_expr'
    categoria= django_filters.CharFilter(field_name='numero_card', lookup_expr='exact')
    data = django_filters.CharFilter(field_name='categoria', lookup_expr='exact')
    quantidade = django_filters.CharFilter(field_name='setor', lookup_expr='exact')

    class Meta:
        model = Eventos
        fields = ['categoria', 'data', 'quantidade']