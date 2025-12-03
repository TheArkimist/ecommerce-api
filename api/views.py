from django.shortcuts import render
from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView
from .models import CategoryModel, ProductModel
from .serializers import CategorySerializer, ProductSerializer

# Create your views here.
class ProductViewSet(ListCreateAPIView):
    queryset = ProductModel.objects.all()
    serializer_class = ProductSerializer

class ProductDetailViewSet(RetrieveUpdateDestroyAPIView):
    queryset = ProductModel.objects.all()
    serializer_class = ProductSerializer

class CategoryViewSet(ListCreateAPIView):
    queryset = CategoryModel.objects.all()
    serializer_class = CategorySerializer

class CategoryDetailViewSet(RetrieveUpdateDestroyAPIView):
    queryset = CategoryModel.objects.all()
    serializer_class = CategorySerializer



