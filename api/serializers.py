from rest_framework import serializers
from .models import ProductModel
from .models import CategoryModel


class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProductModel
        fields = ['id', 'name', 'description', 'stock_quantity', 'price', 'image_url', 'in_stock']

class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = CategoryModel
        fields = ['id', 'name', 'description', 'image_url']
    
