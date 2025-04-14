from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import UsuarioDS16


class UsuarioDS16Admin(UserAdmin):
    list_display = ('username','email', 'data_nascimento', 'idade', 'pets', 'esolaridade')

    fieldsets = UserAdmin.fieldsets + (
        (None,{'fields': ('data_nascimento', 'idade', 'pets', 'esolaridade')}),
    )

    add_fieldsets = UserAdmin.add_fieldsets + (
        (None,{'fields': ('data_nascimento', 'idade', 'pets', 'esolaridade')}),
    )

admin.site.register(UsuarioDS16,UsuarioDS16Admin)