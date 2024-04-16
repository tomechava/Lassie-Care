from django.contrib import admin
from .models import OwnerProfile, PetProfile, DogBreed

# Register your models here.
admin.site.register(OwnerProfile)
admin.site.register(PetProfile)
admin.site.register(DogBreed)