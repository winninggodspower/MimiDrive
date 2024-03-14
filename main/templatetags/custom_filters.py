from django import template
import re

register = template.Library()

@register.filter
def path_class(request, regex):
    if re.match(regex, request.path):
        return 'md:text-orange-400'
    else:
        return None