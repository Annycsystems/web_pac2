# Generated by Django 4.1 on 2022-12-09 20:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('datos', '0017_usr_sol_curp_id_sol_usr_sol_dom_id_sol_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='usr_sol_curp',
            name='track',
            field=models.CharField(max_length=1000, null=True),
        ),
        migrations.AlterField(
            model_name='usr_sol_curp',
            name='usuario_mod_sol',
            field=models.CharField(max_length=255, null=True),
        ),
        migrations.AlterField(
            model_name='usr_sol_dom',
            name='track',
            field=models.CharField(max_length=1000, null=True),
        ),
        migrations.AlterField(
            model_name='usr_sol_dom',
            name='usuario_mod_sol',
            field=models.CharField(max_length=255, null=True),
        ),
        migrations.AlterField(
            model_name='usr_sol_nom',
            name='track',
            field=models.CharField(max_length=1000, null=True),
        ),
        migrations.AlterField(
            model_name='usr_sol_nom',
            name='usuario_mod_sol',
            field=models.CharField(max_length=255, null=True),
        ),
        migrations.AlterField(
            model_name='usr_sol_rfc',
            name='track',
            field=models.CharField(max_length=1000, null=True),
        ),
        migrations.AlterField(
            model_name='usr_sol_rfc',
            name='usuario_mod_sol',
            field=models.CharField(max_length=255, null=True),
        ),
    ]