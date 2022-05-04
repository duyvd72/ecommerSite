from statistics import mode
from django.db import models
class Customer (models.Model):
        idCard= models.CharField()
        mail=models.CharField()
        phone=models.CharField()
        
class Fullname (models.Model):
        FirstName= models.CharField()
        LastName=models.CharField()
        customerID=models.ForeignKey(Customer,on_delete=models.CASCADE)
        
class customerMember(models.Model):
        point=models.IntegerField()
        level=models.CharField()
        customerID=models.ForeignKey(Customer,on_delete=models.CASCADE)

class Address(models.Model):
        nohouse=models.CharField()
        street=models.CharField()
        district=models.CharField()
        city=models.CharField()
        nationality=models.CharField()
        customerID=models.ForeignKey(Customer,on_delete=models.CASCADE)
class Account(models.Model):
        username= models.CharField()
        password=models.CharField()
        customerID=models.ForeignKey(Customer,on_delete=models.CASCADE)
        
class Comment (models.Model):
        cmtbody= models.CharField()
        CreateDate=models.DateTimeField()
        rating=models.FloatField()
        customerID=models.ForeignKey(Customer,on_delete=models.CASCADE)