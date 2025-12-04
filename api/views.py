from django.shortcuts import render
from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView
from .models import ProductModel
from .serializers import ProductSerializer
from rest_framework.permissions import IsAuthenticatedOrReadOnly, IsAuthenticated
from rest_framework.authentication import TokenAuthentication
from rest_framework.filters import SearchFilter

# Create your views here.
class ProductViewSet(ListCreateAPIView):
    queryset = ProductModel.objects.all()
    serializer_class = ProductSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]
    authentication_classes = [TokenAuthentication]
    filter_backends = [SearchFilter]
    search_fields = ['name', 'category__name']

class ProductDetailViewSet(RetrieveUpdateDestroyAPIView):
    queryset = ProductModel.objects.all()
    serializer_class = ProductSerializer
    permission_classes = [IsAuthenticated]
    authentication_classes = [TokenAuthentication]







