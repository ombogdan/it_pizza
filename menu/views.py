from django.shortcuts import render
from .models import *
# Create your views here.

def home(request):
    return render(request, 'home.html')

def it_pizza_pizzas(request):
    pizzas = Pizzas.objects.all()
    context={'pizzas': pizzas}
    return render(request, 'pizzas.html', context)


def it_pizza_deserts(request):
    deserts = Deserts.objects.all()
    context={'deserts': deserts}
    return render(request, 'deserts.html', context)

def it_pizza_drinks(request):
    drinkss = Drinks.objects.all()
    context={'drinkss': drinkss}
    return render(request, 'drinks.html', context)
