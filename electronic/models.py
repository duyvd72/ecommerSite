import mailbox
from django.db import models

# Create your models here.
class Kind(models.Model):
    name = models.CharField(max_length=255, unique=True)
    slug = models.SlugField(max_length=255, unique=True)

    def __str__(self):
        return self.name


class ElectronicBrand(models.Model):
    name = models.CharField(max_length=255, unique=True)
    mail=models.CharField(max_length=255, unique=True)
    phone=models.CharField(max_length=255, unique=True)
    origin = models.CharField(max_length=255)

    def __str__(self):
        return self.name


class Electronic(models.Model):
    name = models.CharField(max_length=255, unique=True)
    publishYear = models.IntegerField()
    code= models.CharField(max_length=255, unique=True)
    ImportPrice= models.FloatField()
    kindID = models.ForeignKey(Kind, on_delete=models.CASCADE, null=True)
    ElectronicBrandID = models.ForeignKey(ElectronicBrand, on_delete=models.CASCADE)

    def __str__(self):
        return self.name



