from django.contrib import admin
from django.urls import path, include

from web_pac2 import settings
from webapp import views
from webapp.views import uploadFile, search_pers, rec_pass, bienvenidos, main, \
    uploadTickdirect, send_email, Tick_val

from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django_postalcodes_mexico import urls as django_postalcodes_mexico_urls

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', main, name='inicio'),
    path('bienvenida', bienvenidos, name='inicio'),
    path('val', search_pers, name='val_pers'),
    path('recuperar', rec_pass, name='recuperar_cont'),
    path('Menu', uploadFile, name='primer_acceso'),
    path('validate', uploadTickdirect, name='cam_dom'),
    path('Inicio', Tick_val, name='cam_dom'),
    path('api/', include(django_postalcodes_mexico_urls)),
]

urlpatterns += staticfiles_urlpatterns(settings.STATIC_URL)

