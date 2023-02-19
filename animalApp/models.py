from django.db import models

class Animal(models.Model):
    name = models.CharField(max_length=128)

    def __str__(self):
        return self.name

class Breed(models.Model):
    name = models.CharField(max_length=128)
    animal = models.ForeignKey(Animal, on_delete=models.CASCADE)

    def __str__(self):
        return self.name


class Siting(models.Model):
    animal = models.ForeignKey(Animal, on_delete=models.CASCADE, blank=False)
    breed = models.ForeignKey(Breed, on_delete=models.CASCADE, blank=False)
    date = models.DateField()

    def __str__(self):
        return f"{self.animal.name} - {self.breed.name} - {self.date}"