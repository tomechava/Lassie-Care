# commands/load_dog_breeds.py
from django.core.management.base import BaseCommand
from Lassie.models import CatBreed  
import os
import json

class Command(BaseCommand):
    help = 'Load dog breeds from dog_breeds.json into the DogBreed model'

    def handle(self, *args, **kwargs):
        # Construct the full path to the JSON file
        json_file_path = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'Cat_Breeds_List.json')
        
        # Load data from the JSON file
        with open(json_file_path, 'r') as file:
            cat_breeds = json.load(file)
        
        # Add dog breeds to the database
        for breed in cat_breeds:
            exist = CatBreed.objects.filter(name=breed['name']).exists()
            if not exist:
                CatBreed.objects.create(
                    name=breed['name'],
                    size=breed['size'],
                    life_expectancy=breed['life_expectancy'],
                    origin=breed['origin'],
                    personality=breed['personality']
                )
                
                
