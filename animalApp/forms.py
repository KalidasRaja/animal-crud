from django import forms
from .models import Animal, Breed, Siting

class AnimalForm(forms.ModelForm):
    class Meta:
        model = Animal
        fields = ('name',)

class BreedForm(forms.ModelForm):
    class Meta:
        model = Breed
        fields = ('name', 'animal')


class SitingForm(forms.ModelForm):
    class Meta:
        model = Siting
        fields = '__all__'
        # fields = ('animal', 'breed', 'date')
        
        widgets = {
            'date' : forms.DateInput(attrs={'type' : 'date'})
        }

        def __int__(self, *args, **kwargs):
            super().__init__(*args, **kwargs)
            self.fields['breed'].queryset = Breed.objects.none()

