from django.forms import ModelForm, EmailInput, PasswordInput
from django import forms

from datos.models import pers_gen, cj_usr


class PersonaForm(ModelForm):
    class Meta:
        model = pers_gen
        fields = ['Codigo_CN', 'Nombre_CN', 'MdC', 'DRV', 'Red', 'CURP', 'RFC']
        widgets = {
            'Codigo_CN': forms.TextInput(attrs={'size': 10, 'title': 'Your name'})
        }


class UploadFileForm(forms.Form):
    CodigoCN_pers = forms.CharField(max_length=50)
    Nombre_pers = forms.CharField(max_length=50)
    ApellidoP_pers = forms.CharField(max_length=50)
    ApellidoM_pers = forms.CharField(max_length=50)
    CURP_pers = forms.CharField(max_length=50)
    CURPFile_pers = forms.FileField()
    INEFile_pers = forms.FileField()


class NewpersonForm(ModelForm):
    def __init__(self, *args, **kwargs):
        super(NewpersonForm, self).__init__(*args, **kwargs)
        for field in self.fields:
            self.fields[field].widget.attrs = {
                'class': 'campo',
            }
            self.fields['usr_pers'].widget.attrs = {
                'class': 'campo',
            }
    field_order = ['usr_pers', 'pass_usr', 'Nombre_usr', 'email_usr']
    class Meta:
        model = cj_usr
        fields = {'usr_pers', 'Nombre_usr', 'email_usr', 'pass_usr'}

        widgets = {
            'email_usr': EmailInput(attrs={'type': 'email'}),
            'pass_usr': PasswordInput(attrs={'type': 'password'})
        }
