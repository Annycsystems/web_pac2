# Generated by Django 4.1.5 on 2023-01-23 20:01

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('datos', '0019_track_sol_usr_sol_domfis_delete_usr_sol_curp_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='track_sol',
            old_name='Status_sol',
            new_name='status_sol',
        ),
    ]
