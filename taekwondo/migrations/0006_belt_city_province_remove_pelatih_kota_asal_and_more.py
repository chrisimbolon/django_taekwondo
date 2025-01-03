# Generated by Django 5.1.4 on 2024-12-22 12:34

import datetime
import django.db.models.deletion
import django_countries.fields
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('taekwondo', '0005_auto_20210910_1424'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Belt',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('rank_name', models.CharField(max_length=50)),
                ('rank_level', models.PositiveIntegerField()),
                ('is_black_belt', models.BooleanField(default=False)),
            ],
        ),
        migrations.CreateModel(
            name='City',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('city_name', models.CharField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='Province',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('province_name', models.CharField(max_length=150)),
                ('country', django_countries.fields.CountryField(max_length=2)),
            ],
        ),
        migrations.RemoveField(
            model_name='pelatih',
            name='Kota_Asal',
        ),
        migrations.RemoveField(
            model_name='pelatih',
            name='Manager',
        ),
        migrations.RemoveField(
            model_name='pelatih',
            name='Provinsi_Asal',
        ),
        migrations.CreateModel(
            name='Coach',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('registration_number', models.CharField(max_length=20, unique=True)),
                ('full_name', models.CharField(max_length=50)),
                ('place_of_birth', models.CharField(max_length=30)),
                ('date_of_birth', models.DateField()),
                ('dojang_name', models.CharField(max_length=30)),
                ('sex', models.CharField(choices=[('male', 'Male'), ('female', 'Female')], max_length=15)),
                ('status', models.CharField(choices=[('active', 'Active'), ('inactive', 'Inactive')], max_length=15)),
                ('phone_number', models.CharField(max_length=15)),
                ('email', models.EmailField(max_length=50)),
                ('photo', models.ImageField(blank=True, upload_to='images/')),
                ('input_date', models.DateField(default=datetime.datetime.now)),
                ('belt', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='taekwondo.belt')),
                ('city', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='taekwondo.city')),
                ('manager', models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
                ('province', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='taekwondo.province')),
            ],
            options={
                'ordering': ['-id'],
            },
        ),
        migrations.AddField(
            model_name='city',
            name='province',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='cities', to='taekwondo.province'),
        ),
        migrations.DeleteModel(
            name='Kota',
        ),
        migrations.DeleteModel(
            name='Pelatih',
        ),
        migrations.DeleteModel(
            name='Provinsi',
        ),
    ]
