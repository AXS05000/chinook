from django.contrib import admin

# Register your models here.
from .models import (
    Administrativo,
    Comercial,

)


admin.site.register(Administrativo)

admin.site.register(Comercial)