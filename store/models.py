from django.db import models
from django.urls import reverse

from clothes.models import Clothes
from laptop.models import Laptop
from mobilePhone.models import MobilePhone


class ItemType(models.Model):
    name = models.CharField(max_length=255, unique=True)
    slug = models.SlugField(max_length=255, unique=True)

    def get_url(self):
        return reverse('items_by_category', args=[self.slug])

    def __str__(self):
        return self.name


class Item(models.Model):
    item_type = models.ForeignKey(ItemType, on_delete=models.CASCADE)
    item_name = models.CharField(max_length=255, unique=True, null=True)
    slug = models.SlugField(max_length=255, unique=True, null=True)
    images = models.ImageField(upload_to='photos/products')
    stock = models.IntegerField()
    description = models.TextField(max_length=500, blank=True)
    public_price = models.FloatField()
    is_available = models.BooleanField(default=True)

    def get_url(self):
        return reverse('item_detail', args=[self.item_type.slug, self.slug])


class LaptopItem(Item):
    version = models.CharField(max_length=255)
    cpu = models.CharField(max_length=255)
    ram = models.CharField(max_length=255)
    color = models.CharField(max_length=255)
    laptop = models.ForeignKey(Laptop, on_delete=models.CASCADE)


class ClothesItem(Item):
    size = models.CharField(max_length=255)
    color = models.CharField(max_length=255)
    clothes = models.ForeignKey(Clothes, on_delete=models.CASCADE)


class MobilePhoneItem(Item):
    chip = models.CharField(max_length=255)
    ram = models.CharField(max_length=255)
    internal_memory = models.CharField(max_length=255, null=True)
    color = models.CharField(max_length=255)
    mobile_phone = models.ForeignKey(MobilePhone, on_delete=models.CASCADE)


