from rest_framework import serializers
from .models import ProductModel
from .models import CategoryModel

# This serializes fields in the Product Table that will be served in JSON when endpoint is reached 
class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProductModel
        fields = ['id', 'name', 'description', 'stock_quantity', 'price', 'image_url', 'in_stock', 'category']

    
# This serializes fields in the Category Table that will be served in JSON when endpoint is reached 
class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = CategoryModel
        fields = ['id', 'name', 'description', 'image_url']
    
