from django.urls import path
from . import views

urlpatterns = [
    path('products/', views.ProductViewSet.as_view(), name='product-list'),
    path('products/detail/<int:pk>/', views.ProductDetailViewSet.as_view(), name='product-detail'),
    path('products/update/<int:pk>/', views.ProductUpdateViewSet.as_view(), name='product-detail'),
    path('products/delete/<int:pk>/', views.ProductDeleteViewSet.as_view(), name='product-detail'),
    path('categories/', views.CategoryViewSet.as_view(), name='category-list'),
    path('categories/detail/<int:pk>/', views.CategoryDetailViewSet.as_view(), name='category-detail'),
    path('categories/update/<int:pk>/', views.CategoryUpdateViewSet.as_view(), name='category-detail'),
    path('categories/delete/<int:pk>/', views.CategoryDeleteViewSet.as_view(), name='category-detail'),

    
]