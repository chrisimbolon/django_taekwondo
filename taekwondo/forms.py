from django import forms
from django_countries.fields import CountryField
from django_countries.widgets import CountrySelectWidget
from .models import Coach

class CoachForm(forms.ModelForm):
    date_of_birth = forms.DateField(
        input_formats=['%d-%m-%Y'],  # Frontend will input DD-MM-YYYY
        widget=forms.DateInput(attrs={"class": "form-control flatpickr", "data-date-format": "d-m-Y"}),
        error_messages={"invalid": "Invalid date format. Please use DD-MM-YYYY."},
    )
    country = CountryField().formfield(  # Add country as a custom field
        widget=CountrySelectWidget(attrs={"class": "form-control"})
    )
      
    class Meta:
        model= Coach
        fields=["registration_number","full_name","place_of_birth","date_of_birth",
               "dojang_name","sex","country","province","city","status","belt","bio",
               "achievements","phone_number","email","photo"]
        
        widgets = {
            "sex": forms.Select(attrs={"class": "form-control"}), 
            "country": forms.Select(attrs={"class": "form-control"}),
            "province": forms.Select(attrs={"class": "form-control"}), 
            "city": forms.Select(attrs={"class": "form-control"}), 
            "belt": forms.Select(attrs={"class": "form-control"}),
            "status": forms.Select(attrs={"class": "form-control"}),
            "bio": forms.Textarea(
                attrs={
                    "class": "form-control",
                    "placeholder": "Write about the coach's background...",
                    "rows": 3,  # Sets height to 3 lines
                }
            ),
            "achievements": forms.Textarea(
                attrs={
                    "class": "form-control limit-lines",
                    "placeholder": "List achievements here...",
                    "rows": 2,  # Sets height to 2 lines
                }
            ),
        }
        labels = {
            "province": "State/Province",  
        }