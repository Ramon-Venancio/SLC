from django.db import models

# Create your models here.

class Product(models.Model):
    name = models.CharField(max_length=64)

    def __str__(self):
        return self.name

class Category(models.Model):
    name = models.CharField(max_length=64)
    prudoto = models.ManyToManyField(Product, related_name="categorias")

    def __str__(self):
        return self.name