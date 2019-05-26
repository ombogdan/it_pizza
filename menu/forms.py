from django import forms
from .models import *
from django.contrib.auth.models import User


class CreatePizzasForm(forms.ModelForm):
    class Meta:
        model = CreatePizzas
        exclude = ('users',)


class OrderPizzasForm(forms.ModelForm):
    class Meta:
        model = OrderPizzas
        fields = ('user', 'phone_number')


class OrderDrinksForm(forms.ModelForm):
    class Meta:
        model = OrderDrinks
        fields = ('user', 'phone_number')


class OrderDesertsForm(forms.ModelForm):
    class Meta:
        model = OrderDeserts
        fields = ('user', 'phone_number')
