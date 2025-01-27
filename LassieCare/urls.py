"""
URL configuration for LassieCare project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from django.contrib.auth.views import LoginView
from Lassie import views as LassieViews
from Chatbot import views as ChatbotViews
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('chatbot/', include('django.contrib.auth.urls')),  # include the auth urls for login, logout, etc.
    path('admin/', admin.site.urls),    #Admin page
    path('', LassieViews.welcome, name='welcome'),     #Welcome page
    path('home', LassieViews.home, name='home'),     #Home page
    path('register', LassieViews.register, name='register'),    #Register page
    path('pets', LassieViews.pets, name='pets'),       #List of pets
    path('pet/new', LassieViews.pet_new, name='pet_new'),      #Register a new pet
    path('pet/new/<str:pet_type>', LassieViews.pet_add, name='pet_add'),      #Register a new pet (with type
    path('pet/<int:pet_id>', LassieViews.pet, name='pet'),      #View a pet
    path('pet/<int:pet_id>/edit', LassieViews.pet_edit, name='pet_edit'),       #Edit a pet
    path('pet/<int:pet_id>/delete', LassieViews.pet_delete, name='pet_delete'),      #Delete a pet
    path('profile/', LassieViews.profile, name='profile'),      #View user profile
    path('profile/edit', LassieViews.profile_edit, name='profile_edit'),      #Edit user profile
    path('login', LoginView.as_view(template_name='login.html'), name="login"),     #Login page
    path('log_out', LassieViews.log_out, name="logout"),    #Logout page   
    path('asklassiechat', ChatbotViews.asklassiechat.as_view(), name='asklassiechat'),    #Chatbot page

] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

