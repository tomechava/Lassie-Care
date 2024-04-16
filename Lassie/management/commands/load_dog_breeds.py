# commands/load_dog_breeds.py
from django.core.management.base import BaseCommand
from Lassie.models import DogBreed  
import os
import json

class Command(BaseCommand):
    help = 'Load dog breeds from dog_breeds.json into the DogBreed model'

    def handle(self, *args, **kwargs):
        # Construct the full path to the JSON file
        json_file_path = 'C:/Users/Usuario/Desktop/P1/LassieCare/Dog_Breeds_List.json'  # Ajusta la ruta al archivo JSON de razas de perro
        
        # Load data from the JSON file
        with open(json_file_path, 'r') as file:
            dog_breeds = json.load(file)
        
        # Add dog breeds to the database
        for breed in dog_breeds:
            exist = DogBreed.objects.filter(name=breed['name']).exists()
            if not exist:
                DogBreed.objects.create(
                    name=breed['name'],
                    size=breed['size'],
                    life_expectancy=breed['life_expectancy'],
                    origin=breed['origin'],
                    #personality=breed['personality']
                )
                
                
