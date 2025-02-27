from django import template
from django.templatetags.static import static
from datetime import date

register = template.Library()

@register.filter
def add_class(field, css_class):
    """Adds a CSS class to form fields."""
    return field.as_widget(attrs={"class": css_class})


@register.filter
def smart_truncate(value, max_length=18):
    """
    Truncate a string at the nearest word boundary without exceeding max_length.
    Adds an ellipsis ("...") if truncated.
    """
    if len(value) <= max_length:
        return value
    
    truncated = value[:max_length].rsplit(' ', 1)[0]
    return f"{truncated}..."

@register.filter
def gender_card_class(coach):
    """Returns card CSS class based on gender."""
    return "boy-card" if coach.sex == "male" else "girl-card"

@register.filter
def gender_icon(coach):
    """Returns font-awesome gender icon class based on gender."""
    return "fa-mars" if coach.sex == "male" else "fa-venus"

@register.filter
def profile_picture(coach):
    """Returns the appropriate profile picture URL."""
    if coach.photo:
        return coach.photo.url
    if coach.sex == "male":
        return static("images/c-man.gif")
    return static("images/c-woman.gif")

@register.filter
def calculate_age(date_of_birth):
    if not date_of_birth:
        return None  # Handle cases where the date of birth is not provided
    today = date.today()
    age = today.year - date_of_birth.year - (
        (today.month, today.day) < (date_of_birth.month, date_of_birth.day)
    )
    return age