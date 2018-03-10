from django import template
from .. import models

register = template.Library()

@register.inclusion_tag('guide/table_of_contents.html')
def table_of_contents(root):
    dict_ = root.as_dict()
    return {'root': dict_}