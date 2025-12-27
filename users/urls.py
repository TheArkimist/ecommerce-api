from django.urls import path
from . import views


urlpatterns = [
    path('register/', views.RegisterUserViewSet.as_view(), name='register'),
]