from django.db import models
from customer.models import Customer

class Payment(models.Model):
        Method=models.CharField(max_length=255)
        status=models.CharField(max_length=255)
        createAt=models.DateTimeField()
        def __str__(self):
                return(self.Method)
class Shipment(models.Model):
        shipfee=models.FloatField()
        shipaddress=models.CharField(max_length=255)
        shipphone=models.CharField(max_length=255)
        shipname=models.CharField(max_length=255)
        PaymentID=models.ForeignKey(Payment, on_delete=models.CASCADE)
class Order(models.Model):
        orderNumber=models.CharField(max_length=255)
        status=models.CharField(max_length=255)
        createAt=models.DateTimeField()
        isOrder=models.BooleanField()
        PaymentID=models.ForeignKey(Payment, on_delete=models.CASCADE)
        ShipmentID=models.ForeignKey(Shipment, on_delete=models.CASCADE)
        CustomerID=models.ForeignKey(Customer, on_delete=models.CASCADE)
        def __str__(self):
                return(self.orderNumber)
        
