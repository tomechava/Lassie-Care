from django.shortcuts import render, reverse
from django.contrib.auth.decorators import login_required
from .models import ChatBot
from django.http import HttpResponseRedirect, JsonResponse, HttpResponse
import google.generativeai as genai
import os
from dotenv import load_dotenv, find_dotenv

# Create your views here.
# add here to your generated API key
_ = load_dotenv('api_keys.env')
genai.configure(api_key=os.environ.get('gemini_api_key'))

#@login_required
def lassiechat(request):
    if request.method == "POST":
        text = request.POST.get("text")
        model = genai.GenerativeModel("gemini-pro")
        response = model.generate_content(text)
        return JsonResponse({"response": response})
    return HttpResponseRedirect(reverse("asklassiechat"))

def asklassiechat(request):
    if request.method == "POST":
        #text = request.POST.get("chat-input")
        model = genai.GenerativeModel("gemini-pro")
        #response = model.generate_content(text)
        return HttpResponse((model.generate_content(request.POST.get("chat-input"))).text)
    else:
        return render(request, 'chat_bot.html')

        