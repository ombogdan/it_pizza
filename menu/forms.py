from django import forms
from .models import *
from django.contrib.auth.models import User


class CreatePizzasForm(forms.ModelForm):
    class Meta:
        model = CreatePizzas
        exclude = ('users', )