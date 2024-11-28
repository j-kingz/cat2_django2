from django.db import models

# Create your models here.
class Product (models.Model):
    p_name = models.CharField(max_length=55)
    p_description = models.CharField(max_length=120)
    price = models.IntegerField()
   
