from django.db import models
from django.conf import settings

# Create your models here.

#This class creates a table and fields for Categories of Products in a database
class CategoryModel(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    image_url = models.ImageField(upload_to='categories/')

    def __str__(self):
        return self.name


#This class creates a table and fields for  Products in a database
class ProductModel(models.Model):
    name = models.CharField(max_length=100)
    category = models.ForeignKey(CategoryModel, related_name='category', on_delete=models.CASCADE)
    description = models.TextField()
    price = models.DecimalField(max_digits=10, decimal_places=2, default=0)
    stock_quantity = models.PositiveIntegerField()
    image_url = models.ImageField(upload_to='products/')
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    in_stock = models.BooleanField(default=True)


    def __str__(self):
        return self.name
    
    