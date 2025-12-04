from rest_framework import serializers
from .models import ProductModel

class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProductModel
        fields = ['id', 'name', 'category', 'description', 'stock_quantity', 'price', 'image_url', 'in_stock']

