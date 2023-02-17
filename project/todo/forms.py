from django import forms
from django.forms import TextInput,ModelForm
from .models import Todo

class TodoForm(ModelForm):
    class Meta:
        model = Todo
        fields = ['item']
        widgets = {'item': TextInput(attrs={'class': 'form-control', 'placeholder':'add a list ....'})}