import django_filters
from .models import Coach, Belt

class CoachFilter(django_filters.FilterSet):
    # Dropdown for country
    country = django_filters.ChoiceFilter(
    field_name='country',
    choices=[(c, c) for c in Coach.objects.values_list('country', flat=True).distinct()],
    label='Country'
)


    # Dropdown for belt rank
    belt_rank = django_filters.ModelChoiceFilter(
    queryset=Belt.objects.all(),
    field_name='belt',
    label='Belt Rank'
)

    # Dropdown for status
    status = django_filters.ChoiceFilter(
        field_name='status',
        choices=[('active', 'Active'), ('inactive', 'Inactive')],
        label='Status'
    )

    class Meta:
        model = Coach
        fields = ['country', 'belt_rank', 'status']
