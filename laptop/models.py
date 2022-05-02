from django.db import models

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
    producer = models.ForeignKey(Producer, on_delete=models.CASCADE)

    def __str__(self):
        return self.name



