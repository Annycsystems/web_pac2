from django.contrib import admin

from datos.models import Consultora, Primer_Registro, Usr_Sol_Dom, Usr_Sol_Domfis, Usr_Sol_Rfc, Track_Sol

# Register your models here.
admin.site.register(Consultora)
admin.site.register(Primer_Registro)
admin.site.register(Usr_Sol_Dom)
admin.site.register(Usr_Sol_Domfis)
admin.site.register(Usr_Sol_Rfc)
admin.site.register(Track_Sol)
