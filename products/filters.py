from django_filters.rest_framework import FilterSet

import django_filters

from .models import *

class ProductFilter(FilterSet):
    brand = django_filters.CharFilter(field_name='brand__title', lookup_expr='contains')
    title = django_filters.CharFilter(field_name='title', lookup_expr='contains')
    brand_id = django_filters.CharFilter(field_name='brand__id', lookup_expr='exact')
    min_price = django_filters.CharFilter(field_name='price', lookup_expr='gte')
    max_price = django_filters.CharFilter(field_name='price', lookup_expr='lte')
    class Meta:
        model = Product
        fields = ['brand', 'title', 'min_price', 'max_price']


