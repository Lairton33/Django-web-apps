from django.db import models

# Create your models here.

class Product(models.Model):
    image_path = models.CharField(max_length=255, blank=True, null=True)
    name = models.CharField(max_length=100, blank=False)
    price = models.FloatField(blank=False)
    description = models.TextField(max_length=255, blank=False)
