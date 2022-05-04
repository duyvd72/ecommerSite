from pyexpat import model
from django.db import models

class Category(models.Model):
    name = models.CharField(max_length=255, unique=True)
    slug = models.SlugField(max_length=255, unique=True)

    def __str__(self):
        return self.name

class Author(models.Model):
    fullName = models.CharField(max_length=255)
    yearOfBirth = models.CharField(max_length=255)
    homeTown = models.CharField(max_length=255)

    def __str__(self):
        return self.fullName

class Publisher(models.Model):
    name = models.CharField(max_length=255)
    address = models.CharField(max_length=255)
    phone = models.CharField(max_length=255)
    email = models.CharField(max_length=255)
    def __str__(self):
        return self.name

class Book(models.Model):
    title = models.CharField(max_length=255)
    isbnCode=  models.CharField(max_length=255)
    publishYear=  models.CharField(max_length=255)
    pageNum= models.IntegerField()
    importPrice= models.FloatField()
    PublisherID = models.ForeignKey(Publisher, on_delete=models.CASCADE, null=True)
# verbose là gì 
    class Meta:
        verbose_name = 'Books'
        verbose_name_plural = 'Books'

    def __str__(self):
        return self.title

class Book_Author(models.Model):
        role=models.CharField(max_length=255)
        BookID= models.ForeignKey(Book,on_delete=models.CASCADE)
        AuthorID=models.ForeignKey(Author,on_delete=models.CASCADE)



