from rest_framework import serializers
from .models import CategoryModel, ProductModel



class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = CategoryModel
        fields = ['id', 'name', 'description', 'image_url']

class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProductModel
        fields = ['id', 'name', 'category', 'customer', 'description', 'stock_quantity', 'image_url', 'created', 'updated', 'in_stock']

