import django_filters
from .models import *

class PostFilter(django_filters.FilterSet):
    location = django_filters.CharFilter(
        field_name='locaiton', lookup_expr='icontains')

    class Meta:
        model = OrganizationProfile
        fields = ['location']