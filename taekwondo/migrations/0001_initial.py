# Generated by Django 3.2.7 on 2021-09-05 17:15

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Kota',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nama_kota', models.CharField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='Provinsi',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nama_provinsi', models.CharField(max_length=150)),
            ],
        ),
        migrations.CreateModel(
            name='Pelatih',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('No_Reg', models.CharField(max_length=20)),
                ('Nama_Lengkap', models.CharField(max_length=50)),
                ('Tempat_Lahir', models.CharField(max_length=30)),
                ('Nama_Dojang', models.CharField(max_length=30)),
                ('Tanggal_Lahir', models.DateField()),
                ('jenis_Kelamin', models.CharField(choices=[('laki-laki', 'Laki-laki'), ('perempuan', 'Perempuan')], max_length=15)),
                ('Status', models.CharField(choices=[('aktif', 'Aktif'), ('tidakAktif', 'Tidak Aktif')], max_length=15)),
                ('Sabuk_Akhir', models.CharField(choices=[('dan3', 'Dan III'), ('dan2', 'Dan II'), ('dan1', 'Dan I'), ('hitam', 'HItam'), ('merah', 'Merah')], max_length=15)),
                ('No_Telp', models.CharField(max_length=15)),
                ('Email', models.EmailField(max_length=50)),
                ('Photo', models.ImageField(blank=True, upload_to='images/')),
                ('Tanggal_Input', models.DateField(auto_now_add=True)),
                ('Kota_Asal', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='taekwondo.kota')),
                ('Provinsi_Asal', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='taekwondo.provinsi')),
            ],
        ),
        migrations.AddField(
            model_name='kota',
            name='provinsi',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='taekwondo.provinsi'),
        ),
    ]
