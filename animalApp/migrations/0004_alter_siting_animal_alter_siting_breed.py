# Generated by Django 4.1.7 on 2023-02-19 11:04

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('animalApp', '0003_remove_breed_createdat_alter_animal_name_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='siting',
            name='animal',
            field=models.ForeignKey(blank=True, on_delete=django.db.models.deletion.CASCADE, to='animalApp.animal'),
        ),
        migrations.AlterField(
            model_name='siting',
            name='breed',
            field=models.ForeignKey(blank=True, on_delete=django.db.models.deletion.CASCADE, to='animalApp.breed'),
        ),
    ]