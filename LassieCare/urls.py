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
urlpatterns = [
    path('chatbot/', include('django.contrib.auth.urls')),  # include the auth urls for login, logout, etc.
    path('admin/', admin.site.urls),
    path('', LassieViews.home),
    path('register', LassieViews.register),
    path('pet', LassieViews.pet),
    path('profile/', LassieViews.profile, name='profile'),
    path('login', LoginView.as_view(template_name='login.html'), name="login"),
    path('log_out', LassieViews.log_out, name="logout"),
    path('lassiechat', ChatbotViews.lassiechat, name='lassiechat'),
    path('asklassiechat', ChatbotViews.asklassiechat, name='asklassiechat'),
]

