from django.contrib import admin
from .models import Usuario
from django.contrib.auth.admin import UserAdmin

class UsuarioAdmin(UserAdmin):
    list_display = ('ni', 'telefone', 'data_contratacao', 'data_nascimento','tipo')

    fieldsets = UserAdmin.fieldsets + (
        (None,{'fields': ('ni', 'telefone', 'data_contratacao', 'data_nascimento','tipo')}),
    )

    add_fieldsets = UserAdmin.add_fieldsets + (
        (None,{'fields': ('ni', 'telefone', 'data_contratacao', 'data_nascimento','tipo')}),
    )


admin.site.register(Usuario,UsuarioAdmin)
