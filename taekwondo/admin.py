from django.contrib import admin
from .models import Pelatih, Kota, Provinsi
from import_export.admin import ImportExportModelAdmin

class PelatihAdmin(ImportExportModelAdmin):
    list_display  = ('id','Nama_Lengkap','Jenis_Kelamin','Sabuk_Akhir','Status','No_Telp')
    list_display_links = ('id','Nama_Lengkap')
    list_editable = ('No_Telp',) 
    list_per_page = 10
    search_fields = ('Nama_Lengkap','Jenis_Kelamin','Sabuk_Akhir','Status','No_Telp')
    list_filter   = ('Jenis_Kelamin','Tanggal_Input')

admin.site.register(Pelatih,PelatihAdmin)
admin.site.register(Provinsi)
admin.site.register(Kota)
