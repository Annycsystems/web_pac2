from django.db import models
from model_utils import Choices


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
     cn_indicante = models.ForeignKey('cjvc.Consultora', null=True, db_constraint=False,
                                      blank=True, on_delete=models.PROTECT, related_name="invitadas")
     cn_lider = models.ForeignKey('cjvc.Consultora', null=True, db_constraint=False,
                                  blank=True, on_delete=models.PROTECT, related_name="gestionadas")
     fecha_asignacion_lider = models.DateTimeField(null=True, blank=True)
     fecha_aprobacion_lider = models.DateTimeField(null=True, blank=True)
     tipo_aprobacion = models.CharField(blank=False, null=True, max_length=20,
                                        choices=TIPO_APROBACION, default=TIPO_APROBACION.pendiente)
     red = models.ForeignKey('cjvc.Red', null=True, db_constraint=False,
                             on_delete=models.PROTECT, related_name="consultoras")
     creado = models.DateTimeField(auto_now_add=True, db_index=True)
     actualizado = models.DateTimeField(auto_now=True, db_index=True)
     First_Acces = models.CharField(max_length=255, null=True)

class Primer_Registro(models.Model):
    Codigocn_Pers = models.CharField(max_length=255)
    Nombre_Pers = models.CharField(max_length=255)
    Apellidop_Pers = models.CharField(max_length=255)
    Apellidom_Pers = models.CharField(max_length=255)
    CURP_Pers = models.CharField(max_length=255)
    CURPfile_Pers = models.FileField(upload_to="Uploaded Files/")
    INEfile_Pers = models.FileField(upload_to="Uploaded Files/")
    JSONresp_Pers = models.CharField(max_length=1000, null=True)

class Usr_Sol_Dom(models.Model):
    CodigoCN_Pers = models.CharField(max_length=255)
    Id_Sol = models.CharField(max_length=255, null=True)
    Tipo_Sol = models.CharField(max_length=255)
    Detalle_Sol = models.CharField(max_length=255)
    Cp_Sol = models.CharField(max_length=255)
    Estado_Sol = models.CharField(max_length=255)
    Alc_Mun_Sol = models.CharField(max_length=255)
    Colonia_Sol = models.CharField(max_length=255)
    Calle_Sol = models.CharField(max_length=255)
    Numint_Sol = models.CharField(max_length=255)
    Numext_Sol = models.CharField(max_length=255)
    Ref_Sol = models.CharField(max_length=255)
    Fecha_Sol = models.CharField(max_length=255)
    Status_Sol = models.CharField(max_length=255)
    Fecha_Ult_Mod = models.CharField(max_length=255)
    Doc1_Sol = models.FileField(upload_to="Uploaded Files/tickets/")

class Usr_Sol_Domfis(models.Model):
    CodigoCN_Pers = models.CharField(max_length=255)
    Id_Sol = models.CharField(max_length=255, null=True)
    Tipo_Sol = models.CharField(max_length=255)
    Detalle_Sol = models.CharField(max_length=255)
    Cp_Sol = models.CharField(max_length=255)
    Estado_Sol = models.CharField(max_length=255)
    Alc_Mun_Sol = models.CharField(max_length=255)
    Colonia_Sol = models.CharField(max_length=255)
    Calle_Sol = models.CharField(max_length=255)
    Numint_Sol = models.CharField(max_length=255)
    Numext_Sol = models.CharField(max_length=255)
    Ref_Sol = models.CharField(max_length=255)
    Fecha_Sol = models.CharField(max_length=255)
    Status_Sol = models.CharField(max_length=255)
    Fecha_Ult_Mod = models.CharField(max_length=255)
    Doc1_Sol = models.FileField(upload_to="Uploaded Files/tickets/")

class Usr_Sol_Rfc(models.Model):
    Codigocn_Pers = models.CharField(max_length=255)
    Id_Sol = models.CharField(max_length=255, null=True)
    Tipo_Sol = models.CharField(max_length=255)
    Detalle_Sol = models.CharField(max_length=255)
    RFC_Sol = models.CharField(max_length=255)
    Fecha_Sol = models.CharField(max_length=255)
    Status_Sol = models.CharField(max_length=255)
    Fecha_ult_mod = models.CharField(max_length=255)
    Doc1_Sol = models.FileField(upload_to="Uploaded Files/tickets/")
    Doc2_Sol = models.FileField(upload_to="Uploaded Files/tickets/")

class Track_Sol(models.Model):
    Id_Sol = models.CharField(max_length=255)
    Status_Sol = models.CharField(max_length=255)
    Fecha_Ult_Mod = models.CharField(max_length=255)
    Usuario_Mod_Sol = models.CharField(max_length=255, null=True)