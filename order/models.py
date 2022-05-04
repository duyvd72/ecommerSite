from django.db import models
from customer.models import Customer

class Payment(models.Model):
        Method=models.CharField()
        status=models.CharField()
        createAt=models.DateTimeField()
class Shipment(models.Model):
        shipfee=models.FloatField()
        shipaddress=models.CharField()
        shipphone=models.CharField()
        shipname=models.CharField()
        PaymentID=models.ForeignKey(Payment, on_delete=models.CASCADE)
class Order(models.Model):
        orderNumber=models.CharField()
        status=models.CharField()
        createAt=models.DateTimeField()
        isOrder=models.BooleanField()
        PaymentID=models.ForeignKey(Payment, on_delete=models.CASCADE)
        ShipmentID=models.ForeignKey(Shipment, on_delete=models.CASCADE)
        CustomerID=models.ForeignKey(Customer, on_delete=models.CASCADE)
        
