from django.db import models

# Create your models here.

class Products(models.Model):

    name = models.CharField(max_length=100)
    image = models.ImageField(upload_to='photos/')
    price = models.IntegerField()
    description = models.TextField(default="")

    def __str__(self):
        return f'Product: {self.name} | Price: {self.price}'
    

