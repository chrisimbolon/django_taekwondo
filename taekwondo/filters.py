import django_filters
from .models import Coach

class CoachFilter(django_filters.FilterSet):
    # Example filters
    country = django_filters.CharFilter(field_name='country__name', lookup_expr='icontains', label='Country')
    belt_rank = django_filters.CharFilter(field_name='belt_rank', lookup_expr='icontains', label='Belt Rank')
    status = django_filters.ChoiceFilter(field_name='status', choices=[('active', 'Active'), ('inactive', 'Inactive')], label='Status')

    class Meta:
        model = Coach
        fields = ['country', 'belt_rank', 'status']
