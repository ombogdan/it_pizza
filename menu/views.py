from django.shortcuts import render

# Create your views here.

def home(request):
    return render(request, 'home.html')

def it_pizza_pizzas(request):
    pass
