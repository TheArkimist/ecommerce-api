from django.urls import path
from . import views

urlpatterns = [
    path('products/', views.ProductViewSet.as_view(), name='product-list'),
    path('products/<int:pk>/', views.ProductDetailViewSet.as_view(), name='product-detail'),
]