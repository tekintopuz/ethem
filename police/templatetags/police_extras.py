from django import template
import os, json
from django.utils.safestring import mark_safe

register = template.Library()


@register.filter(name='has_group')
def has_group(user, group_name):
    return user.groups.filter(name=group_name).exists()


@register.filter(name='addcss')
def addcss(field, css):
    return field.as_widget(attrs={"class": css})


@register.filter(name='filename')
def filename(value):
    return os.path.basename(value.name)


@register.filter(name='my_float')
def my_float(value):
    try:
        return str(round(value, 2)).replace(",", ".")
    except Exception as e:
        return str(value).replace(",", ".")


@register.filter(name='my_completed')
def my_completed(value):
    try:
        return str(round(float(value) * 100, 2)).replace(",", ".")
    except Exception as e:
        return str(value).replace(",", ".")


@register.filter(name='lastname')
def lastname(value):
    """
    Returns the first character of lastname in lowercase for a given name
    """
    if value:
        return value[:2].upper()  # get the first letter of last name in lower case
    else:
        return "A"


@register.filter(name='js', is_safe=True)
def js(obj):
    return mark_safe(json.dumps(obj))
