import django_filters
from .models import Coach, Belt
from django_countries.fields import Country
from django.db.models.functions import Lower



class CoachFilter(django_filters.FilterSet):
    # Dropdown for country with "Country" placeholder
    country = django_filters.ChoiceFilter(
        field_name='country',
        choices=[('', 'Country')] + [
            (code, Country(code).name)  # Convert code to full name
            # for code in Coach.objects.values_list('country', flat=True).distinct() if code
            for code in Coach.objects.order_by(Lower('country')).values_list('country', flat=True).distinct() if code

        ],
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
