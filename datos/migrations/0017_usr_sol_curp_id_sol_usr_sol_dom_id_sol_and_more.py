# Generated by Django 4.1 on 2022-12-09 18:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('datos', '0016_usr_sol_curp_usr_sol_dom_usr_sol_nom_usr_sol_rfc_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='usr_sol_curp',
            name='id_sol',
            field=models.CharField(max_length=255, null=True),
        ),
        migrations.AddField(
            model_name='usr_sol_dom',
            name='id_sol',
            field=models.CharField(max_length=255, null=True),
        ),
        migrations.AddField(
            model_name='usr_sol_nom',
            name='id_sol',
            field=models.CharField(max_length=255, null=True),
        ),
        migrations.AddField(
            model_name='usr_sol_rfc',
            name='id_sol',
            field=models.CharField(max_length=255, null=True),
        ),
    ]