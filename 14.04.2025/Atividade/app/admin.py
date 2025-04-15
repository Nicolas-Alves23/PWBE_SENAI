from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import UsuarioDS16


class UsuarioDS16Admin(UserAdmin):
    list_display = ('username','email', 'data_nascimento', 'idade', 'pets', 'escolaridade')

    fieldsets = UserAdmin.fieldsets + (
        (None,{'fields': ('telefone','endereco','biografia','data_nascimento', 'idade', 'pets', 'escolaridade')}),
    )

    add_fieldsets = UserAdmin.add_fieldsets + (
        (None,{'fields': ('telefone','endereco','biografia','data_nascimento', 'idade', 'pets', 'escolaridade')}),
    )

admin.site.register(UsuarioDS16,UsuarioDS16Admin)