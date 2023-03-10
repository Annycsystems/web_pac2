# Generated by Django 4.1 on 2022-12-29 22:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('datos', '0018_alter_usr_sol_curp_track_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='track_sol',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('id_sol', models.CharField(max_length=255)),
                ('Status_sol', models.CharField(max_length=255)),
                ('fecha_ult_mod', models.CharField(max_length=255)),
                ('usuario_mod_sol', models.CharField(max_length=255, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='usr_sol_domfis',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('CodigoCN_pers', models.CharField(max_length=255)),
                ('id_sol', models.CharField(max_length=255, null=True)),
                ('Tipo_sol', models.CharField(max_length=255)),
                ('Detalle_sol', models.CharField(max_length=255)),
                ('cp_sol', models.CharField(max_length=255)),
                ('estado_sol', models.CharField(max_length=255)),
                ('alc_mun_sol', models.CharField(max_length=255)),
                ('colonia_sol', models.CharField(max_length=255)),
                ('calle_sol', models.CharField(max_length=255)),
                ('NumInt_sol', models.CharField(max_length=255)),
                ('NumExt_sol', models.CharField(max_length=255)),
                ('Ref_sol', models.CharField(max_length=255)),
                ('Fecha_sol', models.CharField(max_length=255)),
                ('Status_sol', models.CharField(max_length=255)),
                ('fecha_ult_mod', models.CharField(max_length=255)),
                ('Doc1_sol', models.FileField(upload_to='Uploaded Files/tickets/')),
            ],
        ),
        migrations.DeleteModel(
            name='usr_sol_curp',
        ),
        migrations.DeleteModel(
            name='usr_sol_nom',
        ),
        migrations.RemoveField(
            model_name='usr_sol_dom',
            name='track',
        ),
        migrations.RemoveField(
            model_name='usr_sol_dom',
            name='usuario_mod_sol',
        ),
        migrations.RemoveField(
            model_name='usr_sol_rfc',
            name='track',
        ),
        migrations.RemoveField(
            model_name='usr_sol_rfc',
            name='usuario_mod_sol',
        ),
    ]
