from django.db import models
from django.contrib.auth.models import User
from phonenumber_field.modelfields import PhoneNumberField
from django.utils import timezone
# Create your models here.
class OwnerProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, null=False, blank=False)  # Connect to Django's User model
    firstName = models.CharField(max_length=200)
    lastName = models.CharField(max_length=200)
    address = models.CharField(max_length=200)
    phone_number = PhoneNumberField(null=False, blank=False, unique=True, default=' ')
    GENDER_CHOICES = [
        ('M', 'Male'),
        ('F', 'Female'),
        ('O', 'Other'),
    ]
    gender = models.CharField(max_length=1, choices=GENDER_CHOICES)
    birthDate = models.DateField()
    email = models.EmailField()
    
    def __str__(self):
        return f"{self.user.username}'s Owner Profile"
    
class DogBreed(models.Model):
    name = models.CharField(max_length=100)
    size = models.CharField(max_length=50)
    life_expectancy = models.CharField(max_length=50)
    origin = models.CharField(max_length=100)
    personality = models.JSONField(default=dict)

    def __str__(self):
        return self.name

class CatBreed(models.Model):
    name = models.CharField(max_length=100)
    size = models.CharField(max_length=50)
    life_expectancy = models.CharField(max_length=50)
    origin = models.CharField(max_length=100)
    personality = models.JSONField(default=dict)

    def __str__(self):
        return self.name
    

class Breed(models.Model):
    name = models.CharField(max_length=100, default='Breed')
    dogBreed = models.ForeignKey(DogBreed, on_delete=models.CASCADE, null=True, blank=True)
    catBreed = models.ForeignKey(CatBreed, on_delete=models.CASCADE, null=True, blank=True)

def rename_image(instance, filename):
    #Get the extension
    extension = filename.split('.')[-1]
    
    #generate new filename
    new_filename = f"{instance.id}.{extension}"
    
    return f"pet_images/{new_filename}"

def rename_medical_history(instance, filename):
    #Get the extension
    extension = filename.split('.')[-1]
    
    #generate new filename
    new_filename = f"{instance.id}.{extension}"
    
    return f"medical_histories/{new_filename}"

class PetProfile(models.Model):
    ownerprofile = models.ForeignKey(OwnerProfile, on_delete=models.CASCADE)
    PET_TYPES = [
        ('D', 'Dog'),
        ('C', 'Cat'),
        ('O', 'Other'),
    ]
    petType = models.CharField(max_length=1, choices=PET_TYPES, default='D')
    petImage = models.ImageField(upload_to='pet_images', default='static/images/DOG_DEFAULT.png')
    namePet = models.CharField(max_length=300)
    weight= models.DecimalField(max_digits=10, decimal_places=2)
    breed = models.ForeignKey(Breed, on_delete=models.CASCADE, null=True, blank=True)
    age = models.CharField(max_length=3)
    SIZE_CHOICES = [
        ('S', 'Small'),
        ('M', 'Medium'),
        ('B', 'Big'),
    ]
    size = models.CharField(max_length=1, choices=SIZE_CHOICES)
    medicalHistory = models.FileField(upload_to='medical_histories', null=True, blank=True)
    allergies = models.TextField(null=True, blank=True)
    
    def __str__(self):
        return self.namePet
    

class DailyTasks(models.Model):
    ownerprofile = models.ForeignKey(OwnerProfile, on_delete=models.CASCADE)
    petprofile = models.ForeignKey(PetProfile, on_delete=models.CASCADE)
    walks = models.IntegerField(default=0)
    food = models.IntegerField(default=0)
    water = models.IntegerField(default=0)
    datetime = models.DateTimeField(default=timezone.now)
    
    def __str__(self):
        return f"{self.ownerprofile.user}'s task for {self.petprofile.namePet}"