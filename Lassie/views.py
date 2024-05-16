from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.auth.models import User
from django.shortcuts import redirect
from .models import OwnerProfile, PetProfile, DogBreed, CatBreed, Breed
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login as auth_login, logout
from datetime import datetime
from django.contrib import messages
from django.templatetags.static import static
# Create your views here.

def home(request):
    return render(request, 'home.html')

def register(request):
    if request.method == 'POST':
        
        # Extract form data
        username = request.POST.get('txtUsername')
        email = request.POST.get('txtEmail')
        password = request.POST.get('txtPassword')
        
        first_name = request.POST.get('txtFirstName')
        last_name = request.POST.get('txtLastName')
        address = request.POST.get('txtAddress')
        phone_number = request.POST.get('txtPhone')
        gender = request.POST.get('selGender')
        
        birthDate_str = request.POST.get('txtBirthDate')
        birthDate = datetime.strptime(birthDate_str, '%Y-%m-%d').date()
        
        # Create User instance
        user = User.objects.create_user(username=username, email=email, password=password)
        user.save()
        
        # Create OwnerProfile instance and link it to the User
        owner_profile = OwnerProfile.objects.create(
            user=user,
            firstName=first_name,
            lastName=last_name,
            address=address,
            phone_number=phone_number,
            gender=gender,
            birthDate=birthDate,
            
        )
        
        owner_profile.save()
        
        # Redirect to a success page or perform other actions
        return redirect('login')
    else:
        # Render registration form
        return render(request, 'register.html')

@login_required
def pets(request):
    pets = PetProfile.objects.filter(ownerprofile=request.user.ownerprofile)    #######
    return render(request, 'pets.html', {'pets': pets})

@login_required
def pet_new(request):
    if request.method == 'POST':
        pet_type = request.POST.get('petType')
        return redirect('pet_add', pet_type=pet_type)
    else:
        return render(request, 'pet_new.html')

@login_required
def pet_add(request, pet_type):
    if(request.method == 'POST'):
        type = pet_type
        if type == 'C':
            default_image = '/static/images/CAT_DEFAULT.png'
        else:
            default_image = '/static/images/DOG_DEFAULT.png'
        pet_image = request.FILES.get('petImage', default_image)
        pet_name = request.POST.get('petName')
        pet_weight = request.POST.get('petWeight')
        pet_age = request.POST.get('petAge')
        pet_size = request.POST.get('selSize')
        pet_medical_history = request.FILES.get('medicalHistory')
        pet_allergies = request.POST.get('petAllergies')
        
        pet_breed_id = request.POST.get('petBreed')

        if type == 'D':
            pet_breed = Breed.objects.get(dogBreed=pet_breed_id)
        elif type == 'C':
            pet_breed = Breed.objects.get(catBreed=pet_breed_id)
        else:
            pet_breed = None
        
        
        # Create PetProfile instance and link it to the OwnerProfile
        pet = PetProfile.objects.create(
            petType=type,
            ownerprofile=request.user.ownerprofile,
            petImage=pet_image,
            namePet=pet_name,
            weight=pet_weight,
            age=pet_age,
            size=pet_size,
            medicalHistory=pet_medical_history,
            breed=pet_breed,
            allergies=pet_allergies
            
        )
        
        pet.save()
        
        return redirect('pets')
    
    if pet_type == 'D':
        breeds = DogBreed.objects.all()
        petType='Dog'
    elif pet_type == 'C':
        petType='Cat'
        breeds = CatBreed.objects.all()
    else:
        petType=''
        breeds = None
        
    
    return render(request, 'pet_add.html', {'breeds': breeds, 'petType': petType})



@login_required
def pet_edit(request, pet_id):
    if(request.method == 'POST'):
        pet = PetProfile.objects.get(id=pet_id)
        if request.FILES.get('petImage'):
            pet.petImage = request.FILES.get('petImage')
        
        pet.namePet = request.POST.get('petName')
        pet.weight = request.POST.get('petWeight')
        pet.age = request.POST.get('petAge')
        pet.size = request.POST.get('selSize')
        pet.allergies = request.POST.get('petAllergies')
        if request.FILES.get('medicalHistory'):
            pet.medicalHistory = request.FILES.get('medicalHistory')
            
        pet_breed_id = request.POST.get('petBreed')
        pet_breed = DogBreed.objects.get(id=pet_breed_id)
        pet.breed = pet_breed
        
        pet.save()
        
        return redirect('pets')
    
    pet = PetProfile.objects.get(id=pet_id)
    #Breeds
    if pet.petType == 'D':
        breeds = DogBreed.objects.all()
    elif pet.petType == 'C':
        breeds = CatBreed.objects.all()
    else:
        breeds = None
    #Image
    if pet.petImage == '/static/images/DOG_DEFAULT.png' or pet.petImage == '/static/images/CAT_DEFAULT.png':
        pet_image = pet.petImage
    else:
        pet_image = pet.petImage.url
        
    return render(request, 'pet_edit.html', {'pet': pet, 'breeds': breeds, 'pet_image': pet_image})

@login_required
def pet_delete(request, pet_id):
    pet = PetProfile.objects.get(id=pet_id)
    pet.delete()
    return redirect('pets')

@login_required
def pet(request, pet_id):
    pet = PetProfile.objects.get(id=pet_id)
    if pet.petImage == '/static/images/DOG_DEFAULT.png' or pet.petImage == '/static/images/CAT_DEFAULT.png':
        pet_image = pet.petImage
    else:
        pet_image = pet.petImage.url
    return render(request, 'pet_view.html', {'pet': pet, 'pet_image': pet_image})

@login_required
def profile(request):
    # Retrieve the current user's profile
    user_profile = OwnerProfile.objects.get(user=request.user)
    return render(request, 'profile.html', {'user_profile': user_profile})

@login_required
def log_out(request):
    logout(request)
    return redirect('/')
