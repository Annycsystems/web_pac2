from django.contrib import admin
from django.urls import path, include

from web_pac2 import settings
from webapp import views
from webapp.views import bienvenido, uploadFile, search_pers, rec_pass, new_pers, bienvenidos, main, \
    uploadTickdirect, main_menu, send_email, Tick_val

from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django_postalcodes_mexico import urls as django_postalcodes_mexico_urls

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', main, name='inicio'),
    path('bienvenida', bienvenidos, name='inicio'),
    path('val', search_pers, name='val_pers'),
    path('Sign_in', new_pers, name='Sign_in'),
    path('recuperar', rec_pass, name='recuperar_cont'),
    path('Menu', uploadFile, name='primer_acceso'),
    path('main', main_menu, name='menu_ini'),
    path('validate', uploadTickdirect, name='cam_dom'),
    path('Inicio', Tick_val, name='cam_dom'),
    path('api/', include(django_postalcodes_mexico_urls)),
]

urlpatterns += staticfiles_urlpatterns(settings.STATIC_URL)

