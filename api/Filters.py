import django_filters
from .models import ProductModel


# This class filters Products based on a price range
class ProductFilter(django_filters.FilterSet):
    min_price = django_filters.NumberFilter(field_name='price', lookup_expr='gte')
    max_price = django_filters.NumberFilter(field_name='price', lookup_expr='lte')

    class Meta:
        model = ProductModel
        fields = ['min_price', 'max_price']