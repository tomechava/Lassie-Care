from django.db import models
from django.contrib.auth.models import User
from phonenumber_field.modelfields import PhoneNumberField

# Create your models here.
class OwnerProfile(models.Model):
    firstName = models.CharField(max_length=200)
    lastName = models.CharField(max_length=200)
    adress = models.CharField(max_length=200)
    phone_number = PhoneNumberField(null=False, blank=False, unique=True, default=' ')
    GENDER_CHOICES = [
        ('M', 'Male'),
        ('F', 'Female'),
        ('O', 'Other'),
    ]
    gender = models.CharField(max_length=1, choices=GENDER_CHOICES)
    birthDate = models.DateField()
    email = models.EmailField()
    username = models.CharField(max_length=150, unique=True)
    password= models.CharField(max_length=128)
    notificaciones = models.BooleanField(default=True)
    
    def __str__(self):
        return self.name

class PetProfile(models.Model):
    ownerprofile = models.ForeignKey(OwnerProfile, on_delete=models.CASCADE)
    namePet = models.CharField(max_length=300)
    Weight= models.DecimalField(max_digits=10, decimal_places=2)
    #breed
    age = models.IntegerField()
    SIZE_CHOICES = [
        ('S', 'Small'),
        ('M', 'Medieum'),
        ('B', 'Big'),
    ]
    size = models.CharField(max_length=1, choices=SIZE_CHOICES)
    files = models.FileField(upload_to='archivos/')
    
    def __str__(self):
        return self.namePet
    
    
class DogBreed(models.Model):
    name = models.CharField(max_length=100)
    size = models.CharField(max_length=50)
    life_expectancy = models.CharField(max_length=50)
    origin = models.CharField(max_length=100)
    personality = models.JSONField(default=dict)

    def __str__(self):
        return self.name