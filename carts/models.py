from django.db import models
from store.models import Item


class Cart(models.Model):
    cart_id = models.CharField(max_length=255, blank=True)
    date_add = models.DateField(auto_now_add=True)

    def __str__(self):
        return self.cart_id

class CartItem(models.Model):
    cart = models.ForeignKey(Cart, on_delete=models.CASCADE)
    item = models.ForeignKey(Item, on_delete=models.CASCADE)
    quantity = models.IntegerField()
    is_active = models.BooleanField(default=True)

    def sub_total(self):
        return self.item.public_price * self.quantity

    def __str__(self):
        return self.item