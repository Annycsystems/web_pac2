from django.db import models
# Create your models here.

class tipo_solicitud(models.Model):
    hab_opc = (
        ('1', 'Habilitado'),
        ('0', 'Deshabilitado'),
    )
    nombre = models.CharField(max_length=255)
    habilitado = models.CharField(max_length=1, choices=hab_opc)

    def __str__(self):
        return f' {self.nombre}'

class tema_solicitud(models.Model):
    hab_opc = (
        ('1', 'Habilitado'),
        ('0', 'Deshabilitado'),
    )
    nombre = models.CharField(max_length=255)
    habilitado = models.CharField(max_length=1,choices=hab_opc)
    tipo = models.ForeignKey(tipo_solicitud, on_delete=models.SET_NULL, null=True)

    def __str__(self):
        return f' {self.nombre}'

class Subtema_solicitud(models.Model):
    hab_opc = (
        ('1', 'Habilitado'),
        ('0', 'Deshabilitado'),
    )
    nombre = models.CharField(max_length=255)
    habilitado = models.CharField(max_length=1, choices=hab_opc)
    tema = models.ForeignKey(tema_solicitud, on_delete=models.SET_NULL, null=True)

    def __str__(self):
        return f' {self.nombre}'

class Roles_usr(models.Model):
    hab_opc = (
        ('1', 'Habilitado'),
        ('0', 'Deshabilitado'),
    )
    Nombre_Rol = models.CharField(max_length=255)
    habilitado = models.CharField(max_length=1, choices=hab_opc)

    def __str__(self):
        return f' {self.Nombre_Rol}'

class Atributos(models.Model):
    hab_opc = (
        ('1', 'Habilitado'),
        ('0', 'Deshabilitado'),
    )
    Nombre_atrib = models.CharField(max_length=255)
    habilitado = models.CharField(max_length=1, choices=hab_opc)

    def __str__(self):
        return f' {self.Nombre_atrib}'

class pers_gen(models.Model):
    Codigo_CN = models.CharField(max_length=255)
    Nombre_CN = models.CharField(max_length=255)
    Apellidos_CN = models.CharField(max_length=255, null=True)
    MdC = models.CharField(max_length=255)
    DRV = models.CharField(max_length=255)
    Red = models.CharField(max_length=255)
    CURP = models.CharField(max_length=255)
    RFC = models.CharField(max_length=255)
    Fecha_alta = models.DateField()
    email = models.CharField(max_length=255, null=True)
    tel_cel =models.CharField(max_length=255,null=True)
    first_Acces =models.CharField(max_length=255,null=True)

    def __str__(self):
        return f' Codigo_CN: {self.Codigo_CN}, Nombre_CN: {self.Nombre_CN}, con MdC: {self.MdC}, email: {self.email}'

class users_sys(models.Model):
    hab_opc = (
        ('1', 'Habilitado'),
        ('0', 'Deshabilitado'),
    )
    usr = models.ForeignKey(pers_gen, on_delete=models.SET_NULL, null=True)
    passw = models.CharField(max_length=255)
    rol = models.ForeignKey(Roles_usr, on_delete=models.SET_NULL, null=True)

    def __str__(self):
        return f' {self.usr}'

class entidades_rep(models.Model):
    entidad = models.CharField(max_length=255)

    def __str__(self):
        return f' {self.entidad}'

class primer_registro(models.Model):
    CodigoCN_pers = models.CharField(max_length=255)
    Nombre_pers = models.CharField(max_length=255)
    ApellidoP_pers = models.CharField(max_length=255)
    ApellidoM_pers = models.CharField(max_length=255)
    CURP_pers = models.CharField(max_length=255)
    CURPFile_pers = models.FileField(upload_to="Uploaded Files/")
    INEFile_pers = models.FileField(upload_to="Uploaded Files/")
    JSONresp_pers = models.CharField(max_length=1000, null=True)

    def __str__(self):
        return f' {self.CodigoCN_pers}, nombre: {self.Nombre_pers}'

class cj_usr(models.Model):
    usr_pers = models.CharField(max_length=255)
    Nombre_usr = models.CharField(max_length=255)
    email_usr = models.CharField(max_length=255, null=True)
    pass_usr = models.CharField(max_length=255, null=True)
    fecha_alta_urs = models.CharField(max_length=255)
    fecha_ultimo_ingreso = models.CharField(max_length=255)

    def __str__(self):
        return f' {self.usr_pers}, nombre: {self.Nombre_usr}'

class usr_sol_dom(models.Model):
    CodigoCN_pers = models.CharField(max_length=255)
    id_sol = models.CharField(max_length=255, null=True)
    Tipo_sol = models.CharField(max_length=255)
    Detalle_sol = models.CharField(max_length=255)
    cp_sol = models.CharField(max_length=255)
    estado_sol = models.CharField(max_length=255)
    alc_mun_sol = models.CharField(max_length=255)
    colonia_sol = models.CharField(max_length=255)
    calle_sol = models.CharField(max_length=255)
    NumInt_sol = models.CharField(max_length=255)
    NumExt_sol = models.CharField(max_length=255)
    Ref_sol = models.CharField(max_length=255)
    Fecha_sol = models.CharField(max_length=255)
    Status_sol = models.CharField(max_length=255)
    fecha_ult_mod = models.CharField(max_length=255)
    Doc1_sol = models.FileField(upload_to="Uploaded Files/tickets/")

class usr_sol_domfis(models.Model):
    CodigoCN_pers = models.CharField(max_length=255)
    id_sol = models.CharField(max_length=255, null=True)
    Tipo_sol = models.CharField(max_length=255)
    Detalle_sol = models.CharField(max_length=255)
    cp_sol = models.CharField(max_length=255)
    estado_sol = models.CharField(max_length=255)
    alc_mun_sol = models.CharField(max_length=255)
    colonia_sol = models.CharField(max_length=255)
    calle_sol = models.CharField(max_length=255)
    NumInt_sol = models.CharField(max_length=255)
    NumExt_sol = models.CharField(max_length=255)
    Ref_sol = models.CharField(max_length=255)
    Fecha_sol = models.CharField(max_length=255)
    Status_sol = models.CharField(max_length=255)
    fecha_ult_mod = models.CharField(max_length=255)
    Doc1_sol = models.FileField(upload_to="Uploaded Files/tickets/")

class usr_sol_rfc(models.Model):
    CodigoCN_pers = models.CharField(max_length=255)
    id_sol = models.CharField(max_length=255, null=True)
    Tipo_sol = models.CharField(max_length=255)
    Detalle_sol = models.CharField(max_length=255)
    RFC_sol = models.CharField(max_length=255)
    Fecha_sol = models.CharField(max_length=255)
    Status_sol = models.CharField(max_length=255)
    fecha_ult_mod = models.CharField(max_length=255)
    Doc1_sol = models.FileField(upload_to="Uploaded Files/tickets/")
    Doc2_sol = models.FileField(upload_to="Uploaded Files/tickets/")

class track_sol(models.Model):
    id_sol = models.CharField(max_length=255)
    status_sol = models.CharField(max_length=255)
    fecha_ult_mod = models.CharField(max_length=255)
    usuario_mod_sol = models.CharField(max_length=255, null=True)

