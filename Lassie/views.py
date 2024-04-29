from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.auth.models import User
from django.shortcuts import redirect
from .models import OwnerProfile, PetProfile, DogBreed
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login as auth_login, logout
from datetime import datetime
from django.contrib import messages
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
def pet_add(request):
    if(request.method == 'POST'):
        pet_image = request.FILES.get('petImage')
        pet_name = request.POST.get('petName')
        pet_weight = request.POST.get('petWeight')
        pet_age = request.POST.get('petAge')
        pet_size = request.POST.get('selSize')
        pet_medical_history = request.FILES.get('medicalHistory')
        pet_breed_id = request.POST.get('petBreed')
        pet_breed = DogBreed.objects.get(id=pet_breed_id)
        
        # Create PetProfile instance and link it to the OwnerProfile
        pet = PetProfile.objects.create(
            ownerprofile=request.user.ownerprofile,
            petImage=pet_image,
            namePet=pet_name,
            weight=pet_weight,
            age=pet_age,
            size=pet_size,
            medicalHistory=pet_medical_history,
            breed=pet_breed
        )
        
        pet.save()
        
        return redirect('pets')
    
    breeds = DogBreed.objects.all()
    return render(request, 'pet_add.html', {'breeds': breeds})


@login_required
def pet_edit(request, pet_id):
    pet = PetProfile.objects.get(id=pet_id)
    return render(request, 'pet_edit.html', {'pet': pet})

@login_required
def pet_delete(request, pet_id):
    pet = PetProfile.objects.get(id=pet_id)
    pet.delete()
    return redirect('pets')

@login_required
def pet(request, pet_id):
    pet = PetProfile.objects.get(id=pet_id)
    return render(request, 'pet_view.html', {'pet': pet})

@login_required
def profile(request):
    # Retrieve the current user's profile
    user_profile = OwnerProfile.objects.get(user=request.user)
    return render(request, 'profile.html', {'user_profile': user_profile})

@login_required
def log_out(request):
    logout(request)
    return redirect('/')
