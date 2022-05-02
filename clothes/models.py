from django.db import models

class Style(models.Model):
    name = models.CharField(max_length=255, unique=True)
    slug = models.SlugField(max_length=255, unique=True)

    def __str__(self):
        return self.name


class Manufacturer(models.Model):
    name = models.CharField(max_length=255)
    mail = models.CharField(max_length=255)
    phone = models.CharField(max_length=255)
    origin = models.CharField(max_length=255)

    def __str__(self):
        return self.name

class Clothes(models.Model):
    name = models.CharField(max_length=255, unique=True)
    fabric = models.CharField(max_length=255)
    import_price = models.FloatField()
    style = models.ForeignKey(Style, on_delete=models.CASCADE, null=True)
    manufacturer = models.ForeignKey(Manufacturer, on_delete=models.CASCADE)

    class Meta:
        verbose_name = 'Clothes'
        verbose_name_plural = 'Clothes'

    def __str__(self):
        return self.name




