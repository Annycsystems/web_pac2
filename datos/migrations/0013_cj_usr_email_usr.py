# Generated by Django 4.1 on 2022-11-26 22:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('datos', '0012_cj_usr'),
    ]

    operations = [
        migrations.AddField(
            model_name='cj_usr',
            name='email_usr',
            field=models.CharField(max_length=255, null=True),
        ),
    ]