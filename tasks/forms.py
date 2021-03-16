from django import forms
from django.forms import ModelForm

from .models import *


class TaskForm(forms.ModelForm):

    class Meta:
        model = Task
        fields = '__all__'


class DetailTaskForm(forms.ModelForm):

    class Meta:
        model = Task
        fields = ['title','extra_info', 'category']

    title = forms.CharField()
    extra_info = forms.CharField()

    category = forms.ModelMultipleChoiceField(
        queryset=Category.objects.all(),
        widget=forms.CheckboxSelectMultiple()
    )
    
