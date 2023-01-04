from django.contrib import admin

from datos.models import tipo_solicitud, tema_solicitud, Subtema_solicitud, Roles_usr, Atributos, pers_gen, users_sys

# Register your models here.
admin.site.register(tipo_solicitud)
admin.site.register(tema_solicitud)
admin.site.register(Subtema_solicitud)
admin.site.register(Roles_usr)
admin.site.register(Atributos)
admin.site.register(pers_gen)
admin.site.register(users_sys)
