from django.shortcuts import render, reverse
from django.contrib.auth.decorators import login_required
from .models import ChatBot
from django.http import HttpResponseRedirect, JsonResponse, HttpResponse
import google.generativeai as genai
import os
from dotenv import load_dotenv, find_dotenv
from django.views.decorators.csrf import csrf_exempt
from django.utils.decorators import method_decorator
from django.views import View
import markdown

# Create your views here.
# add here to your generated API key
_ = load_dotenv('api_keys.env')
genai.configure(api_key=os.environ.get('gemini_api_key'))

@method_decorator(csrf_exempt, name='dispatch')
class asklassiechat(View):
    def post(self, request):
        text = request.POST.get("message")
        model = genai.GenerativeModel("gemini-pro")
        response = model.generate_content(text)
        lassie_response = markdown.markdown(response.text)
        return JsonResponse({'message': lassie_response})
    
    def get(self, request):
        return render(request, 'chat_bot.html')

        