from django import forms
from django_countries.fields import CountryField
from django_countries.widgets import CountrySelectWidget
from .models import Coach

class CoachForm(forms.ModelForm):
    country = CountryField().formfield(  # Add country as a custom field
        widget=CountrySelectWidget(attrs={"class": "form-control"})
    )
     
    class Meta:
        model= Coach
        fields=["registration_number","full_name","place_of_birth","date_of_birth",
               "dojang_name","sex","province","city","status","belt",
               "phone_number","email","photo","input_date"]
        widgets = {
            "date_of_birth": forms.DateInput(attrs={"class": "form-control flatpickr"}),
            "sex": forms.Select(attrs={"class": "form-control"}), 
            "country": forms.Select(attrs={"class": "form-control"}),
            "province": forms.Select(attrs={"class": "form-control"}), 
            "city": forms.Select(attrs={"class": "form-control"}), 
            "belt": forms.Select(attrs={"class": "form-control"}),
            "status": forms.Select(attrs={"class": "form-control"}),  
        }