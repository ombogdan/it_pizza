from django.db import models


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
    photo = models.ImageField(upload_to='images/',default='DEFAULT VALUE', blank=False)

    def __str__(self):
        return self.title


class Deserts(models.Model):
    title = models.TextField(max_length=20)
    price = models.DecimalField(max_digits=50, decimal_places=2, default=0.0)
    mass = models.IntegerField(default=0.0)
    photo = models.ImageField(upload_to='images/', default='DEFAULT VALUE', blank=False)

    def __str__(self):
        return self.title
