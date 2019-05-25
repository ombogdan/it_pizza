from django.db import models
from sign_up.models import *

# Create your models here.
class Pizzas(models.Model):
    title = models.TextField(max_length=20)
    description = models.TextField(max_length=500)
    price = models.DecimalField(max_digits=50, decimal_places=3, default=0.0)
    mass = models.IntegerField(default=0.0)
    photo = models.ImageField(upload_to='images/',default='DEFAULT VALUE', blank=False)

    def __str__(self):
        return self.title


class Drinks(models.Model):
    title = models.TextField(max_length=20)
    price = models.DecimalField(max_digits=50, decimal_places=2, default=0.0)
    ml = models.IntegerField(default=0.0)
    photo = models.ImageField(upload_to='templates/img/drinks_images/',default='DEFAULT VALUE', blank=False)

    def __str__(self):
        return self.title


class Deserts(models.Model):
    title = models.TextField(max_length=20)
    price = models.DecimalField(max_digits=50, decimal_places=2, default=0.0)
    mass = models.IntegerField(default=0.0)
    photo = models.ImageField(upload_to='templates/img/deserts_images/', default='DEFAULT VALUE', blank=False)

    def __str__(self):
        return self.title


class CreatePizzas(models.Model):
    title = models.TextField(max_length=20)
    cheeze = models.BooleanField(name='Моцарелла', default=False)
    cheeze2 = models.BooleanField(name='Подвійний сир', default=False)
    meet = models.BooleanField(name='Бекон ', default=False)
    meet1 = models.BooleanField(name='Курка ', default=False)
    meet2 = models.BooleanField(name='Шинка', default=False)
    green = models.BooleanField(name='Зелень', default=False)
    pineapple = models.BooleanField(name='Ананас', default=False)
    olives = models.BooleanField(name='Оливки ', default=False)
    tomatoes = models.BooleanField(name='Помідори', default=False)
    pickled_cucumbers = models.BooleanField(name='Мариновані огірки', default=False)
    pepper = models.BooleanField(name='Перець', default=False)
    champignons = models.BooleanField(name='Шампіньйони', default=False)
    maize = models.BooleanField(name='Кукурудза', default=False)

    def __str__(self):
        return self.title
