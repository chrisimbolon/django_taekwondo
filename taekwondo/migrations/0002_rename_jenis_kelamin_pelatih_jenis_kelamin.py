# Generated by Django 3.2.7 on 2021-09-06 03:04

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('taekwondo', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='pelatih',
            old_name='jenis_Kelamin',
            new_name='Jenis_Kelamin',
        ),
    ]
