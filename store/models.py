from django.db import models

# Create your models here.
class Item(models.Model):
    slug = models.CharField(max_length=255, unique=True)
    images = models.ImageField(upload_to='photo/products')
    stock = models.IntegerField()
    description = models.TextField(max_length=500, blank=True)
    public_price = models.FloatField()
    is_available = models.BooleanField(default=True)


