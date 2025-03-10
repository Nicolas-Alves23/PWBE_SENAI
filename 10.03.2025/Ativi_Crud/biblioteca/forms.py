from django import forms
from .models import Biblioteca

class Bibliotecaforms(forms.ModelForm):
    class Meta:
        model = Biblioteca
        fields = ['titulo','autor','ano_pubi','descricao']