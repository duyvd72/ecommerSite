from statistics import mode
from django.db import models
class Customer (models.Model):
        idCard= models.CharField(max_length=255)
        mail=models.CharField(max_length=255)
        phone=models.CharField(max_length=255)
        class Meta:
                verbose_name = 'Customer'
                verbose_name_plural = 'Customer'
class Fullname (models.Model):
        FirstName= models.CharField(max_length=255)
        LastName=models.CharField(max_length=255)
        customerID=models.ForeignKey(Customer,on_delete=models.CASCADE)
        
class customerMember(models.Model):
        point=models.IntegerField()
        level=models.CharField(max_length=255)
        customerID=models.ForeignKey(Customer,on_delete=models.CASCADE)

class Address(models.Model):
        nohouse=models.CharField(max_length=255)
        street=models.CharField(max_length=255)
        district=models.CharField(max_length=255)
        city=models.CharField(max_length=255)
        nationality=models.CharField(max_length=255)
        customerID=models.ForeignKey(Customer,on_delete=models.CASCADE)
class Account(models.Model):
        username= models.CharField(max_length=255)
        password=models.CharField(max_length=255)
        customerID=models.ForeignKey(Customer,on_delete=models.CASCADE)
        
class Comment (models.Model):
        cmtbody= models.CharField(max_length=255)
        CreateDate=models.DateTimeField()
        rating=models.FloatField()
        customerID=models.ForeignKey(Customer,on_delete=models.CASCADE)
        
