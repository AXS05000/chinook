from .models import APIKey
from django.core.exceptions import ImproperlyConfigured


def get_api_key(name):
    try:
        api_key = APIKey.objects.get(name=name)
        return api_key.key
    except APIKey.DoesNotExist:
        raise ImproperlyConfigured(f"API key for {name} not found.")
