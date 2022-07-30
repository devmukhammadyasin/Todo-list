from django import forms
from django.forms import ModelForm

from .models import Task

class TaskForm(forms.ModelForm):
    title = forms.CharField(widget=forms.TextInput(attrs={'placeholder':'Add new task name'}))
    hour = forms.DateTimeField(widget=forms.TextInput(attrs={"placeholder":"Add new task time, example - '2022-07-30 07:00:00' "}))

    class Meta:
        model = Task
        fields = '__all__'