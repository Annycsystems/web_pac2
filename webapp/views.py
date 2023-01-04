import tempfile

import requests
import json

from django.http import JsonResponse
from django.shortcuts import render, redirect
from django.template.loader import get_template
from django.core.mail import EmailMultiAlternatives
from django.conf import settings
from django.contrib import messages
from datetime import datetime

from datos.forms import NewpersonForm
from datos.models import tipo_solicitud, pers_gen, users_sys, primer_registro, usr_sol_dom, usr_sol_rfc, track_sol
from django.db.models import Max



def bienvenido(request):
    if request.method == "POST":
        forma_nuevo_usuario = NewpersonForm(request.POST)
        if forma_nuevo_usuario.is_valid():
            forma_nuevo_usuario.save()
            return redirect('inicio')
    else:
        forma_nuevo_usuario = NewpersonForm()
    return render(request, 'inicio_Sesion.html', {'forma_nuevo_usuario': forma_nuevo_usuario})
    # return render(request, 'inicio_Sesion.html')


def rec_pass(request):
    return render(request, 'recuperar_Contrasenia.html')

def main(request):
    return render(request, 'main.html')
# def main(request):
#     return render(request, 'menuPrincipal.html')
# def main(request):
#     return render(request, 'tkn_template.html')

def bienvenidos(request):
    return render(request, 'bienvenido.html')


def new_pers(request):

    if request.method == "POST":
        forma_nuevo_usuario = NewpersonForm(request.POST)
        if forma_nuevo_usuario.is_valid():
            forma_nuevo_usuario.save()
            return redirect('inicio')
    else:
        forma_nuevo_usuario = NewpersonForm()
    return render(request, 'Sign_in.html', {'forma_nuevo_usuario': forma_nuevo_usuario})

def main_menu(request):
    return render(request, 'menuPrincipal.html')


def search_pers(request):
    search = request.POST.get('search')
    exis = pers_gen.objects.filter(Codigo_CN=search).exists()
    if exis:
        # print("ok")
        persons = pers_gen.objects.filter(Codigo_CN=search)
        acce = pers_gen.objects.filter(Codigo_CN=search).values("first_Acces")
        vali = str(acce[0]["first_Acces"])
        data = pers_gen.objects.filter(Codigo_CN=search).values("email","tel_cel")
        data2 = pers_gen.objects.filter(Codigo_CN=search).values("Codigo_CN")
        if vali == '1':
            return render(request, 'car_bievenido.html', {'persons': persons, 'data': data, 'data2': data2})
        else:
            return render(request, 'menuPrincipal.html', {'persons': persons, 'data': data, 'data2': data2})
    messages.success(request, 'Código ingresado no válido o incorrecto,   favor de verificarlo.')
    return render(request, 'bienvenido.html')

def send_email(mail,nombre,temp,adi,folio):
    try:
        context = {'nombre': nombre,'solicitud':adi,'folio':folio}
        template = get_template(temp)
        content = template.render(context)

        email = EmailMultiAlternatives(
            'Notificaciones Cambio de datos Natura MX',
            'Cambio de Datos Natura',
            settings.EMAIL_HOST_USER,
            [mail]
        )
        print(mail)
        email.attach_alternative(content, 'text/html')
        email.send()
        print("ok")
        return JsonResponse({'status': True, 'mensaje': 'Correo enviado exitosamente'})
    except Exception as e:
        print(e.__str__())
        return JsonResponse({'status': False, 'mensaje': 'Ocurrio un error al momento de enviar el correo'})

def uploadFile(request):
    if request.method == "POST":
        Cod = request.POST["cod"]
        Nomb = request.POST["Nomb"]
        AP = request.POST["AP"]
        AM = request.POST["AM"]
        CURP = request.POST["CURP"]
        CURPUpload = request.FILES["CURPUp"]
        INEUpload = request.FILES["INEUp"]
        CURPUpload.name = Cod + "_" + CURPUpload.name
        INEUpload.name = Cod + "_" + INEUpload.name
        url = "https://curp.nubarium.com/renapo/v2/valida_curp"
        payload = json.dumps({
            "curp": CURP,
            "documento": "0"
        })
        headers = {
            'Content-Type': 'application/json',
            'Authorization': 'Basic Y29uc3VsdG9yZXMtY3J6OmY2U2guOVdwX24='
        }
        response = requests.request("POST", url, headers=headers, data=payload)
        resp = response.json()
        document = primer_registro(
            CodigoCN_pers=Cod,
            Nombre_pers=Nomb,
            ApellidoP_pers=AP,
            ApellidoM_pers=AM,
            CURP_pers=CURP,
            CURPFile_pers=CURPUpload,
            INEFile_pers=INEUpload,
            JSONresp_pers=resp
        )
        if str(str(resp["estatus"])) == "OK":
            document.save()
            documents = primer_registro.objects.all()
            pers_gen.objects.filter(Codigo_CN=Cod).update(first_Acces='0')
            acce = pers_gen.objects.filter(Codigo_CN=Cod).values("email")
            acce2 = pers_gen.objects.filter(Codigo_CN=Cod).values("Nombre_CN")
            corr = str(acce[0]["email"])
            nom = str(acce2[0]["Nombre_CN"])
            temp = "correo_datos_gen.html"
            adi="Datos generales"
            folio = ''
            send_email(corr,nom,temp,adi,folio)
            data = pers_gen.objects.filter(Codigo_CN=Cod).values("email", "tel_cel")
            data2 = pers_gen.objects.filter(Codigo_CN=Cod).values("Codigo_CN")
            return render(request, "menuPrincipal.html", {'data': data,'data2': data2})
        if str(str(resp["estatus"])) == "ERROR":
            messages.error(request, 'CURP no valido o incorrecto, favor de verificarlo.')
            print("ok");
            return render(request, "First_access.html")
    return render(request, "First_access.html")

def uploadTickdirect(request):
    if request.method == "POST":
        # fol = usr_sol_dom.objects.aggregate(Max('id'))
        # val_fol = fol["id__max"]
        # if val_fol== None:
        #     val_fol=0
        # val_fol = val_fol+1
        now = datetime.now()
        nowy = now.year
        # if len(str(val_fol)) == 1:
        #     val_fol = '0' + str(val_fol)
        #     tik = 'MD-' + val_fol + '-' + str(nowy)
        # else:
        #     tik = 'MD-' + str(val_fol) + '-' + str(nowy)
        CodigoCN_pers = request.POST["codi"]
        Tipo_sol = "DOMICILIO"
        Detalle_sol = request.POST["direct"]
        cp_sol = request.POST["cp"]
        estado_sol = request.POST["estado"]
        alc_mun_sol = request.POST["municipio"]
        colonia_sol = request.POST["selectColonia"]
        calle_sol = request.POST["calle"]
        NumInt_sol = request.POST["NoInt"]
        NumExt_sol = request.POST["NoExt"]
        Ref_sol = request.POST["Ref"]
        Fecha_sol = now
        Status_sol = "Abierto"
        fecha_ult_mod = now
        # Doc1_sol = request.FILES["INEUp"]
        OTP_via = request.POST["OTP"]
        tk_via = request.POST["tk"]
        # Doc1_sol.name = id_sol + "_" + Doc1_sol.name

        document = {
            "CodigoCN_pers" : CodigoCN_pers,
            "Tipo_sol" : Tipo_sol,
            "Detalle_sol":Detalle_sol,
            "cp_sol":cp_sol,
            "estado_sol":estado_sol,
            "alc_mun_sol":alc_mun_sol,
            "colonia_sol":colonia_sol,
            "calle_sol":calle_sol,
            "NumInt_sol":NumInt_sol,
            "NumExt_sol":NumExt_sol,
            "Ref_sol":Ref_sol,
            "Fecha_sol":Fecha_sol,
            "Status_sol":Status_sol,
            "fecha_ult_mod":fecha_ult_mod,
            # "Doc1_sol":Doc1_sol,
        }
        if (OTP_via == 'mail'):
            acce = pers_gen.objects.filter(Codigo_CN=CodigoCN_pers).values("email")
            acce2 = pers_gen.objects.filter(Codigo_CN=CodigoCN_pers).values("Nombre_CN")
            corr = str(acce[0]["email"])
            nom = str(acce2[0]["Nombre_CN"])
            temp = "correo_tkn.html"
            adi = ""
            folio = tk_via
            send_email(corr, nom, temp, adi, folio)

        # document.save()
            return render(request, "tkn_template.html", {"docs": document})
    return render(request, "menuPrincipal.html")

def Tick_val(request):

    if request.method == "POST":
        fol = usr_sol_dom.objects.aggregate(Max('id'))
        val_fol = fol["id__max"]
        if val_fol== None:
            val_fol=0
        val_fol = val_fol+1
        now = datetime.now()
        nowy = now.year
        if len(str(val_fol)) == 1:
            val_fol = '0' + str(val_fol)
            tik = 'MD-' + val_fol + '-' + str(nowy)
        else:
            tik = 'MD-' + str(val_fol) + '-' + str(nowy)
        CodigoCN_pers = request.POST["CN_sol"]
        Tipo_sol = "DOMICILIO"
        Detalle_sol = request.POST["D_Sol"]
        cp_sol = request.POST["CP_Sol"]
        estado_sol = request.POST["EDO_Sol"]
        alc_mun_sol = request.POST["Alc_Sol"]
        colonia_sol = request.POST["Col_Sol"]
        calle_sol = request.POST["CALLE_Sol"]
        NumInt_sol = request.POST["NUM_int_Sol"]
        NumExt_sol = request.POST["NUM_ext_Sol"]
        Ref_sol = request.POST["REF_Sol"]
        Fecha_sol = now
        Status_sol = "Abierto"
        fecha_ult_mod = now
        Doc1_sol = request.FILES["INEUp"]
        id_sol = tik
        Doc1_sol.name = id_sol + "_" + Doc1_sol.name
        usr_mod = 'CN ' + CodigoCN_pers
        document = usr_sol_dom(
            CodigoCN_pers=CodigoCN_pers,
            Tipo_sol=Tipo_sol,
            Detalle_sol=Detalle_sol,
            cp_sol=cp_sol,
            estado_sol=estado_sol,
            alc_mun_sol=alc_mun_sol,
            colonia_sol=colonia_sol,
            calle_sol=calle_sol,
            NumInt_sol=NumInt_sol,
            NumExt_sol=NumExt_sol,
            Ref_sol=Ref_sol,
            Fecha_sol=Fecha_sol,
            Status_sol=Status_sol,
            fecha_ult_mod=fecha_ult_mod,
            Doc1_sol=Doc1_sol,
            id_sol=id_sol
        )
        document.save()
        document2 = track_sol(
            id_sol=id_sol,
            Status_sol=Status_sol,
            fecha_ult_mod=Fecha_sol,
            usuario_mod_sol=usr_mod
        )
        document2.save()
        messages.success(request, 'Solicitud enviada con éxito Número de folio:' + id_sol + ".")
        data = pers_gen.objects.filter(Codigo_CN=CodigoCN_pers).values("email", "tel_cel")
        data2 = pers_gen.objects.filter(Codigo_CN=CodigoCN_pers).values("Codigo_CN")
        response = redirect('/main')
        return render(request, "menuPrincipal.html", {'data': data,'data2': data2})
    return render(request, "menuPrincipal.html")

def uploadTickRFC(request):
    if request.method == "POST":
        fol = usr_sol_rfc.objects.aggregate(Max('id'))
        val_fol = fol["id__max"]
        if val_fol== None:
            val_fol=0
        val_fol = val_fol+1
        now = datetime.now()
        nowy = now.year
        if len(str(val_fol)) == 1:
            val_fol = '0' + str(val_fol)
            tik = 'MN-' + val_fol + '-' + str(nowy)
        else:
            tik = 'MN-' + str(val_fol) + '-' + str(nowy)
        CodigoCN_pers = request.POST["cod"]
        Tipo_sol = "DOMICILIO"
        Detalle_sol = request.POST["datosG"]
        Nom_sol = request.POST["nom"]
        ApPat_sol = request.POST["Appat"]
        ApMat_sol = request.POST["Apmat"]
        Fecha_sol = now
        Status_sol = "Abierto"
        fecha_ult_mod = now
        usuario_mod_sol = ""
        track = ""
        Doc1_sol = request.FILES["INEUp"]
        Doc2_sol = request.FILES["CURPUp"]
        id_sol = tik
        Doc1_sol.name = id_sol + "_" + Doc1_sol.name
        Doc2_sol.name = id_sol + "_" + Doc2_sol.name
        document = usr_sol_nom(
            CodigoCN_pers=CodigoCN_pers,
            Tipo_sol=Tipo_sol,
            Detalle_sol=Detalle_sol,
            Nom_sol=Nom_sol,
            ApPat_sol=ApPat_sol,
            ApMat_sol=ApMat_sol,
            Fecha_sol=Fecha_sol,
            Status_sol=Status_sol,
            fecha_ult_mod=fecha_ult_mod,
            usuario_mod_sol=usuario_mod_sol,
            track=track,
            Doc1_sol=Doc1_sol,
            Doc2_sol=Doc2_sol,
            id_sol=id_sol
        )
        document.save()
        messages.success(request, 'Solicitud enviada con éxito Número de folio:' + id_sol + ".")
        response = redirect('/main')
        return response
    return render(request, "menuPrincipal.html")

# def cons_sta(request):
