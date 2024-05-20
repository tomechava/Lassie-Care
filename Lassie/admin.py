from django.contrib import admin
from .models import OwnerProfile, PetProfile, DogBreed, CatBreed, Breed, DailyTasks

# Register your models here.
admin.site.register(OwnerProfile)
admin.site.register(PetProfile)
admin.site.register(DogBreed)
admin.site.register(CatBreed)
admin.site.register(Breed)
admin.site.register(DailyTasks)