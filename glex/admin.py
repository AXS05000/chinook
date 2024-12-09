from django.contrib import admin

# Register your models here.
from .models import (
    Administrativo,
    Comercial,
    Base_de_Conhecimento_Geral,

)


admin.site.register(Administrativo)

admin.site.register(Comercial)

admin.site.register(Base_de_Conhecimento_Geral)