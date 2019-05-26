from django.shortcuts import render
from .models import *
from .forms import *
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required


# Create your views here.

def home(request):
    return render(request, 'home.html')


def it_pizza_pizzas(request):
    pizzas = Pizzas.objects.all()
    order = OrderPizzasForm(request.POST)
    if request.method == 'POST':
        if order.is_valid():
            orders = order.save(commit=False)
            orders.save()
            return redirect(it_pizza_pizzas)
    context = {'pizzas': pizzas,
               'order': order}
    return render(request, 'pizzas.html', context)


def it_pizza_deserts(request):
    deserts = Deserts.objects.all()
    order = OrderDesertsForm(request.POST)
    if request.method == 'POST':
        if order.is_valid():
            orders = order.save(commit=False)
            orders.save()
            return redirect(it_pizza_pizzas)
    context = {'deserts': deserts,
               'order': order}
    return render(request, 'deserts.html', context)


def it_pizza_drinks(request):
    drinkss = Drinks.objects.all()
    order = OrderDrinksForm(request.POST)
    if request.method == 'POST':
        if order.is_valid():
            orders = order.save(commit=False)
            orders.save()
            return redirect(it_pizza_pizzas)
    context = {'drinkss': drinkss,
               'order': order}
    return render(request, 'drinks.html', context)


def it_pizza_create_pizza(request):
    create_pizza = CreatePizzasForm()
    if request.method == 'POST':
        create_pizza = CreatePizzasForm(request.POST)
        if create_pizza.is_valid():
            pizza = create_pizza.save(commit=False)
            pizza.save()
            return redirect(it_pizza_pizzas)

    return render(request, 'create_pizza.html',
                  {'create': create_pizza})
