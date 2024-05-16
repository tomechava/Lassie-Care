# commands/load_dog_breeds.py
from django.core.management.base import BaseCommand
from Lassie.models import CatBreed, DogBreed, Breed
import os
import json

class Command(BaseCommand):

    def handle(self, *args, **kwargs):
        dog_breeds = DogBreed.objects.all()
        cat_breeds = CatBreed.objects.all()
    
        for breed in dog_breeds:
            exist = Breed.objects.filter(dogBreed=breed).exists()
            if not exist:
                Breed.objects.create(
                    name = breed.name,
                    dogBreed = breed,
                    catBreed = None
                )
                print(f"Added {breed} to the Breed model")
        
        for breed in cat_breeds:
            exist = Breed.objects.filter(catBreed=breed).exists()
            if not exist:
                Breed.objects.create(
                    name = breed.name,
                    dogBreed = None,
                    catBreed = breed
                )
                print(f"Added {breed} to the Breed model")
        
                
                
