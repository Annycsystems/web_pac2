from django.db import models
from model_utils import Choices


class Gerencia(models.Model):
    nombre = models.CharField(max_length=200)

    class Meta:
        verbose_name = 'Gerencia'
        verbose_name_plural = 'Gerencias'

    def __str__(self):
        return self.nombre


class Red(models.Model):
    nombre = models.CharField(max_length=200, unique=True)
    gerencia = models.ForeignKey('cambiodatos.Gerencia', on_delete=models.PROTECT, related_name='redes')

    class Meta:
        verbose_name = 'Red'
        verbose_name_plural = 'Redes'

    def __str__(self):
        return self.nombre


class Consultora(models.Model):
     MOMENTO_CARRERA = Choices(
         ('cn', 'CN'),
         ('fn1', 'FN1'),
         ('fn2', 'FN2'),
         ('tn1', 'TN1'),
     )
     ESTATUS_CN = Choices(
         ('activa', 'Ativo'),
         ('cadastrada', 'Cadastrada'),
         ('intencion_cadastro', 'IntencaoCadastro'),
         ('inactiva1', 'Inativo1'),
         ('inactiva2', 'Inativo2'),
         ('inactiva3', 'Inativo3'),
         ('inactiva4', 'Inativo4'),
         ('cesada1', 'Cessado1'),
         ('cesada2', 'Cessado2'),
         ('cesada3', 'Cessado3')
     )
     TIPO_APROBACION = Choices(
         ('manual', 'Manual'),
         ('pendiente', 'Pendiente'),
         ('automatica', 'Automatica'),
     )
     TIPO_IDE = Choices(
         ('ine', 'IFE'),
         ('pasaporte', 'Pasaporte/FM'),
     )
     cn = models.BigIntegerField(primary_key=True, unique=True)
     nombre = models.CharField(max_length=200)
     tipo_ide = models.CharField(blank=False, null=True, max_length=20,
                                 choices=TIPO_IDE, default=TIPO_IDE.ine)
     identificacion = models.CharField(max_length=30, null=True, blank=True)
     entidad_federativa = models.CharField(max_length=200, null=True, blank=True)
     fecha_ingreso_prepago = models.DateTimeField(null=True, blank=True)
     fecha_ingreso = models.DateTimeField(null=True, blank=True)
     hora_ingreso = models.CharField(max_length=10, null=True, blank=True)
     num_telefonico = models.CharField(max_length=20, null=True, blank=True)
     num_telefonico_normalizado = models.CharField(max_length=20, null=True, blank=True)
     num_celular = models.CharField(max_length=20, null=True, blank=True)
     num_celular_normalizado = models.CharField(max_length=20, null=True, blank=True)
     email = models.CharField(max_length=100, null=True, blank=True)
     email_normalizado = models.CharField(max_length=100, null=True, blank=True)
     calle_residencial = models.CharField(max_length=200, null=True, blank=True)
     calle_residencial_referencias = models.CharField(max_length=400, null=True, blank=True)
     codigo_postal_residencial = models.CharField(max_length=10, null=True, blank=True)
     calle_comercial = models.CharField(max_length=200, null=True, blank=True)
     calle_comercial_referencias = models.CharField(max_length=400, null=True, blank=True)
     codigo_postal_comercial = models.CharField(max_length=10, null=True, blank=True)
     calle_entrega = models.CharField(max_length=200, null=True, blank=True)
     calle_entrega_referencias = models.CharField(max_length=400, null=True, blank=True)
     codigo_postal_entrega = models.CharField(max_length=10, null=True, blank=True)
     momento_carrera = models.CharField(null=True, max_length=10,
                                        choices=MOMENTO_CARRERA, default=MOMENTO_CARRERA.cn)
     estatus_cn = models.CharField(null=True, max_length=20,
                                   choices=ESTATUS_CN, default=ESTATUS_CN.activa)
     fecha_estatus_cn = models.DateTimeField(null=True, blank=True)
     cn_indicante = models.ForeignKey('cambiodatos.Consultora', null=True, db_constraint=False,
                                      blank=True, on_delete=models.PROTECT, related_name="invitadas")
     cn_lider = models.ForeignKey('cambiodatos.Consultora', null=True, db_constraint=False,
                                  blank=True, on_delete=models.PROTECT, related_name="gestionadas")
     fecha_asignacion_lider = models.DateTimeField(null=True, blank=True)
     fecha_aprobacion_lider = models.DateTimeField(null=True, blank=True)
     tipo_aprobacion = models.CharField(blank=False, null=True, max_length=20,
                                        choices=TIPO_APROBACION, default=TIPO_APROBACION.pendiente)
     red = models.ForeignKey('cambiodatos.Red', null=True, db_constraint=False,
                             on_delete=models.PROTECT, related_name="consultoras")
     creado = models.DateTimeField(auto_now_add=True, db_index=True)
     actualizado = models.DateTimeField(auto_now=True, db_index=True)
     first_acces = models.CharField(max_length=255, null=True)

class Primer_Registro(models.Model):
    codigocn_pers = models.CharField(max_length=255)
    nombre_pers = models.CharField(max_length=255)
    apellidop_pers = models.CharField(max_length=255)
    apellidom_pers = models.CharField(max_length=255)
    curp_pers = models.CharField(max_length=255)
    curpfile_pers = models.FileField(upload_to="Uploaded Files/")
    inefile_pers = models.FileField(upload_to="Uploaded Files/")
    jsonresp_pers = models.CharField(max_length=1000, null=True)

class Usr_Sol_Dom(models.Model):
    codigocn_pers = models.CharField(max_length=255)
    id_sol = models.CharField(max_length=255, null=True)
    tipo_sol = models.CharField(max_length=255)
    detalle_sol = models.CharField(max_length=255)
    cp_sol = models.CharField(max_length=255)
    estado_sol = models.CharField(max_length=255)
    alc_Mun_sol = models.CharField(max_length=255)
    colonia_sol = models.CharField(max_length=255)
    calle_sol = models.CharField(max_length=255)
    numint_sol = models.CharField(max_length=255)
    numext_sol = models.CharField(max_length=255)
    ref_sol = models.CharField(max_length=255)
    fecha_sol = models.CharField(max_length=255)
    status_sol = models.CharField(max_length=255)
    fecha_ult_mod = models.CharField(max_length=255)
    doc1_sol = models.FileField(upload_to="Uploaded Files/tickets/")

class Usr_Sol_Domfis(models.Model):
    codigocn_pers = models.CharField(max_length=255)
    id_sol = models.CharField(max_length=255, null=True)
    tipo_sol = models.CharField(max_length=255)
    detalle_sol = models.CharField(max_length=255)
    cp_sol = models.CharField(max_length=255)
    estado_sol = models.CharField(max_length=255)
    alc_Mun_sol = models.CharField(max_length=255)
    colonia_sol = models.CharField(max_length=255)
    calle_sol = models.CharField(max_length=255)
    numint_sol = models.CharField(max_length=255)
    numext_sol = models.CharField(max_length=255)
    ref_sol = models.CharField(max_length=255)
    fecha_sol = models.CharField(max_length=255)
    status_sol = models.CharField(max_length=255)
    fecha_ult_mod = models.CharField(max_length=255)
    doc1_sol = models.FileField(upload_to="Uploaded Files/tickets/")

class Usr_Sol_Rfc(models.Model):
    codigocn_pers = models.CharField(max_length=255)
    id_sol = models.CharField(max_length=255, null=True)
    tipo_sol = models.CharField(max_length=255)
    detalle_sol = models.CharField(max_length=255)
    rfc_sol = models.CharField(max_length=255)
    fecha_sol = models.CharField(max_length=255)
    status_sol = models.CharField(max_length=255)
    fecha_ult_mod = models.CharField(max_length=255)
    doc1_sol = models.FileField(upload_to="Uploaded Files/tickets/")
    doc2_sol = models.FileField(upload_to="Uploaded Files/tickets/")

class Track_Sol(models.Model):
    id_sol = models.CharField(max_length=255)
    status_sol = models.CharField(max_length=255)
    fecha_ult_mod = models.CharField(max_length=255)
    usuario_mod_sol = models.CharField(max_length=255, null=True)
