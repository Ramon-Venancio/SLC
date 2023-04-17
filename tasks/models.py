from django.db import models

# Create your models here.

class Product(models.Model):
    name = models.CharField(max_length=64)
    quantidade = models.IntegerField(default=1)

    def __str__(self):
        return self.name

class Category(models.Model):
    name = models.CharField(max_length=64)
    produtos = models.ManyToManyField(Product, blank=True, related_name="categorias")

    def __str__(self):
        return self.name