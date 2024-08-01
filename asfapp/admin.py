from django.contrib import admin
from .models import Curso, Aula, Usuario
from django.contrib.auth.admin import UserAdmin

# Register your models here.

campos_usu = list(UserAdmin.fieldsets)
campos_usu.append(
    ("Histórico", {'fields': ('aulas_assistidas',)})
)
UserAdmin.fieldsets = tuple(campos_usu)

admin.site.register(Curso)
admin.site.register(Aula)
admin.site.register(Usuario, UserAdmin)


