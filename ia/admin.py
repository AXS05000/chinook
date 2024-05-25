from django.contrib import admin

# Register your models here.
from .models import Informacao, APIKey

# Register your models here.
admin.site.register(Informacao)

admin.site.register(APIKey)
