from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.auth.models import User
from django.shortcuts import redirect
from .models import OwnerProfile
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
        
        # Redirect to a success page or perform other actions
        return redirect('login')
    else:
        # Render registration form
        return render(request, 'register.html')

@login_required
def pet_add(request):
    return render(request, 'pet_register.html')

@login_required
def profile(request):
    # Retrieve the current user's profile
    user_profile = OwnerProfile.objects.get(user=request.user)
    return render(request, 'profile.html', {'user_profile': user_profile})

@login_required
def log_out(request):
    logout(request)
    return redirect('/')
