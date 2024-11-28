from django.db import models

# Create your models here.
class Product (models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField(max_length=2083)
    price = models.FloatField()
   
    def __str__(self):
        return self.product_name