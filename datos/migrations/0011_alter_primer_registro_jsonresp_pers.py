# Generated by Django 4.1 on 2022-11-05 05:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('datos', '0010_primer_registro_jsonresp_pers'),
    ]

    operations = [
        migrations.AlterField(
            model_name='primer_registro',
            name='JSONresp_pers',
            field=models.CharField(max_length=1000, null=True),
        ),
    ]
