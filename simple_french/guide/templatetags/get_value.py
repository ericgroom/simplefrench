from django import template

register = template.Library()

@register.filter(name='get')
def get_value(dictionary, key):
    return dictionary[key]