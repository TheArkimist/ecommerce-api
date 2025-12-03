from django.urls import path
from . import views

urlpatterns = [
    path('products/', views.ProductViewSet.as_view(), name='product-list'),
    path('products/<int:pk>/', views.ProductDetailViewSet.as_view(), name='product-detail'),
    path('categories/', views.CategoryViewSet.as_view(), name='category-list'),
    path('categories/<int:pk>/', views.CategoryDetailViewSet.as_view(), name='category-detail'),
]