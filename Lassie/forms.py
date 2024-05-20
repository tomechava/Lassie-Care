from django import forms
from django.forms import ModelForm
from .models import DailyTasks

class DailyTaskForm(ModelForm):
    class Meta:
        model = DailyTasks
        fields=('walks' , 'food')
