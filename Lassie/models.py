from django.db import models

# Create your models here.
class OwnerProfile(models.Model):
    name = models.CharField(max_length=200)
    
    def __str__(self):
        return self.name

class PetProfile(models.Model):
    ownerprofile = models.ForeignKey(OwnerProfile, on_delete=models.CASCADE)
    namePet = models.CharField(max_length=300)
    
    
    def __str__(self):
        return self.namePet