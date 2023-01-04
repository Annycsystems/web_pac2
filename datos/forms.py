from django.forms import ModelForm, EmailInput, PasswordInput
from django import forms


class UploadFileForm(forms.Form):
    CodigoCN_pers = forms.CharField(max_length=50)
    Nombre_pers = forms.CharField(max_length=50)
    ApellidoP_pers = forms.CharField(max_length=50)
    ApellidoM_pers = forms.CharField(max_length=50)
    CURP_pers = forms.CharField(max_length=50)
    CURPFile_pers = forms.FileField()
    INEFile_pers = forms.FileField()