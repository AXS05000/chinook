import os
from django import template

register = template.Library()

@register.filter
def basename(value):
    """Retorna apenas o nome do arquivo, ou uma string vazia se o valor for None."""
    if value:
        return os.path.basename(value)
    return ""