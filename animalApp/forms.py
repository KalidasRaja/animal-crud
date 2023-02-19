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
        fields = ('animal', 'breed', 'date')
        
        widgets = {
            # 'breed' : forms.TextInput(),
            'date' : forms.DateInput(attrs={'type' : 'date'})
        }

        # def clean(self):
        #     cleaned_data = super().clean()
        #     animal = cleaned_data.get('animal', None)
        #     breed = cleaned_data.get('breed', None)
            # date = cleaned_data.get('date', None)

        def __int__(self, *args, **kwargs):
            super().__init__(*args, **kwargs)
            self.fields['breed'].queryset = Breed.objects.none()
