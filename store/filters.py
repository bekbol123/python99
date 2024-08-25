from django_filters.rest_framework import FilterSet
from .models import Car

class CarFilter(FilterSet):
    class Meta:
        model = Car
        fields = {
            'price': ['gt', 'lt'],
            'year': ['exact'],
            'car2_model': ['exact'],
            'carmarka': ['exact']
        }