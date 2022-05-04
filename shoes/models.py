from django.db import models

class ShoeCategory(models.Model):
    name = models.CharField(max_length=255, unique=True)
    slug = models.SlugField(max_length=255, unique=True)

    def __str__(self):
        return self.name


class ShoeBrand(models.Model):
    name = models.CharField(max_length=255)
    mail = models.CharField(max_length=255)
    phone = models.CharField(max_length=255)
    origin = models.CharField(max_length=255)

    def __str__(self):
        return self.name

class Shoes(models.Model):
    name = models.CharField(max_length=255, unique=True)
    fabric = models.CharField(max_length=255)
    import_price = models.FloatField()
    ShoeBrandID= models.ForeignKey(ShoeBrand, on_delete=models.CASCADE, null=True)
    ShoeCategoryID = models.ForeignKey(ShoeCategory, on_delete=models.CASCADE)

    class Meta:
        verbose_name = 'Shoes'
        verbose_name_plural = 'Shoes'

    def __str__(self):
        return self.name




