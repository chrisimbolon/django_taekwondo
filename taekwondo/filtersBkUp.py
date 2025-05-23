import django_filters
from .models import Coach, Belt
from django_countries.fields import Country
from django.db.models.functions import Lower
from django_countries import countries  

def get_country_choices():
    try:
        countries_qs = Coach.objects.order_by(Lower('country')).values_list('country', flat=True).distinct()
        return [('', 'Country')] + [
            (code, Country(code).name if code in dict(countries) else code)
            for code in countries_qs if code
        ]
    except Exception:
        return [('', 'Country')]

class CoachFilter(django_filters.FilterSet):
    # Dropdown for country with "Country" placeholder
    country = django_filters.ChoiceFilter(
        field_name='country',
        choices=list(get_country_choices()),  # Convert to list and call the function
        label='Country',
        empty_label=None,  
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
