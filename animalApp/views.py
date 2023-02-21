from django.shortcuts import render
from .models import Animal, Breed, Siting
from django.views.generic import View
from django.http import JsonResponse, HttpResponseRedirect
from django.urls import reverse


class home(View):
    context = {}
    def get(self, request):
        context = {
           'animal' : Animal.objects.all(),
            'breed' : Breed.objects.all(),
            'siting' : Siting.objects.all().order_by('-date')

        }
        return render(request, 'animal/home.html', context)

    def post(self, request):
        if request.method == "POST":
            if request.POST['animal'] != '' :
                animal_id = request.POST['animal']
                breed_id = request.POST['breed']
                date = request.POST['date']
                animal = Animal.objects.get(pk=animal_id)
                breed = Breed.objects.get(pk=breed_id)
                s = Siting(animal=animal, breed=breed, date=date)
                s.save()
            else:
                return

        return HttpResponseRedirect(reverse('home'))
def delete(request, id):
        siting = Siting.objects.get(id=id)
        siting.delete()
        return HttpResponseRedirect(reverse('home'))


def ajax_data(request):
    if request.method == "POST":
        animal_id = request.POST['animal_id']
        try:
            animal = Animal.objects.filter(id = animal_id).first()
            breed = Breed.objects.filter(animal = animal)
        except Exception:
            data['error_message'] = 'error'
            return JsonResponse(data)
    return JsonResponse(list(breed.values('id', 'name')), safe=False)
