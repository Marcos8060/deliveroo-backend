from django.db import models

# Create your models here.

class Product(models.Model):
    name = models.CharField(max_length=30)
    price = models.CharField(max_length=30)
    image = models.ImageField(upload_to='images') # image
    description = models.TextField(max_length=240)

    def __str__(self):
        return self.name

