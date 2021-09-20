from django.db import models
from django.utils.timezone import datetime
from django.contrib.auth.models import User
# Create your models here.

class Provinsi(models.Model):
    nama_provinsi = models.CharField(max_length=150)

    def __str__(self):
        return self.nama_provinsi

class Kota(models.Model):
    nama_kota = models.CharField(max_length=200)
    provinsi = models.ForeignKey('Provinsi', on_delete=models.CASCADE)

    def __str__(self):
        return self.nama_kota

    def testing_function(self):
        return self.provinsi

class Pelatih(models.Model):
    Manager = models.ForeignKey(User, on_delete=models.CASCADE,default=None)
    No_Reg = models.CharField(max_length=20)
    Nama_Lengkap = models.CharField(max_length=50)
    Tempat_Lahir = models.CharField(max_length=30)
    Tanggal_Lahir = models.DateField()
    Nama_Dojang = models.CharField(max_length=30)
    Jenis_Kelamin = models.CharField(max_length=15,choices=(
        ('laki-laki','Laki-laki'),
        ('perempuan','Perempuan')
    ))
    Provinsi_Asal = models.ForeignKey('Provinsi', on_delete=models.SET_NULL, null=True)
    Kota_Asal = models.ForeignKey('Kota', on_delete=models.SET_NULL, null=True)
    Status =models.CharField(max_length=15,choices=(
        ('aktif','Aktif'),
        ('tidak aktif','Tidak Aktif')
    ))
    Sabuk_Akhir = models.CharField(max_length=15,choices=(
        ('dan3','Dan III'),
        ('dan2','Dan II'),
        ('dan1','Dan I'),
        ('hitam','HItam'),
        ('merah','Merah')
    ))
    No_Telp = models.CharField(max_length=15)
    Email = models.EmailField(max_length=50)
    Photo = models.ImageField(upload_to='images/',blank=True)
    Tanggal_Input = models.DateField(default=datetime.now)

    def __str__(self):
        return self.Nama_Lengkap

    class Meta:
        ordering = ['-id']

