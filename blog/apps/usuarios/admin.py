from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import Usuario


# Agregar el modelo Usuario personalizado al panel de administración
class UsuarioAdmin(UserAdmin):
    model = Usuario
    list_display = ['username', 'email', 'first_name', 'last_name', 'is_staff', 'tipo_usuario']
    fieldsets = UserAdmin.fieldsets + (
        (None, {'fields': ('imagen', 'tipo_usuario')}),
    )


admin.site.register(Usuario, UsuarioAdmin)