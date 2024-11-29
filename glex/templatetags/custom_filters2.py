import os
from django import template

register = template.Library()

@register.filter
def basename(value, max_length=None):
    """
    Retorna o nome base do arquivo e opcionalmente trunca o nome se max_length for fornecido.
    """
    if value:
        base_name = os.path.basename(value)
        if max_length and len(base_name) > int(max_length):
            return base_name[:int(max_length)] + "..."
        return base_name
    return ""
