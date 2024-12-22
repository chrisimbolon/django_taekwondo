from django.contrib import admin
from .models import Coach,Province, City, Belt
from import_export.admin import ImportExportModelAdmin


# Province Admin
@admin.register(Province)
class ProvinceAdmin(admin.ModelAdmin):
    list_display = ('province_name', 'country')  # Show these fields in the admin list view
    search_fields = ('province_name', 'country')  # Add search functionality


# City Admin
@admin.register(City)
class CityAdmin(admin.ModelAdmin):
    list_display = ('city_name', 'province')  # Show these fields in the admin list view
    search_fields = ('city_name', 'province__province_name')  # Add search functionality
    list_filter = ('province',)  # Add filtering by province


# Belt Admin
@admin.register(Belt)
class BeltAdmin(admin.ModelAdmin):
    list_display = ('rank_name', 'rank_level', 'is_black_belt')  # Show these fields in the admin list view
    search_fields = ('rank_name',)




@admin.register(Coach)
class CoachAdmin(admin.ModelAdmin):
    list_display = ('full_name', 'registration_number', 'sex', 'belt', 'status', 'province', 'city', 'manager')  # Show these fields
    search_fields = ('full_name', 'registration_number', 'dojang_name', 'email')  # Add search functionality
    list_filter = ('sex', 'status', 'belt', 'province', 'city')  # Add filtering
    ordering = ('-id',)  # Order by ID in descending order

# Editable fields in the list view
    list_editable = ('status',)

    # Fields shown when editing/adding
    fields = (
        'full_name',
        'manager',
        'registration_number',
        'place_of_birth',
        'date_of_birth',
        'dojang_name',
        'sex',
        'province',
        'city',
        'status',
        'belt',
        'phone_number',
        'email',
        'photo',
    )

    # Read-only fields
    readonly_fields = ('manager', 'date_of_birth',)

