from django.db import models
from store.models import Item
from customer.models import Customer
from order.models import Order,Payment


class Cart(models.Model):
    cart_id = models.CharField(max_length=255, blank=True)
    date_add = models.DateField(auto_now_add=True)
    CustomerID= models.ForeignKey(Customer,on_delete=models.CASCADE)
    PaymentID= models.ForeignKey(Payment,on_delete=models.CASCADE)
    OrderID= models.ForeignKey(Order,on_delete=models.CASCADE)
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