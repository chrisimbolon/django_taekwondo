from django import template

register = template.Library()

@register.filter
def add_class(field, css_class):
    """Adds a CSS class to form fields."""
    return field.as_widget(attrs={"class": css_class})


@register.filter
def truncate_chars(value, max_length):
    """Truncate a string after a certain number of characters."""
    if len(value) > max_length:
        return value[:max_length] + "..."
    return value