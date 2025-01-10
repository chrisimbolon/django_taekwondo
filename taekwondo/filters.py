import django_filters
from .models import Coach, Belt

class CoachFilter(django_filters.FilterSet):
    # Dropdown for country with "Country" placeholder
    country = django_filters.ChoiceFilter(
        field_name='country',
        choices=[('', 'Country')] + [
            (c, c) for c in Coach.objects.values_list('country', flat=True).distinct() if c
        ],
        label='Country',
        empty_label=None,  # Ensures no additional placeholder from Django
    )

    # Dropdown for belt rank with "Belt Rank" placeholder
    belt_rank = django_filters.ModelChoiceFilter(
        queryset=Belt.objects.all(),
        field_name='belt',
        label='',  # Remove label so the placeholder acts as the default
        empty_label="Belt Rank",  # This will act as the placeholder
    )

    # Dropdown for status with "Status" placeholder
    status = django_filters.ChoiceFilter(
        field_name='status',
        choices=[('', 'Status'), ('active', 'Active'), ('inactive', 'Inactive')],
        label='',  # Remove label so the placeholder acts as the default
        empty_label=None,
    )

    class Meta:
        model = Coach
        fields = ['country', 'belt_rank', 'status']
