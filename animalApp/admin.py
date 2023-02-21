from django.contrib import admin
from .models import *
from import_export.admin import ImportExportModelAdmin
reclass breedAdmin(ImportExportModelAdmin, admin.ModelAdmin):
    list_display = ['name', 'animal']
    list_filter = ['animal', 'name']
    search_fields = ['name', 'animal']

admin.site.register(Breed, breedAdmin)


@admin.register(Animal)
class AnimalAdmin(ImportExportModelAdmin, admin.ModelAdmin):
    list_display = ['name']

@admin.register(Siting)
class SitingAdmin(ImportExportModelAdmin, admin.ModelAdmin):
    list_display = ['animal', 'breed', 'date']