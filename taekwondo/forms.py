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
               "dojang_name","sex","country","province","city","status","belt","bio",
               "achievements","phone_number","email","photo"]
        
        widgets = {
            "date_of_birth": forms.DateInput(attrs={"class": "form-control flatpickr"}),
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
                    "class": "form-control",
                    "placeholder": "List achievements here...",
                    "rows": 3,  # Sets height to 3 lines
                }
            ),
        }
        labels = {
            "province": "State/Province",  
        }