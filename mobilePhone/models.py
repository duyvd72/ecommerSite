from django.db import models

# Create your models here.
class Design(models.Model):
    name = models.CharField(max_length=255, unique=True)
    slug = models.SlugField(max_length=255, unique=True)

    def __str__(self):
        return self.name


class MobilePhoneBrand(models.Model):
    name = models.CharField(max_length=255, unique=True)
    mail = models.EmailField(max_length=255)
    Phone = models.CharField(max_length=255)
    origin = models.CharField(max_length=255)

    def __str__(self):
        return self.name


class MobilePhone(models.Model):
    name = models.CharField(max_length=255, unique=True)
    width = models.CharField(max_length=255)
    import_price = models.FloatField()
    design = models.ForeignKey(Design, on_delete=models.CASCADE, null=True)
    mobile_phone_brand = models.ForeignKey(MobilePhoneBrand, on_delete=models.CASCADE)

    def __str__(self):
        return self.name



