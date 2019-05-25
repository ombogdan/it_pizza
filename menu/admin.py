from django.contrib import admin
from .models import *
# Register your models here.
admin.site.register(Pizzas)
admin.site.register(Drinks)
admin.site.register(Deserts)
admin.site.register(CreatePizzas)