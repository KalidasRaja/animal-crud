from django.contrib import admin
from .models import *
from import_export.admin import ImportExportModelAdmin
#
# admin.site.register(Animal)
class breedAdmin(ImportExportModelAdmin, admin.ModelAdmin):
    list_display = ['name', 'animal']
    list_filter = ['animal', 'name']
    search_fields = ['name', 'animal']

admin.site.register(Breed, breedAdmin)


from django.contrib import admin
from django.urls import reverse, path
from django.http import HttpResponseRedirect
from django.shortcuts import render

from .models import Animal, Breed, Siting


class BreedInline(admin.TabularInline):
    model = Breed
    extra = 0


@admin.register(Animal)
class AnimalAdmin(admin.ModelAdmin):
    inlines = [BreedInline]


@admin.register(Siting)
class SitingAdmin(ImportExportModelAdmin, admin.ModelAdmin):
    list_display = ['animal', 'breed', 'date']

    def changelist_view(self, request, extra_context=None):
        if request.POST.get('action') == 'add_siting':
            animal_id = request.POST.get('animal')
            breed_id = request.POST.get('breed')
            date = request.POST.get('date')
            animal = Animal.objects.get(pk=animal_id)
            breed = Breed.objects.get(pk=breed_id)
            Siting.objects.create(animal=animal, breed=breed, date=date)
            return HttpResponseRedirect(request.path_info)
        else:
            return super().changelist_view(request, extra_context=extra_context)

    def get_urls(self):
        urls = super().get_urls()
        my_urls = [
            path('add_siting/', self.add_siting),
        ]
        return my_urls + urls

    def add_siting(self, request):
        animals = Animal.objects.all()
        if request.method == 'POST':
            animal_id = request.POST.get('animal')
            breed_id = request.POST.get('breed')
            date = request.POST.get('date')
            animal = Animal.objects.get(pk=animal_id)
            breed = Breed.objects.get(pk=breed_id)
            Siting.objects.create(animal=animal, breed=breed, date=date)
            return HttpResponseRedirect(reverse('admin:siting_siting_changelist'))
        return render(request, 'admin/siting/siting/add_siting.html', {'animals': animals})
