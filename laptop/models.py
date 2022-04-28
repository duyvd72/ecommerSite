from django.db import models
from store.models import Item

# Create your models here.
class Type(models.Model):
    name = models.CharField(max_length=255, unique=True)
    slug = models.SlugField(max_length=255, unique=True)

    def __str__(self):
        return self.name


class Producer(models.Model):
    name = models.CharField(max_length=255, unique=True)
    origin = models.CharField(max_length=255)

    def __str__(self):
        return self.name


class Laptop(models.Model):
    name = models.CharField(max_length=255, unique=True)
    code = models.CharField(max_length=255, unique=True)
    import_price = models.FloatField()
    type = models.ForeignKey(Type, on_delete=models.CASCADE, null=True)
    producer = models.ForeignKey(Producer, on_delete=models.CASCADE, null=True)

    def __str__(self):
        return self.name


class LaptopItem(Item):
    version = models.CharField(max_length=255)
    cpu = models.CharField(max_length=255)
    ram = models.CharField(max_length=255)
    color = models.CharField(max_length=255)
    laptop = models.ForeignKey(Laptop, on_delete=models.CASCADE)



