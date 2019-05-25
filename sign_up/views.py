from django.contrib.auth import authenticate, login
from django.shortcuts import render, redirect
from .forms import *
from menu.views import *


# Create your views here.
def it_pizza_sign_up(request):
    user_form = UserForm(request.POST)
    profile_form = ProfileForm(request.POST)
    if request.method == 'POST':

        if user_form.is_valid() and profile_form.is_valid():
            new_user = User.objects.create_user(**user_form.cleaned_data)
            new_profile_form = profile_form.save(commit=False)
            new_profile_form.user = new_user
            new_profile_form.save()
            user = authenticate(
                username=user_form.cleaned_data['username'],
                password=user_form.cleaned_data['password']
            )
            login(request, user)
            return redirect(it_pizza_pizzas)

    return render(request, 'sign_up.html',
                  {'profile_form': profile_form,
                   'user': user_form})
