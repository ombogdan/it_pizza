from django.db import models
from menu.models import *
# Create your models here.
class CartItem(models.Model):
    pizza = models.ForeignKey(Pizzas, on_delete=models.CASCADE)
    qty = models.PositiveIntegerField(default=1)
    item_total = models.DecimalField(max_digits=9, decimal_places=2, default=0.0)

    def __unicode__(self):
        return "Card item for product {0}".format(str(self.pizza.title))


class Cart(models.Model):
    items = models.ManyToManyField(CartItem, blank=True)
    card_total = models.DecimalField(max_digits=9, decimal_places=2, default=0.0)

    def __str__(self):
        return str(self.id)
