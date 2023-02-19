from .forms import AnimalForm, BreedForm, SitingForm
from django.shortcuts import render, redirect
from .models import Animal, Breed, Siting
from django.views.generic import View
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse


class home(View):
    context = {}
    def get(self, request):
        form = SitingForm
        self.context['form'] = form
        self.context['siting'] = Siting.objects.all().order_by('-date')
        print("Hello Get : ",self.context['siting'])
        return render(request, 'animal/home.html', self.context)

    def post(self, request):
        form = SitingForm(request.POST)
        if form.is_valid():
            instance = form.save(commit=False)
            instance.user = request.user
            instance.save()
            # form.save(commit=True)

        self.context['form'] = form
        self.context['siting'] = Siting.objects.all()
        print("Hello Post : ",self.context['siting'])
        return HttpResponseRedirect(reverse('home'))
        # return render(request, 'animal/home.html', self.context)
def delete(request, id):
        siting = Siting.objects.get(id=id)
        siting.delete()
        return HttpResponseRedirect(reverse('home'))


def index(request):
        animal = Animal.objects.all()
        breed = Breed.objects.all()
        siting = Siting.objects.all()
        context = {
            'breed': breed,
            'animal': animal,
            'siting' : siting
        }

        return render(request, 'field.html', context)



