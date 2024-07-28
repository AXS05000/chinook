from django.contrib import admin

# Register your models here.
from .models import (
    Informacao,
    APIKey,
    Beneficio,
    FolhaPonto,
    Salario,
    Ferias,
    CRM_FUI,
    Respostas_NPS,
)

# Register your models here.
admin.site.register(Informacao)

admin.site.register(APIKey)


admin.site.register(Beneficio)
admin.site.register(FolhaPonto)
admin.site.register(Salario)
admin.site.register(Ferias)

admin.site.register(CRM_FUI)
admin.site.register(Respostas_NPS)
