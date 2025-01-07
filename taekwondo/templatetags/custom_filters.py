from django import template
from django.templatetags.static import static


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
        return static("images/c-man.png")
    return static("images/c-woman.png")

