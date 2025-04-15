import django_filters
from .models import Coach, Belt
from django_countries.fields import Country
from django.db.models.functions import Lower
from django_countries import countries  
from django_filters import ChoiceFilter, FilterSet, ModelChoiceFilter

def get_country_choices():
    try:
        countries = (
            Coach.objects.order_by(Lower('country'))
            .values_list('country', flat=True)
            .distinct()
        )
        return [(country, country) for country in countries if country]
    except Exception:
        return []

class CoachFilter(FilterSet):
    country = ChoiceFilter(
        field_name='country',
        label='Country',
        empty_label=None,
        method='filter_country'  # Custom method instead of static choices
    )

    belt_rank = ModelChoiceFilter(
        queryset=Belt.objects.all(),
        field_name='belt',
        label='',
        empty_label="Belt Rank",
    )

    status = ChoiceFilter(
        field_name='status',
        choices=[('', 'Status'), ('active', 'Active'), ('inactive', 'Inactive')],
        label='',
        empty_label=None,
    )

    class Meta:
        model = Coach
        fields = ['country', 'belt_rank', 'status']

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        # Dynamically set choices in __init__
        country_choices = Coach.objects.order_by(Lower('country')).values_list('country', flat=True).distinct()
        self.filters['country'].extra['choices'] = [('', 'Country')] + [
        (code, countries.name(code) if countries.name(code) else code) for code in country_choices if code
        ]

    def filter_country(self, queryset, name, value):
        if value:
            return queryset.filter(**{name: value})
        return queryset